# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: PositiveRateDtoProto.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import PositiveRateOutputProto_pb2 as PositiveRateOutputProto__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='PositiveRateDtoProto.proto',
  package='',
  syntax='proto3',
  serialized_options=b'\252\002\037TomTaw.eWordIMCIS.WebAPI.Models',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1aPositiveRateDtoProto.proto\x1a\x1dPositiveRateOutputProto.proto\"\x9a\x01\n\x14PositiveRateDtoProto\x12\x34\n\x12positiveRateOutput\x18\x01 \x03(\x0b\x32\x18.PositiveRateOutputProto\x12\x10\n\x08row1Name\x18\x02 \x01(\t\x12\x10\n\x08row2Name\x18\x03 \x01(\t\x12\x13\n\x0b\x63olumn1Name\x18\x04 \x01(\t\x12\x13\n\x0b\x63olumn2Name\x18\x05 \x01(\tB\"\xaa\x02\x1fTomTaw.eWordIMCIS.WebAPI.Modelsb\x06proto3'
  ,
  dependencies=[PositiveRateOutputProto__pb2.DESCRIPTOR,])




_POSITIVERATEDTOPROTO = _descriptor.Descriptor(
  name='PositiveRateDtoProto',
  full_name='PositiveRateDtoProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='positiveRateOutput', full_name='PositiveRateDtoProto.positiveRateOutput', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='row1Name', full_name='PositiveRateDtoProto.row1Name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='row2Name', full_name='PositiveRateDtoProto.row2Name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='column1Name', full_name='PositiveRateDtoProto.column1Name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='column2Name', full_name='PositiveRateDtoProto.column2Name', index=4,
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
  serialized_start=62,
  serialized_end=216,
)

_POSITIVERATEDTOPROTO.fields_by_name['positiveRateOutput'].message_type = PositiveRateOutputProto__pb2._POSITIVERATEOUTPUTPROTO
DESCRIPTOR.message_types_by_name['PositiveRateDtoProto'] = _POSITIVERATEDTOPROTO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PositiveRateDtoProto = _reflection.GeneratedProtocolMessageType('PositiveRateDtoProto', (_message.Message,), {
  'DESCRIPTOR' : _POSITIVERATEDTOPROTO,
  '__module__' : 'PositiveRateDtoProto_pb2'
  # @@protoc_insertion_point(class_scope:PositiveRateDtoProto)
  })
_sym_db.RegisterMessage(PositiveRateDtoProto)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)