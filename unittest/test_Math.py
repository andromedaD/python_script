# from calculator import Math
# import unittest
#
# class TestMath(unittest.TestCase):
#     def setUp(self):
#         print("test start")
#
#     @unittest.skip("it is not match this version")
#     def test_add(self):
#         j=Math(5,10)
#         self.assertEqual(j.add(),15)
#         #self.assertEqual(j.add(),12)
#         pass
#
#     def test_assertTrue(self):
#         j=Math(5,10)
#         self.assertTrue(j.add()>12)
#
#     def test_assertIS(self):
#         self.assertIs("hello","hello")
#
#     def test_assertIn(self):
#         self.assertIn("hello","hel１lo world")
#
#     def tearDown(self):
#         print("test end")
#
# def suite():
#     suite=unittest.TestSuite()
#     # suite.addTest(TestMath("test_add"))
#     suite.addTest(TestMath("test_assertTrue"))
#     suite.addTest(TestMath("test_assertIS"))
#     suite.addTest(TestMath("test_assertIn"))
#
#     runner = unittest.TextTestRunner()
#     runner.run(suite)
#
#
#
# if __name__ == '__main__':
#     suite()
#

from calculator import Math
import unittest

class TestMath(unittest.TestCase):
    def setUp(self):
        print("start test")

    def test_add1(self):
        j=Math(5,10)
        self.assertEqual(j.add(),15)

    def test_sub1(self):
        j=Math(10,5)
        self.assertEqual(j.sub(),5)

    def tearDown(self):
        print("end test")

if __name__ == '__main__':
    suite=unittest.TestSuite()
    suite.addTest(TestMath('test_add1'))
    suite.addTest(TestMath('test_sub1'))

    runner=unittest.TextTestRunner()
    runner.run(suite)
    #
    # unittest.main()































