#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/26 17:45 
# @Author  : Zhangyp
# @File    : script.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
from locust import TaskSet, constant, task
from locust.contrib.fasthttp import FastHttpUser
from getToken import token
from config import cfg

from compileProtobuf.dstPb.UserOrgInfoProto.Proto_pb2 import UserOrgInfoProto

import logging

HOST = cfg.get('Locust', 'host')
# 除登录接口以外的header
HEAD = {'Content-Type': 'application/octet-stream',
        'Authorization': token,
        'UserInfo': '{"userUID":"29d6a026-f774-4c9d-904c-e492a4246e10","organizationID":"-1"}'}

# 接口调用用户对象
user_info = UserOrgInfoProto()
user_info.userUID = "29d6a026-f774-4c9d-904c-e492a4246e10"
user_info.organizationID = "-1"

# 声明api调用的权重
_weight = {"login_task": 1,
           "check_info_list": 5,
           "get_doc_status": 10,
           "get_written_report": 10,
           "get_doc": 10,
           "get_recode_exam": 5}


class ApiTask(TaskSet):
    # tasks = [login_task]
    # 随机选取任务执行
    # tasks = {login_task: 1}
    # 调用api的通用方法
    def api_request(self, path, header, name, payload=None):
        with self.client.post(path=HOST + path, headers=header, name=name, data=payload,
                              catch_reponse=True) as response:  # 接口返回断言
            from compileProtobuf.dstPb.PageResponse_pb2 import PageResponse
            pr = PageResponse()
            pr.ParseFromString(response.content)
            if response.status_code != 200:
                response.failure(response.status_code)
                if not pr.isSuccess:
                    response.failure(pr.message)
            else:
                # from google.protobuf.json_format import MessageToJson
                # json_data = MessageToJson(response)
                # print(response.status_code, pr)
                logging.info("API{0} 返回代码:{1} 测试结果isSuccess:{2}".format(path, response.status_code, pr.isSuccess))
                # logging.info(pr)

    # 登录
    @task(_weight["login_task"])
    def login_task(self):
        from compileProtobuf.dstPb.AuthorizeInfoProto_pb2 import AdminLoginInputProto
        payload = AdminLoginInputProto()
        # 入参
        payload.account = 'Admin'
        payload.password = 'TomTaw@HZ'
        payload.organizationID = '-1'
        payload.userType = 3
        payload = payload.SerializeToString()
        self.api_request('/api/login/userlogin', HEAD, '登录接口', payload)

    # 查询检查列表
    @task(_weight["check_info_list"])
    def check_info_list(self):
        from compileProtobuf.dstPb.CheckInfoProto_pb2 import SearchInputProto
        payload = SearchInputProto()
        payload.ageUnit = '岁'
        payload.currentPage = 1
        payload.examStartTime = '2021-02-09 00:00:00'
        payload.examEndTime = '2021-02-09 23:59:59'
        payload.organizationID = "sxdqyy"
        payload.currentPage = 1
        payload.pageSize = 20
        payload.userInfo.CopyFrom(user_info)
        payload = payload.SerializeToString()
        self.api_request('/api/check/getcheckinfolist', HEAD, '查询检查列表', payload)

    # 获取报告状态
    @task(_weight["get_doc_status"])
    def get_doc_status(self):
        from compileProtobuf.dstPb.CheckInfoProto_pb2 import SearchInputProto
        payload = SearchInputProto()
        payload.ageUnit = '岁'
        payload.accessionNumber = '20210209870975'
        payload.organizationID = "sxdqyy"
        payload.currentPage = 1
        payload.pageSize = 20
        payload.userInfo.CopyFrom(user_info)
        payload = payload.SerializeToString()
        self.api_request('/api/check/getdocstatus', HEAD, '获取报告状态', payload)

    # 获取文字报告
    @task(_weight["get_written_report"])
    def get_written_report(self):
        from compileProtobuf.dstPb.WrittenInputProto_pb2 import WrittenInputProto
        payload = WrittenInputProto()
        payload.examUID = '7cec6f78-7501-443a-9c83-e4f719ce5521'
        payload.userInfo.CopyFrom(user_info)
        payload = payload.SerializeToString()
        self.api_request('/api/check/getwrittenreport', HEAD, '获取文字报告', payload)

    # 获取报告、胶片、影像
    @task(_weight["get_doc"])
    def get_doc(self):
        from compileProtobuf.dstPb.DocumentInputProto_pb2 import DocumentInputProto
        payload = DocumentInputProto()
        payload.examUID = '7cec6f78-7501-443a-9c83-e4f719ce5521'
        payload.typeCode = 'ExamResult'  # 获取的文件类型
        payload.userInfo.CopyFrom(user_info)
        payload = payload.SerializeToString()
        self.api_request('/api/check/getdoc', HEAD, '获取图文报告', payload)

    # 获取相关检查
    @task(_weight["get_recode_exam"])
    def get_recode_exam(self):
        from compileProtobuf.dstPb.PersonalCheckRcdInputProto_pb2 import PersonalCheckRcdInputProto
        payload = PersonalCheckRcdInputProto()
        payload.patientMasterID = '6bfb72a5-0537-4a67-984b-132deac02b46'
        # payload_rec_exam.personExamUID=''
        payload.examUID = '7cec6f78-7501-443a-9c83-e4f719ce5521'
        payload.organizationID = 'sxsrmyy'
        payload.accessionNumber = '20210209870975'
        payload.userInfo.CopyFrom(user_info)
        payload = payload.SerializeToString()
        self.api_request('/api/check/getrecordexam', HEAD, '获取相关检查', payload)


class CallAPIUser(FastHttpUser):
    tasks = [ApiTask]
    # 任务执行间隔时间
    wait_time = constant(2)
