#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/24 10:40
# @Author  : Zhangyp
# @File    : run.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com

from config import cfg
import subprocess

test_host = cfg.get('Locust', 'host')
run_web = cfg.get('Locust', 'web')
port = cfg.get_int('Locust', 'port')


def locust_cl(script):
    cli = "locust -f {0} -H {1} --web-host {2} -P {3} --loglevel INFO".format(script, test_host, run_web, port)
    print(cli)
    try:
        cl = subprocess.Popen(cli, stdout=subprocess.PIPE, shell=True)
        print(cl.stdout.readlines())  # 打印控制台信息
    except Exception as e:
        raise str(e)


if __name__ == '__main__':
    locust_cl('./script/script.py')
