# -*- coding: utf-8 -*-
import pandas as pd
import json
from urllib.request import urlopen, quote
import csv
import traceback
import os


# 构造获取经纬度的函数
def getlnglat(address):
    url = 'http://api.map.baidu.com/geocoder/v2/?address='
    output = 'json'
    ak = 'KFxKtpauFnzGfh8mGwFaej0SNXUDMedI'#需填入自己申请应用后生成的ak
    add = quote(address)  # 本文城市变量为中文，为防止乱码，先用quote进行编码
    url2 = url + add + '&output=' + output + "&ak=" + ak
    req = urlopen(url2)
    res = req.read().decode()
    temp = json.loads(res)
    return temp


file = open('经纬度.json', 'w')  # 建立json数据文件
data_1 = pd.read_csv("house_price.csv")  # 读取小区房价信息
for i in data_1.values:
    try:
        b = i[0].strip()
        c = str(i[1]).strip()
        lng = getlnglat(b)['result']['location']['lng']  # 获取经度
        lat = getlnglat(b)['result']['location']['lat']  # 获取纬度
        str_temp = '{"lat":' + str(lat) + ',"lng":' + str(lng) + ',"count":' + str(c) + '},'
        file.write(str_temp)
    except:
        f = open("异常日志.txt", 'a')
        traceback.print_exc(file=f)
        f.flush()
        f.close()
file.close()
