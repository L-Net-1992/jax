/* Copyright 2024 The JAX Authors.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
==============================================================================*/

#include "jaxlib/mosaic/dialect/gpu/mosaic_gpu.h"

#include <cstdint>
#include <optional>
#include <string>

#include "testing/base/public/gmock.h"
#include "testing/base/public/gunit.h"
#include "absl/container/flat_hash_set.h"
#include "absl/status/status.h"
#include "absl/status/statusor.h"
#include "absl/strings/string_view.h"
#include "third_party/llvm/llvm-project/llvm/include/llvm/ADT/ArrayRef.h"
#include "third_party/llvm/llvm-project/llvm/include/llvm/ADT/SmallVector.h"
#include "mlir/include/mlir/Conversion/LLVMCommon/MemRefBuilder.h"
#include "mlir/include/mlir/Conversion/LLVMCommon/StructBuilder.h"
#include "mlir/include/mlir/Dialect/Bufferization/IR/BufferizableOpInterface.h"
#include "mlir/include/mlir/Dialect/Func/IR/FuncOps.h"
#include "mlir/include/mlir/Dialect/LLVMIR/LLVMDialect.h"
#include "mlir/include/mlir/Dialect/MemRef/IR/MemRef.h"
#include "mlir/include/mlir/Dialect/SCF/Utils/Utils.h"
#include "mlir/include/mlir/IR/Builders.h"
#include "mlir/include/mlir/IR/BuiltinOps.h"
#include "mlir/include/mlir/IR/Diagnostics.h"
#include "mlir/include/mlir/IR/MLIRContext.h"
#include "mlir/include/mlir/IR/OwningOpRef.h"
#include "mlir/include/mlir/IR/Types.h"
#include "mlir/include/mlir/IR/Value.h"
#include "mlir/include/mlir/IR/Verifier.h"
#include "mlir/include/mlir/Interfaces/DataLayoutInterfaces.h"
#include "mlir/include/mlir/Support/LLVM.h"
#include "tsl/platform/errors.h"

namespace mosaic_gpu {
namespace {

using ::testing::HasSubstr;
using ::testing::UnorderedElementsAre;
using ::testing::status::StatusIs;

template <typename T1, typename T2, typename... Ts>
absl::StatusOr<mlir::func::FuncOp> FromCppFunc(
    mlir::ModuleOp module,
    absl::Status (*f)(mlir::OpBuilder&, mlir::TypedValue<T1>,
                      mlir::TypedValue<T2>, Ts...),
    T1 type1, T2 type2, Ts... varargs) {
  mlir::MLIRContext* context = module->getContext();
  mlir::OpBuilder b(context);
  b.setInsertionPointToEnd(module.getBody());

  auto fn = b.create<mlir::func::FuncOp>(
      b.getUnknownLoc(), "function_wrapper",
      b.getFunctionType({type1, type2}, std::nullopt));
  fn.addEntryBlock();
  b.setInsertionPointToStart(&fn.front());

  TF_RETURN_IF_ERROR(f(b, mlir::cast<mlir::TypedValue<T1>>(fn.getArgument(0)),
                       mlir::cast<mlir::TypedValue<T2>>(fn.getArgument(1)),
                       varargs...));

  b.create<mlir::func::ReturnOp>(b.getUnknownLoc());

  if (mlir::failed(mlir::verify(module))) {
    return absl::InternalError("Failed to verify generated module");
  }

  return fn;
}

class MosaicGpuTest : public ::testing::Test {
 public:
  MosaicGpuTest()
      : builder_(&context_),
        module_(mlir::OwningOpRef<mlir::ModuleOp>(
            mlir::ModuleOp::create(builder_.getUnknownLoc(), "module"))) {
    RegisterErrorRecordingHandler();
    context_.loadDialect<mlir::func::FuncDialect, mlir::LLVM::LLVMDialect,
                         mlir::memref::MemRefDialect, MosaicGPUDialect>();
    builder_.setInsertionPointToEnd(module_->getBody());
    mosaic_gpu::DeclareRuntimeFunctions(builder_);
  }

  void ExpectLastErrorContains(absl::string_view substring) {
    EXPECT_THAT(last_error_message_, HasSubstr(substring));
  }

 protected:
  mlir::MLIRContext context_;
  mlir::OpBuilder builder_;
  mlir::OwningOpRef<mlir::ModuleOp> module_;
  std::string last_error_message_;

