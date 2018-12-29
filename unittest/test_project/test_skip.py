# import unittest
#
# class Test_skip(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         print("module class start >>>>>>>>>>>>>>")
#     @classmethod
#     def tearDownClass(cls):
#         print("module class end>>>>>>>>>>>>>>>>>")
#     def setUp(self):
#         print("start test")
#
#     def tearDown(self):
#         print("end test")
#     @unittest.skip("直接跳过测试")
#     def test_skip1(self):
#         print("test skip1")
#     @unittest.skipIf(4>3,"test skip2")
#     def test_skip2(self):
#         print("test skip2")
#
#     @unittest.skipUnless(4>3,"test skip3")
#     def test_skip3(self):
#         print("test skip3")
#     @unittest.expectedFailure
#     def test_skip4(self):
#         print("test skip4")
#
# if __name__ == '__main__':
# #     unittest.main()
#
# import unittest
#
# class Test_skip(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         print("module test start>>>>>>>>>>>>>>>>>>>>>>")
#
#     @classmethod
#     def tearDownClass(cls):
#         print("module test end>>>>>>>>>>>>>>>>>>>>>>>>>")
#
#     def setUp(self):
#         print("start test")
#
#     def tearDown(self):
#         print("end test")
#
#     @unittest.skip("test 1")
#     def test_test1(self):
#         print("test 1")
#
#     @unittest.skipIf(4>3,"test 2")
#     def test_test2(self):
#         print("test 2")
#
#
#     @unittest.skipUnless(4>3,"test 3")
#     def test_test3(self):
#         print("test 3")
#
#     @unittest.expectedFailure
#     def test_test4(self):
#         print("test 4")
#
#
# if __name__ == '__main__':
#     unittest.main()

import unittest

class Test_skipclass(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("test skip test start >>>>>>>>>>>>>>>>>>>>>")

    @classmethod
    def tearDownClass(cls):
        print("test skip test end>>>>>>>>>>>>>>>>>>>>>>>")

    def setUp(self):
        print("start test")

    def tearDown(self):
        print("end test")
    @unittest.skip("test1")
    def test_skip1(self):
        print("test1 ")
    @unittest.skipIf(4>3,"test2")
    def test_skip2(self):
        print("test2 ")
    @unittest.skipUnless(4>3,"test3")
    def test_skip3(self):
        print("test3 ")
    @unittest.expectedFailure
    def test_skip4(self):
        print("test4 ")

if __name__ == '__main__':
    unittest.main()