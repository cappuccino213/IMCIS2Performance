# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: RegisterFilmResponseProto.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='RegisterFilmResponseProto.proto',
  package='',
  syntax='proto3',
  serialized_options=b'\252\002\037TomTaw.eWordIMCIS.WebAPI.Models',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1fRegisterFilmResponseProto.proto\"D\n\x19RegisterFilmResponseProto\x12\x11\n\terrorCode\x18\x01 \x01(\x05\x12\x14\n\x0c\x65rrorMessage\x18\x02 \x01(\tB\"\xaa\x02\x1fTomTaw.eWordIMCIS.WebAPI.Modelsb\x06proto3'
)




_REGISTERFILMRESPONSEPROTO = _descriptor.Descriptor(
  name='RegisterFilmResponseProto',
  full_name='RegisterFilmResponseProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='errorCode', full_name='RegisterFilmResponseProto.errorCode', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='errorMessage', full_name='RegisterFilmResponseProto.errorMessage', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=35,
  serialized_end=103,
)

DESCRIPTOR.message_types_by_name['RegisterFilmResponseProto'] = _REGISTERFILMRESPONSEPROTO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RegisterFilmResponseProto = _reflection.GeneratedProtocolMessageType('RegisterFilmResponseProto', (_message.Message,), {
  'DESCRIPTOR' : _REGISTERFILMRESPONSEPROTO,
  '__module__' : 'RegisterFilmResponseProto_pb2'
  # @@protoc_insertion_point(class_scope:RegisterFilmResponseProto)
  })
_sym_db.RegisterMessage(RegisterFilmResponseProto)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
