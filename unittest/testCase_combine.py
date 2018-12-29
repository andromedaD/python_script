# from calculator import *
# import unittest
#
# class Test_StartEnd(unittest.TestCase):
#     def setUp(self):
#         print("start test")
#
#     def tearDown(self):
#         print("end test")
#
# class Test_add(Test_StartEnd):
#     def test_add(self):
#         j=Math(5,10)
#         self.assertEqual(j.add(),15)
#
# class Test_sub(Test_StartEnd):
#     def test_sub(self):
#         j=Math(10,5)
#         self.assertEqual(j.sub(),5)
#
# if __name__ == '__main__':
#     unittest.main()

from calculator import *
import unittest

class Test_StartEnd(unittest.TestCase):
    def setUp(self):
        print("start test")

    def tearDown(self):
        print("end test")

class Test_case(unittest.TestCase):
    def test_add(self):
        j=Math(5,10)
        self.assertEqual(j.add(),15)

    def test_sub(self):
        j=Math(10,5)
        self.assertEqual(j.sub(),5)

if __name__ == '__main__':
    unittest.main()






T

















