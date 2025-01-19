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

# pytype: skip-file
# automatically generated by the FlatBuffers compiler, do not modify

# namespace: serialization

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class PyTreeDefKind(object):
    leaf = 0
    none = 1
    tuple = 2
    list = 3
    dict = 4
    custom = 5


class AbstractValueKind(object):
    shapedArray = 0
    abstractToken = 1


class DType(object):
    bool = 0
    i8 = 1
    i16 = 2
    i32 = 3
    i64 = 4
    ui8 = 5
    ui16 = 6
    ui32 = 7
    ui64 = 8
    f16 = 9
    f32 = 10
    f64 = 11
    c64 = 12
    c128 = 13
    bf16 = 14
    i4 = 15
    ui4 = 16
    f8_e3m4 = 24
    f8_e4m3 = 23
    f8_e4m3b11fnuz = 17
    f8_e4m3fn = 18
    f8_e4m3fnuz = 19
    f8_e5m2 = 20
    f8_e5m2fnuz = 21
    f0 = 22


class ShardingKind(object):
    unspecified = 0
    hlo_sharding = 1


class DisabledSafetyCheckKind(object):
    platform = 0
    custom_call = 1
    shape_assertions = 2


class PyTreeDef(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = PyTreeDef()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsPyTreeDef(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # PyTreeDef
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # PyTreeDef
    def Kind(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

    # PyTreeDef
    def Children(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            obj = PyTreeDef()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # PyTreeDef
    def ChildrenLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # PyTreeDef
    def ChildrenIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        return o == 0

    # PyTreeDef
    def ChildrenNames(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    # PyTreeDef
    def ChildrenNamesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # PyTreeDef
    def ChildrenNamesIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        return o == 0

    # PyTreeDef
    def CustomName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # PyTreeDef
    def CustomAuxdata(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # PyTreeDef
    def CustomAuxdataAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int8Flags, o)
        return 0

    # PyTreeDef
    def CustomAuxdataLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # PyTreeDef
    def CustomAuxdataIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        return o == 0

def PyTreeDefStart(builder):
    builder.StartObject(5)

def PyTreeDefAddKind(builder, kind):
    builder.PrependInt8Slot(0, kind, 0)

def PyTreeDefAddChildren(builder, children):
    builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(children), 0)

def PyTreeDefStartChildrenVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def PyTreeDefAddChildrenNames(builder, childrenNames):
    builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(childrenNames), 0)

def PyTreeDefStartChildrenNamesVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def PyTreeDefAddCustomName(builder, customName):
    builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(customName), 0)

def PyTreeDefAddCustomAuxdata(builder, customAuxdata):
    builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(customAuxdata), 0)

def PyTreeDefStartCustomAuxdataVector(builder, numElems):
    return builder.StartVector(1, numElems, 1)

def PyTreeDefEnd(builder):
    return builder.EndObject()



class AbstractValue(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = AbstractValue()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsAbstractValue(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # AbstractValue
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # AbstractValue
    def Kind(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

    # AbstractValue
    def Shape(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    # AbstractValue
    def ShapeLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # AbstractValue
    def ShapeIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        return o == 0

    # AbstractValue
    def Dtype(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

def AbstractValueStart(builder):
    builder.StartObject(3)

def AbstractValueAddKind(builder, kind):
    builder.PrependInt8Slot(0, kind, 0)

def AbstractValueAddShape(builder, shape):
    builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(shape), 0)

def AbstractValueStartShapeVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def AbstractValueAddDtype(builder, dtype):
    builder.PrependInt8Slot(2, dtype, 0)

def AbstractValueEnd(builder):
    return builder.EndObject()



class Sharding(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Sharding()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsSharding(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # Sharding
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Sharding
    def Kind(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

    # Sharding
    def HloShardingProto(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # Sharding
    def HloShardingProtoAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int8Flags, o)
        return 0

    # Sharding
    def HloShardingProtoLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Sharding
    def HloShardingProtoIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        return o == 0

def ShardingStart(builder):
    builder.StartObject(2)

def ShardingAddKind(builder, kind):
    builder.PrependInt8Slot(0, kind, 0)

def ShardingAddHloShardingProto(builder, hloShardingProto):
    builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(hloShardingProto), 0)

def ShardingStartHloShardingProtoVector(builder, numElems):
    return builder.StartVector(1, numElems, 1)

def ShardingEnd(builder):
    return builder.EndObject()



class Effect(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Effect()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsEffect(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # Effect
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Effect
    def TypeName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

def EffectStart(builder):
    builder.StartObject(1)

def EffectAddTypeName(builder, typeName):
    builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(typeName), 0)

def EffectEnd(builder):
    return builder.EndObject()



class DisabledSafetyCheck(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = DisabledSafetyCheck()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsDisabledSafetyCheck(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # DisabledSafetyCheck
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # DisabledSafetyCheck
    def Kind(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

    # DisabledSafetyCheck
    def CustomCallTarget(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

def DisabledSafetyCheckStart(builder):
    builder.StartObject(2)

def DisabledSafetyCheckAddKind(builder, kind):
    builder.PrependInt8Slot(0, kind, 0)

def DisabledSafetyCheckAddCustomCallTarget(builder, customCallTarget):
    builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(customCallTarget), 0)

def DisabledSafetyCheckEnd(builder):
    return builder.EndObject()



class Exported(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Exported()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsExported(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # Exported
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # We increment the serialization version every time we change the
    # schema, even if the change is backwards compatible.
    # Note that this field has different semantics and purpose from
    # `mlir_module_serialization_version`, which encodes
    # the calling convention of the `mlir_module_serialized`.
    # Exported
    def SerializationVersion(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint16Flags, o + self._tab.Pos)
        return 0

    # Exported
    def FunctionName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # Exported
    def InTree(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            obj = PyTreeDef()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Exported
    def InAvals(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            obj = AbstractValue()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Exported
    def InAvalsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Exported
    def InAvalsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        return o == 0

    # Exported
    def OutTree(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            obj = PyTreeDef()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Exported
    def OutAvals(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            obj = AbstractValue()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Exported
    def OutAvalsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Exported
    def OutAvalsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        return o == 0

    # Exported
    def NrDevices(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int16Flags, o + self._tab.Pos)
        return 0

    # Exported
    def InShardings(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            obj = Sharding()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Exported
    def InShardingsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Exported
    def InShardingsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        return o == 0

    # Exported
    def OutShardings(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            obj = Sharding()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Exported
    def OutShardingsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Exported
    def OutShardingsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        return o == 0

    # Exported
    def Platforms(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    # Exported
    def PlatformsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Exported
    def PlatformsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        return o == 0

    # Exported
    def OrderedEffects(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            obj = Effect()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Exported
    def OrderedEffectsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Exported
    def OrderedEffectsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        return o == 0

    # Exported
    def UnorderedEffects(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            obj = Effect()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Exported
    def UnorderedEffectsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Exported
    def UnorderedEffectsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        return o == 0

    # Exported
    def DisabledChecks(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            obj = DisabledSafetyCheck()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Exported
    def DisabledChecksLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Exported
    def DisabledChecksIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        return o == 0

    # Exported
    def MlirModuleSerialized(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # Exported
    def MlirModuleSerializedAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int8Flags, o)
        return 0

    # Exported
    def MlirModuleSerializedLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Exported
    def MlirModuleSerializedIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        return o == 0

    # Exported
    def CallingConventionVersion(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint16Flags, o + self._tab.Pos)
        return 0

    # Exported
    def ModuleKeptVarIdx(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint16Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 2))
        return 0

    # Exported
    def ModuleKeptVarIdxAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint16Flags, o)
        return 0

    # Exported
    def ModuleKeptVarIdxLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Exported
    def ModuleKeptVarIdxIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        return o == 0

    # Exported
    def UsesGlobalConstants(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # Exported
    def Vjp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            obj = Exported()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

def ExportedStart(builder):
    builder.StartObject(18)

def ExportedAddSerializationVersion(builder, serializationVersion):
    builder.PrependUint16Slot(0, serializationVersion, 0)

def ExportedAddFunctionName(builder, functionName):
    builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(functionName), 0)

def ExportedAddInTree(builder, inTree):
    builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(inTree), 0)

def ExportedAddInAvals(builder, inAvals):
    builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(inAvals), 0)

def ExportedStartInAvalsVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def ExportedAddOutTree(builder, outTree):
    builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(outTree), 0)

def ExportedAddOutAvals(builder, outAvals):
    builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(outAvals), 0)

def ExportedStartOutAvalsVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def ExportedAddNrDevices(builder, nrDevices):
    builder.PrependInt16Slot(6, nrDevices, 0)

def ExportedAddInShardings(builder, inShardings):
    builder.PrependUOffsetTRelativeSlot(7, flatbuffers.number_types.UOffsetTFlags.py_type(inShardings), 0)

def ExportedStartInShardingsVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def ExportedAddOutShardings(builder, outShardings):
    builder.PrependUOffsetTRelativeSlot(8, flatbuffers.number_types.UOffsetTFlags.py_type(outShardings), 0)

def ExportedStartOutShardingsVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def ExportedAddPlatforms(builder, platforms):
    builder.PrependUOffsetTRelativeSlot(9, flatbuffers.number_types.UOffsetTFlags.py_type(platforms), 0)

def ExportedStartPlatformsVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def ExportedAddOrderedEffects(builder, orderedEffects):
    builder.PrependUOffsetTRelativeSlot(10, flatbuffers.number_types.UOffsetTFlags.py_type(orderedEffects), 0)

def ExportedStartOrderedEffectsVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def ExportedAddUnorderedEffects(builder, unorderedEffects):
    builder.PrependUOffsetTRelativeSlot(11, flatbuffers.number_types.UOffsetTFlags.py_type(unorderedEffects), 0)

def ExportedStartUnorderedEffectsVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def ExportedAddDisabledChecks(builder, disabledChecks):
    builder.PrependUOffsetTRelativeSlot(12, flatbuffers.number_types.UOffsetTFlags.py_type(disabledChecks), 0)

def ExportedStartDisabledChecksVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def ExportedAddMlirModuleSerialized(builder, mlirModuleSerialized):
    builder.PrependUOffsetTRelativeSlot(13, flatbuffers.number_types.UOffsetTFlags.py_type(mlirModuleSerialized), 0)

def ExportedStartMlirModuleSerializedVector(builder, numElems):
    return builder.StartVector(1, numElems, 1)

def ExportedAddCallingConventionVersion(builder, callingConventionVersion):
    builder.PrependUint16Slot(14, callingConventionVersion, 0)

def ExportedAddModuleKeptVarIdx(builder, moduleKeptVarIdx):
    builder.PrependUOffsetTRelativeSlot(15, flatbuffers.number_types.UOffsetTFlags.py_type(moduleKeptVarIdx), 0)

def ExportedStartModuleKeptVarIdxVector(builder, numElems):
    return builder.StartVector(2, numElems, 2)

def ExportedAddUsesGlobalConstants(builder, usesGlobalConstants):
    builder.PrependBoolSlot(16, usesGlobalConstants, 0)

def ExportedAddVjp(builder, vjp):
    builder.PrependUOffsetTRelativeSlot(17, flatbuffers.number_types.UOffsetTFlags.py_type(vjp), 0)

def ExportedEnd(builder):
    return builder.EndObject()
