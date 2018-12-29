from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox()
#
# driver.get('http://www.51zxw.net')
# sleep(2)
# driver.find_element_by_link_text("程序开发").click()
# # element=driver.find_element_by_link_text("程序开发")
# # ActionChains(driver).double_click(element).perform()
# sleep(2)
# driver.find_element_by_partial_link_text("Python").click()
# sleep(2)
# driver.quit()

driver.get('http://www.baidu.com')
sleep(2)
#百度搜索华为云
# driver.find_element_by_id('kw').send_keys('华为云')
# driver.find_element_by_id('su').click()
# sleep(2)


#百度搜索地图
driver.find_element_by_link_text('地图').click()
sleep(5)


driver.quit()