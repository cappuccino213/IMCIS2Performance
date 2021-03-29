#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/24 11:01 
# @Author  : Zhangyp
# @File    : test_request.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com

from config import cfg

import requests

"""调试接口"""


def test_api():
    host = cfg.get('Locust', 'host')
    # header = {'Content-Type': 'application/octet-stream',
    #           'Content-Length': '0'}
    # api = '/api/register/getorgbylogin'
    # res = requests.post(host + api, headers=header, data=None)
    # print(res.content)

    header = {'Content-Type': 'application/octet-stream'}
    api = '/api/login/userlogin'
    from compileProtobuf.dstPb.AuthorizeInfoProto_pb2 import AdminLoginInputProto
    payload = AdminLoginInputProto()
    payload.account = 'Admin'
    # payload.account = 'admin'
    payload.password = 'TomTaw@HZ'
    # payload.password = '123456'
    payload.organizationID = '-1'
    payload.userType = 3
    payload = payload.SerializeToString()

    res = requests.post(host + api, data=payload, headers=header)
    from compileProtobuf.dstPb.PageResponse_pb2 import PageResponse
    response = PageResponse()
    response.ParseFromString(res.content)

    from compileProtobuf.dstPb.AdminLoginUserInfoProto_pb2 import AdminLoginUserInfoProto
    response_data = AdminLoginUserInfoProto()
    response_data.ParseFromString(response.data)

    print(res.status_code, response.isSuccess, response_data)


"""api_performance_statistic.py
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/25 10:50 
# @Author  : Zhangyp
# @File    : api_performance_statistic.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com

from config import cfg
from getToken import token
import requests


def api_test1():
    host = cfg.get('Locust', 'host')
    header = {'Content-Type': 'application/octet-stream',
              'Authorization': token,
              'UserInfo': '{"userUID":"29d6a026-f774-4c9d-904c-e492a4246e10","organizationID":"-1"}'}
    api = '/api/check/getcheckinfolist'
    from compileProtobuf.dstPb.CheckInfoProto_pb2 import SearchInputProto
    payload = SearchInputProto()
    payload.ageUnit = '岁'
    payload.currentPage = 1
    payload.examStartTime = '2021-02-09 00:00:00'
    payload.examEndTime = '2021-02-09 23:59:59'
    payload.organizationID = "sxdqyy"
    payload.currentPage = 1
    payload.pageSize = 20
    from compileProtobuf.dstPb.UserOrgInfoProto.Proto_pb2 import UserOrgInfoProto
    user_info = UserOrgInfoProto()
    user_info.userUID = "29d6a026-f774-4c9d-904c-e492a4246e10"
    user_info.organizationID = "-1"
    payload.userInfo.CopyFrom(user_info)

    payload = payload.SerializeToString()
    res = requests.post(host + api, data=payload, headers=header)
    if res.status_code == 200:
        from compileProtobuf.dstPb.PageResponse_pb2 import PageResponse
        response = PageResponse()
        response.ParseFromString(res.content)
        if response.isSuccess:
            response_time = str(res.elapsed.total_seconds())
            # 解析消息
            # from google.protobuf.json_format import MessageToJson
            # json_data = MessageToJson(response)
            # print(json_data)
            # if response.data:
            #     for msg in response.data:
            #         from google.protobuf.json_format import MessageToJson
            #         json_msg = MessageToJson(msg)
            #         # spe_msg.Unpack(msg)
            #         print(json_msg.encode('utf-8').decode("unicode_escape"))
        else:
            response_time = 'time_out'
        print('响应时间：%s sec.' % response_time)
    else:
        print('响应失败')


def api_test():
    host = cfg.get('Locust', 'host')
    header = {'Content-Type': 'application/octet-stream'}
    api = '/api/login/userlogin'
    from compileProtobuf.dstPb.AuthorizeInfoProto_pb2 import AdminLoginInputProto
    payload = AdminLoginInputProto()
    payload.account = 'Admin'
    # payload.account = 'admin'
    payload.password = 'TomTaw@HZ'
    # payload.password = '123456'
    payload.organizationID = '-1'
    payload.userType = 3
    payload = payload.SerializeToString()
    res = requests.post(host + api, data=payload, headers=header)
    if res.status_code == 200:
        from compileProtobuf.dstPb.PageResponse_pb2 import PageResponse
        response = PageResponse()
        response.ParseFromString(res.content)
        if response.isSuccess:
            response_time = str(res.elapsed.total_seconds())
        else:
            response_time = 'time_out'
        print('响应时间：%s sec.' % response_time)
    else:
        print('响应失败')


if __name__ == '__main__':
    api_test1()

"""


if __name__ == '__main__':
    test_api()
