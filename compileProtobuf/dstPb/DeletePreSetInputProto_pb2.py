# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: DeletePreSetInputProto.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='DeletePreSetInputProto.proto',
  package='',
  syntax='proto3',
  serialized_options=b'\252\002\037TomTaw.eWordIMCIS.WebAPI.Models',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1c\x44\x65letePreSetInputProto.proto\"*\n\x16\x44\x65letePreSetInputProto\x12\x10\n\x08querySeq\x18\x01 \x01(\x05\x42\"\xaa\x02\x1fTomTaw.eWordIMCIS.WebAPI.Modelsb\x06proto3'
)




_DELETEPRESETINPUTPROTO = _descriptor.Descriptor(
  name='DeletePreSetInputProto',
  full_name='DeletePreSetInputProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='querySeq', full_name='DeletePreSetInputProto.querySeq', index=0,
      number=1, type=5, cpp_type=1, label=1,
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
  serialized_start=32,
  serialized_end=74,
)

DESCRIPTOR.message_types_by_name['DeletePreSetInputProto'] = _DELETEPRESETINPUTPROTO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DeletePreSetInputProto = _reflection.GeneratedProtocolMessageType('DeletePreSetInputProto', (_message.Message,), {
  'DESCRIPTOR' : _DELETEPRESETINPUTPROTO,
  '__module__' : 'DeletePreSetInputProto_pb2'
  # @@protoc_insertion_point(class_scope:DeletePreSetInputProto)
  })
_sym_db.RegisterMessage(DeletePreSetInputProto)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
