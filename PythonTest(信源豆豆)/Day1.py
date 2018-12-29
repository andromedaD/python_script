import Day4
from selenium import webdriver
import time

driver = webdriver.Chrome()
#
def login():
    time.sleep(1);
    driver.get("http://bussiness.linkdood.cn:10077/index.html");
    time.sleep(1);
    driver.find_element_by_xpath('//*[@id="loginDiv"]/li[1]/div[1]/a').click();
    time.sleep(1);
    driver.find_element_by_xpath('/html/body/div[2]/div/ul/li[1]').click();
    time.sleep(1);
    driver.find_element_by_xpath('//*[@id="login_form"]/div[1]/div/span[2]').click();
    time.sleep(1);
    driver.find_element_by_xpath('//*[@id="login_form"]/div[1]/div/div/ul/li[2]').click();
    time.sleep(1);
    driver.find_element_by_xpath('//*[@id="telphone"]').send_keys('13813040083');
    time.sleep(1);
    driver.find_element_by_xpath('//*[@id="mpasswordText"]').click()
    time.sleep(1);
    driver.find_element_by_xpath('//*[@id="mpassword"]').send_keys("lx123123");
    time.sleep(1);
    driver.find_element_by_xpath('//*[@id="login_form"]/div[2]/input').click();
    time.sleep(1);

login()
#driver.find_element_by_xpath('//*[@id="download"]').click();
time.sleep(1);
name = driver.find_element_by_id('username').text
if name == '南京产品':
    row01 = ['1', '用户登录', 'OK']
    Day4.savetoexcel(row01,'1234','aa','new1.xlsx');
else:
    row01 = ['1', '用户登录', 'NG']
    Day4.savetoexcel(row01, '1234', 'aa', 'new1.xlsx');