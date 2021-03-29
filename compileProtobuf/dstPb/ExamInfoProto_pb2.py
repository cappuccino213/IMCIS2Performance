# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ExamInfoProto.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ExamInfoProto.proto',
  package='',
  syntax='proto3',
  serialized_options=b'\252\002\037TomTaw.eWordIMCIS.WebAPI.Models',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x13\x45xamInfoProto.proto\"\x8b\x02\n\rExamInfoProto\x12\x11\n\tpatientID\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0b\n\x03sex\x18\x03 \x01(\t\x12\x11\n\tbirthDate\x18\x04 \x01(\t\x12\x13\n\x0bphoneNumber\x18\x05 \x01(\t\x12\x17\n\x0f\x61\x63\x63\x65ssionNumber\x18\x06 \x01(\t\x12\x14\n\x0cpatientClass\x18\x07 \x01(\t\x12\x13\n\x0bserviceSect\x18\x08 \x01(\t\x12\x10\n\x08\x65xamDate\x18\t \x01(\t\x12\x14\n\x0cresultStatus\x18\n \x01(\t\x12\x12\n\nprintTimes\x18\x0b \x01(\x05\x12\x0f\n\x07\x65xamUID\x18\x0c \x01(\t\x12\x13\n\x0b\x64ocInfoList\x18\r \x03(\tB\"\xaa\x02\x1fTomTaw.eWordIMCIS.WebAPI.Modelsb\x06proto3'
)




_EXAMINFOPROTO = _descriptor.Descriptor(
  name='ExamInfoProto',
  full_name='ExamInfoProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='patientID', full_name='ExamInfoProto.patientID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='ExamInfoProto.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sex', full_name='ExamInfoProto.sex', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='birthDate', full_name='ExamInfoProto.birthDate', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='phoneNumber', full_name='ExamInfoProto.phoneNumber', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='accessionNumber', full_name='ExamInfoProto.accessionNumber', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='patientClass', full_name='ExamInfoProto.patientClass', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='serviceSect', full_name='ExamInfoProto.serviceSect', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='examDate', full_name='ExamInfoProto.examDate', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='resultStatus', full_name='ExamInfoProto.resultStatus', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='printTimes', full_name='ExamInfoProto.printTimes', index=10,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='examUID', full_name='ExamInfoProto.examUID', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='docInfoList', full_name='ExamInfoProto.docInfoList', index=12,
      number=13, type=9, cpp_type=9, label=3,
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
  serialized_start=24,
  serialized_end=291,
)

DESCRIPTOR.message_types_by_name['ExamInfoProto'] = _EXAMINFOPROTO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ExamInfoProto = _reflection.GeneratedProtocolMessageType('ExamInfoProto', (_message.Message,), {
  'DESCRIPTOR' : _EXAMINFOPROTO,
  '__module__' : 'ExamInfoProto_pb2'
  # @@protoc_insertion_point(class_scope:ExamInfoProto)
  })
_sym_db.RegisterMessage(ExamInfoProto)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)