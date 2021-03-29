# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: AuthorizeInfoProto.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='AuthorizeInfoProto.proto',
  package='',
  syntax='proto3',
  serialized_options=b'\252\002\027TomTaw.eWordIMCIS.Proto',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x18\x41uthorizeInfoProto.proto\"$\n\x13TokenMsgOutputProto\x12\r\n\x05token\x18\x01 \x01(\t\"\xc8\x01\n\x14\x41\x64minLoginInputProto\x12\x0f\n\x07\x61\x63\x63ount\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\x12\x16\n\x0eorganizationID\x18\x03 \x01(\t\x12\x12\n\nrememberMe\x18\x04 \x01(\t\x12\x0e\n\x06workNO\x18\x05 \x01(\t\x12\x11\n\tloginType\x18\x06 \x01(\x05\x12\x11\n\tuserAgent\x18\x07 \x01(\x05\x12\x10\n\x08userType\x18\x08 \x01(\x05\x12\x0b\n\x03key\x18\t \x01(\t\x12\x0c\n\x04\x63ode\x18\n \x01(\t\"\x97\x01\n\x16PatientLoginInputProto\x12\x13\n\x0bphoneNumber\x18\x01 \x01(\t\x12\x11\n\tloginType\x18\x02 \x01(\x05\x12\x11\n\tvalidCode\x18\x03 \x01(\t\x12\x17\n\x0f\x61\x63\x63\x65ssionNumber\x18\x04 \x01(\t\x12\x11\n\texamToken\x18\x05 \x01(\t\x12\x16\n\x0eorganizationID\x18\x06 \x01(\tB\x1a\xaa\x02\x17TomTaw.eWordIMCIS.Protob\x06proto3'
)




_TOKENMSGOUTPUTPROTO = _descriptor.Descriptor(
  name='TokenMsgOutputProto',
  full_name='TokenMsgOutputProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='TokenMsgOutputProto.token', index=0,
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
  serialized_start=28,
  serialized_end=64,
)


_ADMINLOGININPUTPROTO = _descriptor.Descriptor(
  name='AdminLoginInputProto',
  full_name='AdminLoginInputProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='account', full_name='AdminLoginInputProto.account', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='password', full_name='AdminLoginInputProto.password', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='organizationID', full_name='AdminLoginInputProto.organizationID', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rememberMe', full_name='AdminLoginInputProto.rememberMe', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='workNO', full_name='AdminLoginInputProto.workNO', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='loginType', full_name='AdminLoginInputProto.loginType', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='userAgent', full_name='AdminLoginInputProto.userAgent', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='userType', full_name='AdminLoginInputProto.userType', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='key', full_name='AdminLoginInputProto.key', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='code', full_name='AdminLoginInputProto.code', index=9,
      number=10, type=9, cpp_type=9, label=1,
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
  serialized_start=67,
  serialized_end=267,
)


_PATIENTLOGININPUTPROTO = _descriptor.Descriptor(
  name='PatientLoginInputProto',
  full_name='PatientLoginInputProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='phoneNumber', full_name='PatientLoginInputProto.phoneNumber', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='loginType', full_name='PatientLoginInputProto.loginType', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='validCode', full_name='PatientLoginInputProto.validCode', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='accessionNumber', full_name='PatientLoginInputProto.accessionNumber', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='examToken', full_name='PatientLoginInputProto.examToken', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='organizationID', full_name='PatientLoginInputProto.organizationID', index=5,
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
  serialized_start=270,
  serialized_end=421,
)

DESCRIPTOR.message_types_by_name['TokenMsgOutputProto'] = _TOKENMSGOUTPUTPROTO
DESCRIPTOR.message_types_by_name['AdminLoginInputProto'] = _ADMINLOGININPUTPROTO
DESCRIPTOR.message_types_by_name['PatientLoginInputProto'] = _PATIENTLOGININPUTPROTO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TokenMsgOutputProto = _reflection.GeneratedProtocolMessageType('TokenMsgOutputProto', (_message.Message,), {
  'DESCRIPTOR' : _TOKENMSGOUTPUTPROTO,
  '__module__' : 'AuthorizeInfoProto_pb2'
  # @@protoc_insertion_point(class_scope:TokenMsgOutputProto)
  })
_sym_db.RegisterMessage(TokenMsgOutputProto)

AdminLoginInputProto = _reflection.GeneratedProtocolMessageType('AdminLoginInputProto', (_message.Message,), {
  'DESCRIPTOR' : _ADMINLOGININPUTPROTO,
  '__module__' : 'AuthorizeInfoProto_pb2'
  # @@protoc_insertion_point(class_scope:AdminLoginInputProto)
  })
_sym_db.RegisterMessage(AdminLoginInputProto)

PatientLoginInputProto = _reflection.GeneratedProtocolMessageType('PatientLoginInputProto', (_message.Message,), {
  'DESCRIPTOR' : _PATIENTLOGININPUTPROTO,
  '__module__' : 'AuthorizeInfoProto_pb2'
  # @@protoc_insertion_point(class_scope:PatientLoginInputProto)
  })
_sym_db.RegisterMessage(PatientLoginInputProto)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
