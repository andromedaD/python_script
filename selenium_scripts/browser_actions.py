from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()

driver.get("http://www.51zxw.net")
driver.maximize_window()
print("set maxwindow is ok!!")
sleep(2)

driver.get("http://www.51zxw.net/list.aspx?cid=615")
driver.set_window_size(400,800)
print("set windowsize is ok!!")
driver.refresh()
sleep(3)

driver.back()
print("back!!")
sleep(2)

print("准备关闭！！！")
driver.close()



