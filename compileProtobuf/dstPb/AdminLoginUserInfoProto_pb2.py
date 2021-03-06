# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: AdminLoginUserInfoProto.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='AdminLoginUserInfoProto.proto',
  package='',
  syntax='proto3',
  serialized_options=b'\252\002\027TomTaw.eWordIMCIS.Proto',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1d\x41\x64minLoginUserInfoProto.proto\"\xff\x02\n\x17\x41\x64minLoginUserInfoProto\x12\x0f\n\x07userUID\x18\x01 \x01(\t\x12\x11\n\tloginName\x18\x02 \x01(\t\x12\x10\n\x08userName\x18\x03 \x01(\t\x12\x0e\n\x06workNO\x18\x04 \x01(\t\x12\x13\n\x0bofficePhone\x18\x05 \x01(\t\x12\x14\n\x0cprivatePhone\x18\x06 \x01(\t\x12\r\n\x05\x65mail\x18\x07 \x01(\t\x12\x16\n\x0eisSuperManager\x18\x08 \x01(\t\x12\x16\n\x0eorganizationID\x18\t \x01(\t\x12\x18\n\x10organizationName\x18\n \x01(\t\x12\x0e\n\x06\x64\x65ptID\x18\x0b \x01(\t\x12\x10\n\x08\x64\x65ptName\x18\x0c \x01(\t\x12!\n\tviewParts\x18\r \x03(\x0b\x32\x0e.ViewPartProto\x12%\n\tUserRight\x18\x0e \x01(\x0b\x32\x12.UserRightDtoProto\x12\x13\n\x0b\x61\x63\x63\x65ssToken\x18\x0f \x01(\t\x12\x19\n\x11isCurrentPageOpen\x18\x10 \x01(\t\"X\n\rViewPartProto\x12\x0b\n\x03url\x18\x01 \x01(\t\x12 \n\x08\x63hildren\x18\x02 \x03(\x0b\x32\x0e.ChildrenProto\x12\x18\n\x04meta\x18\x03 \x01(\x0b\x32\n.metaProto\"6\n\rChildrenProto\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\x18\n\x04meta\x18\x02 \x01(\x0b\x32\n.metaProto\"0\n\tmetaProto\x12\x14\n\x0crequiresAuth\x18\x01 \x01(\x08\x12\r\n\x05title\x18\x02 \x01(\t\"\xf3\x01\n\x11UserRightDtoProto\x12\x0f\n\x07userUID\x18\x01 \x01(\t\x12%\n\x08\x65xamInfo\x18\x02 \x01(\x0b\x32\x13.ExamInfoRightProto\x12)\n\nclinicInfo\x18\x03 \x01(\x0b\x32\x15.ClinicInfoRightProto\x12/\n\rstatisticInfo\x18\x04 \x01(\x0b\x32\x18.StatisticInfoRightProto\x12\x1d\n\x04\x64\x61ta\x18\x05 \x01(\x0b\x32\x0f.DataRightProto\x12+\n\x0breportPrint\x18\x06 \x01(\x0b\x32\x16.ReportPrintRightProto\"\x89\x01\n\x12\x45xamInfoRightProto\x12\x0f\n\x07visible\x18\x01 \x01(\t\x12\x15\n\rdoctorVisible\x18\x02 \x01(\t\x12\x19\n\x11\x64\x65partmentVisible\x18\x03 \x01(\t\x12\x1b\n\x13organizationVisible\x18\x04 \x01(\t\x12\x13\n\x0blistVisible\x18\x05 \x01(\t\"v\n\x14\x43linicInfoRightProto\x12\x0f\n\x07visible\x18\x01 \x01(\t\x12\x15\n\rdoctorVisible\x18\x02 \x01(\t\x12\x19\n\x11\x64\x65partmentVisible\x18\x03 \x01(\t\x12\x1b\n\x13organizationVisible\x18\x04 \x01(\t\"y\n\x17StatisticInfoRightProto\x12\x0f\n\x07visible\x18\x01 \x01(\t\x12\x15\n\rdoctorVisible\x18\x02 \x01(\t\x12\x19\n\x11\x64\x65partmentVisible\x18\x03 \x01(\t\x12\x1b\n\x13organizationVisible\x18\x04 \x01(\t\"\x99\x01\n\x0e\x44\x61taRightProto\x12\x16\n\x0erequestVisible\x18\x01 \x01(\t\x12\x15\n\rreportVisible\x18\x02 \x01(\t\x12\x14\n\x0cimageVisible\x18\x03 \x01(\t\x12\x13\n\x0b\x66ilmVisible\x18\x04 \x01(\t\x12\x14\n\x0cisOpenUpload\x18\x05 \x01(\t\x12\x17\n\x0f\x65\x64itExamVisible\x18\x06 \x01(\t\"/\n\x15ReportPrintRightProto\x12\x16\n\x0eServiceSectIDs\x18\x01 \x01(\tB\x1a\xaa\x02\x17TomTaw.eWordIMCIS.Protob\x06proto3'
)




