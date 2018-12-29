from selenium import webdriver
import unittest
import time
from HTMLTestRunner import HTMLTestRunner
class baidu(unittest.TestCase):
    """百度搜索测试"""
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.base_url = "http://www.baidu.com"

    def tearDown(self):
        self.driver.quit()

    def test_baidu(self):
        """搜索关键字：unittest"""
        self.driver.get(self.base_url+"/")
        self.driver.find_element_by_id("kw").clear()
        self.driver.find_element_by_id("kw").send_keys("unittest")
        self.driver.find_element_by_id("su").click()
        time.sleep(2)
        title = self.driver.title
        self.assertEqual(title,"unittest_百度搜索")


if __name__=='__main__':
    suite = unittest.TestSuite()
    suite.addTest(baidu('test_baidu'))
    # fp = open(r'C:\Users\25868\Desktop\result.html',"wb")
    now = time.strftime('%Y-%m-%d %H-%M-%S')
    file_name = './'+now +'result.html'
    fp = open(file_name,'wb')
    # fp = open('./reult.html','wb')
    runner = HTMLTestRunner(stream=fp,title='百度搜索测试报告',description='用例执行情况')
    runner.run(suite)
    fp.close()