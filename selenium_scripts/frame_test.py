# from selenium import webdriver
# from time import sleep
#
# driver=webdriver.Firefox()
# file_path=r'D:\python_script\html\Frame.html'
# driver.get(file_path)
#
#
# driver.switch_to.frame("search")
#
# driver.find_element_by_css_selector("#query").send_keys("hello")
# sleep(2)
# driver.find_element_by_css_selector("#stb").click()
# sleep(2)
#
# driver.quit()
#
# from selenium import webdriver
# from time import sleep
# file_path=r'D:\python_script\html\Frame.html'
# driver=webdriver.Firefox()
# driver.get(file_path)
# driver.switch_to.frame("search")
# driver.find_element_by_css_selector("#query").send_keys("nihao")
# sleep(2)
# driver.find_element_by_css_selector("#stb").click()
# sleep(2)
# driver.quit()



from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()
file_path=r'D:\python_script\html\Frame.html'
driver.get(file_path)
driver.switch_to.frame("search")

driver.find_element_by_css_selector("#query").send_keys("bihao")
driver.find_element_by_css_selector("stb").click()
driver.quit()