_ADMINLOGINUSERINFOPROTO = _descriptor.Descriptor(
  name='AdminLoginUserInfoProto',
  full_name='AdminLoginUserInfoProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='userUID', full_name='AdminLoginUserInfoProto.userUID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='loginName', full_name='AdminLoginUserInfoProto.loginName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='userName', full_name='AdminLoginUserInfoProto.userName', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='workNO', full_name='AdminLoginUserInfoProto.workNO', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='officePhone', full_name='AdminLoginUserInfoProto.officePhone', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='privatePhone', full_name='AdminLoginUserInfoProto.privatePhone', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='email', full_name='AdminLoginUserInfoProto.email', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='isSuperManager', full_name='AdminLoginUserInfoProto.isSuperManager', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='organizationID', full_name='AdminLoginUserInfoProto.organizationID', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='organizationName', full_name='AdminLoginUserInfoProto.organizationName', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='deptID', full_name='AdminLoginUserInfoProto.deptID', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='deptName', full_name='AdminLoginUserInfoProto.deptName', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='viewParts', full_name='AdminLoginUserInfoProto.viewParts', index=12,
      number=13, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='UserRight', full_name='AdminLoginUserInfoProto.UserRight', index=13,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='accessToken', full_name='AdminLoginUserInfoProto.accessToken', index=14,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='isCurrentPageOpen', full_name='AdminLoginUserInfoProto.isCurrentPageOpen', index=15,
      number=16, type=9, cpp_type=9, label=1,
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
  serialized_start=34,
  serialized_end=417,
)


_VIEWPARTPROTO = _descriptor.Descriptor(
  name='ViewPartProto',
  full_name='ViewPartProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='url', full_name='ViewPartProto.url', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='children', full_name='ViewPartProto.children', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='meta', full_name='ViewPartProto.meta', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=419,
  serialized_end=507,
)


_CHILDRENPROTO = _descriptor.Descriptor(
  name='ChildrenProto',
  full_name='ChildrenProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='url', full_name='ChildrenProto.url', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='meta', full_name='ChildrenProto.meta', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=509,
  serialized_end=563,
)


_METAPROTO = _descriptor.Descriptor(
  name='metaProto',
  full_name='metaProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='requiresAuth', full_name='metaProto.requiresAuth', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='title', full_name='metaProto.title', index=1,
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
  serialized_start=565,
  serialized_end=613,
)


_USERRIGHTDTOPROTO = _descriptor.Descriptor(
  name='UserRightDtoProto',
  full_name='UserRightDtoProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='userUID', full_name='UserRightDtoProto.userUID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='examInfo', full_name='UserRightDtoProto.examInfo', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='clinicInfo', full_name='UserRightDtoProto.clinicInfo', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='statisticInfo', full_name='UserRightDtoProto.statisticInfo', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='UserRightDtoProto.data', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='reportPrint', full_name='UserRightDtoProto.reportPrint', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=616,
  serialized_end=859,
)


_EXAMINFORIGHTPROTO = _descriptor.Descriptor(
  name='ExamInfoRightProto',
  full_name='ExamInfoRightProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='visible', full_name='ExamInfoRightProto.visible', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='doctorVisible', full_name='ExamInfoRightProto.doctorVisible', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='departmentVisible', full_name='ExamInfoRightProto.departmentVisible', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='organizationVisible', full_name='ExamInfoRightProto.organizationVisible', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='listVisible', full_name='ExamInfoRightProto.listVisible', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
  serialized_start=862,
  serialized_end=999,
)


