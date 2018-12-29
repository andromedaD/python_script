from calculator import *
from StartEnd import *


class Test_add(StartEnd_test):
    def test_add1(self):
        j=Math(5,10)
        self.assertEqual(j.add(),15)

    def test_add2(self):
        j=Math(19,10)
        self.assertEqual(j.add(),20)