# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ClinicDtoProto.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import ExamRequestDtoProto_pb2 as ExamRequestDtoProto__pb2
import ExamRequestProto_pb2 as ExamRequestProto__pb2
import MedicalDtoProto_pb2 as MedicalDtoProto__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ClinicDtoProto.proto',
  package='',
  syntax='proto3',
  serialized_options=b'\252\002\037TomTaw.eWordIMCIS.WebAPI.Models',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x14\x43linicDtoProto.proto\x1a\x19\x45xamRequestDtoProto.proto\x1a\x16\x45xamRequestProto.proto\x1a\x15MedicalDtoProto.proto\"\xe2\x01\n\x0e\x43linicDtoProto\x12\x1a\n\x12obRequestExamCount\x18\x01 \x01(\x05\x12\x19\n\x11obRequestLabCount\x18\x02 \x01(\x05\x12\x1a\n\x12medicalRecordCount\x18\x03 \x01(\x05\x12+\n\robRequestExam\x18\x04 \x03(\x0b\x32\x14.ExamRequestDtoProto\x12\'\n\x0cobRequestLab\x18\x05 \x03(\x0b\x32\x11.ExamRequestProto\x12\'\n\rmedicalRecord\x18\x06 \x03(\x0b\x32\x10.MedicalDtoProtoB\"\xaa\x02\x1fTomTaw.eWordIMCIS.WebAPI.Modelsb\x06proto3'
  ,
  dependencies=[ExamRequestDtoProto__pb2.DESCRIPTOR,ExamRequestProto__pb2.DESCRIPTOR,MedicalDtoProto__pb2.DESCRIPTOR,])




_CLINICDTOPROTO = _descriptor.Descriptor(
  name='ClinicDtoProto',
  full_name='ClinicDtoProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='obRequestExamCount', full_name='ClinicDtoProto.obRequestExamCount', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='obRequestLabCount', full_name='ClinicDtoProto.obRequestLabCount', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='medicalRecordCount', full_name='ClinicDtoProto.medicalRecordCount', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='obRequestExam', full_name='ClinicDtoProto.obRequestExam', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='obRequestLab', full_name='ClinicDtoProto.obRequestLab', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='medicalRecord', full_name='ClinicDtoProto.medicalRecord', index=5,
      number=6, type=11, cpp_type=10, label=3,
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
  serialized_start=99,
  serialized_end=325,
)

_CLINICDTOPROTO.fields_by_name['obRequestExam'].message_type = ExamRequestDtoProto__pb2._EXAMREQUESTDTOPROTO
_CLINICDTOPROTO.fields_by_name['obRequestLab'].message_type = ExamRequestProto__pb2._EXAMREQUESTPROTO
_CLINICDTOPROTO.fields_by_name['medicalRecord'].message_type = MedicalDtoProto__pb2._MEDICALDTOPROTO
DESCRIPTOR.message_types_by_name['ClinicDtoProto'] = _CLINICDTOPROTO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClinicDtoProto = _reflection.GeneratedProtocolMessageType('ClinicDtoProto', (_message.Message,), {
  'DESCRIPTOR' : _CLINICDTOPROTO,
  '__module__' : 'ClinicDtoProto_pb2'
  # @@protoc_insertion_point(class_scope:ClinicDtoProto)
  })
_sym_db.RegisterMessage(ClinicDtoProto)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
