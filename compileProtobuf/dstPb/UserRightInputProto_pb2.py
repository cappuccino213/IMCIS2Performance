# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: UserRightInputProto.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='UserRightInputProto.proto',
  package='',
  syntax='proto3',
  serialized_options=b'\252\002\037TomTaw.eWordIMCIS.WebAPI.Models',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x19UserRightInputProto.proto\"&\n\x13UserRightInputProto\x12\x0f\n\x07userUID\x18\x01 \x01(\tB\"\xaa\x02\x1fTomTaw.eWordIMCIS.WebAPI.Modelsb\x06proto3'
)




_USERRIGHTINPUTPROTO = _descriptor.Descriptor(
  name='UserRightInputProto',
  full_name='UserRightInputProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='userUID', full_name='UserRightInputProto.userUID', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_end=67,
)

DESCRIPTOR.message_types_by_name['UserRightInputProto'] = _USERRIGHTINPUTPROTO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UserRightInputProto = _reflection.GeneratedProtocolMessageType('UserRightInputProto', (_message.Message,), {
  'DESCRIPTOR' : _USERRIGHTINPUTPROTO,
  '__module__' : 'UserRightInputProto_pb2'
  # @@protoc_insertion_point(class_scope:UserRightInputProto)
  })
_sym_db.RegisterMessage(UserRightInputProto)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)