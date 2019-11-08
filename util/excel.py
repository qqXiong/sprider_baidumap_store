#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/16 14:11
# @Author  : Lqq
# @FileName: excel.py
# @Software: PyCharm

import xlrd

'''
    读取XLS,XLSX文件
    @filename 文件路径
    @index 打开excel第几个工作薄
'''


def read_excel(filename, index):
    # 打开工作表
    workbook = xlrd.open_workbook(filename=filename)
    # 用索引取第一个工作薄
    booksheet = workbook.sheet_by_index(index)
    return booksheet


'''
    列对列变成键值对集合
    @colnumber_a key
    @colnumber_b value
    @booksheet sheet
'''


def get_cell_map(colnumber_a, colnumber_b, booksheet):
    map = {}
    for i in range(booksheet.nrows):
        if i > 0:
            map[booksheet.cell(i, colnumber_a).value] = booksheet.cell(i, colnumber_b).value
    return map


if __name__ == "__main__":
    booksheet = read_excel("../file/行业分类.xlsx", 0)
    # writeExcel(booksheet)
    # colnumber_b = ord('B')-ord('A')
    # colnumber_c = ord('C')-ord('A')
    # map = get_cell_map(colnumber_b,colnumber_c,booksheet)
    # print(map)
    # headers = ['名称','类型','电话','经纬度','地址','营业时间','评价','评论','图片']
    # writeExcelFile("../file/excel/"+TimeDuration().now()+".xlsx",headers,)
