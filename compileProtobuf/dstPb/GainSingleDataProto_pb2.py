# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: GainSingleDataProto.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='GainSingleDataProto.proto',
  package='',
  syntax='proto3',
  serialized_options=b'\252\002\027TomTaw.eWordIMCIS.Proto',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x19GainSingleDataProto.proto\"B\n\x13GainSingleDataProto\x12\x17\n\x0f\x61\x63\x63\x65ssionNumber\x18\x01 \x01(\t\x12\x12\n\nserviceUID\x18\x02 \x01(\t\"S\n\x11GainFileDataProto\x12\x17\n\x0f\x61\x63\x63\x65ssionNumber\x18\x01 \x01(\t\x12\x0f\n\x07\x65xamUID\x18\x02 \x01(\t\x12\x14\n\x0c\x64ownloadType\x18\x03 \x01(\x05\"V\n\x18ResetBusinessStatusProto\x12\x17\n\x0f\x61\x63\x63\x65ssionNumber\x18\x01 \x01(\t\x12\x0f\n\x07\x65xamUID\x18\x02 \x01(\t\x12\x10\n\x08\x66ileType\x18\x03 \x01(\x05\x42\x1a\xaa\x02\x17TomTaw.eWordIMCIS.Protob\x06proto3'
)




_GAINSINGLEDATAPROTO = _descriptor.Descriptor(
  name='GainSingleDataProto',
  full_name='GainSingleDataProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='accessionNumber', full_name='GainSingleDataProto.accessionNumber', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='serviceUID', full_name='GainSingleDataProto.serviceUID', index=1,
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
  serialized_start=29,
  serialized_end=95,
)


_GAINFILEDATAPROTO = _descriptor.Descriptor(
  name='GainFileDataProto',
  full_name='GainFileDataProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='accessionNumber', full_name='GainFileDataProto.accessionNumber', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='examUID', full_name='GainFileDataProto.examUID', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='downloadType', full_name='GainFileDataProto.downloadType', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=97,
  serialized_end=180,
)


_RESETBUSINESSSTATUSPROTO = _descriptor.Descriptor(
  name='ResetBusinessStatusProto',
  full_name='ResetBusinessStatusProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='accessionNumber', full_name='ResetBusinessStatusProto.accessionNumber', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='examUID', full_name='ResetBusinessStatusProto.examUID', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fileType', full_name='ResetBusinessStatusProto.fileType', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=182,
  serialized_end=268,
)

DESCRIPTOR.message_types_by_name['GainSingleDataProto'] = _GAINSINGLEDATAPROTO
DESCRIPTOR.message_types_by_name['GainFileDataProto'] = _GAINFILEDATAPROTO
DESCRIPTOR.message_types_by_name['ResetBusinessStatusProto'] = _RESETBUSINESSSTATUSPROTO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GainSingleDataProto = _reflection.GeneratedProtocolMessageType('GainSingleDataProto', (_message.Message,), {
  'DESCRIPTOR' : _GAINSINGLEDATAPROTO,
  '__module__' : 'GainSingleDataProto_pb2'
  # @@protoc_insertion_point(class_scope:GainSingleDataProto)
  })
_sym_db.RegisterMessage(GainSingleDataProto)

GainFileDataProto = _reflection.GeneratedProtocolMessageType('GainFileDataProto', (_message.Message,), {
  'DESCRIPTOR' : _GAINFILEDATAPROTO,
  '__module__' : 'GainSingleDataProto_pb2'
  # @@protoc_insertion_point(class_scope:GainFileDataProto)
  })
_sym_db.RegisterMessage(GainFileDataProto)

ResetBusinessStatusProto = _reflection.GeneratedProtocolMessageType('ResetBusinessStatusProto', (_message.Message,), {
  'DESCRIPTOR' : _RESETBUSINESSSTATUSPROTO,
  '__module__' : 'GainSingleDataProto_pb2'
  # @@protoc_insertion_point(class_scope:ResetBusinessStatusProto)
  })
_sym_db.RegisterMessage(ResetBusinessStatusProto)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
