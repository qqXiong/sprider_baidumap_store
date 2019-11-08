#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/18 17:32
# @Author  : Lqq
# @FileName: business.py
# @Software: PyCharm

from util.excel import read_excel, get_cell_map

booksheet = read_excel("./file/行业关键字.xlsx", 0)

'''
    获取三级类别关键字
'''


def map_all_classa():
    try:
        colnumber_b = ord('A') - ord('A')
        colnumber_c = ord('B') - ord('A')
        map_classa = get_cell_map(colnumber_b, colnumber_c, booksheet)
        return map_classa
    except Exception as e:
        print(e)


if __name__ == "__main__":
    print(map_all_classa())
