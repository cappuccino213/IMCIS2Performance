#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/24 11:23 
# @Author  : Zhangyp
# @File    : getToken.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
import requests

from config import cfg


def get_token():
    header = {'Content-Type': 'application/json'}
    url = cfg.get('Token', 'url')+'/Token/RetriveInternal'
    body = {
        "ProductName": "eWordIMCIS",
        "HospitalCode": "QWYHZYFZX",
        "RequestIP": "192.168.1.56"
    }
    token_str = requests.post(url, headers=header, json=body).json()['token']
    return token_str


token = get_token()

if __name__ == '__main__':
    print(token)
