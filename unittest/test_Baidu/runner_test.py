import time
import unittest
from HTMLTestRunner import HTMLTestRunner

#case_path
case_dir='./test_case'
discover=unittest.defaultTestLoader.discover(case_dir,pattern='test*.py')

if __name__ == '__main__':
    #report_path
    report_dir='./test_report'
    report_time=time.strftime(
        "%Y-%m-%d %H_%M_%S"
    )
    report_path=report_dir+'/'+report_time+"result.html"

    try:
        with open(report_path,'wb') as fb:
            runner=HTMLTestRunner(
                stream=fb,title='test report',description='this is baidu test report'
            )
            runner.run(discover)
    finally:
        fb.close()