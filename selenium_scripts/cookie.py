# from selenium import webdriver
#
# driver=webdriver.Firefox()
#
# driver.get("http://www.51zxw.net")
#
# cookie=driver.get_cookies()
# print(cookie)
# print(cookie[4])
#
# driver.add_cookie({"name":"benben","value":"handsome"})
# for cookie in driver.get_cookies():
#     print("%s--%s"%(cookie['name'],cookie['value']))
# driver.quit()
#

# from selenium import webdriver
# from time import sleep
#
# driver=webdriver.Firefox()
#
# driver.get("http://www.baidu.com")
#
# cookie=driver.get_cookies()
# print(cookie)
# print(cookie[4])
#
# driver.add_cookie({"name":"benben","value":"hel"})
# for cookie in driver.get_cookies():
#     print("%s--%s"%(cookie['name'],cookie['value']))
#
# driver.quit()


#基于验证马登录cookie绕过百度验证码登录，fiddler抓包获取BUIDUID和BDUSS,注意cookie有时效性
#百度基于cookie绕过登录尝试失败
#BAIDUID=00F02352A10E196BDBB72995D83C90F4:SL=0:NR=10:FG=1
#BDUSS=VOSEhDdlBEQ3RQa2tIYkNrZXB2MlZmU2lNT2MydUFlbzhsOWdKMmxDdEFnU2RjQVFBQUFBJCQAAAAAAAAAAAEAAAAbiGgnY8PXw9fD1wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAED0~1tA9P9bS2
# from selenium import webdriver
# from time import sleep
#
# driver=webdriver.Firefox()
# driver.get("http://www.baidu.com")
# sleep(3)
# #手动添加cookie
# driver.add_cookie(
#     {'name':'BAIDUID','value':'00F02352A10E196BDBB72995D83C90F4:SL=0:NR=10:FG=1'}
# )
#
# driver.add_cookie(
#     {'name':'BDUSS','value':'VOSEhDdlBEQ3RQa2tIYkNrZXB2MlZmU2lNT2MydUFlbzhsOWdKMm\
#     xDdEFnU2RjQVFBQUFBJCQAAAAAAAAAAAEAAAAbiGgnY8PXw9fD1wAAAAAAAAAAAAAAAAAAAAAAAAA\
#     AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAED0'}
# )
#
# sleep(3)
#
# driver.refresh()
# sleep(3)


#尝试51自学网基于cookie登录,依然失败，不知道add_cookie添加哪些参数
#
# from selenium import webdriver
# from time import sleep
#
# driver=webdriver.Firefox()
# driver.get("http://www.51zxw.net")
# sleep(3)
# driver.add_cookie(
#     {'name':'username','value':'huangjian102329'}
# )
#
# driver.add_cookie(
#     {'name':'password','value':'E435E24B5308BC9BA2BBBE561A634BA5'}
# )
#
# sleep(2)
# driver.refresh()





