_CLINICINFORIGHTPROTO = _descriptor.Descriptor(
  name='ClinicInfoRightProto',
  full_name='ClinicInfoRightProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='visible', full_name='ClinicInfoRightProto.visible', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='doctorVisible', full_name='ClinicInfoRightProto.doctorVisible', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='departmentVisible', full_name='ClinicInfoRightProto.departmentVisible', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='organizationVisible', full_name='ClinicInfoRightProto.organizationVisible', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=1001,
  serialized_end=1119,
)


_STATISTICINFORIGHTPROTO = _descriptor.Descriptor(
  name='StatisticInfoRightProto',
  full_name='StatisticInfoRightProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='visible', full_name='StatisticInfoRightProto.visible', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='doctorVisible', full_name='StatisticInfoRightProto.doctorVisible', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='departmentVisible', full_name='StatisticInfoRightProto.departmentVisible', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='organizationVisible', full_name='StatisticInfoRightProto.organizationVisible', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=1121,
  serialized_end=1242,
)


_DATARIGHTPROTO = _descriptor.Descriptor(
  name='DataRightProto',
  full_name='DataRightProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='requestVisible', full_name='DataRightProto.requestVisible', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='reportVisible', full_name='DataRightProto.reportVisible', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='imageVisible', full_name='DataRightProto.imageVisible', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='filmVisible', full_name='DataRightProto.filmVisible', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='isOpenUpload', full_name='DataRightProto.isOpenUpload', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='editExamVisible', full_name='DataRightProto.editExamVisible', index=5,
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
  serialized_start=1245,
  serialized_end=1398,
)


_REPORTPRINTRIGHTPROTO = _descriptor.Descriptor(
  name='ReportPrintRightProto',
  full_name='ReportPrintRightProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ServiceSectIDs', full_name='ReportPrintRightProto.ServiceSectIDs', index=0,
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
  serialized_start=1400,
  serialized_end=1447,
)

_ADMINLOGINUSERINFOPROTO.fields_by_name['viewParts'].message_type = _VIEWPARTPROTO
_ADMINLOGINUSERINFOPROTO.fields_by_name['UserRight'].message_type = _USERRIGHTDTOPROTO
_VIEWPARTPROTO.fields_by_name['children'].message_type = _CHILDRENPROTO
_VIEWPARTPROTO.fields_by_name['meta'].message_type = _METAPROTO
_CHILDRENPROTO.fields_by_name['meta'].message_type = _METAPROTO
_USERRIGHTDTOPROTO.fields_by_name['examInfo'].message_type = _EXAMINFORIGHTPROTO
_USERRIGHTDTOPROTO.fields_by_name['clinicInfo'].message_type = _CLINICINFORIGHTPROTO
_USERRIGHTDTOPROTO.fields_by_name['statisticInfo'].message_type = _STATISTICINFORIGHTPROTO
_USERRIGHTDTOPROTO.fields_by_name['data'].message_type = _DATARIGHTPROTO
_USERRIGHTDTOPROTO.fields_by_name['reportPrint'].message_type = _REPORTPRINTRIGHTPROTO
DESCRIPTOR.message_types_by_name['AdminLoginUserInfoProto'] = _ADMINLOGINUSERINFOPROTO
DESCRIPTOR.message_types_by_name['ViewPartProto'] = _VIEWPARTPROTO
DESCRIPTOR.message_types_by_name['ChildrenProto'] = _CHILDRENPROTO
DESCRIPTOR.message_types_by_name['metaProto'] = _METAPROTO
DESCRIPTOR.message_types_by_name['UserRightDtoProto'] = _USERRIGHTDTOPROTO
DESCRIPTOR.message_types_by_name['ExamInfoRightProto'] = _EXAMINFORIGHTPROTO
DESCRIPTOR.message_types_by_name['ClinicInfoRightProto'] = _CLINICINFORIGHTPROTO
DESCRIPTOR.message_types_by_name['StatisticInfoRightProto'] = _STATISTICINFORIGHTPROTO
DESCRIPTOR.message_types_by_name['DataRightProto'] = _DATARIGHTPROTO
DESCRIPTOR.message_types_by_name['ReportPrintRightProto'] = _REPORTPRINTRIGHTPROTO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AdminLoginUserInfoProto = _reflection.GeneratedProtocolMessageType('AdminLoginUserInfoProto', (_message.Message,), {
  'DESCRIPTOR' : _ADMINLOGINUSERINFOPROTO,
  '__module__' : 'AdminLoginUserInfoProto_pb2'
  # @@protoc_insertion_point(class_scope:AdminLoginUserInfoProto)
  })
