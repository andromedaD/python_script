import smtplib
from email.header import Header
from email.mime.text import MIMEText
import os
import time
import unittest
from HTMLTestRunner import HTMLTestRunner

def send_mail(latest_report):
    f=open(latest_report,'rb')
    mail_content=f.read()
    f.close()
    # print(mail_content)
    smtpserver = 'smtp.163.com'

    user = 'k568898699@163.com'
    password = '306359211xxx'

    sender = 'k568898699@163.com'
    recives = ['568898699@qq.com', '306359211@qq.com','k568898699@126.com']

    subject = 'Web selenium 自动化测试报告'

    msgs = MIMEText(mail_content, 'html', 'utf-8')
    msgs['Subject'] = Header(subject, 'utf-8')
    msgs['From'] = 'k568898699@163.com'
    msgs['To'] = ','.join(recives)

    smtp = smtplib.SMTP_SSL(smtpserver, 465)
    print("Start Send mail")
    smtp.helo(smtpserver)
    smtp.ehlo(smtpserver)
    smtp.login(user, password)
    smtp.sendmail(sender, recives, msgs.as_string())
    print("Send Mail over!!!")

def latest_report(report_dir):
    lists = os.listdir(report_dir)
    print(lists)

    lists.sort(key=lambda fn: os.path.getatime(report_dir + '\\' + fn))
    print("the latest report is" + lists[-1])
    file = os.path.join(report_dir, lists[-1])
    print(file)
    return file

if __name__ == '__main__':
    # case_path
    case_dir = './test_case'
    discover = unittest.defaultTestLoader.discover(case_dir, pattern='test*.py')
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

    latest_report=latest_report(report_dir)
    send_mail(latest_report)