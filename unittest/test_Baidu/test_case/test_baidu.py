# from selenium import webdriver
# import unittest
# from time import sleep
#
# class Testbaidu(unittest.TestCase):
#     def setUp(self):
#         self.driver=webdriver.Firefox()
#         self.driver.get('http://www.baidu.com')
#         self.driver.implicitly_wait(10)
#
#     def test_baidu(self):
#         driver=self.driver
#         driver.find_element_by_css_selector("#kw").clear()
#         driver.find_element_by_css_selector("#kw").send_keys("hello")
#         driver.find_element_by_css_selector("#su").click()
#         sleep(3)
#
#         title=driver.title
#         self.assertEqual(title,"hello_百度搜索")
#
#     def tearDown(self):
#         self.driver.quit()
#
# if __name__ == '__main__':
#     unittest.main()

# from selenium import webdriver
# import unittest
# from time import sleep
# from selenium.webdriver.support import expected_conditions as EC
#
# class Test_Baidu(unittest.TestCase):
#     def setUp(self):
#         self.driver=webdriver.Firefox()
#         self.driver.implicitly_wait(10)
#         self.driver.get("http://www.baidu.com")
#         sleep(2)
#
#     def test_baiducase(self):
#         try:
#             self.driver.find_element_by_css_selector("#kw").clear()
#             self.driver.find_element_by_css_selector("#kw").send_keys("你好")
#             self.driver.find_element_by_css_selector("#su").click()
#             sleep(2)
#         except EC.NoSuchElementException as msg:
#             print(msg)
#         finally:
#             title=self.driver.title
#             self.assertEqual(title,"你好_百度搜索")
#     def tearDown(self):
#         self.driver.quit()
#
# if __name__ == '__main__':
#     unittest.main()


from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import unittest
from time import sleep

class Test_baidu_title(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.get("http://www.baidu.com")
        sleep(2)
    def tearDown(self):
        self.driver.quit()

    def test_title(self):
        try:
            self.driver.find_element_by_css_selector("#kw").clear()
            self.driver.find_element_by_css_selector("#kw").send_keys("你好")
            self.driver.find_element_by_css_selector("#su").click()
        except EC.NoSuchElementException as msg:
            print(msg)
        finally:
            sleep(2)
            title=self.driver.title
            self.assertEqual(title,"你好_百度搜索")

if __name__ == '__main__':
    unittest.main()




























