# -*-coding:utf-8-*-
__author__ = "pawpawDu"
import unittest
import inspect
class TestClass02(unittest.TestCase):
    def test_case02(self):
        print "\nRunning Test Method："+inspect.stack()[0][3]#inspect.stack()[0][3]打印测试方法的名称

    def test_case03(self):
        print "\nRunning Test Method：" + inspect.stack()[0][3]

if __name__ == '__main__':
    unittest.main(verbosity=2)