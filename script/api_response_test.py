#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/26 10:45 
# @Author  : Zhangyp
# @File    : api_response_test.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
from getToken import token
import requests
from config import cfg

HOST = cfg.get('Locust', 'host')
# 除登录接口以外的header
HEAD = {'Content-Type': 'application/octet-stream',
        'Authorization': token,
        'UserInfo': '{"userUID":"29d6a026-f774-4c9d-904c-e492a4246e10","organizationID":"-1"}'}


def api_response_time_test(method, path, header, payload=None):
    response = requests.request(method=method, url=HOST + path, headers=header, data=payload)
    if response.status_code == 200:
        from compileProtobuf.dstPb.PageResponse_pb2 import PageResponse
        pr = PageResponse()
        pr.ParseFromString(response.content)
        if pr.isSuccess:
            response_time = str(response.elapsed.total_seconds())
        else:
            response_time = 'time_out'
            print(pr.message)
        print('接口{0}的响应时间：{1} sec.'.format(path, response_time))
    else:
        print('接口{0}响应失败,返回结果：{1}'.format(path, response.text))


"""声明用例"""
# 登录
from compileProtobuf.dstPb.AuthorizeInfoProto_pb2 import AdminLoginInputProto

payload_lg = AdminLoginInputProto()
payload_lg.account = 'Admin'
payload_lg.password = 'TomTaw@HZ'
payload_lg.organizationID = '-1'
payload_lg.userType = 3
payload_lg = payload_lg.SerializeToString()

login_case = {'method': 'post',
              'path': '/api/login/userlogin',
              # 'header': {'Content-Type': 'application/octet-stream'},
              'header': HEAD,
              'payload': payload_lg}

# 检查列表
from compileProtobuf.dstPb.CheckInfoProto_pb2 import SearchInputProto

payload_cil = SearchInputProto()
payload_cil.ageUnit = '岁'
payload_cil.currentPage = 1
payload_cil.examStartTime = '2021-02-09 00:00:00'
payload_cil.examEndTime = '2021-02-09 23:59:59'
payload_cil.organizationID = "sxdqyy"
payload_cil.currentPage = 1
payload_cil.pageSize = 20

from compileProtobuf.dstPb.UserOrgInfoProto.Proto_pb2 import UserOrgInfoProto

user_info = UserOrgInfoProto()
user_info.userUID = "29d6a026-f774-4c9d-904c-e492a4246e10"
user_info.organizationID = "-1"
payload_cil.userInfo.CopyFrom(user_info)
payload_cil = payload_cil.SerializeToString()

check_info_list_case = {'method': 'post',
                        'path': '/api/check/getcheckinfolist',
                        'header': HEAD,
                        'payload': payload_cil}

# 获取检查结果状态
payload_dt = SearchInputProto()
payload_dt.ageUnit = '岁'
payload_dt.accessionNumber = '20210209870975'
payload_dt.organizationID = "sxdqyy"
payload_dt.currentPage = 1
payload_dt.pageSize = 20
# from compileProtobuf.dstPb.UserOrgInfoProto.Proto_pb2 import UserOrgInfoProto
# user_info = UserOrgInfoProto()
# user_info.userUID = "29d6a026-f774-4c9d-904c-e492a4246e10"
# user_info.organizationID = "-1"
payload_dt.userInfo.CopyFrom(user_info)
payload_dt = payload_dt.SerializeToString()

get_doc_status_case = {'method': 'post',
                       'path': '/api/check/getdocstatus',
                       'header': HEAD,
                       'payload': payload_dt}

# 获取文字报告
from compileProtobuf.dstPb.WrittenInputProto_pb2 import WrittenInputProto

payload_wtr = WrittenInputProto()
payload_wtr.examUID = '7cec6f78-7501-443a-9c83-e4f719ce5521'
# payload_wtr.currentPage = 1
# payload_wtr.pageSize = 20

payload_wtr.userInfo.CopyFrom(user_info)
payload_wtr = payload_wtr.SerializeToString()

get_report_case = {'method': 'post',
                   'path': '/api/check/getwrittenreport',
                   'header': HEAD,
                   'payload': payload_wtr}

# 获取图文报告
from compileProtobuf.dstPb.DocumentInputProto_pb2 import DocumentInputProto

payload_doc = DocumentInputProto()
payload_doc.examUID = '7cec6f78-7501-443a-9c83-e4f719ce5521'
payload_doc.typeCode = 'ExamResult'  # 获取的文件类型
payload_doc.userInfo.CopyFrom(user_info)
payload_doc = payload_doc.SerializeToString()

get_doc_case = {'method': 'post',
                'path': '/api/check/getdoc',
                'header': HEAD,
                'payload': payload_doc}

# 相关检查
from compileProtobuf.dstPb.PersonalCheckRcdInputProto_pb2 import PersonalCheckRcdInputProto

payload_rec_exam = PersonalCheckRcdInputProto()
payload_rec_exam.patientMasterID = '6bfb72a5-0537-4a67-984b-132deac02b46'
# payload_rec_exam.personExamUID=''
payload_rec_exam.examUID = '7cec6f78-7501-443a-9c83-e4f719ce5521'
payload_rec_exam.organizationID = 'sxsrmyy'
payload_rec_exam.accessionNumber = '20210209870975'
payload_rec_exam.userInfo.CopyFrom(user_info)
payload_rec_exam = payload_rec_exam.SerializeToString()

get_record_exam = {'method': 'post',
                'path': '/api/check/getrecordexam',
                'header': HEAD,
                'payload': payload_rec_exam}

"""装载用例"""
# case_list = [get_record_exam]
case_list = [login_case, check_info_list_case, get_doc_status_case, get_report_case, get_doc_case,get_record_exam]
# case_list.extend([login_case, check_info_list_case, get_doc_status_case, get_report_case, get_doc_case])

if __name__ == '__main__':
    for case in case_list:
        api_response_time_test(case['method'], case['path'], case['header'], case['payload'])
