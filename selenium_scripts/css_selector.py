# from selenium import webdriver
# from time import sleep
#
# driver=webdriver.Firefox()
#
# # driver.get("http://www.baidu.com")
# # #根据id定位
# # driver.find_element_by_css_selector("#kw").send_keys('hello')
# # driver.find_element_by_css_selector("#kw").clear()
# #
# # sleep(2)
# # #class
# # driver.find_element_by_css_selector(".s_ipt").send_keys('hello')
# # driver.find_element_by_css_selector(".s_ipt").clear()
# # sleep(2)
# # #属性
# # driver.find_element_by_css_selector("[autocomplete='off']").send_keys('hello')
# # driver.find_element_by_css_selector("[autocomplete='off']").clear()
# # sleep(2)
# #层级
# driver.get("http://www.baidu.com")
# sleep(3)
# # driver.find_element_by_link_text('登录').click()
# # driver.implicitly_wait(10)
#
# driver.find_element_by_css_selector("form#form.fm>span.bg.s_ipt_wr.quickdelete-wrap>input#kw").send_keys("wow")
# #注意，如果属性值有空格要加“.”
#
# # driver.find_element_by_css_selector("form#loginForm>div.login>div.inputRow[1]>#pwd").send_keys("wow")
# # driver.find_element_by_css_selector("form#loginForm>div.login>div.inputRow[1]>#pwd").clear()
# #
# sleep(2)
# driver.quit()

#通过css 父节点定位子节点
# from selenium import webdriver
# from time import sleep
#
# driver=webdriver.Firefox()
# driver.implicitly_wait(10)
# driver.maximize_window()
# driver.get("http://www.baidu.com")
#
# driver.find_element_by_css_selector("form#form.fm>span[class^='bg s_ipt']>input#kw").send_keys("wow")
# a_herf=driver.find_elements_by_css_selector(".result.c-container h3 a:nth-child(1) ")
# for i in a_herf:
#     print(i.text)
#
# driver.quit()


