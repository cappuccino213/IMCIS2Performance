# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WorkloadInputProto.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='WorkloadInputProto.proto',
  package='',
  syntax='proto3',
  serialized_options=b'\252\002\037TomTaw.eWordIMCIS.WebAPI.Models',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x18WorkloadInputProto.proto\"\x8b\x02\n\x12WorkloadInputProto\x12\x0c\n\x04rows\x18\x01 \x01(\t\x12\x0f\n\x07\x63olumns\x18\x02 \x01(\t\x12\x14\n\x0cregisterTime\x18\x03 \x01(\t\x12\x14\n\x0cpatientClass\x18\x04 \x01(\t\x12\x16\n\x0eorganizationID\x18\x05 \x01(\t\x12\x17\n\x0frequestDeptName\x18\x06 \x01(\t\x12\x15\n\rserviceSectID\x18\x07 \x01(\t\x12\x14\n\x0cresultStatus\x18\x08 \x01(\t\x12\x15\n\rcriticalValue\x18\t \x01(\t\x12\x11\n\tdateField\x18\n \x01(\t\x12\x11\n\tstartDate\x18\x0b \x01(\t\x12\x0f\n\x07\x65ndDate\x18\x0c \x01(\tB\"\xaa\x02\x1fTomTaw.eWordIMCIS.WebAPI.Modelsb\x06proto3'
)




_WORKLOADINPUTPROTO = _descriptor.Descriptor(
  name='WorkloadInputProto',
  full_name='WorkloadInputProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='rows', full_name='WorkloadInputProto.rows', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='columns', full_name='WorkloadInputProto.columns', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='registerTime', full_name='WorkloadInputProto.registerTime', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='patientClass', full_name='WorkloadInputProto.patientClass', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='organizationID', full_name='WorkloadInputProto.organizationID', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='requestDeptName', full_name='WorkloadInputProto.requestDeptName', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='serviceSectID', full_name='WorkloadInputProto.serviceSectID', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='resultStatus', full_name='WorkloadInputProto.resultStatus', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='criticalValue', full_name='WorkloadInputProto.criticalValue', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dateField', full_name='WorkloadInputProto.dateField', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='startDate', full_name='WorkloadInputProto.startDate', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='endDate', full_name='WorkloadInputProto.endDate', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=29,
  serialized_end=296,
)

DESCRIPTOR.message_types_by_name['WorkloadInputProto'] = _WORKLOADINPUTPROTO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

WorkloadInputProto = _reflection.GeneratedProtocolMessageType('WorkloadInputProto', (_message.Message,), {
  'DESCRIPTOR' : _WORKLOADINPUTPROTO,
  '__module__' : 'WorkloadInputProto_pb2'
  # @@protoc_insertion_point(class_scope:WorkloadInputProto)
  })
_sym_db.RegisterMessage(WorkloadInputProto)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)