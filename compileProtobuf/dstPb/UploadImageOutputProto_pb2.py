# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: UploadImageOutputProto.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='UploadImageOutputProto.proto',
  package='',
  syntax='proto3',
  serialized_options=b'\252\002\037TomTaw.eWordIMCIS.WebAPI.Models',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1cUploadImageOutputProto.proto\"2\n\x16UploadImageOutputProto\x12\x18\n\x10relativePathList\x18\x01 \x03(\tB\"\xaa\x02\x1fTomTaw.eWordIMCIS.WebAPI.Modelsb\x06proto3'
)




_UPLOADIMAGEOUTPUTPROTO = _descriptor.Descriptor(
  name='UploadImageOutputProto',
  full_name='UploadImageOutputProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='relativePathList', full_name='UploadImageOutputProto.relativePathList', index=0,
      number=1, type=9, cpp_type=9, label=3,
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
  serialized_start=32,
  serialized_end=82,
)

DESCRIPTOR.message_types_by_name['UploadImageOutputProto'] = _UPLOADIMAGEOUTPUTPROTO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UploadImageOutputProto = _reflection.GeneratedProtocolMessageType('UploadImageOutputProto', (_message.Message,), {
  'DESCRIPTOR' : _UPLOADIMAGEOUTPUTPROTO,
  '__module__' : 'UploadImageOutputProto_pb2'
  # @@protoc_insertion_point(class_scope:UploadImageOutputProto)
  })
_sym_db.RegisterMessage(UploadImageOutputProto)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)