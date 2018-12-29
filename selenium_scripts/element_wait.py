# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from time import sleep
# driver=webdriver.Firefox()
# driver.get("http://www.baidu.com")
# sleep(2)
#
# driver.find_element_by_css_selector("#kw").send_keys("51zxw")
# element=WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located((By.ID,'s1u')))
# element.click()
#
# sleep(3)

# from selenium import webdriver
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from time import sleep
# driver=webdriver.Firefox()
# driver.get("http://www.baidu.com")
# sleep(2)
#
# driver.find_element_by_css_selector("#kw").send_keys("51zxw")
# try:
#     element=WebDriverWait(driver,5,0.5).until(
#         EC.presence_of_element_located((By.ID,'su'))
#     )
# finally:
#     element.click()



# from selenium import webdriver
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
#
# driver=webdriver.Firefox()
# driver.get("http://www.baidu.com")
# driver.find_element_by_css_selector("#kw").send_keys("51zxw")
# try:
#     element=WebDriverWait(driver,5,0.5).until(
#         EC.presence_of_element_located((By.ID,"su"))
#     )
# finally:
#     element.click()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchWindowException
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver=webdriver.Firefox()

driver.get("http://www.baidu.com")

driver.find_element_by_css_selector("#kw").send_keys("wow")

try:
    element=WebDriverWait(driver,5,0.5).until(
        EC.presence_of_element_located((By.ID,"su"))
    )
finally:
    element.click()























