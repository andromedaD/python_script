# # import urllib
# # import urllib.request
# # import re
# # def load_page(url):
# #     request=urllib.request.Request(url)
# #     response=urllib.request.urlopen(request)
# #     data=response.read()
# #     return data
# # def get_image(html):
# #     regx=r'http://[\S]*jpg'
# #     pattern=re.compile(regx)
# #     get_image=re.findall(pattern,repr(html))
# #
# #     num=1
# #     for img in get_image:
# #         image=load_page(img)
# #         with open('D:\\Photo\\%s.jpg' %num,'wb')as fb:
# #             fb.write(image)
# #             print("正在下载图片第%s张图片"%num)
# #             num=num+1
# #     print("下载完成!!")
# # url='http://p.weather.com.cn/2017/06/2720826.shtml#p=7'
# # html=load_page(url)
# # get_image(html)
#
#
# import urllib
# import urllib.request
# import re
#
# #加载网页
# def load_page(url):
#     request=urllib.request.Request(url)
#     response=urllib.request.urlopen(request)
#     data=response.read()
#     return data
#
# #存储图片
# def get_image(html):
#     repx=r'http://[\S]*jpg'
#     pattern=re.compile(repx)
#     get_image=re.findall(pattern,repr(html))
#     #设置图片名称
#     num=1
#
#     for img in get_image:
#         image=load_page(img)
#         with open('D:\\Photo\\%s.jpg'%num,'wb') as fb:
#             fb.write(image)
#             print("正在下载第%s张图片"%num)
#         num=num+1
#     print("下载完成!!!")
#
# #调用
# url='http://p.weather.com.cn/2017/06/2720826.shtml#p=7'
# html=load_page(url)
# get_image(html)

# import urllib
# import urllib.request
# import re
#
# #加载页面
# def load_page(url):
#     request=urllib.request.Request(url)
#     response=urllib.request.urlopen(request)
#     data=response.read()
#     return data
# #x下载图片
# def get_image(html):
#     regx=r'http://[\S]*jpg'
#     a=re.compile(regx)
#     get_image=re.findall(a,repr(html))
#
#     num=1
#     for img in get_image:
#         b=load_page(img)
#         with open('D:\\Photo\\%s.jpg'%num,'wb')as fb:
#             fb.write(b)
#             print("正在下载第%s张图片"%num)
#         num=num+1
#     print("下载完成！！！")
#
# #调用
# url='http://p.weather.com.cn/2017/06/2720826.shtml#p=7'
# html=load_page(url)
# get_image(html)

import urllib
import urllib.request
import re

#加载图片
def load_page(url):
    request=urllib.request.Request(url)
    response=urllib.request.urlopen(request)
    data=response.read()
    return data

#下载图片
def get_image(html):
    #正则匹配网页
    regx=r'http://[\S]*jpg'
    pattern=re.compile(regx)
    get_image=re.findall(pattern,repr(html))

    num=1

    for img in get_image:
        image = load_page(img)
        with open('D:\\Photo\\%s.jpg'%num,'wb')as fb:
            fb.write(image)
            print('正在下载第%s张图片'%num)
        num=num+1
    print("下载完成")

#调用
url='http://p.weather.com.cn/2017/06/2720826.shtml#p=7'
html=load_page(url)
get_image(html)























