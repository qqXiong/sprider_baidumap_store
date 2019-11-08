#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Lqq
# @Software: PyCharm

import pymysql


class Database:
    def __init__(self, host, port, user, passwd, db, charset, table):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.db = db
        self.charset = charset
        self.table = table

    # 获取连接对象
    def get_conn(self):

        try:
            conn = pymysql.connect(
                host=self.host,
                port=int(self.port),
                user=self.user,
                passwd=self.passwd,
                db=self.db,
                charset=self.charset
            )
            return conn
        except Exception as e:
            print(e)
            exit(-1)

    def is_exsit(self, values):
        # 获取执行工具
        conn = self.get_conn()
        cur = conn.cursor()
        try:
            select_sql = "SELECT * FROM " + self.table + " WHERE name='%s' AND di_tag='%s' AND tel='%s' AND point='%s' " \
                                                         "AND lat_lon='%s' AND addr='%s' AND shop_hours='%s' AND image='%s' " % values
            if cur.execute(select_sql) == 0:
                return True
            else:
                return False
        except Exception as e:
            print(e)
            return False
        finally:
            # 对该数据库操作完记得关闭
            cur.close()
            conn.close()

    '''  
        插入
        @website_name
        @website_url
    '''

    def insert_store(self, fdata):
        # 获取执行工具
        conn = self.get_conn()
        cur = conn.cursor()
        try:
            # self.headers = {'名称': '', '类型': '', '电话': '', '坐标': '', '经纬度': '', '地址': '', '营业时间': '', '评价': '', '图片': '',
            #                 '评论': '', '关键字': '', '城市编码': '', '页码': ''}
            v = (
                pymysql.escape_string(fdata["名称"]),
                pymysql.escape_string(fdata["类型"]),
                pymysql.escape_string(fdata["电话"]),
                pymysql.escape_string(fdata["坐标"]),
                pymysql.escape_string(fdata["经纬度"]),
                pymysql.escape_string(fdata["地址"]),
                pymysql.escape_string(fdata["营业时间"]),
                pymysql.escape_string(fdata["图片"]))

            flag = self.is_exsit(v)
            if flag:
                values = (pymysql.escape_string(fdata["名称"]), pymysql.escape_string(fdata["类型"]),
                          pymysql.escape_string(fdata["电话"]), pymysql.escape_string(fdata["坐标"]),
                          pymysql.escape_string(fdata["经纬度"]), pymysql.escape_string(fdata["地址"]),
                          pymysql.escape_string(fdata["营业时间"]), pymysql.escape_string(fdata["评价"]),
                          pymysql.escape_string(fdata["图片"]), pymysql.escape_string(fdata["评论"]),
                          pymysql.escape_string(fdata["关键字"]), pymysql.escape_string(fdata["城市编码"]),
                          pymysql.escape_string(fdata["页码"]))
                # Sql语句
                sql = "INSERT INTO " + self.table + "(name, di_tag,tel,point,lat_lon,addr,shop_hours,cater_tag,image," \
                                                    "comment,keyword,city_code,page) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s," \
                                                    "%s,%s,%s,%s)"

                cur.execute(sql, values)
                conn.commit()
        except Exception as e:
            print(e)
            conn.rollback()
        finally:
            # 对该数据库操作完记得关闭
            cur.close()
            conn.close()


if __name__ == '__main__':
    fdata = {}
    fdata['名称'] = '宝哥味馆'
    fdata['类型'] = '美食 火锅'
    fdata['电话'] = '+852-23320998 '
    fdata['坐标'] = '12710983.60,2532369.29'
    fdata['经纬度'] = '(22.1772547329618, 114.19561851341852)'
    fdata['地址'] = '香港佐敦长乐街6-12A号 Man Hing Building'
    fdata['营业时间'] = '17:30-24:00'
    fdata['评价'] = ''
    fdata['图片'] = '8694a4c27d1ed21bcaa21a4fa36eddc451da3f34.jpg'
    fdata['评论'] = ''
    fdata['关键字'] = '火锅'
    fdata['城市编码'] = '2912'
    fdata['页码'] = '1'
    Database('localhost', '3306', 'root', '123456', 'local_database', 'utf8', 'store').insert_store(fdata)
    pass
