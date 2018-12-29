import unittest
from model import function,myunit
from page_object.LoginPage import *
from time import sleep

class LoginTest(myunit.StartEnd):
    def test_login_normal(self):
        '''username and password is normal'''
        print("test_login_normal is start test...")
        po=LoginPage(self.driver)
        po.Login_action('wangjin1','123456')
        sleep(2)

        self.assertEqual(po.type_loginPass_hint(),'我的空间')
        sleep(3)
        function.insert_img(self.driver,"wangjin_login_normal.jpg")
        print("test_login_normal test end!!")

    def test_login2_PasswdError(self):
        '''username and password is error'''
        print('test_login2_passError is start test!!')
        po=LoginPage(self.driver)
        po.Login_action('hhhh','21')
        sleep(2)

        self.assertEqual(po.type_loginFail_hint(),'')
        sleep(3)
        function.insert_img(self.driver,'test_login2_passwdError.jpg')

    def test_login3_empty(self):
        '''usename and passwd is empty'''
        print("test_login3_empty is start test..")
        po=LoginPage(self.driver)
        po.Login_action('','')
        sleep(2)

        self.assertEqual(po.type_loginFail_hint(),'')
        sleep(3)
        function.insert_img(self.driver,'test_login3_passwdError.jpg')


if __name__ == '__main__':
    unittest.main()