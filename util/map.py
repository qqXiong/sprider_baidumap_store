#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/17 11:54
# @Author  : Lqq
# @FileName: map.py
# @Software: PyCharm
import traceback

import requests
import json
import hashlib
import urllib3

import time
from urllib.parse import urlencode
from urllib import parse
from requests.auth import HTTPBasicAuth
from gevent import monkey

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
monkey.patch_socket()

'''
设置请求头，模拟浏览器访问
'''
headers = {
    # 'User-Agent':useragent.random
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    # 'Host':"map.baidu.com",
    # "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    # "Accept-Encoding": "gzip, deflate",
    # "Accept-Language": "en-US,en;q=0.5",
    # "Connection": "keep-alive",
    # "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:39.0) Gecko/20100101 Firefox/39.0"
}

'''
    读取url百度地图列表页面url
    http://map.baidu.com/?newmap=1&reqflag=pcmap&biz=1&from=webmap&da_par=direct&pcevaname=pc4.1&qt=s&da_src=searchBox.button&wd=人民广场&c=289&pn=0
    # 百度地图搜索url
    https://map.baidu.com/?newmap=1&reqflag=pcmap&biz=1&from=webmap&da_par=direct&pcevaname=pc4.1&qt=spot&from=webmap&c=179&wd=%E6%B5%B7%E9%B2%9C&wd2=&pn=0&nn=0&db=0&sug=0
    &addr=0&district_name=%E8%A5%BF%E6%B9%96%E5%8C%BA&business_name=%E9%BB%84%E9%BE%99
    &pl_data_type=cater&pl_sub_type=%E4%B8%AD%E9%A4%90%E9%A6%86-%E6%B5%B7%E9%B2%9C&pl_price_section=0%2C%2B&pl_sort_type=default
    &pl_sort_rule=0&pl_discount2_section=0%2C%2B&pl_groupon_section=0%2C%2B&pl_cater_book_pc_section=0%2C%2B&pl_hotel_book_pc_section=0%2C%2B&pl_ticket_book_flag_section=0%2C%2B
    &pl_movie_book_section=0%2C%2B&pl_business_type=cater&pl_business_id=&da_src=pcmappg.poi.page&src=7&l=16&rn=50&tn=B_NORMAL_MAP&
    auth=dxNAW8Z1CNOg4LPNWw38K%40YVd3b9%3DEe9uxHNxBNTEBEt1qo6DF%3D%3DCy1uVt1GgvPUDZYOYIZuNtJiCPB4A300b0z8yPWv3GuNNt%3DkVJ0IUvhgMZSguxzBEHLNRTVtcEWe1GD8zv7ucvY1SGpuxxti0XE22b1n1G%408DvxKtx3MV%40MP8P8hhJeh33uxxtC00dE224
    &u_loc=13357224,3518203&ie=utf-8&b=(13373117.128707765,3512479.402371555;13381309.128707765,3515015.402371555)&
    t=1571379434715
    百度地图查看店铺信息
    https://map.baidu.com/?uid=b79c73d5bc657c049b68b466&primaryUid=10169780587290664768&ugc_type=3&ugc_ver=1&qt=detailConInfo&device_ratio=2&compat=1&t=1571386127460&
    auth=FzcRXb6bI%40a7RfJ2EG8xaLgOBK7yFfuxHNxBRLxzEtykiOxAXXwy1uVt1GgvPUDZYOYIZuBtGfyMxXwGccZcuVtPWv3GuRtVcOC%40BUvhgMZSguxzBEHLNRTVtcEWe1GDdw8E62qvy7ue21aD%40ZPuTtmDFSCtvJrvIKTZKNbNMMTHimNNzCys99XvF
    # 百度地图评论信息
    http://map.baidu.com/detail?qt=ugccmtlist&from=mapwap&type=cater&orderBy=1&pageCount=10&uid=b79c73d5bc657c049b68b466&pageIndex=1
    关键字auth 少了这个 会少了数据
    @keyword1 关键字
    @keyword2 关键字
    @code 城市code
'''


