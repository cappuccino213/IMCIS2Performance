# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ExamItemsOutputProto.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ExamItemsOutputProto.proto',
  package='',
  syntax='proto3',
  serialized_options=b'\252\002\037TomTaw.eWordIMCIS.WebAPI.Models',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1a\x45xamItemsOutputProto.proto\"\x92\x01\n\x14\x45xamItemsOutputProto\x12\x0f\n\x07\x65xamUID\x18\x01 \x01(\t\x12\x13\n\x0bserviceText\x18\x02 \x01(\t\x12\x10\n\x08\x65xamTime\x18\x03 \x01(\t\x12\x15\n\rserviceSectID\x18\x04 \x01(\t\x12\x14\n\x0cresultStatus\x18\x05 \x01(\t\x12\x15\n\rabnormalFlags\x18\x06 \x01(\tB\"\xaa\x02\x1fTomTaw.eWordIMCIS.WebAPI.Modelsb\x06proto3'
)




_EXAMITEMSOUTPUTPROTO = _descriptor.Descriptor(
  name='ExamItemsOutputProto',
  full_name='ExamItemsOutputProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='examUID', full_name='ExamItemsOutputProto.examUID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='serviceText', full_name='ExamItemsOutputProto.serviceText', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='examTime', full_name='ExamItemsOutputProto.examTime', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='serviceSectID', full_name='ExamItemsOutputProto.serviceSectID', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='resultStatus', full_name='ExamItemsOutputProto.resultStatus', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='abnormalFlags', full_name='ExamItemsOutputProto.abnormalFlags', index=5,
      number=6, type=9, cpp_type=9, label=1,
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
  serialized_start=31,
  serialized_end=177,
)

DESCRIPTOR.message_types_by_name['ExamItemsOutputProto'] = _EXAMITEMSOUTPUTPROTO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ExamItemsOutputProto = _reflection.GeneratedProtocolMessageType('ExamItemsOutputProto', (_message.Message,), {
  'DESCRIPTOR' : _EXAMITEMSOUTPUTPROTO,
  '__module__' : 'ExamItemsOutputProto_pb2'
  # @@protoc_insertion_point(class_scope:ExamItemsOutputProto)
  })
_sym_db.RegisterMessage(ExamItemsOutputProto)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
