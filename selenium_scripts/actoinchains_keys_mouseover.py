from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver=webdriver.Firefox()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('http://sahitest.com/demo/mouseover.htm')

# write=driver.find_element_by_xpath('//input[@value="Write on hover"]')#鼠标移动至元素下，下面input框会显示“Mouse over”
# blank=driver.find_element_by_xpath('//input[@value="Blank on hover"]')#鼠标移动至元素下，会清空input框值
#
# result= driver.find_element_by_name('t1')
#
# action=ActionChains(driver)
# action.move_to_element(write).perform()#移动到mouse下，input显示“mouse moved”
# print(result.get_attribute("value"))
#
# action.move_by_offset(10,50).perform()#移动到当前位置(10,50)的点
# print(result.get_attribute("value"))
#
# action.move_to_element_with_offset(blank,10,-40).perform()#移动到距离blank位置（10，-40）位置
# print(result.get_attribute("value"))
#
# sleep(2)
# driver.quit()

write=driver.find_element_by_xpath('//input[@value="Write on hover"]')
blank=driver.find_element_by_xpath('//input[@value="Blank on hover"]')

result=driver.find_element_by_name('t1')
ActionChains(driver).move_to_element(write).perform()
print(result.get_attribute("value"))
ActionChains(driver).move_by_offset(10,50).perform()
print(result.get_attribute("value"))
ActionChains(driver).move_to_element_with_offset(blank,10,-40).perform()
print(result.get_attribute("value"))

sleep(2)
driver.quit()