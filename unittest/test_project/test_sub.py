
from calculator import *
from StartEnd import *

class Test_sub(StartEnd_test):
    def test_sub1(self):
        h=Math(18,2)
        self.assertEqual(h.sub(),16)

    def test_sub2(self):
        h=Math(15,2)
        self.assertEqual(h.sub(),11)