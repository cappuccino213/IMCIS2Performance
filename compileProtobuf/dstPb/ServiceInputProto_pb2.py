# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ServiceInputProto.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ServiceInputProto.proto',
  package='',
  syntax='proto3',
  serialized_options=b'\252\002\037TomTaw.eWordIMCIS.WebAPI.Models',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x17ServiceInputProto.proto\"\x87\x01\n\x11ServiceInputProto\x12\x12\n\nserviceUID\x18\x01 \x01(\t\x12\x13\n\x0bserviceName\x18\x02 \x01(\t\x12\x10\n\x08ifEnable\x18\x03 \x01(\t\x12\x10\n\x08ifDelete\x18\x04 \x01(\t\x12\x10\n\x08pageSize\x18\x05 \x01(\x05\x12\x13\n\x0b\x63urrentPage\x18\x06 \x01(\x05\x42\"\xaa\x02\x1fTomTaw.eWordIMCIS.WebAPI.Modelsb\x06proto3'
)




_SERVICEINPUTPROTO = _descriptor.Descriptor(
  name='ServiceInputProto',
  full_name='ServiceInputProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='serviceUID', full_name='ServiceInputProto.serviceUID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='serviceName', full_name='ServiceInputProto.serviceName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ifEnable', full_name='ServiceInputProto.ifEnable', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ifDelete', full_name='ServiceInputProto.ifDelete', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pageSize', full_name='ServiceInputProto.pageSize', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='currentPage', full_name='ServiceInputProto.currentPage', index=5,
      number=6, type=5, cpp_type=1, label=1,
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
  serialized_start=28,
  serialized_end=163,
)

DESCRIPTOR.message_types_by_name['ServiceInputProto'] = _SERVICEINPUTPROTO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ServiceInputProto = _reflection.GeneratedProtocolMessageType('ServiceInputProto', (_message.Message,), {
  'DESCRIPTOR' : _SERVICEINPUTPROTO,
  '__module__' : 'ServiceInputProto_pb2'
  # @@protoc_insertion_point(class_scope:ServiceInputProto)
  })
_sym_db.RegisterMessage(ServiceInputProto)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
