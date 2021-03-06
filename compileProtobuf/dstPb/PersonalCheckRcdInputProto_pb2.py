# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: PersonalCheckRcdInputProto.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from compileProtobuf.dstPb.UserOrgInfoProto import Proto_pb2 as UserOrgInfoProto_dot_Proto__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='PersonalCheckRcdInputProto.proto',
  package='',
  syntax='proto3',
  serialized_options=b'\252\002\027TomTaw.eWordIMCIS.Proto',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n PersonalCheckRcdInputProto.proto\x1a\x16UserOrgInfoProto.Proto\"\xde\x03\n\x1aPersonalCheckRcdInputProto\x12\x17\n\x0fpatientMasterID\x18\x01 \x01(\t\x12\x15\n\rpersonExamUID\x18\x02 \x01(\t\x12\x10\n\x08pageSize\x18\x03 \x01(\x05\x12\x13\n\x0b\x63urrentPage\x18\x04 \x01(\x05\x12\r\n\x05token\x18\x05 \x01(\t\x12\x15\n\risInteragency\x18\x06 \x01(\t\x12\x19\n\x11isInteragencyExam\x18\x07 \x01(\t\x12\x1b\n\x13isInteragencyClinic\x18\x08 \x01(\t\x12\x1e\n\x16isInteragencyStatistic\x18\t \x01(\t\x12#\n\x08userInfo\x18\n \x01(\x0b\x32\x11.UserOrgInfoProto\x12\x19\n\x11isInteragencyData\x18\x0b \x01(\t\x12\x0f\n\x07\x65xamUID\x18\x0c \x01(\t\x12\x13\n\x0b\x61pplyMethod\x18\r \x01(\t\x12\x1a\n\x12isInterconnectData\x18\x0e \x01(\t\x12\x11\n\texamToken\x18\x0f \x01(\t\x12\x17\n\x0f\x61\x63\x63\x65ssionNumber\x18\x10 \x01(\t\x12\x16\n\x0eorganizationID\x18\x11 \x01(\t\x12\x10\n\x08iDCardNo\x18\x12 \x01(\t\x12\x13\n\x0binsuranceID\x18\x13 \x01(\tB\x1a\xaa\x02\x17TomTaw.eWordIMCIS.Protob\x06proto3'
  ,
  dependencies=[UserOrgInfoProto_dot_Proto__pb2.DESCRIPTOR,])




_PERSONALCHECKRCDINPUTPROTO = _descriptor.Descriptor(
  name='PersonalCheckRcdInputProto',
  full_name='PersonalCheckRcdInputProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='patientMasterID', full_name='PersonalCheckRcdInputProto.patientMasterID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='personExamUID', full_name='PersonalCheckRcdInputProto.personExamUID', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pageSize', full_name='PersonalCheckRcdInputProto.pageSize', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='currentPage', full_name='PersonalCheckRcdInputProto.currentPage', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='token', full_name='PersonalCheckRcdInputProto.token', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='isInteragency', full_name='PersonalCheckRcdInputProto.isInteragency', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='isInteragencyExam', full_name='PersonalCheckRcdInputProto.isInteragencyExam', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='isInteragencyClinic', full_name='PersonalCheckRcdInputProto.isInteragencyClinic', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='isInteragencyStatistic', full_name='PersonalCheckRcdInputProto.isInteragencyStatistic', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='userInfo', full_name='PersonalCheckRcdInputProto.userInfo', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='isInteragencyData', full_name='PersonalCheckRcdInputProto.isInteragencyData', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='examUID', full_name='PersonalCheckRcdInputProto.examUID', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='applyMethod', full_name='PersonalCheckRcdInputProto.applyMethod', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='isInterconnectData', full_name='PersonalCheckRcdInputProto.isInterconnectData', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='examToken', full_name='PersonalCheckRcdInputProto.examToken', index=14,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='accessionNumber', full_name='PersonalCheckRcdInputProto.accessionNumber', index=15,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='organizationID', full_name='PersonalCheckRcdInputProto.organizationID', index=16,
      number=17, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='iDCardNo', full_name='PersonalCheckRcdInputProto.iDCardNo', index=17,
      number=18, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='insuranceID', full_name='PersonalCheckRcdInputProto.insuranceID', index=18,
      number=19, type=9, cpp_type=9, label=1,
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
  serialized_start=61,
  serialized_end=539,
)

_PERSONALCHECKRCDINPUTPROTO.fields_by_name['userInfo'].message_type = UserOrgInfoProto_dot_Proto__pb2._USERORGINFOPROTO
DESCRIPTOR.message_types_by_name['PersonalCheckRcdInputProto'] = _PERSONALCHECKRCDINPUTPROTO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PersonalCheckRcdInputProto = _reflection.GeneratedProtocolMessageType('PersonalCheckRcdInputProto', (_message.Message,), {
  'DESCRIPTOR' : _PERSONALCHECKRCDINPUTPROTO,
  '__module__' : 'PersonalCheckRcdInputProto_pb2'
  # @@protoc_insertion_point(class_scope:PersonalCheckRcdInputProto)
  })
_sym_db.RegisterMessage(PersonalCheckRcdInputProto)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
