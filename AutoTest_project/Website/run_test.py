import unittest
from function import *
from HTMLTestRunner import HTMLTestRunner
import time
report_dir='./test_report'
test_dir='./test_case'

print("start run test case")
discover=unittest.defaultTestLoader.discover(test_dir,pattern="test_login.py")

now_time=time.strftime("%Y-%m-%d %H_%M_%S")
report_name=report_dir+"/"+now_time+'result.html'

print("start write report...")
with open(report_name,'wb')as fb:
    runner=HTMLTestRunner(stream=fb,title='Test Report',description="localhost test report")
    runner.run(discover)
    fb.close()

print("find latest report")
latest_report=latest_report(report_dir)

print("send email start...")
send_mail(latest_report)
print("send is over!!!")





