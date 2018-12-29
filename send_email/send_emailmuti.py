import smtplib
from email.header import Header
from email.mime.text import MIMEText

smtpserver='smtp.163.com'

user='k568898699@163.com'
password='306359211xxx'

sender='k568898699@163.com'
recives=['568898699@qq.com','306359211@qq.com']

subject='Web selenium 自动化测试报告'
content='<html><h1 style="red:color">你好</html></h1>'

msgs=MIMEText(content,'html','utf-8')
msgs['Subject']=Header(subject,'utf-8')
msgs['From']='k568898699@163.com'
msgs['To']=','.join(recives)

smtp=smtplib.SMTP_SSL(smtpserver,465)
smtp.helo(smtpserver)
smtp.ehlo(smtpserver)
smtp.login(user,password)
smtp.sendmail(sender,recives,msgs.as_string())

