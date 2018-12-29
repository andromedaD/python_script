# -*- coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# 共37页进行爬虫
driver = webdriver.Firefox()
driver.get('http://api.map.baidu.com/lbsapi/getpoint/index.html')
time.sleep(5)
element1 = driver.find_element_by_link_text("更换城市")
element1.click()
element2 = driver.find_element_by_link_text("上海")
element2.click()
time.sleep(5)
element3 = driver.find_element_by_id("localvalue")
element3.send_keys("地铁站")
element3.send_keys(Keys.RETURN)  # 此步为关键格式！！！这样html内容才会改变
time.sleep(2)

element = ''
for i in range(37):
    element += driver.find_element_by_id("txtPanel").text
    loc = driver.find_element_by_link_text("下一页")
    loc.click()
    time.sleep(5)
    i += 1

file_handle = open("C:\\Users\\metro.txt", mode='w+')
file_handle.write(element)
file_handle.close()