def get_url(keyword, keyword2, code, page):
    try:
        auth = HTTPBasicAuth('ryan', 'password')
        data = {
            'newmap': '1',
            'reqflag': 'pcmap',
            'biz': '1',
            # 'from': 'webmap',
            'da_par': 'direct',
            'pcevaname': 'pc4.1',
            "qt": "s",  # con
            # 'from': 'webmap',
            # 'da_src': 'searchBox.button',
            'c': code,  # 城市代码
            'wd': keyword,  # 修改关键字
            # 'wd2': keyword2,
            'pn': page,  # 页数
            'da_src': 'searchBox.button',
            # "nn": 70,
            # "db": 0,
            # "sug": 0,
            # "addr": 0,
            # 'district_name': district_name,  # 限制区
            # 'business_name': business_name,
            # 'rn': 50,  # 显示内容数量
            # 'auth': auth,
            # 'pl_data_type': "data_type",
            # 'pl_sub_type': "0,+",
            # "pl_price_section": "0,+",
            # "pl_sort_type": "default",
            # "pl_sort_rule": "0",
            # "pl_discount2_section": "0,+",
            # "pl_groupon_section": "0,+",
            # "pl_cater_book_pc_section": "0,+",
            # "pl_hotel_book_pc_section": "0,+",
            # "pl_ticket_book_flag_section": "0,+",
            # "pl_movie_book_section": "0,+",
            # 'pl_business_type': "0,+",
            # 'pl_business_id': "0,+",
            # "da_src": "pcmappg.poi.page",  # 固定
            # "on_gel": "1",
            # "src": "7",
            # "gr": "3",
            # 'l': '10',
            # "tn": "B_NORMAL_MAP",
            # 'ie': 'utf-8',
            # 'auth':auth,
            # "t": "1468896652886",
        }
        # 把字典对象转化为url的请求参数
        url = 'https://map.baidu.com/?' + urlencode(data)
        return url
    except Exception as e:
        print(e)
        traceback.print_exc()


'''
    获取页面
    @url
'''


def get_json(url):
    while 1:
        try:
            response = requests.get(url, headers=headers, timeout=60)
            response.encoding = 'utf-8'
            data = response.text
            jdata = json.loads(data)
            return jdata
        except Exception as e:
            print(e)
            print("Connection refused by the server..")
            print("Let me sleep for 5 seconds")
            print("ZZzzzz...")
            time.sleep(5)
            print("Was a nice sleep, now let me continue...")
            continue


'''
    检测目标字段tagkey是否在data(json数据)中
    @data json
    @tagkey key
'''


def is_extend(jsonObject, tagkey):
    try:
        if (tagkey in jsonObject):
            return True
        else:
            return False
    except Exception as e:
        print(e)
        traceback.print_exc()


'''
    页数
    @html
'''


def page_total(url):
    try:
        jdata = get_json(url)
        if is_extend(jdata, 'result'):
            num = jdata['result']['total']
            return num
    except Exception as e:
        print(e)
        traceback.print_exc()


'''
    根据ak百度地图地址转经纬度
    @addr
'''


def addr_lan(addr):
    # 以get请求为例http://api.map.baidu.com/geocoder/v2/?address=百度大厦&output=json&ak=你的ak
    queryStr = '/geocoder/v2/?address=%s&output=json&ak=rBHgzWXGwp7M0w0E8MSUUzrr' % addr
    # 对queryStr进行转码，safe内的保留字符不转换
    encodedStr = parse.quote(queryStr, safe="/:=&?#+!$,;'@()*[]")
    # 在最后直接追加上yoursk
    rawStr = encodedStr + 'rBHgzWXGwp7M0w0E8MSUUzrr'
    # 计算sn
    sn = (hashlib.md5(parse.quote_plus(rawStr).encode("utf8")).hexdigest())
    # 由于URL里面含有中文，所以需要用parse.quote进行处理，然后返回最终可调用的url
    url = parse.quote("http://api.map.baidu.com" + queryStr + "&sn=" + sn, safe="/:=&?#+!$,;'@()*[]")
    while 1:
        try:
            response = requests.get(url, headers=headers, timeout=60, verify=False)
            response.encoding = 'utf-8'
            return response.text
        except Exception as e:
            print(e)
            print("Connection refused by the server..")
            print("Let me sleep for 5 seconds")
            print("ZZzzzz...")
            time.sleep(5)
            print("Was a nice sleep, now let me continue...")
            continue



'''
    百度地图评论页面
    http://map.baidu.com/detail?qt=ninf&uid=648e73c9455b962c9d95de67&detail=cater
    http://map.baidu.com/detail?qt=ugccmtlist&from=mapwap&type=cater&orderBy=1&pageCount=10&uid=648e73c9455b962c9d95de67&=1
    @uid
'''


