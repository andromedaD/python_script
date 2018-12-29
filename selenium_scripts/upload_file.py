#文本上传关键是send_keys(r'D:\python_script\image\test.jpg')

# from selenium import webdriver
# from time import sleep
#
# driver=webdriver.Firefox()
# driver.get("http://www.baidu.com")
#
# driver.find_element_by_css_selector(".soutu-btn").click()
# sleep(2)
# driver.find_element_by_css_selector(".upload-pic").send_keys(
#     r'D:\python_script\image\test.jpg'
# )
#
# driver.quit()

# from selenium import webdriver
# from time import sleep
#
# driver=webdriver.Firefox()
# driver.get("http://www.baidu.com")
# sleep(2)
# driver.find_element_by_css_selector(".soutu-btn").click()
# sleep(2)
# driver.find_element_by_css_selector(".upload-pic").send_keys(
#     r'D:\python_script\image\test.jpg'
# )
# sleep(2)
# driver.quit()

from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()
driver.get("http://www.baidu.com")

driver.find_element_by_css_selector(".soutu-btn").click()

driver.find_element_by_css_selector(".upload-pic").send_keys(
    r'D:\python_script\image\test.jpg'
)

sleep(2)
driver.quit()














