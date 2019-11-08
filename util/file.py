#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/28 12:57
# @Author  : Lqq
# @FileName: file.py
# @Software: PyCharm
# 引入模块
import os


def get_desk_p():
    return os.path.join(os.path.expanduser('~'), "Desktop")


def mkdir(path):
    try:
        # 去除首位空格
        path = path.strip()
        # 去除尾部 \ 符号
        path = path.rstrip("\\")

        # 判断路径是否存在
        # 存在     True
        # 不存在   False
        isExists = os.path.exists(path)

        # 判断结果
        if not isExists:
            # 如果不存在则创建目录
            # 创建目录操作函数
            os.makedirs(path)
            return True
        else:
            # 如果目录存在则不创建，并提示目录已存在
            return False
    except Exception as e:
        print(e)


if __name__ == '__main__':
    # 定义要创建的目录
    mkpath = "d:\\qttc\\web\\"
    # 调用函数
    mkdir(mkpath)
