# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: GetOperateRecordListOutputProto.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='GetOperateRecordListOutputProto.proto',
  package='',
  syntax='proto3',
  serialized_options=b'\252\002\027TomTaw.eWordIMCIS.Proto',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n%GetOperateRecordListOutputProto.proto\"\x95\x01\n\x1fGetOperateRecordListOutputProto\x12\x18\n\x10operateRecordUID\x18\x01 \x01(\t\x12\x16\n\x0eorganizationID\x18\x02 \x01(\t\x12\x12\n\nrequestURL\x18\x03 \x01(\t\x12\x12\n\ncreateTime\x18\x04 \x01(\t\x12\x18\n\x10organizationName\x18\x05 \x01(\tB\x1a\xaa\x02\x17TomTaw.eWordIMCIS.Protob\x06proto3'
)




_GETOPERATERECORDLISTOUTPUTPROTO = _descriptor.Descriptor(
  name='GetOperateRecordListOutputProto',
  full_name='GetOperateRecordListOutputProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='operateRecordUID', full_name='GetOperateRecordListOutputProto.operateRecordUID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='organizationID', full_name='GetOperateRecordListOutputProto.organizationID', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='requestURL', full_name='GetOperateRecordListOutputProto.requestURL', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='createTime', full_name='GetOperateRecordListOutputProto.createTime', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='organizationName', full_name='GetOperateRecordListOutputProto.organizationName', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
  serialized_start=42,
  serialized_end=191,
)

DESCRIPTOR.message_types_by_name['GetOperateRecordListOutputProto'] = _GETOPERATERECORDLISTOUTPUTPROTO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetOperateRecordListOutputProto = _reflection.GeneratedProtocolMessageType('GetOperateRecordListOutputProto', (_message.Message,), {
  'DESCRIPTOR' : _GETOPERATERECORDLISTOUTPUTPROTO,
  '__module__' : 'GetOperateRecordListOutputProto_pb2'
  # @@protoc_insertion_point(class_scope:GetOperateRecordListOutputProto)
  })
_sym_db.RegisterMessage(GetOperateRecordListOutputProto)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
