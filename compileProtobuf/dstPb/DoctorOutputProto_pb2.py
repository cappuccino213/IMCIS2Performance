# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: DoctorOutputProto.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='DoctorOutputProto.proto',
  package='',
  syntax='proto3',
  serialized_options=b'\252\002\027TomTaw.eWordIMCIS.Proto',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x17\x44octorOutputProto.proto\"\x97\x01\n\x11\x44octorOutputProto\x12\x16\n\x0eorganizationID\x18\x01 \x01(\t\x12\x18\n\x10organizationName\x18\x02 \x01(\t\x12\x0e\n\x06\x64\x65ptID\x18\x03 \x01(\t\x12\x12\n\ndoctorName\x18\x04 \x01(\t\x12\x0f\n\x07userUID\x18\x05 \x01(\t\x12\x0c\n\x04type\x18\x06 \x01(\t\x12\r\n\x05value\x18\x07 \x01(\tB\x1a\xaa\x02\x17TomTaw.eWordIMCIS.Protob\x06proto3'
)




_DOCTOROUTPUTPROTO = _descriptor.Descriptor(
  name='DoctorOutputProto',
  full_name='DoctorOutputProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='organizationID', full_name='DoctorOutputProto.organizationID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='organizationName', full_name='DoctorOutputProto.organizationName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='deptID', full_name='DoctorOutputProto.deptID', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='doctorName', full_name='DoctorOutputProto.doctorName', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='userUID', full_name='DoctorOutputProto.userUID', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='DoctorOutputProto.type', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='DoctorOutputProto.value', index=6,
      number=7, type=9, cpp_type=9, label=1,
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
  serialized_start=28,
  serialized_end=179,
)

DESCRIPTOR.message_types_by_name['DoctorOutputProto'] = _DOCTOROUTPUTPROTO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DoctorOutputProto = _reflection.GeneratedProtocolMessageType('DoctorOutputProto', (_message.Message,), {
  'DESCRIPTOR' : _DOCTOROUTPUTPROTO,
  '__module__' : 'DoctorOutputProto_pb2'
  # @@protoc_insertion_point(class_scope:DoctorOutputProto)
  })
_sym_db.RegisterMessage(DoctorOutputProto)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
