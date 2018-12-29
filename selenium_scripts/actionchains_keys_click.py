from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from  selenium.webdriver.common.keys import Keys
from time import sleep

driver=webdriver.Firefox()

#点击操作
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('http://sahitest.com/demo/clicks.htm')

# click_btn=driver.find_element_by_xpath('//input[@value="click me"]')#单击操作
# double_click=driver.find_element_by_xpath('//input[@value="dbl click me"]')#双击操作
# rightclick_btn=driver.find_element_by_xpath('//input[@value="right click me"]')#右击按钮操作
#
# ActionChains(driver).click(click_btn).double_click(double_click).context_click(rightclick_btn).perform()#链式用法
#
# print(driver.find_element_by_name('t2').get_attribute('value'))
# sleep(2)
#
# driver.quit()

# click_btn=driver.find_element_by_xpath('//input[@value="click me"]')
# doubleclick_btn=driver.find_element_by_xpath('//input[@value="dbl click me"]')
# rightclick_btn=driver.find_element_by_xpath('//input[@value="right click me"]')
#
# ActionChains(driver).click(click_btn)\
#     .double_click(doubleclick_btn)\
#     .context_click(rightclick_btn)\
#     .perform()
#
# print(driver.find_element_by_name('t2').get_attribute('value'))
# sleep(2)
#
# driver.quit()

click_btn=driver.find_element_by_xpath('//input[@value="click me"]')
doubleclick_btn=driver.find_element_by_xpath('//input[@value="dbl click me"]')
rightclick_btn=driver.find_element_by_xpath('//input[@value="right click me"]')

ActionChains(driver).click(click_btn)\
    .double_click(doubleclick_btn)\
    .context_click(rightclick_btn)\
    .perform()

print(driver.find_element_by_name("t2").get_attribute("value"))
sleep(2)
driver.quit()