def comment_html(uid, cater):
    req = {
        'qt': 'ugccmtlist',
        'from': 'mapwap',
        'type': cater,
        'orderBy': '1',
        "uid": uid,
        "pageIndex": '1',
    }
    url = 'https://map.baidu.com/detail?' + urlencode(req)
    # s = requests.Session()
    # response = s.get(url=url,headers=header)
    while 1:
        try:
            response = requests.get(url, headers=headers, timeout=60, verify=False)
            response.encoding = 'utf-8'
            return response.text
        except Exception as e:
            print(e)
            print("Connection refused by the server..")
            print("Let me sleep for 5 seconds")
            print("ZZzzzz...")
            time.sleep(5)
            print("Was a nice sleep, now let me continue...")
            continue



'''
    百度地图评论
    @html
'''


def get_comment(html):
    count = 0
    couments = []
    try:
        data = json.loads(html)
        for comment_item in data["comment"]["comment_list"]:
            count = count + 1
            if count > 0:
                couments.append(comment_item["user_name"])  # 姓名
                couments.append(comment_item["date"])  # 日期
                couments.append(comment_item["content"])  # 评论内容
            elif count > 3:
                break

        return "|".join(str(i) for i in couments)
    except Exception as e:
        print(e)
        traceback.print_exc()


if __name__ == '__main__':
    # ls('30.697218', '104.073694')
    # print(ll('12641100.91','2514969.31'))
    count = 0
    # result = []
    # # for keyword in map_all_classc():
    # #     url = get_url(keyword, '', '2911', 0)
    #
    # url = get_url('火锅', '', '2911', 0)
    # total = page_total(url)
    # # aa = ['''https://map.baidu.com/?newmap=1&reqflag=pcmap&biz=1&from=webmap&da_par=direct&pcevaname=pc4.1&qt=con&c=179&wd=%E6%B5%B7%E9%B2%9C&wd2=%E7%BE%8E%E9%A3%9F&pn={}'''.format(i+1)for i in range(5) ]
    # # # for i in aa:
    # #     # print(i)
    # for i in range(total):
    #     u = get_url('火锅', '', '2911', str(i+1))
    #     # print(u)
    #     result.extend(get_content(u))
    #     print(len(result))

    # # headers = ['名称','类型','电话','经度','纬度','地址','营业时间','评价','评论','图片']
    # # writeExcelFile("../file/excel/"+TimeDuration().now()+".xlsx",headers,all_data)
    # df =pandas.DataFrame(result)
    # df.to_excel("../file/excel/"+time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))+".xlsx",index=False)

    # aa = [(
    #     '''https://map.baidu.com/?newmap=1&reqflag=pcmap&biz=1&from=webmap&da_par=direct&pcevaname=pc4.1&qt=con&da_src=pcmappg.poi.page&c=179&wd=%E6%B5%B7%E9%B2%9C&wd2=%E7%BE%8E%E9%A3%9F&pn={}&nn=70&db=0&sug=0&addr=0&district_name=%E8%A5%BF%E6%B9%96%E5%8C%BA&business_name=%E9%BB%84%E9%BE%99&rn=50&auth=%3Crequests.auth.HTTPBasicAuth+object+at+0x0000019CFBBBED08%3E&tn=B_NORMAL_MAP&pl_data_type=0%2C%2B&pl_sub_type=0%2C%2B&pl_price_section=0%2C%2B&pl_sort_type=default&pl_sort_rule=0&pl_discount2_section=0%2C%2B&pl_groupon_section=0%2C%2B&pl_cater_book_pc_section=0%2C%2B&pl_hotel_book_pc_section=0%2C%2B&pl_ticket_book_flag_section=0%2C%2B&pl_movie_book_section=0%2C%2B&pl_business_type=0%2C%2B&pl_business_id=0%2C%2B&on_gel=1&src=7&gr=3&ie=utf-8&t=1468896652886''').format(
    #     i + 1) for i in range(2019)]
    # for c in aa:
    #     print(c)
    #     # html = get_html(c)
    #     data = get_content(c)
    #     print(len(all_data))
    # total = page_total(html)
    # count = count + total
    # print(count)
    # print(count)
    # for page in range(total):
    #     html = get_page('海鲜', '179', page,'西湖区','黄龙')
    #     r = get_data(html)
    #     if r == None:
    #         break
    #     result.extend(r)
    # print(result)
    # while True:
    #     html = get_page('海鲜', '179', str(count),'西湖区','黄龙')
    #     num = page_total(html)
    #     count = count + num
    #     r = get_data(html)
    #     if len(r):
    #         # print(r)
    #         result.extend(r)
    #     else:
    #         break
    # print(count)
    # headers = ['名称','类型','电话','经度','纬度','地址','营业时间','评价','评论','图片']
    # writeExcelFile("../file/excel/"+TimeDuration().now()+".xlsx",headers,result)
