# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: PrintInfoProto.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='PrintInfoProto.proto',
  package='',
  syntax='proto3',
  serialized_options=b'\252\002\027TomTaw.eWordIMCIS.Proto',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x14PrintInfoProto.proto\"\x8c\x01\n\x14PrintLogRequestProto\x12\x11\n\tpatientID\x18\x01 \x01(\t\x12\x12\n\nsourceType\x18\x02 \x01(\x05\x12\x16\n\x0eorganizationID\x18\x03 \x01(\t\x12\x11\n\toprerator\x18\x04 \x01(\t\x12\x11\n\trequestIP\x18\x05 \x01(\t\x12\x0f\n\x07\x65xamUID\x18\x06 \x01(\t\"{\n\x12PrintLogInputProto\x12\x16\n\x0eorganizationID\x18\x01 \x01(\t\x12\x11\n\toprerator\x18\x02 \x01(\t\x12\x13\n\x0boperateTime\x18\x03 \x01(\t\x12\x10\n\x08pageSize\x18\x04 \x01(\x05\x12\x13\n\x0b\x63urrentPage\x18\x05 \x01(\x05\"\xd3\x01\n\x17PrintLogRequestDtoProto\x12\x11\n\tpatientID\x18\x01 \x01(\t\x12\x12\n\nsourceType\x18\x02 \x01(\t\x12\x16\n\x0eorganizationID\x18\x03 \x01(\t\x12\x11\n\toprerator\x18\x04 \x01(\t\x12\x11\n\trequestIP\x18\x05 \x01(\t\x12\x0f\n\x07\x65xamUID\x18\x06 \x01(\t\x12\x13\n\x0bpatientName\x18\x07 \x01(\t\x12\x18\n\x10organizationName\x18\x08 \x01(\t\x12\x13\n\x0boperateTime\x18\t \x01(\tB\x1a\xaa\x02\x17TomTaw.eWordIMCIS.Protob\x06proto3'
)




_PRINTLOGREQUESTPROTO = _descriptor.Descriptor(
  name='PrintLogRequestProto',
  full_name='PrintLogRequestProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='patientID', full_name='PrintLogRequestProto.patientID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sourceType', full_name='PrintLogRequestProto.sourceType', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='organizationID', full_name='PrintLogRequestProto.organizationID', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='oprerator', full_name='PrintLogRequestProto.oprerator', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='requestIP', full_name='PrintLogRequestProto.requestIP', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='examUID', full_name='PrintLogRequestProto.examUID', index=5,
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
  serialized_start=25,
  serialized_end=165,
)


_PRINTLOGINPUTPROTO = _descriptor.Descriptor(
  name='PrintLogInputProto',
  full_name='PrintLogInputProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='organizationID', full_name='PrintLogInputProto.organizationID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='oprerator', full_name='PrintLogInputProto.oprerator', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='operateTime', full_name='PrintLogInputProto.operateTime', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pageSize', full_name='PrintLogInputProto.pageSize', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='currentPage', full_name='PrintLogInputProto.currentPage', index=4,
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
  serialized_start=167,
  serialized_end=290,
)


_PRINTLOGREQUESTDTOPROTO = _descriptor.Descriptor(
  name='PrintLogRequestDtoProto',
  full_name='PrintLogRequestDtoProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='patientID', full_name='PrintLogRequestDtoProto.patientID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sourceType', full_name='PrintLogRequestDtoProto.sourceType', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='organizationID', full_name='PrintLogRequestDtoProto.organizationID', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='oprerator', full_name='PrintLogRequestDtoProto.oprerator', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='requestIP', full_name='PrintLogRequestDtoProto.requestIP', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='examUID', full_name='PrintLogRequestDtoProto.examUID', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='patientName', full_name='PrintLogRequestDtoProto.patientName', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='organizationName', full_name='PrintLogRequestDtoProto.organizationName', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='operateTime', full_name='PrintLogRequestDtoProto.operateTime', index=8,
      number=9, type=9, cpp_type=9, label=1,
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
  serialized_start=293,
  serialized_end=504,
)

DESCRIPTOR.message_types_by_name['PrintLogRequestProto'] = _PRINTLOGREQUESTPROTO
DESCRIPTOR.message_types_by_name['PrintLogInputProto'] = _PRINTLOGINPUTPROTO
DESCRIPTOR.message_types_by_name['PrintLogRequestDtoProto'] = _PRINTLOGREQUESTDTOPROTO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PrintLogRequestProto = _reflection.GeneratedProtocolMessageType('PrintLogRequestProto', (_message.Message,), {
  'DESCRIPTOR' : _PRINTLOGREQUESTPROTO,
  '__module__' : 'PrintInfoProto_pb2'
  # @@protoc_insertion_point(class_scope:PrintLogRequestProto)
  })
_sym_db.RegisterMessage(PrintLogRequestProto)

PrintLogInputProto = _reflection.GeneratedProtocolMessageType('PrintLogInputProto', (_message.Message,), {
  'DESCRIPTOR' : _PRINTLOGINPUTPROTO,
  '__module__' : 'PrintInfoProto_pb2'
  # @@protoc_insertion_point(class_scope:PrintLogInputProto)
  })
_sym_db.RegisterMessage(PrintLogInputProto)

PrintLogRequestDtoProto = _reflection.GeneratedProtocolMessageType('PrintLogRequestDtoProto', (_message.Message,), {
  'DESCRIPTOR' : _PRINTLOGREQUESTDTOPROTO,
  '__module__' : 'PrintInfoProto_pb2'
  # @@protoc_insertion_point(class_scope:PrintLogRequestDtoProto)
  })
_sym_db.RegisterMessage(PrintLogRequestDtoProto)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
