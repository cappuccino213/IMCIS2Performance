#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/19 15:31
# @Author  : Zhangyp
# @File    : CompileProto.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com

import os

"""找proto文件"""


def find_proto(path):
    import os
    dirs = os.listdir(path)  # 获取指定路径下的文件
    proto_list = [i for i in dirs if os.path.splitext(i)[1].lower() == '.proto']
    return proto_list


"""编译proto成.py"""


def proto2py(src_path, des_path):
    import subprocess
    proto_files = find_proto(src_path)
    if proto_files:
        for file in proto_files:
            cli = "protoc -I=%s --python_out=%s %s" % (src_path, des_path, file)
            print(cli)
            try:
                subprocess.Popen(cli, stdout=subprocess.PIPE, shell=True)  # 编译proto生成py文件
            except Exception as e:
                raise str(e)


if __name__ == '__main__':
    proto2py('srcProto', 'dstPb')
    # files = find_proto('srcProto')
    # print(files)
