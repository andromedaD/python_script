# from selenium import webdriver
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.common.action_chains import ActionChains
# from time import sleep
#
# driver=webdriver.Firefox()
#
# driver.get("http://www.baidu.com")
# driver.implicitly_wait(10)
# driver.find_element_by_css_selector("div.head_wrapper>div#u1>a.pf").click()
# #driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[3]/a[8]").click()
# # driver.find_element_by_link_text("设置").click()
#
# driver.find_element_by_css_selector("div#wrapper>div.bdpfmenu>a.setpref").click()
# #serach_set=driver.find_element_by_xpath("/html/body/div[1]/div[6]/a[1]")
# # driver.find_element_by_link_text("搜索设置").click()
#
# # ActionChains(driver).move_to_element(tj_selection).move_to_element(serach_set).click().perform()#应该是哪里错了
#
# select=Select(driver.find_element_by_css_selector("select#nr"))
# select.select_by_index("0")
# select.select_by_value("20")
# select.select_by_visible_text("每页显示50条")
# #鼠标悬停
# # above=driver.find_element_by_css_selector(".pf")
# # ActionChains(driver).move_to_element(above).perform()
# # sleep(3)
# # driver.quit()


from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from time import sleep

driver=webdriver.Firefox()
driver.get('http://www.baidu.com')
driver.implicitly_wait(10)
driver.maximize_window()

driver.find_element_by_css_selector("div#u1>a.pf").click()
sleep(1)
driver.find_element_by_css_selector("a.setpref").click()
select=Select(driver.find_element_by_css_selector("select#nr"))
select.select_by_index("0")
select.select_by_value("20")
select.select_by_visible_text("每页显示50条")
driver.find_element_by_css_selector("input#sh_2").click()
driver.find_element_by_css_selector("a.prefpanelgo").click()
driver.switch_to_alert().accept()
sleep(5)
driver.quit()



