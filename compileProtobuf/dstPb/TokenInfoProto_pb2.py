# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: TokenInfoProto.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='TokenInfoProto.proto',
  package='',
  syntax='proto3',
  serialized_options=b'\252\002\027TomTaw.eWordIMCIS.Proto',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x14TokenInfoProto.proto\"R\n\x0eTokenInfoProto\x12\x13\n\x0btokenServer\x18\x01 \x01(\t\x12\x13\n\x0b\x61\x63\x63\x65ssToken\x18\x02 \x01(\t\x12\x16\n\x0eorganizationID\x18\x03 \x01(\tB\x1a\xaa\x02\x17TomTaw.eWordIMCIS.Protob\x06proto3'
)




_TOKENINFOPROTO = _descriptor.Descriptor(
  name='TokenInfoProto',
  full_name='TokenInfoProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='tokenServer', full_name='TokenInfoProto.tokenServer', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='accessToken', full_name='TokenInfoProto.accessToken', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='organizationID', full_name='TokenInfoProto.organizationID', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=24,
  serialized_end=106,
)

DESCRIPTOR.message_types_by_name['TokenInfoProto'] = _TOKENINFOPROTO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TokenInfoProto = _reflection.GeneratedProtocolMessageType('TokenInfoProto', (_message.Message,), {
  'DESCRIPTOR' : _TOKENINFOPROTO,
  '__module__' : 'TokenInfoProto_pb2'
  # @@protoc_insertion_point(class_scope:TokenInfoProto)
  })
_sym_db.RegisterMessage(TokenInfoProto)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
