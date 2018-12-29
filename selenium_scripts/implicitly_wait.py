# from selenium import webdriver
# from selenium.common.exceptions import NoSuchElementException
# from time import sleep,ctime
#
# driver=webdriver.Firefox()
# driver.get("http://www.baidu.com")
# sleep(2)
#
# driver.implicitly_wait(5)
#
# try:
#     print(ctime())
#     driver.find_element_by_css_selector("#kw").send_keys("python")
#     driver.find_element_by_css_selector("#su").click()
# except NoSuchElementException as msg:
#     print(msg)
# finally:
#     print(ctime())
# sleep(3)

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import ctime,sleep

driver=webdriver.Firefox()
driver.get("http://www.baidu.com")
driver.implicitly_wait(5)

try:
    print(ctime())
    driver.find_element_by_css_selector("#kw").send_keys("hello")
    driver.find_element_by_css_selector("#su").click()
except NoSuchElementException as msg:
    print(msg)
finally:
    print(ctime())

driver.quit()

