# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: RoleMstOutputProto.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='RoleMstOutputProto.proto',
  package='',
  syntax='proto3',
  serialized_options=b'\252\002\037TomTaw.eWordIMCIS.WebAPI.Models',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x18RoleMstOutputProto.proto\"\xce\x01\n\x12RoleMstOutputProto\x12\x0f\n\x07roleUID\x18\x01 \x01(\t\x12\x10\n\x08roleName\x18\x02 \x01(\t\x12\x15\n\rcreateUserUID\x18\x03 \x01(\t\x12\x16\n\x0e\x63reateUserName\x18\x04 \x01(\t\x12\x12\n\ncreateDate\x18\x05 \x01(\t\x12\x0c\n\x04memo\x18\x06 \x01(\t\x12\x12\n\nlAYChecked\x18\x07 \x01(\t\x12\x16\n\x0eorganizationID\x18\x08 \x01(\t\x12\x18\n\x10organizationName\x18\t \x01(\tB\"\xaa\x02\x1fTomTaw.eWordIMCIS.WebAPI.Modelsb\x06proto3'
)




_ROLEMSTOUTPUTPROTO = _descriptor.Descriptor(
  name='RoleMstOutputProto',
  full_name='RoleMstOutputProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='roleUID', full_name='RoleMstOutputProto.roleUID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='roleName', full_name='RoleMstOutputProto.roleName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='createUserUID', full_name='RoleMstOutputProto.createUserUID', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='createUserName', full_name='RoleMstOutputProto.createUserName', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='createDate', full_name='RoleMstOutputProto.createDate', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='memo', full_name='RoleMstOutputProto.memo', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lAYChecked', full_name='RoleMstOutputProto.lAYChecked', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='organizationID', full_name='RoleMstOutputProto.organizationID', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='organizationName', full_name='RoleMstOutputProto.organizationName', index=8,
      number=9, type=9, cpp_type=9, label=1,
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
  serialized_end=235,
)

DESCRIPTOR.message_types_by_name['RoleMstOutputProto'] = _ROLEMSTOUTPUTPROTO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RoleMstOutputProto = _reflection.GeneratedProtocolMessageType('RoleMstOutputProto', (_message.Message,), {
  'DESCRIPTOR' : _ROLEMSTOUTPUTPROTO,
  '__module__' : 'RoleMstOutputProto_pb2'
  # @@protoc_insertion_point(class_scope:RoleMstOutputProto)
  })
_sym_db.RegisterMessage(RoleMstOutputProto)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
