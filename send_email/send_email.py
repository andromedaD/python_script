# import smtplib
# from email.mime.text import MIMEText
# from email.header import Header
# smtpserver='smtp.163.com'
#
# user='k568898699@163.com'
# password='306359211xxx'
#
# sender='k568898699@163.com'
# receive='568898699@qq.com'
#
# subject='Web Selenium 自动化测试报告'
# content='<html><h1 style="color:red">加油少年</h1></html>'
#
# msg=MIMEText(content,'html','utf-8')
# msg['Subject']=Header(subject,'utf-8')
# msg['From']='k568898699@163.com'
# msg['To']='568898699@qq.com'
#
# smtp=smtplib.SMTP_SSL(smtpserver,465)
# smtp.helo(smtpserver)
# smtp.ehlo(smtpserver)
# smtp.login(user,password)
#
# print("Start send Email")
# smtp.sendmail(sender,receive,msg.as_string())
# smtp.quit()
# print("Send Email end")


# import smtplib
# from email.mime.text import MIMEText
# from email.header import Header
#
# #邮件服务器
# smtpserver='smtp.163.com'
# #用户账号密码
# user='k568898699@163.com'
# password='306359211xxx'
# #发件人收件人
# sender='k568898699@163.com'
# receive='568898699@qq.com'
#
# #邮件标题，正文
# subject='Web selenium 邮件发送'
# content='<html><h1 style="color:red">你好</h1></html>'
#
# #HTML邮件正文
# msg=MIMEText(content,'html','utf-8')
# msg['Subject']=Header(subject,'utf-8')
# msg['From']='k568898699@163.com'
# msg['To']='568898699@qq.com'
#
# #定义smtp发送协议
# smtp=smtplib.SMTP_SSL(smtpserver,465)
#
# #向服务器标识用户身份
# smtp.helo(smtpserver)
# #服务器确认身份
# smtp.ehlo(smtpserver)
# #登录用户名及密码
# smtp.login(user,password)
# print("Start Send Email")
# smtp.sendmail(sender,receive,msg.as_string())
# smtp.quit()
# print("Send End!!!!")

import smtplib
from email.header import Header
from email.mime.text import MIMEText

smtpserver='smtp.163.com'

user='k568898699@163.com'
password='306359211xxx'

sender='k568898699@163.com'
recive='568898699@qq.com'

subject='Web selenium 自动化'
content='<html><h1 style="color:red">你好</h1></html>'

msg=MIMEText(content,'html','utf-8')
msg['Subject']=Header(subject,'utf-8')
msg['From']='k568898699@163.com'
msg['To']='568898699@qq.com'

smtp=smtplib.SMTP_SSL(smtpserver,465)
smtp.helo(smtpserver)
smtp.ehlo(smtpserver)
smtp.login(user,password)

print("Start Send Email")
smtp.sendmail(sender,recive,msg.as_string())
smtp.quit()
print("Send End!!!")























