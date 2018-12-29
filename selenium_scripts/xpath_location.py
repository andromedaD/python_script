from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
#启动浏览器
driver=webdriver.Firefox()
#获取百度地址
driver.get("http://www.baidu.com")
sleep(2)
#通过xpath定位元素
driver.find_element_by_xpath("//input[@id='kw']").send_keys("hello world")
#用Keys方法模拟键盘输入
driver.find_element_by_xpath("//input[@id='su']").send_keys(Keys.RETURN)
sleep(2)
print("完成")
#关闭浏览器
driver.quit()



























