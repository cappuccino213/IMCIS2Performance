# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: OrganizationDtoNewProto.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import DeptMstDtoNewProto_pb2 as DeptMstDtoNewProto__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='OrganizationDtoNewProto.proto',
  package='',
  syntax='proto3',
  serialized_options=b'\252\002\037TomTaw.eWordIMCIS.WebAPI.Models',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1dOrganizationDtoNewProto.proto\x1a\x18\x44\x65ptMstDtoNewProto.proto\"`\n\x17OrganizationDtoNewProto\x12\r\n\x05value\x18\x01 \x01(\t\x12\r\n\x05label\x18\x02 \x01(\t\x12\'\n\nDeptMstDto\x18\x03 \x03(\x0b\x32\x13.DeptMstDtoNewProtoB\"\xaa\x02\x1fTomTaw.eWordIMCIS.WebAPI.Modelsb\x06proto3'
  ,
  dependencies=[DeptMstDtoNewProto__pb2.DESCRIPTOR,])




_ORGANIZATIONDTONEWPROTO = _descriptor.Descriptor(
  name='OrganizationDtoNewProto',
  full_name='OrganizationDtoNewProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='OrganizationDtoNewProto.value', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='label', full_name='OrganizationDtoNewProto.label', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='DeptMstDto', full_name='OrganizationDtoNewProto.DeptMstDto', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=59,
  serialized_end=155,
)

_ORGANIZATIONDTONEWPROTO.fields_by_name['DeptMstDto'].message_type = DeptMstDtoNewProto__pb2._DEPTMSTDTONEWPROTO
DESCRIPTOR.message_types_by_name['OrganizationDtoNewProto'] = _ORGANIZATIONDTONEWPROTO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

OrganizationDtoNewProto = _reflection.GeneratedProtocolMessageType('OrganizationDtoNewProto', (_message.Message,), {
  'DESCRIPTOR' : _ORGANIZATIONDTONEWPROTO,
  '__module__' : 'OrganizationDtoNewProto_pb2'
  # @@protoc_insertion_point(class_scope:OrganizationDtoNewProto)
  })
_sym_db.RegisterMessage(OrganizationDtoNewProto)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
