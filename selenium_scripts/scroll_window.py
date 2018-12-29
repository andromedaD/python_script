#窗口滚动条不是页面元素，关键在于用js的交互操作document.documentElement,然后用Python内置运行脚本execute_script()
# from selenium import webdriver
# from time import sleep
#
# driver=webdriver.Firefox()
# driver.get("http://www.51zxw.net/list.aspx?page=3&cid=615")
#
# js="var action=document.documentElement.scrollTop=10000"
# driver.execute_script(js)
# sleep(3)
# js="var action=document.documentElement.scrollTop=0"
# driver.execute_script(js)
# sleep(3)
# driver.quit()

# from selenium import webdriver
# from time import sleep
#
# driver=webdriver.Firefox()
# driver.get("http://www.51zxw.net/list.aspx?page=3&cid=615")
#
# js="var action=document.documentElement.scrollTop=10000"
# driver.execute_script(js)
# sleep(3)
# js="var action=document.documentElement.scrollTop=0"
# driver.execute_script(js)
# sleep(3)
# driver.quit()

from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()
driver.get("http://www.51zxw.net")

js="var action=document.documentElement.scrollTop=10000"
driver.execute_script(js)

driver.quit()
















