# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: GetUploadRecordListInputProto.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='GetUploadRecordListInputProto.proto',
  package='',
  syntax='proto3',
  serialized_options=b'\252\002\027TomTaw.eWordIMCIS.Proto',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n#GetUploadRecordListInputProto.proto\"z\n\x1dGetUploadRecordListInputProto\x12\x13\n\x0b\x63urrentPage\x18\x01 \x01(\x05\x12\x10\n\x08pageSize\x18\x02 \x01(\x05\x12\x0c\n\x04\x64\x61te\x18\x03 \x01(\t\x12\x0c\n\x04type\x18\x04 \x01(\x05\x12\x16\n\x0eorganizationID\x18\x05 \x01(\t\"\x81\x01\n\x1eGetUploadRecordListOutputProto\x12\x11\n\tuploadUID\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\x05\x12\x12\n\ncreateTime\x18\x03 \x01(\t\x12\x18\n\x10organizationName\x18\x04 \x01(\t\x12\x10\n\x08typeName\x18\x05 \x01(\tB\x1a\xaa\x02\x17TomTaw.eWordIMCIS.Protob\x06proto3'
)




_GETUPLOADRECORDLISTINPUTPROTO = _descriptor.Descriptor(
  name='GetUploadRecordListInputProto',
  full_name='GetUploadRecordListInputProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='currentPage', full_name='GetUploadRecordListInputProto.currentPage', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pageSize', full_name='GetUploadRecordListInputProto.pageSize', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='date', full_name='GetUploadRecordListInputProto.date', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='GetUploadRecordListInputProto.type', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='organizationID', full_name='GetUploadRecordListInputProto.organizationID', index=4,
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
  serialized_start=39,
  serialized_end=161,
)


_GETUPLOADRECORDLISTOUTPUTPROTO = _descriptor.Descriptor(
  name='GetUploadRecordListOutputProto',
  full_name='GetUploadRecordListOutputProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uploadUID', full_name='GetUploadRecordListOutputProto.uploadUID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='GetUploadRecordListOutputProto.type', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='createTime', full_name='GetUploadRecordListOutputProto.createTime', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='organizationName', full_name='GetUploadRecordListOutputProto.organizationName', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='typeName', full_name='GetUploadRecordListOutputProto.typeName', index=4,
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
  serialized_start=164,
  serialized_end=293,
)

DESCRIPTOR.message_types_by_name['GetUploadRecordListInputProto'] = _GETUPLOADRECORDLISTINPUTPROTO
DESCRIPTOR.message_types_by_name['GetUploadRecordListOutputProto'] = _GETUPLOADRECORDLISTOUTPUTPROTO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetUploadRecordListInputProto = _reflection.GeneratedProtocolMessageType('GetUploadRecordListInputProto', (_message.Message,), {
  'DESCRIPTOR' : _GETUPLOADRECORDLISTINPUTPROTO,
  '__module__' : 'GetUploadRecordListInputProto_pb2'
  # @@protoc_insertion_point(class_scope:GetUploadRecordListInputProto)
  })
_sym_db.RegisterMessage(GetUploadRecordListInputProto)

GetUploadRecordListOutputProto = _reflection.GeneratedProtocolMessageType('GetUploadRecordListOutputProto', (_message.Message,), {
  'DESCRIPTOR' : _GETUPLOADRECORDLISTOUTPUTPROTO,
  '__module__' : 'GetUploadRecordListInputProto_pb2'
  # @@protoc_insertion_point(class_scope:GetUploadRecordListOutputProto)
  })
_sym_db.RegisterMessage(GetUploadRecordListOutputProto)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
