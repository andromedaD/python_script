from selenium import webdriver

def browser():
    driver=webdriver.Firefox()
    #driver=webdriver.Chrome()
    # driver=webdriver.Ie()
    #
    # driver.get("http://www.baidu.com")

    return driver
if __name__ == '__main__':
    browser()

# from selenium import webdriver
#
# def browser():
#     driver=webdriver.Firefox()
#     # driver=webdriver.Chrome()
#     # driver=webdriver.Ie()
#     # driver.get("http://www.baidu.com")
#     return driver
#
# if __name__ == '__main__':
#     browser()