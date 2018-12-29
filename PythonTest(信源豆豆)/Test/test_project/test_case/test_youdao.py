from selenium import webdriver
import unittest
import time
class youdao(unittest.TestCase):
    """有道搜索测试"""
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.base_url = "http://www.youdao.com"

    def tearDown(self):
        self.driver.quit()

    def test_youdao(self):
        """搜索关键字：你好"""
        self.driver.get(self.base_url + "/")
        self.driver.find_element_by_xpath('//*[@id="translateContent"]').clear()
        self.driver.find_element_by_xpath('//*[@id="translateContent"]').send_keys("你好")
        self.driver.find_element_by_xpath('//*[@id="form"]/button').click()
        time.sleep(2)
        title = self.driver.title
        self.assertEqual(title, "【你好】英语怎么说_在线翻译_有道词典")




if __name__=='__main__':
    unittest.main()