 private:
  void RegisterErrorRecordingHandler() {
    // Make sure to make the context single-threaded to avoid race conditions
    // when recording the last error message.
    context_.disableMultithreading();
    mlir::DiagnosticEngine& diagnostic_engine = context_.getDiagEngine();
    diagnostic_engine.registerHandler([&](mlir::Diagnostic& diagnostic) {
      last_error_message_ = diagnostic.str();
    });
  }
};

TEST_F(MosaicGpuTest, InitTmaDescriptorRequiresSliceShapeHasTheCorrectRank) {
  std::vector<int64_t> shape{1, 2, 3};
  std::vector<int64_t> slice_shape{1, 2};

  mlir::LLVM::LLVMPointerType pointer_type =
      mlir::LLVM::LLVMPointerType::get(&context_);
  mlir::MemRefType memref_type =
      mlir::MemRefType::get(shape, builder_.getF32Type());

  EXPECT_THAT(
      FromCppFunc(*module_, mosaic_gpu::InitTmaDescriptor, pointer_type,
                  memref_type, mlir::ArrayRef<int64_t>(slice_shape)),
      StatusIs(
          absl::StatusCode::kFailedPrecondition,
          HasSubstr(
              "Slice shape should have the same rank as the target tensor")));
}

TEST_F(MosaicGpuTest, InitTmaDescriptorGracefullyRejectsSubByteTypes) {
  std::vector<int64_t> shape{1, 2, 3};
  std::vector<int64_t> slice_shape{1, 2, 3};

  mlir::LLVM::LLVMPointerType pointer_type =
      mlir::LLVM::LLVMPointerType::get(&context_);
  mlir::MemRefType memref_type =
      mlir::MemRefType::get(shape, builder_.getI4Type());

  EXPECT_THAT(FromCppFunc(*module_, mosaic_gpu::InitTmaDescriptor, pointer_type,
                          memref_type, mlir::ArrayRef<int64_t>(slice_shape)),
              StatusIs(absl::StatusCode::kUnimplemented,
                       HasSubstr("Sub-byte types are not yet supported")));
}

TEST_F(MosaicGpuTest, InitTmaDescriptorProducesACallToRuntime) {
  std::vector<int64_t> shape{1, 2, 3};
  std::vector<int64_t> slice_shape{1, 2, 3};

  mlir::LLVM::LLVMPointerType pointer_type =
      mlir::LLVM::LLVMPointerType::get(&context_);
  mlir::MemRefType memref_type =
      mlir::MemRefType::get(shape, builder_.getF32Type());

  absl::StatusOr<mlir::func::FuncOp> fn_or =
      FromCppFunc(*module_, mosaic_gpu::InitTmaDescriptor, pointer_type,
                  memref_type, mlir::ArrayRef<int64_t>(slice_shape));
  ASSERT_OK(fn_or);

  llvm::SmallVector<mlir::func::CallOp> call_ops =
      llvm::to_vector(fn_or->getBlocks().front().getOps<mlir::func::CallOp>());
  EXPECT_EQ(call_ops.size(), 1);
  EXPECT_EQ(call_ops.front().getCallee().str(),
            mosaic_gpu::kRuntimeTmaDescriptorInitializerName);
}

TEST_F(MosaicGpuTest, RuntimeFunctionsAreRegistered) {
  // Deliberately introduce a new module to explicitly register the runtime
  // functions.
  mlir::OwningOpRef<mlir::ModuleOp> module_op =
      mlir::ModuleOp::create(builder_.getUnknownLoc(), "new_module");
  builder_.setInsertionPointToEnd(module_op->getBody());
  mosaic_gpu::DeclareRuntimeFunctions(builder_);

  llvm::SmallVector<mlir::func::FuncOp> func_ops =
      llvm::to_vector(module_op->getBody()->getOps<mlir::func::FuncOp>());
  EXPECT_EQ(func_ops.size(), 2);

  absl::flat_hash_set<std::string> func_names;
  for (mlir::func::FuncOp& func_op : func_ops) {
    func_names.insert(func_op.getSymName().str());
  }

  EXPECT_THAT(func_names, UnorderedElementsAre(
                              mosaic_gpu::kRuntimeTmaDescriptorInitializerName,
                              mosaic_gpu::kRuntimeMemcpyAsyncH2DName));
}

TEST_F(MosaicGpuTest, InitializeBarrierOpEnforcesRelevantInvariants) {
  auto loc = builder_.getUnknownLoc();
  auto f32 = builder_.getF32Type();
  auto barrier = BarrierType::get(&context_);

  // InitializeBarrierOp requires a memref with type `BarrierType`.
  auto initialize_op = builder_.create<InitializeBarrierOp>(
      loc, mlir::MemRefType::get({1, 2}, f32), /*arrival_count=*/1);
  EXPECT_FALSE(mlir::succeeded(mlir::verify(*module_)));
  ExpectLastErrorContains("must be memref of barrier values");
  initialize_op->erase();

  // InitializeBarrierOp requires a non-negative arrival count.
  initialize_op = builder_.create<InitializeBarrierOp>(
      loc, mlir::MemRefType::get({1, 2}, barrier), /*arrival_count=*/0);
  EXPECT_FALSE(mlir::succeeded(mlir::verify(*module_)));
  ExpectLastErrorContains("value is positive");
  initialize_op->erase();

  // Checks that InitializeBarrierOp prints nicely.
  initialize_op = builder_.create<InitializeBarrierOp>(
      loc, mlir::MemRefType::get({1, 2}, barrier), /*arrival_count=*/1);
  EXPECT_TRUE(mlir::succeeded(mlir::verify(*module_)));
  EXPECT_THAT(
      MlirToString(initialize_op),
      HasSubstr(
          "mosaic_gpu.initialize_barrier 1 : memref<1x2x!mosaic_gpu.barrier>"));
}

}  // anonymous namespace
}  // namespace mosaic_gpu