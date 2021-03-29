/*eslint-disable block-scoped-var, id-length, no-control-regex, no-magic-numbers, no-prototype-builtins, no-redeclare, no-shadow, no-var, sort-vars*/
"use strict";

var $protobuf = require("protobufjs/light");

var $root = ($protobuf.roots["default"] || ($protobuf.roots["default"] = new $protobuf.Root()))
.setOptions({
  csharp_namespace: "TomTaw.eWordIMCIS.Proto"
})
.addJSON({
  AddOperateRecordInputProto: {
    fields: {
      organizationID: {
        type: "string",
        id: 1
      },
      requestURL: {
        type: "string",
        id: 2
      }
    }
  },
  AddRoleInputProto: {
    fields: {
      userUID: {
        type: "string",
        id: 1
      },
      searchOrganizationID: {
        type: "string",
        id: 2
      },
      right: {
        rule: "repeated",
        type: "RoleMstOutputProto",
        id: 3
      }
    }
  },
  RoleMstOutputProto: {
    fields: {
      roleUID: {
        type: "string",
        id: 1
      },
      roleName: {
        type: "string",
        id: 2
      },
      createUserUID: {
        type: "string",
        id: 3
      },
      createUserName: {
        type: "string",
        id: 4
      },
      createDate: {
        type: "string",
        id: 5
      },
      memo: {
        type: "string",
        id: 6
      },
      lAYChecked: {
        type: "string",
        id: 7
      },
      organizationID: {
        type: "string",
        id: 8
      },
      organizationName: {
        type: "string",
        id: 9
      }
    }
  },
  AdminChangePasswordInputProto: {
    fields: {
      userUID: {
        type: "string",
        id: 1
      },
      oldPassword: {
        type: "string",
        id: 2
      },
      newPassword: {
        type: "string",
        id: 3
      },
      cofirmPassword: {
        type: "string",
        id: 4
      }
    }
  },
  AdminLoginUserInfoProto: {
    fields: {
      userUID: {
        type: "string",
        id: 1
      },
      loginName: {
        type: "string",
        id: 2
      },
      userName: {
        type: "string",
        id: 3
      },
      workNO: {
        type: "string",
        id: 4
      },
      officePhone: {
        type: "string",
        id: 5
      },
      privatePhone: {
        type: "string",
        id: 6
      },
      email: {
        type: "string",
        id: 7
      },
      isSuperManager: {
        type: "string",
        id: 8
      },
      organizationID: {
        type: "string",
        id: 9
      },
      organizationName: {
        type: "string",
        id: 10
      },
      deptID: {
        type: "string",
        id: 11
      },
      deptName: {
        type: "string",
        id: 12
      },
      viewParts: {
        rule: "repeated",
        type: "ViewPartProto",
        id: 13
      },
      UserRight: {
        type: "UserRightDtoProto",
        id: 14
      },
      accessToken: {
        type: "string",
        id: 15
      },
      isCurrentPageOpen: {
        type: "string",
        id: 16
      }
    }
  },
  ViewPartProto: {
    fields: {
      url: {
        type: "string",
        id: 1
      },
      children: {
        rule: "repeated",
        type: "ChildrenProto",
        id: 2
      },
      meta: {
        type: "metaProto",
        id: 3
      }
    }
  },
  ChildrenProto: {
    fields: {
      url: {
        type: "string",
        id: 1
      },
      meta: {
        type: "metaProto",
        id: 2
      }
    }
  },
  metaProto: {
    fields: {
      requiresAuth: {
        type: "bool",
        id: 1
      },
      title: {
        type: "string",
        id: 2
      }
    }
  },
  UserRightDtoProto: {
    fields: {
      userUID: {
        type: "string",
        id: 1
      },
      examInfo: {
        type: "ExamInfoRightProto",
        id: 2
      },
      clinicInfo: {
        type: "ClinicInfoRightProto",
        id: 3
      },
      statisticInfo: {
        type: "StatisticInfoRightProto",
        id: 4
      },
      data: {
        type: "DataRightProto",
        id: 5
      },
      reportPrint: {
        type: "ReportPrintRightProto",
        id: 6
      }
    }
  },
  ExamInfoRightProto: {
    fields: {
      visible: {
        type: "string",
        id: 1
      },
      doctorVisible: {
        type: "string",
        id: 2
      },
      departmentVisible: {
        type: "string",
        id: 3
      },
      organizationVisible: {
        type: "string",
        id: 4
      },
      listVisible: {
        type: "string",
        id: 5
      }
    }
  },
  ClinicInfoRightProto: {
    fields: {
      visible: {
        type: "string",
        id: 1
      },
      doctorVisible: {
        type: "string",
        id: 2
      },
      departmentVisible: {
        type: "string",
        id: 3
      },
      organizationVisible: {
        type: "string",
        id: 4
      }
    }
  },
  StatisticInfoRightProto: {
    fields: {
      visible: {
        type: "string",
        id: 1
      },
      doctorVisible: {
        type: "string",
        id: 2
      },
      departmentVisible: {
        type: "string",
        id: 3
      },
      organizationVisible: {
        type: "string",
        id: 4
      }
    }
  },
  DataRightProto: {
    fields: {
      requestVisible: {
        type: "string",
        id: 1
      },
      reportVisible: {
        type: "string",
        id: 2
      },
      imageVisible: {
        type: "string",
        id: 3
      },
      filmVisible: {
        type: "string",
        id: 4
      },
      isOpenUpload: {
        type: "string",
        id: 5
      }
    }
  },
  ReportPrintRightProto: {
    fields: {
      ServiceSectIDs: {
        type: "string",
        id: 1
      }
    }
  },
  TokenMsgOutputProto: {
    fields: {
      token: {
        type: "string",
        id: 1
      }
    }
  },
  AdminLoginInputProto: {
    fields: {
      account: {
        type: "string",
        id: 1
      },
      password: {
        type: "string",
        id: 2
      },
      organizationID: {
        type: "string",
        id: 3
      },
      rememberMe: {
        type: "string",
        id: 4
      },
      workNO: {
        type: "string",
        id: 5
      },
      loginType: {
        type: "int32",
        id: 6
      },
      userAgent: {
        type: "int32",
        id: 7
      },
      userType: {
        type: "int32",
        id: 8
      },
      key: {
        type: "string",
        id: 9
      },
      code: {
        type: "string",
        id: 10
      }
    }
  },
  PatientLoginInputProto: {
    fields: {
      phoneNumber: {
        type: "string",
        id: 1
      },
      loginType: {
        type: "int32",
        id: 2
      },
      validCode: {
        type: "string",
        id: 3
      },
      accessionNumber: {
        type: "string",
        id: 4
      },
      examToken: {
        type: "string",
        id: 5
      },
      organizationID: {
        type: "string",
        id: 6
      }
    }
  },
  BaseResponse: {
    fields: {
      IsSuccess: {
        type: "bool",
        id: 1
      },
      Message: {
        type: "string",
        id: 2
      },
      Token: {
        type: "string",
        id: 3
      },
      data: {
        type: "google.protobuf.Any",
        id: 4
      }
    }
  },
  google: {
    nested: {
      protobuf: {
        nested: {
          Any: {
            fields: {
              type_url: {
                type: "string",
                id: 1
              },
              value: {
                type: "bytes",
                id: 2
              }
            }
          }
        }
      }
    }
  },
  PluginInfoProto: {
    fields: {
      pluginUID: {
        type: "string",
        id: 1
      },
      pluginName: {
        type: "string",
        id: 2
      },
      dllName: {
        type: "string",
        id: 3
      },
      className: {
        type: "string",
        id: 4
      },
      description: {
        type: "string",
        id: 5
      },
      pluginType: {
        type: "string",
        id: 6
      },
      BasicFormProto: {
        rule: "repeated",
        type: "BasicFormProto",
        id: 7
      }
    }
  },
  BasicFormProto: {
    fields: {
      type: {
        type: "string",
        id: 1
      },
      label: {
        type: "string",
        id: 2
      },
      prop: {
        type: "string",
        id: 3
      },
      opt: {
        rule: "repeated",
        type: "OptionProto",
        id: 4
      },
      linkFlag: {
        type: "string",
        id: 5
      },
      fieldDescription: {
        type: "string",
        id: 6
      },
      dataDefault: {
        type: "string",
        id: 7
      }
    }
  },
  PluginInfoDtoProto: {
    fields: {
      serviceUID: {
        type: "string",
        id: 1
      },
      pluginUID: {
        type: "string",
        id: 2
      },
      ifEnable: {
        type: "bool",
        id: 3
      },
      pluginName: {
        type: "string",
        id: 4
      },
      BasicFormConfigProto: {
        rule: "repeated",
        type: "BasicFormConfigProto",
        id: 5
      }
    }
  },
  PluginInfoDtoMstProto: {
    fields: {
      serviceUID: {
        type: "string",
        id: 1
      },
      pluginUID: {
        type: "string",
        id: 2
      },
      ifEnable: {
        type: "bool",
        id: 3
      },
      pluginName: {
        type: "string",
        id: 4
      },
      triggerTimes: {
        type: "string",
        id: 5
      },
      BasicFormConfigProto: {
        rule: "repeated",
        type: "BasicFormConfigProto",
        id: 6
      }
    }
  },
  BasicFormConfigProto: {
    fields: {
      type: {
        type: "string",
        id: 1
      },
      label: {
        type: "string",
        id: 2
      },
      prop: {
        type: "string",
        id: 3
      },
      opt: {
        rule: "repeated",
        type: "OptionProto",
        id: 4
      },
      linkFlag: {
        type: "string",
        id: 5
      },
      fieldDescription: {
        type: "string",
        id: 6
      },
      data: {
        type: "string",
        id: 7
      },
      pluginConfigUID: {
        type: "string",
        id: 8
      }
    }
  },
  OptionProto: {
    fields: {
      label: {
        type: "string",
        id: 1
      },
      prop: {
        type: "string",
        id: 2
      }
    }
  },
  CheckInfoDtoProto: {
    fields: {
      id: {
        type: "string",
        id: 1
      },
      patientName: {
        type: "string",
        id: 2
      },
      gender: {
        type: "string",
        id: 3
      },
      age: {
        type: "int32",
        id: 4
      },
      ageUnit: {
        type: "string",
        id: 5
      },
      birthDay: {
        type: "string",
        id: 6
      },
      iDCardNo: {
        type: "string",
        id: 7
      },
      serviceSectID: {
        type: "string",
        id: 8
      },
      examItem: {
        type: "string",
        id: 9
      },
      checkArea: {
        type: "string",
        id: 10
      },
      medRecNO: {
        type: "string",
        id: 11
      },
      patientClass: {
        type: "string",
        id: 12
      },
      visitID: {
        type: "string",
        id: 13
      },
      alternateVisitID: {
        type: "string",
        id: 14
      },
      outPatientID: {
        type: "string",
        id: 15
      },
      pointOfCareID: {
        type: "string",
        id: 16
      },
      pointOfCare: {
        type: "string",
        id: 17
      },
      bed: {
        type: "string",
        id: 18
      },
      organizationName: {
        type: "string",
        id: 19
      },
      requestOrgName: {
        type: "string",
        id: 20
      },
      requestDept: {
        type: "string",
        id: 21
      },
      requestDocName: {
        type: "string",
        id: 22
      },
      requestTime: {
        type: "string",
        id: 23
      },
      regTime: {
        type: "string",
        id: 24
      },
      examTime: {
        type: "string",
        id: 25
      },
      examEndDate: {
        type: "string",
        id: 26
      },
      resultDate: {
        type: "string",
        id: 27
      },
      auditDate: {
        type: "string",
        id: 28
      },
      reviseDate: {
        type: "string",
        id: 29
      },
      patientID: {
        type: "string",
        id: 30
      },
      accessionNumber: {
        type: "string",
        id: 31
      },
      abnormalFlags: {
        type: "string",
        id: 32
      },
      criticalValue: {
        type: "string",
        id: 33
      },
      consultationStatus: {
        type: "string",
        id: 34
      },
      consultRequestDate: {
        type: "string",
        id: 35
      },
      consultEndDate: {
        type: "string",
        id: 36
      },
      ifHasImage: {
        type: "string",
        id: 37
      },
      examStatus: {
        type: "string",
        id: 38
      },
      examCode: {
        type: "string",
        id: 39
      },
      clinicDiagnosis: {
        type: "string",
        id: 40
      },
      placerOrderNO: {
        type: "string",
        id: 41
      },
      reason: {
        type: "string",
        id: 42
      },
      contactPhoneNO: {
        type: "string",
        id: 43
      },
      symptom: {
        type: "string",
        id: 44
      },
      patientMasterID: {
        type: "string",
        id: 45
      },
      examUID: {
        type: "string",
        id: 46
      },
      resultStatus: {
        type: "string",
        id: 47
      },
      studyInstanceUID: {
        type: "string",
        id: 48
      },
      otherClinicalInfo: {
        type: "string",
        id: 49
      },
      attention: {
        type: "string",
        id: 50
      },
      resultReviseName: {
        type: "string",
        id: 51
      },
      ifHasReport: {
        type: "string",
        id: 52
      },
      digitalimageneed: {
        type: "string",
        id: 53
      },
      examMethod: {
        type: "string",
        id: 54
      },
      organizationID: {
        type: "string",
        id: 55
      },
      pIDAssigningAuthority: {
        type: "string",
        id: 56
      },
      ageAndUnit: {
        type: "string",
        id: 57
      },
      lockFlag: {
        type: "string",
        id: 58
      },
      examUploadFlag: {
        type: "string",
        id: 59
      },
      reportUploadFlag: {
        type: "string",
        id: 60
      },
      imageUploadFlag: {
        type: "string",
        id: 61
      },
      filmUploadFlag: {
        type: "string",
        id: 62
      },
      isInterconnectData: {
        type: "string",
        id: 63
      },
      displayAge: {
        type: "string",
        id: 64
      },
      isCanPrint: {
        type: "string",
        id: 65
      },
      resultPrintCount: {
        type: "int32",
        id: 66
      },
      resultSelfPrintCount: {
        type: "int32",
        id: 67
      },
      insuranceID: {
        type: "string",
        id: 68
      },
      qrCodeUrl: {
        type: "string",
        id: 69
      }
    }
  },
  SearchInputProto: {
    fields: {
      patientName: {
        type: "string",
        id: 1
      },
      gender: {
        type: "string",
        id: 2
      },
      age: {
        type: "int32",
        id: 3
      },
      ageUnit: {
        type: "string",
        id: 4
      },
      birthDay: {
        type: "string",
        id: 5
      },
      iDCardNo: {
        type: "string",
        id: 6
      },
      medRecNO: {
        type: "string",
        id: 7
      },
      visitID: {
        type: "string",
        id: 8
      },
      alternateVisitID: {
        type: "string",
        id: 9
      },
      outPatientID: {
        type: "string",
        id: 10
      },
      patientClass: {
        type: "string",
        id: 11
      },
      requestDeptID: {
        type: "string",
        id: 12
      },
      requestDocName: {
        type: "string",
        id: 13
      },
      accessionNumber: {
        type: "string",
        id: 14
      },
      organizationID: {
        type: "string",
        id: 15
      },
      organizationIDPerson: {
        type: "string",
        id: 16
      },
      serviceSectID: {
        type: "string",
        id: 17
      },
      resultAssistantName: {
        type: "string",
        id: 18
      },
      examStartTime: {
        type: "string",
        id: 19
      },
      examEndTime: {
        type: "string",
        id: 20
      },
      registerStartTime: {
        type: "string",
        id: 21
      },
      registerEndTime: {
        type: "string",
        id: 22
      },
      resultStartDate: {
        type: "string",
        id: 23
      },
      resultEndDate: {
        type: "string",
        id: 24
      },
      requestStartTime: {
        type: "string",
        id: 25
      },
      requestEndTime: {
        type: "string",
        id: 26
      },
      consultRequestStartDate: {
        type: "string",
        id: 27
      },
      consultRequestEndDate: {
        type: "string",
        id: 28
      },
      consultEndDateStart: {
        type: "string",
        id: 29
      },
      consultEndDateEnd: {
        type: "string",
        id: 30
      },
      appointmentSaveStartDate: {
        type: "string",
        id: 31
      },
      appointmentSaveEndDate: {
        type: "string",
        id: 32
      },
      lastUpdateStartDate: {
        type: "string",
        id: 33
      },
      lastUpdateEndDate: {
        type: "string",
        id: 34
      },
      examStatus: {
        type: "string",
        id: 35
      },
      ifHasImage: {
        type: "string",
        id: 36
      },
      resultPrintCount: {
        type: "string",
        id: 37
      },
      criticalValue: {
        type: "string",
        id: 38
      },
      patientMasterID: {
        type: "string",
        id: 39
      },
      examUID: {
        type: "string",
        id: 40
      },
      personExamUID: {
        type: "string",
        id: 41
      },
      quickSearch: {
        type: "string",
        id: 42
      },
      pageSize: {
        type: "int32",
        id: 43
      },
      currentPage: {
        type: "int32",
        id: 44
      },
      token: {
        type: "string",
        id: 45
      },
      isInteragency: {
        type: "string",
        id: 46
      },
      isInteragencyExam: {
        type: "string",
        id: 47
      },
      isInteragencyClinic: {
        type: "string",
        id: 48
      },
      isInteragencyStatistic: {
        type: "string",
        id: 49
      },
      userInfo: {
        type: "UserOrgInfoProto",
        id: 50
      },
      isInteragencyData: {
        type: "string",
        id: 51
      },
      outPatientNO: {
        type: "string",
        id: 52
      },
      inPatientNO: {
        type: "string",
        id: 53
      },
      contactPhoneNO: {
        type: "string",
        id: 54
      },
      ifHasReport: {
        type: "string",
        id: 55
      },
      digitalimageneed: {
        type: "string",
        id: 56
      },
      auditStartDate: {
        type: "string",
        id: 57
      },
      auditEndDate: {
        type: "string",
        id: 58
      },
      patientId: {
        type: "string",
        id: 59
      }
    }
  },
  UserQuerySetMstDtoProto: {
    fields: {
      querySeq: {
        type: "int32",
        id: 1
      },
      queryType: {
        type: "string",
        id: 2
      },
      userUID: {
        type: "string",
        id: 3
      },
      name: {
        type: "string",
        id: 4
      },
      queryCondition: {
        type: "string",
        id: 5
      },
      sortNO: {
        type: "int32",
        id: 6
      },
      defaultFlag: {
        type: "string",
        id: 7
      },
      publicFlag: {
        type: "string",
        id: 8
      },
      userInfo: {
        type: "UserOrgInfoProto",
        id: 9
      }
    }
  },
  UserOrgInfoProto: {
    fields: {
      userUID: {
        type: "string",
        id: 1
      },
      deptID: {
        type: "string",
        id: 2
      },
      deptName: {
        type: "string",
        id: 3
      },
      organizationID: {
        type: "string",
        id: 4
      },
      organizationName: {
        type: "string",
        id: 5
      },
      isSuperManager: {
        type: "string",
        id: 6
      },
      loginName: {
        type: "string",
        id: 7
      },
      userName: {
        type: "string",
        id: 8
      },
      workNO: {
        type: "string",
        id: 9
      },
      officePhone: {
        type: "string",
        id: 10
      },
      privatePhone: {
        type: "string",
        id: 11
      },
      email: {
        type: "string",
        id: 12
      }
    }
  },
  ClinicDtoInputProto: {
    fields: {
      patientMasterID: {
        type: "string",
        id: 1
      },
      visitUID: {
        type: "string",
        id: 2
      },
      pageSize: {
        type: "int32",
        id: 3
      },
      currentPage: {
        type: "int32",
        id: 4
      },
      token: {
        type: "string",
        id: 5
      },
      isInteragency: {
        type: "string",
        id: 6
      },
      isInteragencyExam: {
        type: "string",
        id: 7
      },
      isInteragencyClinic: {
        type: "string",
        id: 8
      },
      isInteragencyStatistic: {
        type: "string",
        id: 9
      },
      userInfo: {
        type: "UserOrgInfoProto",
        id: 10
      },
      isInteragencyData: {
        type: "string",
        id: 11
      },
      orgnizationID: {
        type: "string",
        id: 12
      }
    }
  },
  ClinicDtoProto: {
    fields: {
      obRequestExamCount: {
        type: "int32",
        id: 1
      },
      obRequestLabCount: {
        type: "int32",
        id: 2
      },
      medicalRecordCount: {
        type: "int32",
        id: 3
      },
      obRequestExam: {
        rule: "repeated",
        type: "ExamRequestDtoProto",
        id: 4
      },
      obRequestLab: {
        rule: "repeated",
        type: "ExamRequestProto",
        id: 5
      },
      medicalRecord: {
        rule: "repeated",
        type: "MedicalDtoProto",
        id: 6
      }
    }
  },
  ExamRequestDtoProto: {
    fields: {
      examUID: {
        type: "string",
        id: 1
      },
      patientID: {
        type: "string",
        id: 2
      },
      pIDAssigningAuthority: {
        type: "string",
        id: 3
      },
      patientMasterID: {
        type: "string",
        id: 4
      },
      patientClass: {
        type: "string",
        id: 5
      },
      visitUID: {
        type: "string",
        id: 6
      },
      orderUID: {
        type: "string",
        id: 7
      },
      organizationID: {
        type: "string",
        id: 8
      },
      placerOrderNO: {
        type: "string",
        id: 9
      },
      placerAssigningAuthority: {
        type: "string",
        id: 10
      },
      placerOrderDetailNO: {
        type: "string",
        id: 11
      },
      fillerOrderNO: {
        type: "string",
        id: 12
      },
      fillerAssigningAuthority: {
        type: "string",
        id: 13
      },
      fillerPatientID: {
        type: "string",
        id: 14
      },
      accessionNumber: {
        type: "string",
        id: 15
      },
      serviceID: {
        type: "string",
        id: 16
      },
      serviceCodeScheme: {
        type: "string",
        id: 17
      },
      serviceText: {
        type: "string",
        id: 18
      },
      serviceIDInsur: {
        type: "string",
        id: 19
      },
      serviceSectID: {
        type: "string",
        id: 20
      },
      procedureID: {
        type: "string",
        id: 21
      },
      procedureName: {
        type: "string",
        id: 22
      },
      providerID: {
        type: "string",
        id: 23
      },
      providerName: {
        type: "string",
        id: 24
      },
      providerPhone: {
        type: "string",
        id: 25
      },
      requestDeptID: {
        type: "string",
        id: 26
      },
      requestDeptName: {
        type: "string",
        id: 27
      },
      requestOrgID: {
        type: "string",
        id: 28
      },
      requestOrgName: {
        type: "string",
        id: 29
      },
      requestedDate: {
        type: "string",
        id: 30
      },
      reason: {
        type: "string",
        id: 31
      },
      attention: {
        type: "string",
        id: 32
      },
      symptom: {
        type: "string",
        id: 33
      },
      adverseReaction: {
        type: "string",
        id: 34
      },
      clinicDiagnosis: {
        type: "string",
        id: 35
      },
      relevantClinicalInfo: {
        type: "string",
        id: 36
      },
      fastingFlag: {
        type: "string",
        id: 37
      },
      transportationMode: {
        type: "string",
        id: 38
      },
      regTime: {
        type: "string",
        id: 39
      },
      registerID: {
        type: "string",
        id: 40
      },
      registerName: {
        type: "string",
        id: 41
      },
      examDeptID: {
        type: "string",
        id: 42
      },
      examDeptName: {
        type: "string",
        id: 43
      },
      examDate: {
        type: "string",
        id: 44
      },
      examEndDate: {
        type: "string",
        id: 45
      },
      examLocation: {
        type: "string",
        id: 46
      },
      examEquipmentID: {
        type: "string",
        id: 47
      },
      examEquipment: {
        type: "string",
        id: 48
      },
      equipmentModel: {
        type: "string",
        id: 49
      },
      examMethod: {
        type: "string",
        id: 50
      },
      studyInstanceUID: {
        type: "string",
        id: 51
      },
      technicianID: {
        type: "string",
        id: 52
      },
      technicianName: {
        type: "string",
        id: 53
      },
      resultAssistantID: {
        type: "string",
        id: 54
      },
      resultAssistantName: {
        type: "string",
        id: 55
      },
      resultPrincipalID: {
        type: "string",
        id: 56
      },
      resultPrincipalName: {
        type: "string",
        id: 57
      },
      resultReviseID: {
        type: "string",
        id: 58
      },
      resultReviseName: {
        type: "string",
        id: 59
      },
      preliminaryDate: {
        type: "string",
        id: 60
      },
      auditDate: {
        type: "string",
        id: 61
      },
      reviseDate: {
        type: "string",
        id: 62
      },
      resultDate: {
        type: "string",
        id: 63
      },
      resultOrganizationID: {
        type: "string",
        id: 64
      },
      resultServiceCenterUID: {
        type: "string",
        id: 65
      },
      resultStatus: {
        type: "string",
        id: 66
      },
      resultStatusCode: {
        type: "string",
        id: 67
      },
      resultPrintCount: {
        type: "string",
        id: 68
      },
      resultPrintTime: {
        type: "string",
        id: 69
      },
      abnormalFlags: {
        type: "string",
        id: 70
      },
      criticalValue: {
        type: "string",
        id: 71
      },
      infectionName: {
        type: "string",
        id: 72
      },
      privacyLevel: {
        type: "string",
        id: 73
      },
      privacyLevelExt: {
        type: "string",
        id: 74
      },
      charges: {
        type: "string",
        id: 75
      },
      payments: {
        type: "string",
        id: 76
      },
      paymentsFlag: {
        type: "string",
        id: 77
      },
      filmCount: {
        type: "string",
        id: 78
      },
      filmNeed: {
        type: "string",
        id: 79
      },
      hasImage: {
        type: "string",
        id: 80
      },
      imageLocation: {
        type: "string",
        id: 81
      },
      consultStatus: {
        type: "string",
        id: 82
      },
      consultRequestDate: {
        type: "string",
        id: 83
      },
      consultEndDate: {
        type: "string",
        id: 84
      },
      lastUpdateDate: {
        type: "string",
        id: 85
      },
      dataSource: {
        type: "string",
        id: 86
      },
      lockFlag: {
        type: "string",
        id: 87
      },
      lockUserUID: {
        type: "string",
        id: 88
      },
      lockReason: {
        type: "string",
        id: 89
      },
      inWritingUserUID: {
        type: "string",
        id: 90
      },
      messageCount: {
        type: "string",
        id: 91
      },
      unProcessWorkflowCount: {
        type: "string",
        id: 92
      },
      pushState: {
        type: "string",
        id: 93
      },
      deleteFlag: {
        type: "string",
        id: 94
      },
      rowTimestamp: {
        type: "string",
        id: 95
      },
      groupID: {
        type: "string",
        id: 96
      },
      resultSelfPrintCount: {
        type: "string",
        id: 97
      },
      careWorkerID: {
        type: "string",
        id: 98
      },
      careWorkerName: {
        type: "string",
        id: 99
      },
      escortResultStatus: {
        type: "string",
        id: 100
      },
      drugDose: {
        type: "string",
        id: 101
      },
      medicalRecord: {
        type: "string",
        id: 102
      },
      physicalExam: {
        type: "string",
        id: 103
      },
      requestMemo: {
        type: "string",
        id: 104
      },
      idcasState: {
        type: "string",
        id: 105
      },
      multiDrugFastFlag: {
        type: "string",
        id: 106
      },
      priorityFlag: {
        type: "string",
        id: 107
      },
      providerIDCardNO: {
        type: "string",
        id: 108
      },
      height: {
        type: "string",
        id: 109
      },
      weight: {
        type: "string",
        id: 110
      },
      metalFlag: {
        type: "string",
        id: 111
      },
      operationDate: {
        type: "string",
        id: 112
      },
      surgeryFindings: {
        type: "string",
        id: 113
      },
      surgeryExam: {
        type: "string",
        id: 114
      },
      pastHistory: {
        type: "string",
        id: 115
      },
      clinicInfoType: {
        type: "string",
        id: 116
      },
      requestDocName: {
        type: "string",
        id: 117
      },
      uploadFlag: {
        type: "string",
        id: 118
      },
      patientName: {
        type: "string",
        id: 119
      }
    }
  },
  ExamRequestProto: {
    fields: {
      examUID: {
        type: "string",
        id: 1
      },
      patientID: {
        type: "string",
        id: 2
      },
      pIDAssigningAuthority: {
        type: "string",
        id: 3
      },
      patientMasterID: {
        type: "string",
        id: 4
      },
      patientClass: {
        type: "string",
        id: 5
      },
      visitUID: {
        type: "string",
        id: 6
      },
      orderUID: {
        type: "string",
        id: 7
      },
      organizationID: {
        type: "string",
        id: 8
      },
      placerOrderNO: {
        type: "string",
        id: 9
      },
      placerAssigningAuthority: {
        type: "string",
        id: 10
      },
      placerOrderDetailNO: {
        type: "string",
        id: 11
      },
      fillerOrderNO: {
        type: "string",
        id: 12
      },
      fillerAssigningAuthority: {
        type: "string",
        id: 13
      },
      fillerPatientID: {
        type: "string",
        id: 14
      },
      accessionNumber: {
        type: "string",
        id: 15
      },
      serviceID: {
        type: "string",
        id: 16
      },
      serviceCodeScheme: {
        type: "string",
        id: 17
      },
      serviceText: {
        type: "string",
        id: 18
      },
      serviceIDInsur: {
        type: "string",
        id: 19
      },
      serviceSectID: {
        type: "string",
        id: 20
      },
      procedureID: {
        type: "string",
        id: 21
      },
      procedureName: {
        type: "string",
        id: 22
      },
      providerID: {
        type: "string",
        id: 23
      },
      providerName: {
        type: "string",
        id: 24
      },
      providerPhone: {
        type: "string",
        id: 25
      },
      requestDeptID: {
        type: "string",
        id: 26
      },
      requestDeptName: {
        type: "string",
        id: 27
      },
      requestOrgID: {
        type: "string",
        id: 28
      },
      requestOrgName: {
        type: "string",
        id: 29
      },
      requestedDate: {
        type: "string",
        id: 30
      },
      reason: {
        type: "string",
        id: 31
      },
      attention: {
        type: "string",
        id: 32
      },
      symptom: {
        type: "string",
        id: 33
      },
      adverseReaction: {
        type: "string",
        id: 34
      },
      clinicDiagnosis: {
        type: "string",
        id: 35
      },
      relevantClinicalInfo: {
        type: "string",
        id: 36
      },
      fastingFlag: {
        type: "string",
        id: 37
      },
      transportationMode: {
        type: "string",
        id: 38
      },
      regTime: {
        type: "string",
        id: 39
      },
      registerID: {
        type: "string",
        id: 40
      },
      registerName: {
        type: "string",
        id: 41
      },
      examDeptID: {
        type: "string",
        id: 42
      },
      examDeptName: {
        type: "string",
        id: 43
      },
      examDate: {
        type: "string",
        id: 44
      },
      examEndDate: {
        type: "string",
        id: 45
      },
      examLocation: {
        type: "string",
        id: 46
      },
      examEquipmentID: {
        type: "string",
        id: 47
      },
      examEquipment: {
        type: "string",
        id: 48
      },
      equipmentModel: {
        type: "string",
        id: 49
      },
      examMethod: {
        type: "string",
        id: 50
      },
      studyInstanceUID: {
        type: "string",
        id: 51
      },
      technicianID: {
        type: "string",
        id: 52
      },
      technicianName: {
        type: "string",
        id: 53
      },
      resultAssistantID: {
        type: "string",
        id: 54
      },
      resultAssistantName: {
        type: "string",
        id: 55
      },
      resultPrincipalID: {
        type: "string",
        id: 56
      },
      resultPrincipalName: {
        type: "string",
        id: 57
      },
      resultReviseID: {
        type: "string",
        id: 58
      },
      resultReviseName: {
        type: "string",
        id: 59
      },
      preliminaryDate: {
        type: "string",
        id: 60
      },
      auditDate: {
        type: "string",
        id: 61
      },
      reviseDate: {
        type: "string",
        id: 62
      },
      resultDate: {
        type: "string",
        id: 63
      },
      resultOrganizationID: {
        type: "string",
        id: 64
      },
      resultServiceCenterUID: {
        type: "string",
        id: 65
      },
      resultStatus: {
        type: "string",
        id: 66
      },
      resultStatusCode: {
        type: "string",
        id: 67
      },
      resultPrintCount: {
        type: "string",
        id: 68
      },
      resultPrintTime: {
        type: "string",
        id: 69
      },
      abnormalFlags: {
        type: "string",
        id: 70
      },
      criticalValue: {
        type: "string",
        id: 71
      },
      infectionName: {
        type: "string",
        id: 72
      },
      privacyLevel: {
        type: "string",
        id: 73
      },
      privacyLevelExt: {
        type: "string",
        id: 74
      },
      charges: {
        type: "string",
        id: 75
      },
      payments: {
        type: "string",
        id: 76
      },
      paymentsFlag: {
        type: "string",
        id: 77
      },
      filmCount: {
        type: "string",
        id: 78
      },
      filmNeed: {
        type: "string",
        id: 79
      },
      hasImage: {
        type: "string",
        id: 80
      },
      imageLocation: {
        type: "string",
        id: 81
      },
      consultStatus: {
        type: "string",
        id: 82
      },
      consultRequestDate: {
        type: "string",
        id: 83
      },
      consultEndDate: {
        type: "string",
        id: 84
      },
      lastUpdateDate: {
        type: "string",
        id: 85
      },
      dataSource: {
        type: "string",
        id: 86
      },
      lockFlag: {
        type: "string",
        id: 87
      },
      lockUserUID: {
        type: "string",
        id: 88
      },
      lockReason: {
        type: "string",
        id: 89
      },
      inWritingUserUID: {
        type: "string",
        id: 90
      },
      messageCount: {
        type: "string",
        id: 91
      },
      unProcessWorkflowCount: {
        type: "string",
        id: 92
      },
      pushState: {
        type: "string",
        id: 93
      },
      deleteFlag: {
        type: "string",
        id: 94
      },
      rowTimestamp: {
        type: "string",
        id: 95
      },
      groupID: {
        type: "string",
        id: 96
      },
      resultSelfPrintCount: {
        type: "string",
        id: 97
      },
      careWorkerID: {
        type: "string",
        id: 98
      },
      careWorkerName: {
        type: "string",
        id: 99
      },
      escortResultStatus: {
        type: "string",
        id: 100
      },
      drugDose: {
        type: "string",
        id: 101
      },
      medicalRecord: {
        type: "string",
        id: 102
      },
      physicalExam: {
        type: "string",
        id: 103
      },
      requestMemo: {
        type: "string",
        id: 104
      },
      idcasState: {
        type: "string",
        id: 105
      },
      multiDrugFastFlag: {
        type: "string",
        id: 106
      },
      priorityFlag: {
        type: "string",
        id: 107
      },
      providerIDCardNO: {
        type: "string",
        id: 108
      },
      height: {
        type: "string",
        id: 109
      },
      weight: {
        type: "string",
        id: 110
      },
      metalFlag: {
        type: "string",
        id: 111
      },
      operationDate: {
        type: "string",
        id: 112
      },
      surgeryFindings: {
        type: "string",
        id: 113
      },
      surgeryExam: {
        type: "string",
        id: 114
      },
      pastHistory: {
        type: "string",
        id: 115
      },
      clinicInfoType: {
        type: "string",
        id: 116
      },
      requestDocName: {
        type: "string",
        id: 117
      },
      uploadFlag: {
        type: "string",
        id: 118
      },
      digitalImageNeed: {
        type: "string",
        id: 119
      }
    }
  },
  MedicalDtoProto: {
    fields: {
      recordUID: {
        type: "string",
        id: 1
      },
      createDate: {
        type: "string",
        id: 2
      },
      recordTypeID: {
        type: "string",
        id: 3
      },
      recordTypeName: {
        type: "string",
        id: 4
      },
      status: {
        type: "string",
        id: 5
      },
      detailSeq: {
        type: "string",
        id: 6
      },
      itemName: {
        type: "string",
        id: 7
      },
      valueTitle: {
        type: "string",
        id: 8
      },
      valueType: {
        type: "string",
        id: 9
      },
      valueText: {
        type: "string",
        id: 10
      },
      valueCode: {
        type: "string",
        id: 11
      },
      doctorName: {
        type: "string",
        id: 12
      }
    }
  },
  DeletePreSetInputProto: {
    fields: {
      querySeq: {
        type: "int32",
        id: 1
      }
    }
  },
  DeptInfoProto: {
    fields: {
      name: {
        type: "string",
        id: 1
      },
      value: {
        type: "string",
        id: 2
      },
      organizationID: {
        type: "string",
        id: 3
      },
      organizationName: {
        type: "string",
        id: 4
      },
      deptName: {
        type: "string",
        id: 5
      },
      deptID: {
        type: "string",
        id: 6
      },
      deptType: {
        type: "string",
        id: 7
      }
    }
  },
  DeptMstDtoNewProto: {
    fields: {
      organizationID: {
        type: "string",
        id: 1
      },
      label: {
        type: "string",
        id: 2
      },
      value: {
        type: "string",
        id: 3
      },
      organizationName: {
        type: "string",
        id: 4
      },
      deptType: {
        type: "string",
        id: 5
      }
    }
  },
  DeptMstInfoProto: {
    fields: {
      deptID: {
        type: "string",
        id: 1
      },
      deptOrganizationID: {
        type: "string",
        id: 2
      },
      deptName: {
        type: "string",
        id: 3
      },
      officePhoneNO: {
        type: "string",
        id: 4
      },
      inputCode: {
        type: "string",
        id: 5
      },
      memo: {
        type: "string",
        id: 6
      },
      deleteFlag: {
        type: "string",
        id: 7
      },
      rowTimestamp: {
        type: "string",
        id: 8
      },
      deptType: {
        type: "string",
        id: 9
      },
      examClass: {
        type: "string",
        id: 10
      },
      alias: {
        type: "string",
        id: 11
      },
      deptTypeName: {
        type: "string",
        id: 12
      },
      examClassName: {
        type: "string",
        id: 13
      }
    }
  },
  DeptMstInputProto: {
    fields: {
      searchOrganizationID: {
        type: "string",
        id: 1
      },
      deptID: {
        type: "string",
        id: 2
      },
      deptName: {
        type: "string",
        id: 3
      },
      pageSize: {
        type: "int32",
        id: 4
      },
      currentPage: {
        type: "int32",
        id: 5
      }
    }
  },
  DeptMstProto: {
    fields: {
      deptID: {
        type: "string",
        id: 1
      },
      searchOrganizationID: {
        type: "string",
        id: 2
      },
      deptName: {
        type: "string",
        id: 3
      },
      officePhoneNO: {
        type: "string",
        id: 4
      },
      inputCode: {
        type: "string",
        id: 5
      },
      memo: {
        type: "string",
        id: 6
      },
      deleteFlag: {
        type: "string",
        id: 7
      },
      rowTimestamp: {
        type: "string",
        id: 8
      },
      deptType: {
        type: "string",
        id: 9
      },
      examClass: {
        type: "string",
        id: 10
      },
      alias: {
        type: "string",
        id: 11
      }
    }
  },
  DicItemMstInputProto: {
    fields: {
      itemCode: {
        type: "string",
        id: 1
      },
      itemCodeScheme: {
        type: "string",
        id: 2
      },
      typeCode: {
        type: "string",
        id: 3
      },
      pageSize: {
        type: "int32",
        id: 4
      },
      currentPage: {
        type: "int32",
        id: 5
      },
      token: {
        type: "string",
        id: 6
      },
      isInteragency: {
        type: "string",
        id: 7
      },
      isInteragencyExam: {
        type: "string",
        id: 8
      },
      isInteragencyClinic: {
        type: "string",
        id: 9
      },
      isInteragencyStatistic: {
        type: "string",
        id: 10
      },
      userInfo: {
        type: "UserOrgInfoProto",
        id: 11
      },
      isInteragencyData: {
        type: "string",
        id: 12
      }
    }
  },
  DicItemMstProto: {
    fields: {
      typeCode: {
        type: "string",
        id: 1
      },
      itemCode: {
        type: "string",
        id: 2
      },
      organizationID: {
        type: "string",
        id: 3
      },
      itemName: {
        type: "string",
        id: 4
      },
      parentItemCode: {
        type: "string",
        id: 5
      },
      inputCode: {
        type: "string",
        id: 6
      },
      sortNO: {
        type: "string",
        id: 7
      },
      memo: {
        type: "string",
        id: 8
      },
      defaultFlag: {
        type: "string",
        id: 9
      },
      deleteFlag: {
        type: "string",
        id: 10
      },
      itemRepresen: {
        type: "string",
        id: 11
      },
      itemRepresenExt1: {
        type: "string",
        id: 12
      },
      itemRepresenExt2: {
        type: "string",
        id: 13
      },
      itemRepresenExt3: {
        type: "string",
        id: 14
      },
      itemRepresenExt4: {
        type: "string",
        id: 15
      },
      itemRepresenExt5: {
        type: "string",
        id: 16
      },
      itemRepresenExt6: {
        type: "string",
        id: 17
      },
      itemRepresenExt7: {
        type: "string",
        id: 18
      },
      itemRepresenExt8: {
        type: "string",
        id: 19
      },
      itemRepresenExt9: {
        type: "string",
        id: 20
      },
      itemRepresenExt10: {
        type: "string",
        id: 21
      },
      itemRepresenExt11: {
        type: "string",
        id: 22
      },
      itemRepresenExt12: {
        type: "string",
        id: 23
      },
      itemRepresenExt13: {
        type: "string",
        id: 24
      },
      itemRepresenExt14: {
        type: "string",
        id: 25
      },
      itemRepresenExt15: {
        type: "string",
        id: 26
      },
      itemRepresenExt16: {
        type: "string",
        id: 27
      },
      itemRepresenExt17: {
        type: "string",
        id: 28
      },
      itemRepresenExt18: {
        type: "string",
        id: 29
      },
      itemRepresenExt19: {
        type: "string",
        id: 30
      },
      itemRepresenExt20: {
        type: "string",
        id: 31
      }
    }
  },
  DicTypeMstInputProto: {
    fields: {
      typeClass: {
        type: "string",
        id: 1
      },
      typeCode: {
        type: "string",
        id: 2
      },
      typeName: {
        type: "string",
        id: 3
      },
      pageSize: {
        type: "int32",
        id: 4
      },
      currentPage: {
        type: "int32",
        id: 5
      }
    }
  },
  DicTypeMstProto: {
    fields: {
      typeCode: {
        type: "string",
        id: 1
      },
      typeName: {
        type: "string",
        id: 2
      },
      codeScheme: {
        type: "string",
        id: 3
      },
      typeClass: {
        type: "string",
        id: 4
      },
      allowCreateItem: {
        type: "string",
        id: 5
      },
      allowUpdateItem: {
        type: "string",
        id: 6
      },
      allowDeleteItem: {
        type: "string",
        id: 7
      },
      memo: {
        type: "string",
        id: 8
      },
      itemRepresenTitle: {
        type: "string",
        id: 9
      },
      itemRepresenExt1Title: {
        type: "string",
        id: 10
      },
      itemRepresenExt2Title: {
        type: "string",
        id: 11
      },
      itemRepresenExt3Title: {
        type: "string",
        id: 12
      },
      itemRepresenExt4Title: {
        type: "string",
        id: 13
      },
      itemRepresenExt5Title: {
        type: "string",
        id: 14
      },
      itemRepresenExt6Title: {
        type: "string",
        id: 15
      },
      itemRepresenExt7Title: {
        type: "string",
        id: 16
      },
      itemRepresenExt8Title: {
        type: "string",
        id: 17
      },
      itemRepresenExt9Title: {
        type: "string",
        id: 18
      },
      itemRepresenExt10Title: {
        type: "string",
        id: 19
      },
      itemRepresenExt11Title: {
        type: "string",
        id: 20
      },
      itemRepresenExt12Title: {
        type: "string",
        id: 21
      },
      itemRepresenExt13Title: {
        type: "string",
        id: 22
      },
      itemRepresenExt14Title: {
        type: "string",
        id: 23
      },
      itemRepresenExt15Title: {
        type: "string",
        id: 24
      },
      itemRepresenExt16Title: {
        type: "string",
        id: 25
      },
      itemRepresenExt17Title: {
        type: "string",
        id: 26
      },
      itemRepresenExt18Title: {
        type: "string",
        id: 27
      },
      itemRepresenExt19Title: {
        type: "string",
        id: 28
      },
      itemRepresenExt20Title: {
        type: "string",
        id: 29
      }
    }
  },
  DigitalImageExamInputProto: {
    fields: {
      organizationID: {
        type: "string",
        id: 1
      },
      accessionNumber: {
        type: "string",
        id: 2
      }
    }
  },
  DigitalImageExamOutputProto: {
    fields: {
      errorCode: {
        type: "int32",
        id: 1
      },
      organizationID: {
        type: "string",
        id: 2
      },
      accessionNumber: {
        type: "string",
        id: 3
      }
    }
  },
  DigitalImageInputProto: {
    fields: {
      digitalImageState: {
        type: "int32",
        id: 1
      },
      examList: {
        rule: "repeated",
        type: "DigitalImageExamInputProto",
        id: 2
      }
    }
  },
  DocStatusProto: {
    fields: {
      examResultStatus: {
        type: "bool",
        id: 1
      },
      examWrittenStatus: {
        type: "bool",
        id: 2
      },
      examFilmStatus: {
        type: "bool",
        id: 3
      },
      examImgStatus: {
        type: "bool",
        id: 4
      }
    }
  },
  DoctorInputProto: {
    fields: {
      organizationId: {
        type: "string",
        id: 1
      },
      deptId: {
        type: "string",
        id: 2
      },
      userType: {
        type: "string",
        id: 3
      },
      pageSize: {
        type: "int32",
        id: 4
      },
      currentPage: {
        type: "int32",
        id: 5
      },
      token: {
        type: "string",
        id: 6
      },
      isInteragency: {
        type: "string",
        id: 7
      },
      isInteragencyExam: {
        type: "string",
        id: 8
      },
      isInteragencyClinic: {
        type: "string",
        id: 9
      },
      isInteragencyStatistic: {
        type: "string",
        id: 10
      },
      userInfo: {
        type: "UserOrgInfoProto",
        id: 11
      },
      isInteragencyData: {
        type: "string",
        id: 12
      }
    }
  },
  DoctorOutputProto: {
    fields: {
      organizationID: {
        type: "string",
        id: 1
      },
      organizationName: {
        type: "string",
        id: 2
      },
      deptID: {
        type: "string",
        id: 3
      },
      doctorName: {
        type: "string",
        id: 4
      },
      userUID: {
        type: "string",
        id: 5
      },
      type: {
        type: "string",
        id: 6
      },
      value: {
        type: "string",
        id: 7
      }
    }
  },
  DocumentListProto: {
    fields: {
      document: {
        rule: "repeated",
        type: "DocumentProto",
        id: 1
      }
    }
  },
  DocumentProto: {
    fields: {
      documentDtos: {
        rule: "repeated",
        type: "DocumentDtoProto",
        id: 1
      }
    }
  },
  DocumentDtoProto: {
    fields: {
      businessType: {
        type: "string",
        id: 1
      },
      businessTime: {
        type: "string",
        id: 2
      },
      classCode: {
        type: "string",
        id: 3
      },
      typeCode: {
        type: "string",
        id: 4
      },
      mimeType: {
        type: "string",
        id: 5
      },
      fileSize: {
        type: "string",
        id: 6
      },
      fileCreateTime: {
        type: "string",
        id: 7
      },
      fileCreateUserID: {
        type: "string",
        id: 8
      },
      fileCreateUserName: {
        type: "string",
        id: 9
      },
      originalFileName: {
        type: "string",
        id: 10
      },
      title: {
        type: "string",
        id: 11
      },
      uploadTime: {
        type: "string",
        id: 12
      },
      dicomInfo: {
        type: "string",
        id: 13
      },
      fileRelativePath: {
        type: "string",
        id: 14
      },
      mediaName: {
        type: "string",
        id: 15
      },
      pathType: {
        type: "string",
        id: 16
      },
      mediaHost: {
        type: "string",
        id: 17
      },
      path: {
        type: "string",
        id: 18
      },
      base64url: {
        type: "bytes",
        id: 19
      },
      subDir: {
        type: "string",
        id: 20
      },
      patientID: {
        type: "string",
        id: 21
      },
      accessionNumber: {
        type: "string",
        id: 22
      },
      serviceSectID: {
        type: "string",
        id: 23
      },
      studyInstanceUID: {
        type: "string",
        id: 24
      },
      organizationID: {
        type: "string",
        id: 25
      },
      imgUrl: {
        type: "string",
        id: 26
      },
      access_Token: {
        type: "string",
        id: 27
      },
      examUID: {
        type: "string",
        id: 28
      },
      resultSeq: {
        type: "string",
        id: 29
      },
      imagingFinding: {
        type: "string",
        id: 30
      },
      imagingDiagnosis: {
        type: "string",
        id: 31
      }
    }
  },
  DocumentInputProto: {
    fields: {
      examUID: {
        type: "string",
        id: 1
      },
      typeCode: {
        type: "string",
        id: 2
      },
      classCode: {
        type: "string",
        id: 3
      },
      businessType: {
        type: "string",
        id: 4
      },
      access_Token: {
        type: "string",
        id: 5
      },
      shareAddress: {
        type: "string",
        id: 6
      },
      shareUserName: {
        type: "string",
        id: 7
      },
      sharePassWord: {
        type: "string",
        id: 8
      },
      pageSize: {
        type: "int32",
        id: 9
      },
      currentPage: {
        type: "int32",
        id: 10
      },
      token: {
        type: "string",
        id: 11
      },
      isInteragency: {
        type: "string",
        id: 12
      },
      isInteragencyExam: {
        type: "string",
        id: 13
      },
      isInteragencyClinic: {
        type: "string",
        id: 14
      },
      isInteragencyStatistic: {
        type: "string",
        id: 15
      },
      userInfo: {
        type: "UserOrgInfoProto",
        id: 16
      },
      isInteragencyData: {
        type: "string",
        id: 17
      },
      applyMethod: {
        type: "string",
        id: 18
      },
      isInterconnectData: {
        type: "string",
        id: 19
      },
      accessionNumber: {
        type: "string",
        id: 20
      },
      organizationID: {
        type: "string",
        id: 21
      },
      examToken: {
        type: "string",
        id: 22
      }
    }
  },
  DocumentRequestProto: {
    fields: {
      cardNo: {
        type: "string",
        id: 1
      },
      organizationID: {
        type: "string",
        id: 2
      },
      cardType: {
        type: "int32",
        id: 3
      },
      typeCode: {
        type: "string",
        id: 4
      },
      classCode: {
        type: "string",
        id: 5
      },
      businessType: {
        type: "string",
        id: 6
      },
      serviceSectID: {
        type: "string",
        id: 7
      },
      rePrint: {
        type: "string",
        id: 8
      },
      examDate: {
        type: "string",
        id: 9
      }
    }
  },
  EditUserRightInputProto: {
    fields: {
      organizationID: {
        type: "string",
        id: 1
      },
      roleUID: {
        type: "string",
        id: 2
      },
      right: {
        rule: "repeated",
        type: "RoleRightOutputProto",
        id: 3
      }
    }
  },
  RoleRightOutputProto: {
    fields: {
      rightID: {
        type: "string",
        id: 1
      },
      rightClass: {
        type: "string",
        id: 2
      },
      rightName: {
        type: "string",
        id: 3
      },
      title: {
        type: "string",
        id: 4
      },
      controllerName: {
        type: "string",
        id: 5
      },
      actionName: {
        type: "string",
        id: 6
      },
      parameter: {
        type: "string",
        id: 7
      },
      active: {
        type: "string",
        id: 8
      },
      parentRightID: {
        type: "string",
        id: 9
      },
      sortNO: {
        type: "string",
        id: 10
      },
      memo: {
        type: "string",
        id: 11
      },
      createUserUID: {
        type: "string",
        id: 12
      },
      createUserName: {
        type: "string",
        id: 13
      },
      createDate: {
        type: "string",
        id: 14
      },
      LAYChecked: {
        type: "string",
        id: 15
      }
    }
  },
  ExamInfoProto: {
    fields: {
      patientID: {
        type: "string",
        id: 1
      },
      name: {
        type: "string",
        id: 2
      },
      sex: {
        type: "string",
        id: 3
      },
      birthDate: {
        type: "string",
        id: 4
      },
      phoneNumber: {
        type: "string",
        id: 5
      },
      accessionNumber: {
        type: "string",
        id: 6
      },
      patientClass: {
        type: "string",
        id: 7
      },
      serviceSect: {
        type: "string",
        id: 8
      },
      examDate: {
        type: "string",
        id: 9
      },
      resultStatus: {
        type: "string",
        id: 10
      },
      printTimes: {
        type: "int32",
        id: 11
      },
      examUID: {
        type: "string",
        id: 12
      },
      docInfoList: {
        rule: "repeated",
        type: "string",
        id: 13
      }
    }
  },
  ExamItemsInputProto: {
    fields: {
      visitUID: {
        type: "string",
        id: 1
      },
      pageSize: {
        type: "int32",
        id: 2
      },
      currentPage: {
        type: "int32",
        id: 3
      },
      token: {
        type: "string",
        id: 4
      },
      isInteragency: {
        type: "string",
        id: 5
      },
      isInteragencyExam: {
        type: "string",
        id: 6
      },
      isInteragencyClinic: {
        type: "string",
        id: 7
      },
      isInteragencyStatistic: {
        type: "string",
        id: 8
      },
      userInfo: {
        type: "UserOrgInfoProto",
        id: 9
      },
      isInteragencyData: {
        type: "string",
        id: 10
      },
      orgnizationID: {
        type: "string",
        id: 11
      }
    }
  },
  ExamItemsOutputProto: {
    fields: {
      examUID: {
        type: "string",
        id: 1
      },
      serviceText: {
        type: "string",
        id: 2
      },
      examTime: {
        type: "string",
        id: 3
      },
      serviceSectID: {
        type: "string",
        id: 4
      },
      resultStatus: {
        type: "string",
        id: 5
      },
      abnormalFlags: {
        type: "string",
        id: 6
      }
    }
  },
  GainSingleDataProto: {
    fields: {
      accessionNumber: {
        type: "string",
        id: 1
      },
      serviceUID: {
        type: "string",
        id: 2
      }
    }
  },
  GainFileDataProto: {
    fields: {
      accessionNumber: {
        type: "string",
        id: 1
      },
      examUID: {
        type: "string",
        id: 2
      },
      downloadType: {
        type: "int32",
        id: 3
      }
    }
  },
  ResetBusinessStatusProto: {
    fields: {
      accessionNumber: {
        type: "string",
        id: 1
      },
      examUID: {
        type: "string",
        id: 2
      },
      fileType: {
        type: "int32",
        id: 3
      }
    }
  },
  GetGainRecordListInputProto: {
    fields: {
      currentPage: {
        type: "int32",
        id: 1
      },
      pageSize: {
        type: "int32",
        id: 2
      },
      date: {
        type: "string",
        id: 3
      },
      type: {
        type: "int32",
        id: 4
      },
      organizationID: {
        type: "string",
        id: 5
      }
    }
  },
  GetGainRecordListOutProto: {
    fields: {
      gainRecordUID: {
        type: "string",
        id: 1
      },
      type: {
        type: "int32",
        id: 2
      },
      createTime: {
        type: "string",
        id: 3
      },
      organizationName: {
        type: "string",
        id: 4
      },
      typeName: {
        type: "string",
        id: 5
      }
    }
  },
  GetOperateRecordListInputProto: {
    fields: {
      organizationID: {
        type: "string",
        id: 1
      },
      currentPage: {
        type: "int32",
        id: 2
      },
      pageSize: {
        type: "int32",
        id: 3
      },
      date: {
        type: "string",
        id: 4
      }
    }
  },
  GetOperateRecordListOutputProto: {
    fields: {
      operateRecordUID: {
        type: "string",
        id: 1
      },
      organizationID: {
        type: "string",
        id: 2
      },
      requestURL: {
        type: "string",
        id: 3
      },
      createTime: {
        type: "string",
        id: 4
      },
      organizationName: {
        type: "string",
        id: 5
      }
    }
  },
  GetPatientClientConfigInputProto: {
    fields: {
      organizationID: {
        type: "string",
        id: 1
      }
    }
  },
  GetPatientInputProto: {
    fields: {
      accessionNumber: {
        type: "string",
        id: 1
      },
      organizationID: {
        type: "string",
        id: 2
      },
      examToken: {
        type: "string",
        id: 3
      }
    }
  },
  GetPatientOutputProto: {
    fields: {
      patientName: {
        type: "string",
        id: 1
      },
      sex: {
        type: "string",
        id: 2
      },
      age: {
        type: "string",
        id: 3
      },
      ageUnit: {
        type: "string",
        id: 4
      },
      procedureName: {
        type: "string",
        id: 5
      },
      examDate: {
        type: "string",
        id: 6
      },
      accessionNumber: {
        type: "string",
        id: 7
      },
      examItem: {
        type: "string",
        id: 8
      },
      hasImage: {
        type: "bool",
        id: 9
      },
      hasResult: {
        type: "bool",
        id: 10
      },
      hasFilm: {
        type: "bool",
        id: 11
      },
      imagingFinding: {
        type: "string",
        id: 12
      },
      imagingDiagnosis: {
        type: "string",
        id: 13
      },
      serviceSectID: {
        type: "string",
        id: 14
      },
      organizationName: {
        type: "string",
        id: 15
      },
      organizationID: {
        type: "string",
        id: 16
      },
      relatedAuth: {
        type: "bool",
        id: 17
      }
    }
  },
  GetUploadRecordListInputProto: {
    fields: {
      currentPage: {
        type: "int32",
        id: 1
      },
      pageSize: {
        type: "int32",
        id: 2
      },
      date: {
        type: "string",
        id: 3
      },
      type: {
        type: "int32",
        id: 4
      },
      organizationID: {
        type: "string",
        id: 5
      }
    }
  },
  GetUploadRecordListOutputProto: {
    fields: {
      uploadUID: {
        type: "string",
        id: 1
      },
      type: {
        type: "int32",
        id: 2
      },
      createTime: {
        type: "string",
        id: 3
      },
      organizationName: {
        type: "string",
        id: 4
      },
      typeName: {
        type: "string",
        id: 5
      }
    }
  },
  OrganizationDtoNewProto: {
    fields: {
      value: {
        type: "string",
        id: 1
      },
      label: {
        type: "string",
        id: 2
      },
      DeptMstDto: {
        rule: "repeated",
        type: "DeptMstDtoNewProto",
        id: 3
      }
    }
  },
  OrganizationDtoProto: {
    fields: {
      organizationID: {
        type: "string",
        id: 1
      },
      organizationName: {
        type: "string",
        id: 2
      },
      deptMstDto: {
        rule: "repeated",
        type: "DeptMstDtoProto",
        id: 3
      }
    }
  },
  DeptMstDtoProto: {
    fields: {
      organizationID: {
        type: "string",
        id: 1
      },
      deptName: {
        type: "string",
        id: 2
      },
      deptID: {
        type: "string",
        id: 3
      },
      organizationName: {
        type: "string",
        id: 4
      },
      deptType: {
        type: "string",
        id: 5
      }
    }
  },
  organizationIDInputProto: {
    fields: {
      organizationID: {
        type: "string",
        id: 1
      }
    }
  },
  OrganizationInputProto: {
    fields: {
      organizationName: {
        type: "string",
        id: 1
      },
      organizationID: {
        type: "string",
        id: 2
      },
      deptType: {
        type: "string",
        id: 3
      }
    }
  },
  OrganizationMstProto: {
    fields: {
      searchOrganizationID: {
        type: "string",
        id: 1
      },
      organizationName: {
        type: "string",
        id: 2
      },
      alias: {
        type: "string",
        id: 3
      },
      inputCode: {
        type: "string",
        id: 4
      },
      contactUserName: {
        type: "string",
        id: 5
      },
      officePhoneNO: {
        type: "string",
        id: 6
      },
      personalPhoneNO: {
        type: "string",
        id: 7
      },
      email: {
        type: "string",
        id: 8
      },
      address: {
        type: "string",
        id: 9
      },
      organizationTypeCode: {
        type: "string",
        id: 10
      },
      parentOrganizationID: {
        type: "string",
        id: 11
      },
      createUserUID: {
        type: "string",
        id: 12
      },
      createDate: {
        type: "string",
        id: 13
      },
      memo: {
        type: "string",
        id: 14
      },
      deleteFlag: {
        type: "string",
        id: 15
      },
      rowTimestamp: {
        type: "string",
        id: 16
      },
      organizationCode: {
        type: "string",
        id: 17
      },
      province: {
        type: "string",
        id: 18
      },
      city: {
        type: "string",
        id: 19
      },
      district: {
        type: "string",
        id: 20
      },
      sortNO: {
        type: "string",
        id: 21
      },
      defaultShareDuration: {
        type: "int32",
        id: 22
      },
      cardBackgroundColour: {
        type: "string",
        id: 23
      },
      logoURL: {
        type: "string",
        id: 24
      },
      backGroundURL: {
        type: "string",
        id: 25
      }
    }
  },
  OrganizationTreeProto: {
    fields: {
      searchOrganizationID: {
        type: "string",
        id: 1
      },
      organizationName: {
        type: "string",
        id: 2
      },
      alias: {
        type: "string",
        id: 3
      },
      inputCode: {
        type: "string",
        id: 4
      },
      contactUserName: {
        type: "string",
        id: 5
      },
      officePhoneNO: {
        type: "string",
        id: 6
      },
      personalPhoneNO: {
        type: "string",
        id: 7
      },
      email: {
        type: "string",
        id: 8
      },
      address: {
        type: "string",
        id: 9
      },
      organizationTypeCode: {
        type: "string",
        id: 10
      },
      parentOrganizationID: {
        type: "string",
        id: 11
      },
      createUserUID: {
        type: "string",
        id: 12
      },
      createDate: {
        type: "string",
        id: 13
      },
      memo: {
        type: "string",
        id: 14
      },
      deleteFlag: {
        type: "string",
        id: 15
      },
      organizationCode: {
        type: "string",
        id: 16
      },
      province: {
        type: "string",
        id: 17
      },
      city: {
        type: "string",
        id: 18
      },
      district: {
        type: "string",
        id: 19
      },
      sortNO: {
        type: "int32",
        id: 20
      },
      children: {
        rule: "repeated",
        type: "OrganizationTreeProto",
        id: 21
      },
      defaultShareDuration: {
        type: "int32",
        id: 22
      },
      cardBackgroundColour: {
        type: "string",
        id: 23
      },
      logoURL: {
        type: "string",
        id: 24
      },
      backGroundURL: {
        type: "string",
        id: 25
      }
    }
  },
  OrgInputProto: {
    fields: {
      organizationName: {
        type: "string",
        id: 1
      },
      searchOrganizationID: {
        type: "string",
        id: 2
      },
      deptType: {
        type: "string",
        id: 3
      }
    }
  },
  PageResponse: {
    fields: {
      isSuccess: {
        type: "bool",
        id: 1
      },
      message: {
        type: "string",
        id: 2
      },
      pageBase: {
        type: "PageBase",
        id: 3
      },
      data: {
        rule: "repeated",
        type: "google.protobuf.Any",
        id: 4
      },
      warnCode: {
        type: "int32",
        id: 5
      }
    }
  },
  PageBase: {
    fields: {
      currentPage: {
        type: "int32",
        id: 1
      },
      pageSize: {
        type: "int32",
        id: 2
      },
      totalRecords: {
        type: "int32",
        id: 3
      },
      token: {
        type: "string",
        id: 4
      },
      errorTimes: {
        type: "int32",
        id: 5
      },
      loginStatus: {
        type: "int32",
        id: 6
      }
    }
  },
  PatientIndexProto: {
    fields: {
      patientID: {
        type: "string",
        id: 1
      },
      pIDAssigningAuthority: {
        type: "string",
        id: 2
      },
      isMPI: {
        type: "int32",
        id: 3
      },
      patientMasterID: {
        type: "string",
        id: 4
      },
      password: {
        type: "string",
        id: 5
      },
      createDate: {
        type: "string",
        id: 6
      },
      createUserID: {
        type: "string",
        id: 7
      },
      createUserName: {
        type: "string",
        id: 8
      },
      createOrgnizationID: {
        type: "string",
        id: 9
      },
      name: {
        type: "string",
        id: 10
      },
      nameSpell: {
        type: "string",
        id: 11
      },
      motherName: {
        type: "string",
        id: 12
      },
      sex: {
        type: "string",
        id: 13
      },
      birthDate: {
        type: "string",
        id: 14
      },
      birthPlace: {
        type: "string",
        id: 15
      },
      nation: {
        type: "string",
        id: 16
      },
      citizenship: {
        type: "string",
        id: 17
      },
      maritalStatus: {
        type: "string",
        id: 18
      },
      identityType: {
        type: "string",
        id: 19
      },
      identityID: {
        type: "string",
        id: 20
      },
      iDCardNO: {
        type: "string",
        id: 21
      },
      healthCardNO: {
        type: "string",
        id: 22
      },
      insuranceType: {
        type: "string",
        id: 23
      },
      insuranceID: {
        type: "string",
        id: 24
      },
      contactPhoneNO: {
        type: "string",
        id: 25
      },
      homePhoneNO: {
        type: "string",
        id: 26
      },
      businessPhoneNO: {
        type: "string",
        id: 27
      },
      email: {
        type: "string",
        id: 28
      },
      addressProvince: {
        type: "string",
        id: 29
      },
      addressCity: {
        type: "string",
        id: 30
      },
      addressDistrict: {
        type: "string",
        id: 31
      },
      addressStreet: {
        type: "string",
        id: 32
      },
      addressRoad: {
        type: "string",
        id: 33
      },
      addressDetail: {
        type: "string",
        id: 34
      },
      postalcode: {
        type: "string",
        id: 35
      },
      occupation: {
        type: "string",
        id: 36
      },
      workUnit: {
        type: "string",
        id: 37
      },
      language: {
        type: "string",
        id: 38
      },
      lastUpdateDate: {
        type: "string",
        id: 39
      },
      inHospitalFlag: {
        type: "string",
        id: 40
      },
      status: {
        type: "string",
        id: 41
      }
    }
  },
  PatientInputProto: {
    fields: {
      patientName: {
        type: "string",
        id: 1
      },
      iDCardNo: {
        type: "string",
        id: 2
      },
      healthCardNO: {
        type: "string",
        id: 3
      },
      insuranceID: {
        type: "string",
        id: 4
      },
      userOrganizationID: {
        type: "string",
        id: 5
      },
      quickSearch: {
        type: "string",
        id: 6
      },
      pageSize: {
        type: "int32",
        id: 7
      },
      currentPage: {
        type: "int32",
        id: 8
      },
      token: {
        type: "string",
        id: 9
      },
      userInfo: {
        type: "UserOrgInfoProto",
        id: 10
      },
      isInteragency: {
        type: "string",
        id: 11
      },
      isInteragencyExam: {
        type: "string",
        id: 12
      },
      IsInteragencyClinic: {
        type: "string",
        id: 13
      },
      IsInteragencyStatistic: {
        type: "string",
        id: 14
      },
      test: {
        type: "string",
        id: 15
      }
    }
  },
  PatientLoginUserInfoProto: {
    fields: {
      patientName: {
        type: "string",
        id: 1
      },
      sex: {
        type: "string",
        id: 2
      },
      age: {
        type: "string",
        id: 3
      },
      ageUnit: {
        type: "string",
        id: 4
      },
      procedureName: {
        type: "string",
        id: 5
      },
      examDate: {
        type: "string",
        id: 6
      },
      accessionNumber: {
        type: "string",
        id: 7
      }
    }
  },
  Person: {
    fields: {
      Id: {
        type: "int32",
        id: 1
      },
      Name: {
        type: "string",
        id: 2
      },
      Address: {
        type: "Address",
        id: 3
      }
    }
  },
  Address: {
    fields: {
      Line1: {
        type: "string",
        id: 1
      },
      Line2: {
        type: "string",
        id: 2
      }
    }
  },
  PersonalCheckRcdDtoProto: {
    fields: {
      patientName: {
        type: "string",
        id: 1
      },
      gender: {
        type: "string",
        id: 2
      },
      serviceSectID: {
        type: "string",
        id: 3
      },
      examItem: {
        type: "string",
        id: 4
      },
      checkArea: {
        type: "string",
        id: 5
      },
      medRecNO: {
        type: "string",
        id: 6
      },
      pointOfCare: {
        type: "string",
        id: 7
      },
      patientClass: {
        type: "string",
        id: 8
      },
      visitID: {
        type: "string",
        id: 9
      },
      pointOfCareID: {
        type: "string",
        id: 10
      },
      bed: {
        type: "string",
        id: 11
      },
      organizationName: {
        type: "string",
        id: 12
      },
      requestOrgName: {
        type: "string",
        id: 13
      },
      requestDept: {
        type: "string",
        id: 14
      },
      requestDocName: {
        type: "string",
        id: 15
      },
      requestTime: {
        type: "string",
        id: 16
      },
      regTime: {
        type: "string",
        id: 17
      },
      examTime: {
        type: "string",
        id: 18
      },
      patientID: {
        type: "string",
        id: 19
      },
      accessionNumber: {
        type: "string",
        id: 20
      },
      abnormalFlags: {
        type: "string",
        id: 21
      },
      criticalValue: {
        type: "string",
        id: 22
      },
      resultStatus: {
        type: "string",
        id: 23
      },
      ifHasImage: {
        type: "string",
        id: 24
      },
      examStatus: {
        type: "string",
        id: 25
      },
      examCode: {
        type: "string",
        id: 26
      },
      patientMasterID: {
        type: "string",
        id: 27
      },
      examUID: {
        type: "string",
        id: 28
      },
      outPatientID: {
        type: "string",
        id: 29
      },
      alternateVisitID: {
        type: "string",
        id: 30
      },
      applyMethod: {
        type: "string",
        id: 31
      },
      displayAge: {
        type: "string",
        id: 32
      },
      organizationID: {
        type: "string",
        id: 33
      }
    }
  },
  PersonalCheckRcdInputProto: {
    fields: {
      patientMasterID: {
        type: "string",
        id: 1
      },
      personExamUID: {
        type: "string",
        id: 2
      },
      pageSize: {
        type: "int32",
        id: 3
      },
      currentPage: {
        type: "int32",
        id: 4
      },
      token: {
        type: "string",
        id: 5
      },
      isInteragency: {
        type: "string",
        id: 6
      },
      isInteragencyExam: {
        type: "string",
        id: 7
      },
      isInteragencyClinic: {
        type: "string",
        id: 8
      },
      isInteragencyStatistic: {
        type: "string",
        id: 9
      },
      userInfo: {
        type: "UserOrgInfoProto",
        id: 10
      },
      isInteragencyData: {
        type: "string",
        id: 11
      },
      examUID: {
        type: "string",
        id: 12
      },
      applyMethod: {
        type: "string",
        id: 13
      },
      isInterconnectData: {
        type: "string",
        id: 14
      },
      examToken: {
        type: "string",
        id: 15
      },
      accessionNumber: {
        type: "string",
        id: 16
      },
      organizationID: {
        type: "string",
        id: 17
      },
      iDCardNo: {
        type: "string",
        id: 18
      },
      insuranceID: {
        type: "string",
        id: 19
      }
    }
  },
  PluginDtoProto: {
    fields: {
      pluginUID: {
        type: "string",
        id: 1
      },
      pluginName: {
        type: "string",
        id: 2
      }
    }
  },
  PluginProto: {
    fields: {
      pluginUID: {
        type: "string",
        id: 1
      },
      pluginName: {
        type: "string",
        id: 2
      },
      dllName: {
        type: "string",
        id: 3
      },
      className: {
        type: "string",
        id: 4
      },
      description: {
        type: "string",
        id: 5
      },
      pluginType: {
        type: "string",
        id: 6
      },
      pluginConfigs: {
        type: "string",
        id: 7
      },
      defaultKeyValue: {
        type: "string",
        id: 8
      },
      pluginFunction: {
        type: "string",
        id: 9
      },
      pluginRule: {
        type: "string",
        id: 10
      },
      configVersion: {
        type: "string",
        id: 11
      },
      ifSupportCheck: {
        type: "bool",
        id: 12
      },
      isShow: {
        type: "bool",
        id: 13
      }
    }
  },
  PluginServiceMapProto: {
    fields: {
      serviceUID: {
        type: "string",
        id: 1
      },
      pluginUID: {
        type: "string",
        id: 2
      },
      ifEnable: {
        type: "bool",
        id: 3
      },
      ifDelete: {
        type: "bool",
        id: 4
      },
      pluginName: {
        type: "string",
        id: 5
      },
      pluginConfigValues: {
        type: "string",
        id: 6
      },
      pluginConfigKeyValue: {
        type: "string",
        id: 7
      },
      triggerInternal: {
        type: "int32",
        id: 8
      },
      ifTriggerByTime: {
        type: "string",
        id: 9
      },
      triggerTime: {
        type: "string",
        id: 10
      },
      ifTriggerByDay: {
        type: "string",
        id: 11
      },
      triggerDayOfWeek: {
        type: "string",
        id: 12
      },
      ifTriggerByDate: {
        type: "string",
        id: 13
      },
      triggerBeginDate: {
        type: "string",
        id: 14
      },
      triggerEndDate: {
        type: "string",
        id: 15
      },
      triggerBeginTime: {
        type: "string",
        id: 16
      },
      triggerEndTime: {
        type: "string",
        id: 17
      },
      triggerTimes: {
        type: "int32",
        id: 18
      },
      taskFieldValue: {
        type: "string",
        id: 19
      },
      pluginRule: {
        type: "string",
        id: 20
      },
      configVersion: {
        type: "string",
        id: 21
      },
      pluginServiceMapUID: {
        type: "string",
        id: 22
      },
      ifSupportCheck: {
        type: "bool",
        id: 23
      }
    }
  },
  PluginOutputProto: {
    fields: {
      value: {
        type: "string",
        id: 1
      },
      label: {
        type: "string",
        id: 2
      },
      dllName: {
        type: "string",
        id: 3
      },
      className: {
        type: "string",
        id: 4
      },
      description: {
        type: "string",
        id: 5
      },
      pluginType: {
        type: "string",
        id: 6
      },
      pluginConfigs: {
        type: "string",
        id: 7
      }
    }
  },
  PluginRecordInputProto: {
    fields: {
      serviceName: {
        type: "string",
        id: 1
      },
      pluginName: {
        type: "string",
        id: 2
      },
      operateDate: {
        type: "string",
        id: 3
      },
      timeSpan: {
        type: "string",
        id: 4
      },
      splitChar: {
        type: "string",
        id: 5
      },
      currentPage: {
        type: "int32",
        id: 6
      },
      pageSize: {
        type: "int32",
        id: 7
      }
    }
  },
  PluginRecordOutputProto: {
    fields: {
      seqID: {
        type: "int32",
        id: 1
      },
      serviceName: {
        type: "string",
        id: 2
      },
      serviceUID: {
        type: "string",
        id: 3
      },
      pluginName: {
        type: "string",
        id: 4
      },
      pluginUID: {
        type: "string",
        id: 5
      },
      operateTime: {
        type: "string",
        id: 6
      },
      operateInfo: {
        type: "string",
        id: 7
      }
    }
  },
  PluginServiceManaProto: {
    fields: {
      pluginType: {
        type: "string",
        id: 1
      },
      ifEnable: {
        type: "string",
        id: 2
      }
    }
  },
  PluginServiceProto: {
    fields: {
      serviceUID: {
        type: "string",
        id: 1
      },
      serviceName: {
        type: "string",
        id: 2
      },
      ifEnable: {
        type: "bool",
        id: 3
      },
      ifDelete: {
        type: "string",
        id: 4
      }
    }
  },
  PositiveRateDtoProto: {
    fields: {
      positiveRateOutput: {
        rule: "repeated",
        type: "PositiveRateOutputProto",
        id: 1
      },
      row1Name: {
        type: "string",
        id: 2
      },
      row2Name: {
        type: "string",
        id: 3
      },
      column1Name: {
        type: "string",
        id: 4
      },
      column2Name: {
        type: "string",
        id: 5
      }
    }
  },
  PositiveRateOutputProto: {
    fields: {
      positive: {
        type: "string",
        id: 1
      },
      count: {
        type: "string",
        id: 2
      },
      row1: {
        type: "string",
        id: 3
      },
      row2: {
        type: "string",
        id: 4
      },
      column1: {
        type: "string",
        id: 5
      },
      column2: {
        type: "string",
        id: 6
      }
    }
  },
  PresetSearchInputProto: {
    fields: {
      querySeq: {
        type: "int32",
        id: 1
      },
      pageSize: {
        type: "int32",
        id: 2
      },
      currentPage: {
        type: "int32",
        id: 3
      },
      token: {
        type: "string",
        id: 4
      },
      isInteragency: {
        type: "string",
        id: 5
      },
      isInteragencyExam: {
        type: "string",
        id: 6
      },
      isInteragencyClinic: {
        type: "string",
        id: 7
      },
      isInteragencyStatistic: {
        type: "string",
        id: 8
      },
      userInfo: {
        type: "UserOrgInfoProto",
        id: 9
      },
      isInteragencyData: {
        type: "string",
        id: 10
      }
    }
  },
  PrintLogRequestProto: {
    fields: {
      patientID: {
        type: "string",
        id: 1
      },
      sourceType: {
        type: "int32",
        id: 2
      },
      organizationID: {
        type: "string",
        id: 3
      },
      oprerator: {
        type: "string",
        id: 4
      },
      requestIP: {
        type: "string",
        id: 5
      },
      examUID: {
        type: "string",
        id: 6
      }
    }
  },
  PrintLogInputProto: {
    fields: {
      organizationID: {
        type: "string",
        id: 1
      },
      oprerator: {
        type: "string",
        id: 2
      },
      operateTime: {
        type: "string",
        id: 3
      },
      pageSize: {
        type: "int32",
        id: 4
      },
      currentPage: {
        type: "int32",
        id: 5
      }
    }
  },
  PrintLogRequestDtoProto: {
    fields: {
      patientID: {
        type: "string",
        id: 1
      },
      sourceType: {
        type: "string",
        id: 2
      },
      organizationID: {
        type: "string",
        id: 3
      },
      oprerator: {
        type: "string",
        id: 4
      },
      requestIP: {
        type: "string",
        id: 5
      },
      examUID: {
        type: "string",
        id: 6
      },
      patientName: {
        type: "string",
        id: 7
      },
      organizationName: {
        type: "string",
        id: 8
      },
      operateTime: {
        type: "string",
        id: 9
      }
    }
  },
  PrintInputProto: {
    fields: {
      examUID: {
        type: "string",
        id: 1
      },
      accessionNumber: {
        type: "string",
        id: 2
      }
    }
  },
  RegisterFilmResponseProto: {
    fields: {
      errorCode: {
        type: "int32",
        id: 1
      },
      errorMessage: {
        type: "string",
        id: 2
      }
    }
  },
  RequestReportDtoProto: {
    fields: {
      placerOrderNO: {
        type: "string",
        id: 1
      },
      patientName: {
        type: "string",
        id: 2
      },
      gender: {
        type: "string",
        id: 3
      },
      age: {
        type: "int32",
        id: 4
      },
      ageUnit: {
        type: "string",
        id: 5
      },
      contactPhoneNO: {
        type: "string",
        id: 6
      },
      medRecNO: {
        type: "string",
        id: 7
      },
      patientClass: {
        type: "string",
        id: 8
      },
      outPatientID: {
        type: "string",
        id: 9
      },
      checkArea: {
        type: "string",
        id: 10
      },
      examItem: {
        type: "string",
        id: 11
      },
      alternateVisitID: {
        type: "string",
        id: 12
      },
      bed: {
        type: "string",
        id: 13
      },
      symptom: {
        type: "string",
        id: 14
      },
      clinicDiagnosis: {
        type: "string",
        id: 15
      },
      otherClinicalInfo: {
        type: "string",
        id: 16
      },
      reason: {
        type: "string",
        id: 17
      },
      attention: {
        type: "string",
        id: 18
      },
      requestDocName: {
        type: "string",
        id: 19
      },
      requestDept: {
        type: "string",
        id: 20
      },
      requestTime: {
        type: "string",
        id: 21
      },
      displayAge: {
        type: "string",
        id: 22
      }
    }
  },
  RightInputProto: {
    fields: {
      roleUID: {
        type: "string",
        id: 1
      },
      userUID: {
        type: "string",
        id: 2
      },
      isSuperManager: {
        type: "string",
        id: 3
      }
    }
  },
  RightMstOutputProto: {
    fields: {
      rightID: {
        type: "string",
        id: 1
      },
      rightClass: {
        type: "string",
        id: 2
      },
      rightName: {
        type: "string",
        id: 3
      },
      title: {
        type: "string",
        id: 4
      },
      controllerName: {
        type: "string",
        id: 5
      },
      actionName: {
        type: "string",
        id: 6
      },
      parameter: {
        type: "string",
        id: 7
      },
      active: {
        type: "string",
        id: 8
      },
      parentRightID: {
        type: "string",
        id: 9
      },
      sortNO: {
        type: "string",
        id: 10
      },
      memo: {
        type: "string",
        id: 11
      },
      lAY_CHECKED: {
        type: "string",
        id: 12
      }
    }
  },
  RoleMstInputProto: {
    fields: {
      roleUID: {
        type: "string",
        id: 1
      },
      roleName: {
        type: "string",
        id: 2
      },
      createUserUID: {
        type: "string",
        id: 3
      },
      createUserName: {
        type: "string",
        id: 4
      },
      createDate: {
        type: "string",
        id: 5
      },
      memo: {
        type: "string",
        id: 6
      },
      organizationID: {
        type: "string",
        id: 7
      },
      currentPage: {
        type: "int32",
        id: 8
      },
      pageSize: {
        type: "int32",
        id: 9
      }
    }
  },
  RoleMstProto: {
    fields: {
      roleUID: {
        type: "string",
        id: 1
      },
      roleName: {
        type: "string",
        id: 2
      },
      createUserUID: {
        type: "string",
        id: 3
      },
      createUserName: {
        type: "string",
        id: 4
      },
      createDate: {
        type: "string",
        id: 5
      },
      memo: {
        type: "string",
        id: 6
      },
      organizationID: {
        type: "string",
        id: 7
      },
      organizationName: {
        type: "string",
        id: 8
      }
    }
  },
  RoleRightMstInputProto: {
    fields: {
      roleUID: {
        type: "string",
        id: 1
      },
      rightID: {
        type: "string",
        id: 2
      },
      userUID: {
        type: "string",
        id: 3
      }
    }
  },
  ScriptMstProto: {
    fields: {
      scriptID: {
        type: "int32",
        id: 1
      },
      script: {
        type: "string",
        id: 2
      },
      scriptType: {
        type: "string",
        id: 3
      },
      createDate: {
        type: "string",
        id: 4
      },
      lastEditDate: {
        type: "string",
        id: 5
      },
      creator: {
        type: "string",
        id: 6
      },
      lastEditor: {
        type: "string",
        id: 7
      },
      scriptDescription: {
        type: "string",
        id: 8
      },
      scriptMemo: {
        type: "string",
        id: 9
      },
      programVersion: {
        type: "string",
        id: 10
      },
      scriptContent: {
        type: "string",
        id: 11
      }
    }
  },
  ScriptMstBatchProto: {
    fields: {
      scriptIDs: {
        type: "string",
        id: 1
      }
    }
  },
  SendPathientPhoneCodeInput: {
    fields: {
      phoneNumber: {
        type: "string",
        id: 1
      },
      accessionNumber: {
        type: "string",
        id: 2
      },
      organizationID: {
        type: "string",
        id: 3
      }
    }
  },
  SendPathientPhoneCodeOutput: {
    fields: {
      validCode: {
        type: "string",
        id: 1
      }
    }
  },
  ServiceInputProto: {
    fields: {
      serviceUID: {
        type: "string",
        id: 1
      },
      serviceName: {
        type: "string",
        id: 2
      },
      ifEnable: {
        type: "string",
        id: 3
      },
      ifDelete: {
        type: "string",
        id: 4
      },
      pageSize: {
        type: "int32",
        id: 5
      },
      currentPage: {
        type: "int32",
        id: 6
      }
    }
  },
  ServiceOutputProto: {
    fields: {
      serviceUID: {
        type: "string",
        id: 1
      },
      serviceName: {
        type: "string",
        id: 2
      },
      ifEnable: {
        type: "bool",
        id: 3
      },
      ifDelete: {
        type: "bool",
        id: 4
      }
    }
  },
  ShareExamInputProto: {
    fields: {
      accessionNumber: {
        type: "string",
        id: 1
      },
      organizationID: {
        type: "string",
        id: 2
      },
      expireMin: {
        type: "int32",
        id: 3
      },
      relatedAuth: {
        type: "bool",
        id: 4
      }
    }
  },
  ShareExamOutputProto: {
    fields: {
      examToken: {
        type: "string",
        id: 1
      }
    }
  },
  StorageDtoProto: {
    fields: {
      mediaUID: {
        type: "string",
        id: 1
      },
      name: {
        type: "string",
        id: 2
      },
      type: {
        type: "string",
        id: 3
      },
      path: {
        type: "string",
        id: 4
      },
      organizationID: {
        type: "string",
        id: 5
      },
      subDir: {
        type: "string",
        id: 6
      },
      ifEnable: {
        type: "string",
        id: 7
      },
      customConfig: {
        type: "string",
        id: 8
      },
      description: {
        type: "string",
        id: 9
      },
      host: {
        type: "string",
        id: 10
      },
      bucket: {
        type: "string",
        id: 11
      },
      accessID: {
        type: "string",
        id: 12
      },
      accessKey: {
        type: "string",
        id: 13
      },
      isSharePath: {
        type: "string",
        id: 14
      },
      shareAddress: {
        type: "string",
        id: 15
      },
      shareUserName: {
        type: "string",
        id: 16
      },
      sharePassWord: {
        type: "string",
        id: 17
      },
      uploadMediaUID: {
        type: "string",
        id: 18
      },
      userUID: {
        type: "string",
        id: 19
      },
      uploadURL: {
        type: "string",
        id: 20
      },
      downloadURL: {
        type: "string",
        id: 21
      }
    }
  },
  StorageInputProto: {
    fields: {
      mediaUID: {
        type: "string",
        id: 1
      },
      pageSize: {
        type: "int32",
        id: 2
      },
      currentPage: {
        type: "int32",
        id: 3
      },
      organizationID: {
        type: "string",
        id: 4
      }
    }
  },
  StorageTempProto: {
    fields: {
      mediaUID: {
        type: "string",
        id: 1
      },
      name: {
        type: "string",
        id: 2
      },
      type: {
        type: "string",
        id: 3
      },
      path: {
        type: "string",
        id: 4
      },
      organizationID: {
        type: "string",
        id: 5
      },
      subDir: {
        type: "string",
        id: 6
      },
      ifEnable: {
        type: "string",
        id: 7
      },
      customConfig: {
        type: "string",
        id: 8
      },
      description: {
        type: "string",
        id: 9
      },
      organizationName: {
        type: "string",
        id: 10
      },
      bucket: {
        type: "string",
        id: 11
      },
      accessID: {
        type: "string",
        id: 12
      },
      accessKey: {
        type: "string",
        id: 13
      },
      isSharePath: {
        type: "string",
        id: 14
      },
      shareAddress: {
        type: "string",
        id: 15
      },
      shareUserName: {
        type: "string",
        id: 16
      },
      sharePassWord: {
        type: "string",
        id: 17
      },
      host: {
        type: "string",
        id: 18
      },
      uploadMediaUID: {
        type: "string",
        id: 19
      },
      userUID: {
        type: "string",
        id: 20
      },
      uploadURL: {
        type: "string",
        id: 21
      },
      downloadURL: {
        type: "string",
        id: 22
      }
    }
  },
  DicItemInputProto: {
    fields: {
      typeCode: {
        type: "string",
        id: 1
      },
      searchOrganizationID: {
        type: "string",
        id: 2
      }
    }
  },
  DicItemOutputProto: {
    fields: {
      label: {
        type: "string",
        id: 1
      },
      value: {
        type: "string",
        id: 2
      }
    }
  },
  SysParameterMstProto: {
    fields: {
      code: {
        type: "string",
        id: 1
      },
      name: {
        type: "string",
        id: 2
      },
      value: {
        type: "string",
        id: 3
      },
      module: {
        type: "string",
        id: 4
      },
      memo: {
        type: "string",
        id: 5
      }
    }
  },
  SysParameterInputProto: {
    fields: {
      code: {
        type: "string",
        id: 1
      },
      name: {
        type: "string",
        id: 2
      },
      pageSize: {
        type: "int32",
        id: 3
      },
      currentPage: {
        type: "int32",
        id: 4
      }
    }
  },
  ParamAppenderProto: {
    fields: {
      file: {
        type: "string",
        id: 1
      },
      maxSizeRollBackups: {
        type: "string",
        id: 2
      },
      appendToFile: {
        type: "string",
        id: 3
      },
      maximumFileSize: {
        type: "string",
        id: 4
      },
      layoutPattern: {
        type: "string",
        id: 5
      },
      rollingStyle: {
        type: "string",
        id: 6
      },
      datePattern: {
        type: "string",
        id: 7
      },
      level: {
        type: "string",
        id: 8
      }
    }
  },
  DBConfigDtoProto: {
    fields: {
      dbType: {
        type: "string",
        id: 1
      },
      lsSlave: {
        type: "string",
        id: 2
      },
      dataSource: {
        type: "string",
        id: 3
      },
      initialCatalog: {
        type: "string",
        id: 4
      },
      userId: {
        type: "string",
        id: 5
      },
      password: {
        type: "string",
        id: 6
      },
      hostPort: {
        type: "string",
        id: 7
      },
      dbInstallType: {
        type: "string",
        id: 8
      }
    }
  },
  TokenInfoProto: {
    fields: {
      tokenServer: {
        type: "string",
        id: 1
      },
      accessToken: {
        type: "string",
        id: 2
      },
      organizationID: {
        type: "string",
        id: 3
      }
    }
  },
  UploadImageOutputProto: {
    fields: {
      relativePathList: {
        rule: "repeated",
        type: "string",
        id: 1
      }
    }
  },
  UserDisableInputProto: {
    fields: {
      userUID: {
        type: "string",
        id: 1
      },
      status: {
        type: "bool",
        id: 2
      }
    }
  },
  UserMstEntityInputProto: {
    fields: {
      userUID: {
        type: "string",
        id: 1
      },
      account: {
        type: "string",
        id: 2
      },
      password: {
        type: "string",
        id: 3
      },
      type: {
        type: "string",
        id: 4
      },
      name: {
        type: "string",
        id: 5
      },
      iDCardNO: {
        type: "string",
        id: 6
      },
      officePhone: {
        type: "string",
        id: 7
      },
      privatePhone: {
        type: "string",
        id: 8
      },
      email: {
        type: "string",
        id: 9
      },
      address: {
        type: "string",
        id: 10
      },
      status: {
        type: "string",
        id: 11
      },
      organizationID: {
        type: "string",
        id: 12
      },
      deptID: {
        type: "string",
        id: 13
      },
      workNO: {
        type: "string",
        id: 14
      },
      validityStartDate: {
        type: "string",
        id: 15
      },
      validityEndDate: {
        type: "string",
        id: 16
      },
      createUserUID: {
        type: "string",
        id: 17
      },
      createUserName: {
        type: "string",
        id: 18
      },
      createDate: {
        type: "string",
        id: 19
      },
      lastLogonTime: {
        type: "string",
        id: 20
      },
      memo: {
        type: "string",
        id: 21
      },
      rowTimestamp: {
        type: "string",
        id: 22
      },
      updateDate: {
        type: "string",
        id: 23
      },
      isSuperManager: {
        type: "string",
        id: 24
      }
    }
  },
  UserMstInfoOutputProto: {
    fields: {
      userUID: {
        type: "string",
        id: 1
      },
      account: {
        type: "string",
        id: 2
      },
      password: {
        type: "string",
        id: 3
      },
      type: {
        type: "string",
        id: 4
      },
      name: {
        type: "string",
        id: 5
      },
      iDCardNO: {
        type: "string",
        id: 6
      },
      officePhone: {
        type: "string",
        id: 7
      },
      privatePhone: {
        type: "string",
        id: 8
      },
      email: {
        type: "string",
        id: 9
      },
      address: {
        type: "string",
        id: 10
      },
      status: {
        type: "bool",
        id: 11
      },
      organizationID: {
        type: "string",
        id: 12
      },
      deptID: {
        type: "string",
        id: 13
      },
      workNO: {
        type: "string",
        id: 14
      },
      validityStartDate: {
        type: "string",
        id: 15
      },
      validityEndDate: {
        type: "string",
        id: 16
      },
      createUserUID: {
        type: "string",
        id: 17
      },
      createUserName: {
        type: "string",
        id: 18
      },
      createDate: {
        type: "string",
        id: 19
      },
      lastLogonTime: {
        type: "string",
        id: 20
      },
      memo: {
        type: "string",
        id: 21
      },
      updateDate: {
        type: "string",
        id: 22
      },
      userStatus: {
        type: "string",
        id: 23
      },
      organizationName: {
        type: "string",
        id: 24
      },
      deptName: {
        type: "string",
        id: 25
      }
    }
  },
  UserAccountProto: {
    fields: {
      account: {
        type: "string",
        id: 1
      }
    }
  },
  UserWorkNOInfoProto: {
    fields: {
      workNO: {
        type: "string",
        id: 1
      },
      organizationID: {
        type: "string",
        id: 2
      }
    }
  },
  UserMstInputProto: {
    fields: {
      userUID: {
        type: "string",
        id: 1
      },
      account: {
        type: "string",
        id: 2
      },
      password: {
        type: "string",
        id: 3
      },
      type: {
        type: "string",
        id: 4
      },
      name: {
        type: "string",
        id: 5
      },
      iDCardNO: {
        type: "string",
        id: 6
      },
      officePhone: {
        type: "string",
        id: 7
      },
      privatePhone: {
        type: "string",
        id: 8
      },
      email: {
        type: "string",
        id: 9
      },
      address: {
        type: "string",
        id: 10
      },
      status: {
        type: "string",
        id: 11
      },
      organizationID: {
        type: "string",
        id: 12
      },
      deptID: {
        type: "string",
        id: 13
      },
      workNO: {
        type: "string",
        id: 14
      },
      validityStartDate: {
        type: "string",
        id: 15
      },
      validityEndDate: {
        type: "string",
        id: 16
      },
      createUserUID: {
        type: "string",
        id: 17
      },
      createUserName: {
        type: "string",
        id: 18
      },
      createDate: {
        type: "string",
        id: 19
      },
      lastLogonTime: {
        type: "string",
        id: 20
      },
      memo: {
        type: "string",
        id: 21
      },
      updateDate: {
        type: "string",
        id: 22
      },
      currentPage: {
        type: "int32",
        id: 23
      },
      pageSize: {
        type: "int32",
        id: 24
      }
    }
  },
  UserMstProto: {
    fields: {
      userUID: {
        type: "string",
        id: 1
      },
      account: {
        type: "string",
        id: 2
      },
      password: {
        type: "string",
        id: 3
      },
      type: {
        type: "string",
        id: 4
      },
      name: {
        type: "string",
        id: 5
      },
      iDCardNO: {
        type: "string",
        id: 6
      },
      officePhone: {
        type: "string",
        id: 7
      },
      privatePhone: {
        type: "string",
        id: 8
      },
      email: {
        type: "string",
        id: 9
      },
      address: {
        type: "string",
        id: 10
      },
      status: {
        type: "string",
        id: 11
      },
      organizationID: {
        type: "string",
        id: 12
      },
      deptID: {
        type: "string",
        id: 13
      },
      workNO: {
        type: "string",
        id: 14
      },
      validityStartDate: {
        type: "string",
        id: 15
      },
      validityEndDate: {
        type: "string",
        id: 16
      },
      createUserUID: {
        type: "string",
        id: 17
      },
      createUserName: {
        type: "string",
        id: 18
      },
      createDate: {
        type: "string",
        id: 19
      },
      lastLogonTime: {
        type: "string",
        id: 20
      },
      memo: {
        type: "string",
        id: 21
      },
      rowTimestamp: {
        type: "string",
        id: 22
      },
      updateDate: {
        type: "string",
        id: 23
      },
      isCurrentPageOpen: {
        type: "string",
        id: 24
      }
    }
  },
  VerificationCodeProto: {
    fields: {
      key: {
        type: "string",
        id: 1
      },
      code: {
        type: "string",
        id: 2
      }
    }
  },
  UserQuerySetInputProto: {
    fields: {
      userId: {
        type: "string",
        id: 1
      },
      querySeq: {
        type: "int32",
        id: 2
      },
      userInfo: {
        type: "UserOrgInfoProto",
        id: 3
      },
      queryType: {
        type: "string",
        id: 4
      }
    }
  },
  UserQuerySetMstProto: {
    fields: {
      querySeq: {
        type: "int32",
        id: 1
      },
      queryType: {
        type: "string",
        id: 2
      },
      userUID: {
        type: "string",
        id: 3
      },
      name: {
        type: "string",
        id: 4
      },
      queryCondition: {
        type: "string",
        id: 5
      },
      sortNO: {
        type: "string",
        id: 6
      },
      defaultFlag: {
        type: "string",
        id: 7
      },
      publicFlag: {
        type: "string",
        id: 8
      }
    }
  },
  UserResetInputProto: {
    fields: {
      userUID: {
        type: "string",
        id: 1
      },
      account: {
        type: "string",
        id: 2
      },
      organizationID: {
        type: "string",
        id: 3
      }
    }
  },
  UserRightInputProto: {
    fields: {
      userUID: {
        type: "string",
        id: 1
      }
    }
  },
  UserRoleInputProto: {
    fields: {
      userUID: {
        type: "string",
        id: 1
      },
      organizationID: {
        type: "string",
        id: 2
      }
    }
  },
  UserUIDInputProto: {
    fields: {
      userUID: {
        type: "string",
        id: 1
      }
    }
  },
  VisitInputProto: {
    fields: {
      patientName: {
        type: "string",
        id: 1
      },
      pointOfCareID: {
        type: "string",
        id: 2
      },
      bed: {
        type: "string",
        id: 3
      },
      admitDeptID: {
        type: "string",
        id: 4
      },
      attendingDoctorID: {
        type: "string",
        id: 5
      },
      directorDoctorName: {
        type: "string",
        id: 6
      },
      medRecNO: {
        type: "string",
        id: 7
      },
      visitID: {
        type: "string",
        id: 8
      },
      age: {
        type: "int32",
        id: 9
      },
      ageUnit: {
        type: "string",
        id: 10
      },
      gender: {
        type: "string",
        id: 11
      },
      birthDay: {
        type: "string",
        id: 12
      },
      organizationID: {
        type: "string",
        id: 13
      },
      patientClass: {
        type: "string",
        id: 14
      },
      admitStartDate: {
        type: "string",
        id: 15
      },
      admitEndDate: {
        type: "string",
        id: 16
      },
      curPatCondition: {
        type: "string",
        id: 17
      },
      nursingGrade: {
        type: "string",
        id: 18
      },
      dietType: {
        type: "string",
        id: 19
      },
      quickSearch: {
        type: "string",
        id: 20
      },
      pageSize: {
        type: "int32",
        id: 21
      },
      currentPage: {
        type: "int32",
        id: 22
      },
      token: {
        type: "string",
        id: 23
      },
      isInteragency: {
        type: "string",
        id: 24
      },
      isInteragencyExam: {
        type: "string",
        id: 25
      },
      IsInteragencyClinic: {
        type: "string",
        id: 26
      },
      IsInteragencyStatistic: {
        type: "string",
        id: 27
      },
      userInfo: {
        type: "UserOrgInfoProto",
        id: 28
      },
      IsInteragencyData: {
        type: "string",
        id: 29
      }
    }
  },
  VisitPeopleInputProto: {
    fields: {
      patientMasterID: {
        type: "string",
        id: 1
      },
      visitUID: {
        type: "string",
        id: 2
      },
      pageSize: {
        type: "int32",
        id: 3
      },
      CurrentPage: {
        type: "int32",
        id: 4
      },
      token: {
        type: "string",
        id: 5
      },
      isInteragency: {
        type: "string",
        id: 6
      },
      isInteragencyExam: {
        type: "string",
        id: 7
      },
      isInteragencyClinic: {
        type: "string",
        id: 8
      },
      isInteragencyStatistic: {
        type: "string",
        id: 9
      },
      userInfo: {
        type: "UserOrgInfoProto",
        id: 10
      },
      isInteragencyData: {
        type: "string",
        id: 11
      }
    }
  },
  VisitPeopleProto: {
    fields: {
      patientName: {
        type: "string",
        id: 1
      },
      gender: {
        type: "string",
        id: 2
      },
      age: {
        type: "int32",
        id: 3
      },
      ageUnit: {
        type: "string",
        id: 4
      },
      patientClass: {
        type: "string",
        id: 5
      },
      patientMasterID: {
        type: "string",
        id: 6
      },
      visitUID: {
        type: "string",
        id: 7
      },
      medRecNO: {
        type: "string",
        id: 8
      },
      patientID: {
        type: "string",
        id: 9
      },
      pointOfCare: {
        type: "string",
        id: 10
      },
      pointOfCareID: {
        type: "string",
        id: 11
      },
      bed: {
        type: "string",
        id: 12
      },
      healthCardNO: {
        type: "string",
        id: 13
      },
      nation: {
        type: "string",
        id: 14
      },
      birthPlace: {
        type: "string",
        id: 15
      },
      maritalStatus: {
        type: "string",
        id: 16
      },
      iDCardNo: {
        type: "string",
        id: 17
      },
      occupation: {
        type: "string",
        id: 18
      },
      contactPhoneNO: {
        type: "string",
        id: 19
      },
      email: {
        type: "string",
        id: 20
      },
      homePhoneNO: {
        type: "string",
        id: 21
      },
      addressDetail: {
        type: "string",
        id: 22
      },
      workUnit: {
        type: "string",
        id: 23
      },
      businessPhoneNO: {
        type: "string",
        id: 24
      },
      cardType: {
        type: "string",
        id: 25
      },
      cardNO: {
        type: "string",
        id: 26
      },
      outPatientNO: {
        type: "string",
        id: 27
      },
      inPatientNO: {
        type: "string",
        id: 28
      },
      reAmissionFlag: {
        type: "string",
        id: 29
      },
      directorDoctorName: {
        type: "string",
        id: 30
      },
      attendingDoctorName: {
        type: "string",
        id: 31
      },
      admitDate: {
        type: "string",
        id: 32
      },
      dischargeDate: {
        type: "string",
        id: 33
      },
      deptName: {
        type: "string",
        id: 34
      }
    }
  },
  WorkloadDtoProto: {
    fields: {
      count: {
        type: "string",
        id: 1
      },
      row1: {
        type: "string",
        id: 2
      },
      row2: {
        type: "string",
        id: 3
      },
      column1: {
        type: "string",
        id: 4
      },
      column2: {
        type: "string",
        id: 5
      }
    }
  },
  WorkloadInputProto: {
    fields: {
      rows: {
        type: "string",
        id: 1
      },
      columns: {
        type: "string",
        id: 2
      },
      registerTime: {
        type: "string",
        id: 3
      },
      patientClass: {
        type: "string",
        id: 4
      },
      organizationID: {
        type: "string",
        id: 5
      },
      requestDeptName: {
        type: "string",
        id: 6
      },
      serviceSectID: {
        type: "string",
        id: 7
      },
      resultStatus: {
        type: "string",
        id: 8
      },
      criticalValue: {
        type: "string",
        id: 9
      },
      dateField: {
        type: "string",
        id: 10
      },
      startDate: {
        type: "string",
        id: 11
      },
      endDate: {
        type: "string",
        id: 12
      }
    }
  },
  WorkloadPlusDtoProto: {
    fields: {
      workloadDto: {
        rule: "repeated",
        type: "WorkloadDtoProto",
        id: 1
      },
      row1Name: {
        type: "string",
        id: 2
      },
      row2Name: {
        type: "string",
        id: 3
      },
      column1Name: {
        type: "string",
        id: 4
      },
      column2Name: {
        type: "string",
        id: 5
      },
      row1DisplayName: {
        type: "string",
        id: 6
      },
      row2DisplayName: {
        type: "string",
        id: 7
      },
      column1DisplayName: {
        type: "string",
        id: 8
      },
      column2DisplayName: {
        type: "string",
        id: 9
      },
      rowTotal: {
        type: "int32",
        id: 10
      },
      columnTotal: {
        type: "int32",
        id: 11
      }
    }
  },
  WrittenInputProto: {
    fields: {
      examUID: {
        type: "string",
        id: 1
      },
      pageSize: {
        type: "int32",
        id: 2
      },
      currentPage: {
        type: "int32",
        id: 3
      },
      token: {
        type: "string",
        id: 4
      },
      isInteragency: {
        type: "string",
        id: 5
      },
      isInteragencyExam: {
        type: "string",
        id: 6
      },
      isInteragencyClinic: {
        type: "string",
        id: 7
      },
      isInteragencyStatistic: {
        type: "string",
        id: 8
      },
      userInfo: {
        type: "UserOrgInfoProto",
        id: 9
      },
      isInteragencyData: {
        type: "string",
        id: 10
      },
      applyMethod: {
        type: "string",
        id: 13
      },
      isInterconnectData: {
        type: "string",
        id: 14
      }
    }
  },
  WrittenReportProto: {
    fields: {
      patientName: {
        type: "string",
        id: 1
      },
      gender: {
        type: "string",
        id: 2
      },
      age: {
        type: "int32",
        id: 3
      },
      ageUnit: {
        type: "string",
        id: 4
      },
      patientID: {
        type: "string",
        id: 5
      },
      medRecNO: {
        type: "string",
        id: 6
      },
      alternateVisitID: {
        type: "string",
        id: 7
      },
      outPatientID: {
        type: "string",
        id: 8
      },
      requestDept: {
        type: "string",
        id: 9
      },
      pointOfCareID: {
        type: "string",
        id: 10
      },
      pointOfCare: {
        type: "string",
        id: 11
      },
      bed: {
        type: "string",
        id: 12
      },
      serviceSectID: {
        type: "string",
        id: 13
      },
      examItem: {
        type: "string",
        id: 14
      },
      examTime: {
        type: "string",
        id: 15
      },
      clinicDiagnosis: {
        type: "string",
        id: 16
      },
      checkArea: {
        type: "string",
        id: 17
      },
      observationMethod: {
        type: "string",
        id: 18
      },
      dicomView: {
        type: "string",
        id: 19
      },
      dicomConsultation: {
        type: "string",
        id: 20
      },
      resultAssistantName: {
        type: "string",
        id: 21
      },
      resultPrincipalName: {
        type: "string",
        id: 22
      },
      resultDate: {
        type: "string",
        id: 23
      },
      resultReviseName: {
        type: "string",
        id: 24
      },
      reviseDate: {
        type: "string",
        id: 25
      },
      auditDate: {
        type: "string",
        id: 26
      },
      organizationName: {
        type: "string",
        id: 27
      }
    }
  }
});

module.exports = $root;
