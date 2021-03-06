# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: DigitalImageInputProto.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import DigitalImageExamInputProto_pb2 as DigitalImageExamInputProto__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='DigitalImageInputProto.proto',
  package='',
  syntax='proto3',
  serialized_options=b'\252\002\037TomTaw.eWordIMCIS.WebAPI.Models',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1c\x44igitalImageInputProto.proto\x1a DigitalImageExamInputProto.proto\"b\n\x16\x44igitalImageInputProto\x12\x19\n\x11\x64igitalImageState\x18\x01 \x01(\x05\x12-\n\x08\x65xamList\x18\x02 \x03(\x0b\x32\x1b.DigitalImageExamInputProtoB\"\xaa\x02\x1fTomTaw.eWordIMCIS.WebAPI.Modelsb\x06proto3'
  ,
  dependencies=[DigitalImageExamInputProto__pb2.DESCRIPTOR,])




_DIGITALIMAGEINPUTPROTO = _descriptor.Descriptor(
  name='DigitalImageInputProto',
  full_name='DigitalImageInputProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='digitalImageState', full_name='DigitalImageInputProto.digitalImageState', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='examList', full_name='DigitalImageInputProto.examList', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=66,
  serialized_end=164,
)

_DIGITALIMAGEINPUTPROTO.fields_by_name['examList'].message_type = DigitalImageExamInputProto__pb2._DIGITALIMAGEEXAMINPUTPROTO
DESCRIPTOR.message_types_by_name['DigitalImageInputProto'] = _DIGITALIMAGEINPUTPROTO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DigitalImageInputProto = _reflection.GeneratedProtocolMessageType('DigitalImageInputProto', (_message.Message,), {
  'DESCRIPTOR' : _DIGITALIMAGEINPUTPROTO,
  '__module__' : 'DigitalImageInputProto_pb2'
  # @@protoc_insertion_point(class_scope:DigitalImageInputProto)
  })
_sym_db.RegisterMessage(DigitalImageInputProto)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
