import unittest
def setUpModule():
    print("test module start>>>>>>>>")
def tearDownModule():
    print("test module end>>>>>>>>")
class cs(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("test class start>>>>")
    @classmethod
    def tearDownClass(cls):
        print("test class end>>>> ")
    def setUp(self):
        print("test case start")
    def tearDown(self):
        print("test case end")
    def test_case001(self):
        print("test001 begin")
    def test_case002(self):
        print("test002 begin")
if __name__ == '__main__':
    unittest.main()

