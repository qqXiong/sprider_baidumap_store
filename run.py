#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/10 10:58
# @Author  : Lqq
# @FileName:
# @Software: PyCharm

import time
import sys, os
import traceback
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']

from PyQt5 import QtCore, QtWidgets
from view.provinces import Ui_Form
from util.provinces import map_all_city, map_city_code
from util.point import LngLatTransfer
from util.map import get_url, page_total, get_json, get_comment, is_extend, comment_html
from util.business import map_all_classa
from util.file import get_desk_p
from util.pic import save_img
from util.database import Database

class Worker(QtCore.QThread):
    sig = QtCore.pyqtSignal(dict)

    def __init__(self, parent=None):
        super(Worker, self).__init__(parent)
        self.working = True
        self.city_name = None
        self.keyword = None
        # 获取所有的城市code
        self.map_city_codes = map_city_code("./file/BaiduMap_cityCode.txt")
        # 获取所有的关键词
        self.keywords = map_all_classa()

    def __del__(self):
        self.working = False
        self.wait()

    def setVal(self, city_name,keyword):
        self.city_name = str(city_name)
        self.keyword = str(keyword)

        ##执行线程的run方法
        self.start()

    def run(self):
        while self.working == True:
            count = 0
            if self.city_name:
                city_code = self.map_city_codes[self.city_name]
                if self.keyword:
                    url = get_url(self.keyword, '', str(city_code), 0)
                    # 获取页总数
                    total = page_total(url)
                    for page in range(total):
                        u = get_url(self.keyword, '', str(city_code), page)
                        self.get_content(u, self.city_name, page, city_code, self.keywords.get(key))
                else:
                    for key in self.keywords:
                        if key:
                            url = get_url(self.keywords.get(key), '', str(city_code), 0)
                            # 获取页总数
                            total = page_total(url)
                            count = count + total
                            for page in range(total):
                                u = get_url(self.keywords.get(key), '', str(city_code), page)
                                self.get_content(u,self.city_name,page,city_code,self.keywords.get(key))
                        pass


    def get_content(self, url, city_name, page, city_code, keyword):
        try:
            global location, comment, l
            jdata = get_json(url)
            if is_extend(jdata, 'content'):
                for i in jdata['content']:
                    fdata = {}
                    if i.get('area_name'):
                        area_name = str(i.get('area_name'))[0:len(city_name)]
                        if area_name == city_name:
                            if i.get('name'):

                                try:
                                    fdata['名称'] = i['name']
                                except:
                                    fdata['名称'] = ''

                                try:
                                    fdata['类型'] = i['di_tag']
                                except:
                                    fdata['类型'] = ''

                                try:
                                    fdata['电话'] = i['tel']
                                except:
                                    fdata['电话'] = '0'

                                try:
                                    strs = i['geo'].split("|")
                                    p = strs[2][:-1].split(",")
                                    lng, lat = LngLatTransfer().WebMercator_to_WGS84(float(p[0]), float(p[1]))
                                    l = LngLatTransfer().WGS84_to_BD09(lng, lat)
                                    fdata['坐标'] = strs[2][:-1]
                                    fdata['经纬度'] = str(l)
                                except:
                                    fdata['坐标'] = ''
                                    fdata['经纬度'] = ''

                                try:
                                    fdata['地址'] = i['addr']
                                except:
                                    fdata['地址'] = ''

                                try:
                                    fdata['营业时间'] = i['ext']['detail_info']['shop_hours']
                                except:
                                    fdata['营业时间'] = ''

                                try:
                                    fdata['评价'] = i['ext']['detail_info']['cater_tag']
                                except:
                                    fdata['评价'] = ''

                                try:
                                    imgurl = i['ext']['detail_info']['image']
                                    self.dir_ = get_desk_p() + "/img"
                                    pic_path = save_img(self.dir_, imgurl)
                                    fdata['图片'] = pic_path
                                except:
                                    fdata['图片'] = ''

                                try:
                                    text = comment_html(i['uid'], i['ext']['src_name'])
                                    comment = get_comment(text)
                                    fdata['评论'] = comment
                                except:
                                    fdata['评论'] = ''

                                fdata['关键字'] = keyword
                                fdata['城市编码'] = city_code
                                fdata['页码'] = str(page)
                                self.sig.emit(fdata)
                time.sleep(1)
        except Exception:
            traceback.print_exc()

class Combosel(QtWidgets.QWidget):
    def __init__(self):
        super(Combosel, self).__init__()

        self.db = ''

        # 获取所有的城市code
        self.map_city_codes = map_city_code("./file/BaiduMap_cityCode.txt")
        # 获取所有的关键词
        self.keywords = map_all_classa()

        self.ui_sel = Ui_Form()
        self.ui_sel.setupUi(self)
        self.ui_sel.comboBox_city.clear()
        self.ui_sel.comboBox_city.addItem(u'请选择')
        self.dict_city = map_all_city()
        # 初始化城市
        for (keys, val) in self.dict_city.items():
            self.ui_sel.comboBox_city.addItem(val, QtCore.QVariant(keys))

        # 创建新线程，将自定义信号sinOut连接到slotAdd()槽函数
        self.thread = Worker()
        self.thread.sig.connect(self.get_result)

        # 连接自己的槽函数
        self.ui_sel.okButton.clicked.connect(self.onActivatedokButton)


    def get_result(self, fdata):
        print(fdata)

        host = self.ui_sel.host.text()
        port = self.ui_sel.port.text()
        user = self.ui_sel.user.text()
        passwd = self.ui_sel.passwd.text()
        db = self.ui_sel.database.text()
        charset = self.ui_sel.charset.text()

        table = self.ui_sel.table.text()
        Database(host, port, user, passwd, db, charset, table).insert_store(fdata)
        self.ui_sel.result.insertPlainText("店名：" + fdata['名称'] + "\n")
        text_cur = self.ui_sel.result.textCursor().End
        self.ui_sel.result.moveCursor(text_cur)
        pass

    # 点击确定导出excel到本地
    def onActivatedokButton(self):
        try:
            #清理结果集
            self.ui_sel.result.clear()
            self.ui_sel.result.insertPlainText("请稍等正在获取数据....." + "\n")
            city_index = self.ui_sel.comboBox_city.currentIndex()
            keyword = self.ui_sel.keyWord.text()
            city_name = self.ui_sel.comboBox_city.itemText(city_index)

            # 清理结果集
            self.ui_sel.result.clear()
            self.thread.setVal(city_name,keyword)
            self.thread.start()
        except Exception:
            traceback.print_exc()


if __name__ == "__main__":
    try:
        app = QtWidgets.QApplication(sys.argv)
        Appcombosel = Combosel()
        Appcombosel.show()
        sys.exit(app.exec_())
    except Exception:
        traceback.print_exc()
