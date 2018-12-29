# from selenium import webdriver
# from time import sleep
#
# driver=webdriver.Firefox()
# driver.get("httP://www.51zxw.net")
# driver.get_screenshot_as_file(r"D:\python_script\image\test1.jpg")
# sleep(2)
#
# driver.get("http://www.baidu.com")
# driver.get_screenshot_as_file(r"D:\python_script\image\test2.jpg")
# sleep(2)
# driver.quit()

# from selenium import webdriver
# from time import sleep
#
# driver=webdriver.Firefox()
# driver.get("http://www.51zxw.net")
#
# driver.get_screenshot_as_file(r"D:\python_script\image\test3.jpg")
# sleep(2)
# driver.get("http://www.baidu.com")
# driver.get_screenshot_as_file(r"D:\python_script\image\test4.jpg")
# sleep(2)
# driver.quit()

from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()
driver.get("http://www.baidu.com")
driver.get_screenshot_as_file(r"D:\python_script\image\test3.jpg")
driver.quit()
