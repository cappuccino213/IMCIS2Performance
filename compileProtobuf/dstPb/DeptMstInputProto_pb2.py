# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: DeptMstInputProto.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='DeptMstInputProto.proto',
  package='',
  syntax='proto3',
  serialized_options=b'\252\002\037TomTaw.eWordIMCIS.WebAPI.Models',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x17\x44\x65ptMstInputProto.proto\"z\n\x11\x44\x65ptMstInputProto\x12\x1c\n\x14searchOrganizationID\x18\x01 \x01(\t\x12\x0e\n\x06\x64\x65ptID\x18\x02 \x01(\t\x12\x10\n\x08\x64\x65ptName\x18\x03 \x01(\t\x12\x10\n\x08pageSize\x18\x04 \x01(\x05\x12\x13\n\x0b\x63urrentPage\x18\x05 \x01(\x05\x42\"\xaa\x02\x1fTomTaw.eWordIMCIS.WebAPI.Modelsb\x06proto3'
)




_DEPTMSTINPUTPROTO = _descriptor.Descriptor(
  name='DeptMstInputProto',
  full_name='DeptMstInputProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='searchOrganizationID', full_name='DeptMstInputProto.searchOrganizationID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='deptID', full_name='DeptMstInputProto.deptID', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='deptName', full_name='DeptMstInputProto.deptName', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pageSize', full_name='DeptMstInputProto.pageSize', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='currentPage', full_name='DeptMstInputProto.currentPage', index=4,
      number=5, type=5, cpp_type=1, label=1,
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
  serialized_start=27,
  serialized_end=149,
)

DESCRIPTOR.message_types_by_name['DeptMstInputProto'] = _DEPTMSTINPUTPROTO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DeptMstInputProto = _reflection.GeneratedProtocolMessageType('DeptMstInputProto', (_message.Message,), {
  'DESCRIPTOR' : _DEPTMSTINPUTPROTO,
  '__module__' : 'DeptMstInputProto_pb2'
  # @@protoc_insertion_point(class_scope:DeptMstInputProto)
  })
_sym_db.RegisterMessage(DeptMstInputProto)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