_sym_db.RegisterMessage(AdminLoginUserInfoProto)

ViewPartProto = _reflection.GeneratedProtocolMessageType('ViewPartProto', (_message.Message,), {
  'DESCRIPTOR' : _VIEWPARTPROTO,
  '__module__' : 'AdminLoginUserInfoProto_pb2'
  # @@protoc_insertion_point(class_scope:ViewPartProto)
  })
_sym_db.RegisterMessage(ViewPartProto)

ChildrenProto = _reflection.GeneratedProtocolMessageType('ChildrenProto', (_message.Message,), {
  'DESCRIPTOR' : _CHILDRENPROTO,
  '__module__' : 'AdminLoginUserInfoProto_pb2'
  # @@protoc_insertion_point(class_scope:ChildrenProto)
  })
_sym_db.RegisterMessage(ChildrenProto)

metaProto = _reflection.GeneratedProtocolMessageType('metaProto', (_message.Message,), {
  'DESCRIPTOR' : _METAPROTO,
  '__module__' : 'AdminLoginUserInfoProto_pb2'
  # @@protoc_insertion_point(class_scope:metaProto)
  })
_sym_db.RegisterMessage(metaProto)

UserRightDtoProto = _reflection.GeneratedProtocolMessageType('UserRightDtoProto', (_message.Message,), {
  'DESCRIPTOR' : _USERRIGHTDTOPROTO,
  '__module__' : 'AdminLoginUserInfoProto_pb2'
  # @@protoc_insertion_point(class_scope:UserRightDtoProto)
  })
_sym_db.RegisterMessage(UserRightDtoProto)

ExamInfoRightProto = _reflection.GeneratedProtocolMessageType('ExamInfoRightProto', (_message.Message,), {
  'DESCRIPTOR' : _EXAMINFORIGHTPROTO,
  '__module__' : 'AdminLoginUserInfoProto_pb2'
  # @@protoc_insertion_point(class_scope:ExamInfoRightProto)
  })
_sym_db.RegisterMessage(ExamInfoRightProto)

ClinicInfoRightProto = _reflection.GeneratedProtocolMessageType('ClinicInfoRightProto', (_message.Message,), {
  'DESCRIPTOR' : _CLINICINFORIGHTPROTO,
  '__module__' : 'AdminLoginUserInfoProto_pb2'
  # @@protoc_insertion_point(class_scope:ClinicInfoRightProto)
  })
_sym_db.RegisterMessage(ClinicInfoRightProto)

StatisticInfoRightProto = _reflection.GeneratedProtocolMessageType('StatisticInfoRightProto', (_message.Message,), {
  'DESCRIPTOR' : _STATISTICINFORIGHTPROTO,
  '__module__' : 'AdminLoginUserInfoProto_pb2'
  # @@protoc_insertion_point(class_scope:StatisticInfoRightProto)
  })
_sym_db.RegisterMessage(StatisticInfoRightProto)

DataRightProto = _reflection.GeneratedProtocolMessageType('DataRightProto', (_message.Message,), {
  'DESCRIPTOR' : _DATARIGHTPROTO,
  '__module__' : 'AdminLoginUserInfoProto_pb2'
  # @@protoc_insertion_point(class_scope:DataRightProto)
  })
_sym_db.RegisterMessage(DataRightProto)

ReportPrintRightProto = _reflection.GeneratedProtocolMessageType('ReportPrintRightProto', (_message.Message,), {
  'DESCRIPTOR' : _REPORTPRINTRIGHTPROTO,
  '__module__' : 'AdminLoginUserInfoProto_pb2'
  # @@protoc_insertion_point(class_scope:ReportPrintRightProto)
  })
_sym_db.RegisterMessage(ReportPrintRightProto)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
