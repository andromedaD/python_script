from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()
#
# driver.get("http://www.baidu.com")
# # driver.find_element_by_id("kw").send_keys("51自学网")
# driver.find_element_by_name("wd").send_keys("51自学网")
# sleep(2)
#
# driver.fin_element_by_id("su").click()
# sleep(2)
#
# driver.quit()
driver.get("http://www.51zxw.net")

# driver.find_element_by_tag_name("input").send_keys("51zxw")
driver.find_elements_by_tag_name("input")[0].send_keys("51zxw")
sleep(3)

driver.quit()