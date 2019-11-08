#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/16 14:06
# @Author  : Lqq
# @FileName: provinces.py
# @Software: PyCharm

import codecs
from util.excel import read_excel, get_cell_map

booksheet = read_excel("./file/行政区划乡镇清单201907.xlsx", 0)

'''
    获取所有省
'''


def map_all_province():
    colnumber_b = ord('B') - ord('A')
    colnumber_c = ord('C') - ord('A')
    map_province = get_cell_map(colnumber_b, colnumber_c, booksheet)
    return map_province


'''
    获取所有地级市
'''


def map_all_city():
    colnumber_d = ord('D') - ord('A')
    colnumber_e = ord('E') - ord('A')
    map_city = get_cell_map(colnumber_d, colnumber_e, booksheet)
    return map_city


'''
    获取所有区县
'''


def map_all_town():
    colnumber_f = ord('F') - ord('A')
    colnumber_g = ord('G') - ord('A')
    map_town = get_cell_map(colnumber_f, colnumber_g, booksheet)
    return map_town


'''
    获取所有乡镇
'''


def map_all_village():
    colnumber_h = ord('H') - ord('A')
    colnumber_i = ord('I') - ord('A')
    map_village = get_cell_map(colnumber_h, colnumber_i, booksheet)
    return map_village


'''
    获取所有的城市code
    @txt_url key
'''


def map_city_code(txt_url):
    f = codecs.open(txt_url, mode='r', encoding='utf-8')  # 打开txt文件，以‘utf-8'编码读取
    line = f.readline()  # 以行的形式进行读取文件
    map = {}
    while line:
        a = line.split(",")
        map[a[1]] = a[0]
        line = f.readline()
        line = line.rstrip("\r\n")
    f.close()
    return map


if __name__ == "__main__":
    print(map_all_village())
    print(map_city_code("../file/BaiduMap_cityCode_1102.txt"))
