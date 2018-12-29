from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Firefox()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('http://sahitest.com/demo/label.htm')

# input1=driver.find_elements_by_tag_name('input')[3]
# input2=driver.find_elements_by_tag_name('input')[4]
#
# action=ActionChains(driver)
# input1.click()
# action.send_keys('Test Keys').perform()
# action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()#ctrl+a
# action.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()#ctrl+c
#
# action.key_down(Keys.CONTROL,input2).send_keys('v').key_up(Keys.CONTROL).perform()#ctrl+v
#
# print(input1.get_attribute("value"))
# print(input2.get_attribute("value"))
#
# sleep(2)
# driver.quit()

input1=driver.find_elements_by_tag_name('input')[3]
input2=driver.find_elements_by_tag_name('input')[4]

action=ActionChains(driver)
input1.click()
action.send_keys('Test Keys')
action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
action.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()

action.key_down(Keys.CONTROL,input2).send_keys('v').key_up(Keys.CONTROL).perform()

print(input1.get_attribute("value"))
print(input2.get_attribute("value"))

driver.quit()