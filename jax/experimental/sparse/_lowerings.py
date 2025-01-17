# Copyright 2023 The JAX Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Primitives for calling out to cusparse.

In general, these primitives are not meant to be used directly, but rather
are used internally in GPU translation rules of higher-level primitives.
"""

from jax import core
from jax._src import dispatch
from jax._src.interpreters import mlir
from jax._src.lib import gpu_sparse
import numpy as np


SUPPORTED_DATA_DTYPES = [np.float32, np.float64, np.complex64, np.complex128]
SUPPORTED_INDEX_DTYPES = [np.int32]

# coo_spmv_p
# This is an internal-only primitive that calls into cusparse coo SpMV.
# This is a raw lowering that does no validation of inputs; the indices are
# assumed to be lexicographically sorted, deduplicated, and in-bounds.
coo_spmv_p = core.Primitive("coo_spmv")

def _coo_spmv_abstract_eval(data, row, col, x, *, transpose, shape):
  # TODO(jakevdp) support for batched matvec.
  assert data.shape == row.shape == col.shape
  assert row.ndim == 1
  assert x.ndim == 1

  assert row.dtype == col.dtype
  assert row.dtype in SUPPORTED_INDEX_DTYPES

  assert data.dtype == x.dtype
  assert x.dtype in SUPPORTED_DATA_DTYPES

  assert len(shape) == 2
  assert x.shape[0] == (shape[0] if transpose else shape[1])

  return core.ShapedArray(
    shape=shape[1:] if transpose else shape[:1],
    dtype=x.dtype)

def _coo_spmv_gpu_lowering(ctx, data, row, col, x, *, transpose, shape):
  data_aval, row_aval, _, x_aval = ctx.avals_in
  return [gpu_sparse.cuda_coo_matvec(
            data, row, col, x,
            shape=shape,
            transpose=transpose,
            data_dtype=data_aval.dtype,
            index_dtype=row_aval.dtype,
            x_dtype=x_aval.dtype)]

coo_spmv_p.def_abstract_eval(_coo_spmv_abstract_eval)
dispatch.simple_impl(coo_spmv_p)
if gpu_sparse.cuda_is_supported:
  mlir.register_lowering(coo_spmv_p, _coo_spmv_gpu_lowering, platform='cuda')
if gpu_sparse.rocm_is_supported:
  mlir.register_lowering(coo_spmv_p, _coo_spmv_gpu_lowering, platform='rocm')


# coo_spmm_p
# This is an internal-only primitive that calls into cusparse COO SpMM.
# This is a raw lowering that does no validation of inputs; the indices are
# assumed to be lexicographically sorted, deduplicated, and in-bounds.
coo_spmm_p = core.Primitive("coo_spmm")

def _coo_spmm_abstract_eval(data, row, col, x, *, transpose, shape):
  # TODO(jakevdp) support for batched matmat.
  assert data.shape == row.shape == col.shape
  assert row.ndim == 1
  assert x.ndim == 2

  assert row.dtype == col.dtype
  assert row.dtype in SUPPORTED_INDEX_DTYPES

  assert data.dtype == x.dtype
  assert x.dtype in SUPPORTED_DATA_DTYPES

  assert len(shape) == 2
  assert x.shape[0] == (shape[0] if transpose else shape[1])

  return core.ShapedArray(
    shape=(shape[1] if transpose else shape[0], x.shape[1]),
    dtype=x.dtype)

def _coo_spmm_gpu_lowering(ctx, data, row, col, x, *, transpose, shape):
  data_aval, row_aval, _, x_aval = ctx.avals_in
  return [gpu_sparse.cuda_coo_matmat(
            data, row, col, x,
            shape=shape,
            transpose=transpose,
            data_dtype=data_aval.dtype,
            index_dtype=row_aval.dtype,
            x_dtype=x_aval.dtype)]

coo_spmm_p.def_abstract_eval(_coo_spmm_abstract_eval)
dispatch.simple_impl(coo_spmm_p)
if gpu_sparse.cuda_is_supported:
  mlir.register_lowering(coo_spmm_p, _coo_spmm_gpu_lowering, platform='cuda')
if gpu_sparse.rocm_is_supported:
  mlir.register_lowering(coo_spmm_p, _coo_spmm_gpu_lowering, platform='rocm')
