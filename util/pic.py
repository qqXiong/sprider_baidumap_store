#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/28 9:52
# @Author  : Lqq
# @FileName: pic.py
# @Software: PyCharm

import requests

from PIL import Image
from io import BytesIO
from util.file import mkdir,get_desk_p


def save_img(dir_, imgurl):
    if imgurl:
        pics =imgurl.split(".")
        pic = pics[len(pics)-2].split("/")
        pic_name = pic[len(pic)-1]
        mkdir(dir_)
        response = requests.get(imgurl)
        response = response.content
        BytesIOObj = BytesIO()
        BytesIOObj.write(response)
        BytesIOObj.seek(0)
        img = Image.open(BytesIOObj)
        if img.mode == "P":
            img = img.convert('RGB')
        elif img.mode == "RGBA":
            img = img.convert('RGB')
        img.save(dir_+"/"+pic_name+".jpg")
        return pic_name +".jpg"


if __name__ == '__main__':
    dir_ = get_desk_p() + "/img"
    save_img(dir_,"https://img-my.csdn.net/uploads/201212/25/1356422284_1112.jpg")
