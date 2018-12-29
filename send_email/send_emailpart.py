# import smtplib
# from email.mime.text import MIMENonMultipart
# from email.mime.text import MIMEText
#
# smtpserver='smtp.163.com'
#
# user='k568898699@163.com'
# password='306359211xxx'
#
# sender='k568898699@163.com'
# recive=['568898699@qq.com','306359211@qq.com']
#
# subject='Web selenium 自动化邮件'
# content='<html><h1 style="color:red">你好，这是一封邮件</h1></html></html>'
#
# #构造文件
# send_file=open(r'D:\python_script\image\test.jpg','rb').read()
# att=MIMEText(send_file,'base64','utf-8')
# att['Content-Type']='application/octet-stream'
# att['Content-Disposition']='attachment;filename="test.jpg"'
# #构建发送信息与接收信息
# msgRoot=MIMENonMultipart()
# msgRoot.attach(MIMEText(content,'html','utf-8'))
# msgRoot['Subject']=subject
# msgRoot['From']=''
# msgRoot['To']=','.join(recive)
#
# smtp=smtplib.SMTP_SSL(smtpserver,465)
# smtp.helo(smtpserver)
# smtp.ehlo(smtpserver)
# smtp.login(user,password)
# smtp.sendmail(sender,recive,msgRoot.as_string())

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

smtpserver='smtp.163.com'

user='k568898699@163.com'
password='306359211xxx'

sender='k568898699@163.com'
receive=['568898699@qq.com','306359211@qq.com','k568898699@126.com']

subject='Web selenium 自动化模板'
content='<html><h1 style="color:red">你好，很高兴见到你</h1></html>'

send_file=open(r'D:\python_script\image\test.jpg','rb').read()
att=MIMEText(send_file,'base64','utf-8')
att['Content-Type']='application/octet-stream'
att['Content-Disposition']='attchment;filename="test.jpg"'


msgRoot=MIMEMultipart()
msgRoot.attach(MIMEText(content,'html','utf-8'))
msgRoot['Subject']=subject
msgRoot['From']='k568898699@163.com'
msgRoot['To']=','.join(receive)
msgRoot.attach(att)

print("Start Send Email")
smtp=smtplib.SMTP_SSL(smtpserver,465)
smtp.helo(smtpserver)
smtp.ehlo(smtpserver)
smtp.login(user,password)
smtp.sendmail(sender,receive,msgRoot.as_string())
print("Send Email is over!!!")



