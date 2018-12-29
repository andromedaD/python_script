from selenium import webdriver
import os
from time import sleep
import smtplib
from email.mime.text import MIMEText
from email.header import Header

def insert_img(driver,filename):
    func_path=os.path.dirname(__file__)
    print(func_path)

    base_dir=str(func_path)
    base_dir=base_dir.replace('\\','/')
    print(base_dir)

    base=base_dir.split('/Website')[0]
    print(base)


    filepath=base+'/Website/test_report/screenshot'+filename
    driver.get_screenshot_as_file(filepath)

def latest_report(report_dir):
    lists = os.listdir(report_dir)
    print(lists)

    lists.sort(key=lambda fn: os.path.getatime(report_dir + '\\' + fn))
    print("the latest report is" + lists[-1])
    file = os.path.join(report_dir, lists[-1])
    print(file)
    return file

def send_mail(latest_report):
    f = open(latest_report, 'rb')
    mail_content = f.read()
    f.close()
    # print(mail_content)
    smtpserver = 'smtp.163.com'

    user = 'k568898699@163.com'
    password = '306359211xxx'

    sender = 'k568898699@163.com'
    recives = ['568898699@qq.com', '306359211@qq.com', 'k568898699@126.com']

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







if __name__=='__main__':
    driver=webdriver.Firefox()
    driver.get('http://www.sogou.com')
    sleep(3)
    insert_img(driver,'sogou.jpg')
    driver.quit()