# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ServiceOutputProto.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ServiceOutputProto.proto',
  package='',
  syntax='proto3',
  serialized_options=b'\252\002\037TomTaw.eWordIMCIS.WebAPI.Models',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x18ServiceOutputProto.proto\"a\n\x12ServiceOutputProto\x12\x12\n\nserviceUID\x18\x01 \x01(\t\x12\x13\n\x0bserviceName\x18\x02 \x01(\t\x12\x10\n\x08ifEnable\x18\x03 \x01(\x08\x12\x10\n\x08ifDelete\x18\x04 \x01(\x08\x42\"\xaa\x02\x1fTomTaw.eWordIMCIS.WebAPI.Modelsb\x06proto3'
)




_SERVICEOUTPUTPROTO = _descriptor.Descriptor(
  name='ServiceOutputProto',
  full_name='ServiceOutputProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='serviceUID', full_name='ServiceOutputProto.serviceUID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='serviceName', full_name='ServiceOutputProto.serviceName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ifEnable', full_name='ServiceOutputProto.ifEnable', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ifDelete', full_name='ServiceOutputProto.ifDelete', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_end=125,
)

DESCRIPTOR.message_types_by_name['ServiceOutputProto'] = _SERVICEOUTPUTPROTO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ServiceOutputProto = _reflection.GeneratedProtocolMessageType('ServiceOutputProto', (_message.Message,), {
  'DESCRIPTOR' : _SERVICEOUTPUTPROTO,
  '__module__' : 'ServiceOutputProto_pb2'
  # @@protoc_insertion_point(class_scope:ServiceOutputProto)
  })
_sym_db.RegisterMessage(ServiceOutputProto)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
