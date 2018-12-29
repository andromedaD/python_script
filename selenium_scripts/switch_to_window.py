# from selenium import webdriver
# from time import sleep
#
# driver=webdriver.Firefox()
# driver.get("http://www.51zxw.net/list.aspx?page=3&cid=615")
#
# selenium_index=driver.current_window_handle
#
# #切换窗口，局部链接定位2-1课
# driver.find_element_by_partial_link_text("2-1").click()
# sleep(2)
#
# driver.switch_to.window(selenium_index)
# sleep(3)
# driver.find_element_by_partial_link_text("3-1").click()
# sleep(3)
#
# driver.quit()

from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()
driver.get("http://www.baidu.com")
sleep(3)
driver.window_handles
handle1=driver.current_window_handle
print(handle1)
# driver.find_element_by_css_selector("#username").click()
# driver.switch_to.window(handle1)
#
#
# driver.find_element_by_css_selector("").click()
# driver.quit()






















