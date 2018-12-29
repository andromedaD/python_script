from LoginPage import *
from selenium import webdriver
import threading
driver=webdriver.Firefox()

username='wangjin'
password='123456'


test_user_login(driver,username,password)


sleep(2)
driver.quit()


