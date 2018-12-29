# from selenium import webdriver
# from time import sleep
#
# #加载浏览器驱动
# driver=webdriver.Firefox()
#
# #打开51自学网
# driver.get('http://www.51zxw.net')
# print(driver.title)
# sleep(3)
#
# #打开百度首页
# driver.get("http://www.baidu.com")
# print(driver.title)
# sleep(3)
#
# #关闭浏览器
# driver.close()
import os, sys

# import os,sys
# def search(curpath,s):
#     L=os.listdir(curpath)
#     for subpath in L:
#         if os.path.isdir(os.path.join(curpath,subpath))
#             newpath=os.path.join(curpath,subpath)
#             search(newpath,s)
#         elif os.path.isfile(os.path.join(curpath,subpath))
#             if s in subpath:
#                 print(os.path.join(curpath,subpath))
#
#
# def main():
#     workingpath=os.path.abspath('.')
#     s=sys.argv[1]
#     search(workingpath,s)
#
# if __name__ == '__main__':
#     main()


# import sys,os
#
# #定义函数查找函数
def search(curpath,s):
    #输出当前目录
    L=os.listdir(curpath)
    for subpath in L:
        # 判断当前是否为文件夹
        if os.path.isdir(curpath):
            newpath=os.path.join(curpath,subpath)
            search(newpath,s)
        #判断当前是否为文件
        elif os.path.isfile(curpath):
            #判断s字符是否在文件里
            if s in subpath:
                print(os.path.join(curpath,subpath))
#
# #调用
# def main():
#     #设置文件路径
#     workingpath=os.path.abspath('.')
#     #设置输入字符
#     s=sys.argv[1]
#     search(workingpath,s)
# if __name__ == '__main__':
#     main()


#我靠，自己莫名写了类似的的，不同表达
import os

def search_file(curpath,s):
    if os.path.isdir(curpath):
        subpath = os.listdir(curpath)
        for newpath in subpath:
            search_file(os.path.join(curpath,newpath),s)
    elif os.path.isfile(curpath):
        if s in curpath:
            print(curpath)
        else:
            search_file(curpath,s)







































