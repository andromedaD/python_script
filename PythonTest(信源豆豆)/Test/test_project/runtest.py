import unittest,time
from HTMLTestRunner import HTMLTestRunner
import os
# test_dir = os.path.dirname(os.path.abspath(__file__))+'/test_case'
test_dir = './test_case'
discover = unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')
if __name__=='__main__':
    now = time.strftime("%Y-%m-%d %H-%M-%S")
    filename = test_dir + '/' + now + 'result.html'
    fp = open(filename,'wb')
    runner = HTMLTestRunner(stream=fp,title='测试报告',description='用例执行情况:')
    runner.run(discover)