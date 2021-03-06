# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: UserQuerySetInputProto.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from UserOrgInfoProto import Proto_pb2 as UserOrgInfoProto_dot_Proto__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='UserQuerySetInputProto.proto',
  package='',
  syntax='proto3',
  serialized_options=b'\252\002\027TomTaw.eWordIMCIS.Proto',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1cUserQuerySetInputProto.proto\x1a\x16UserOrgInfoProto.Proto\"r\n\x16UserQuerySetInputProto\x12\x0e\n\x06userId\x18\x01 \x01(\t\x12\x10\n\x08querySeq\x18\x02 \x01(\x05\x12#\n\x08userInfo\x18\x03 \x01(\x0b\x32\x11.UserOrgInfoProto\x12\x11\n\tqueryType\x18\x04 \x01(\tB\x1a\xaa\x02\x17TomTaw.eWordIMCIS.Protob\x06proto3'
  ,
  dependencies=[UserOrgInfoProto_dot_Proto__pb2.DESCRIPTOR,])




_USERQUERYSETINPUTPROTO = _descriptor.Descriptor(
  name='UserQuerySetInputProto',
  full_name='UserQuerySetInputProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='userId', full_name='UserQuerySetInputProto.userId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='querySeq', full_name='UserQuerySetInputProto.querySeq', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='userInfo', full_name='UserQuerySetInputProto.userInfo', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='queryType', full_name='UserQuerySetInputProto.queryType', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=56,
  serialized_end=170,
)

_USERQUERYSETINPUTPROTO.fields_by_name['userInfo'].message_type = UserOrgInfoProto_dot_Proto__pb2._USERORGINFOPROTO
DESCRIPTOR.message_types_by_name['UserQuerySetInputProto'] = _USERQUERYSETINPUTPROTO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UserQuerySetInputProto = _reflection.GeneratedProtocolMessageType('UserQuerySetInputProto', (_message.Message,), {
  'DESCRIPTOR' : _USERQUERYSETINPUTPROTO,
  '__module__' : 'UserQuerySetInputProto_pb2'
  # @@protoc_insertion_point(class_scope:UserQuerySetInputProto)
  })
_sym_db.RegisterMessage(UserQuerySetInputProto)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
