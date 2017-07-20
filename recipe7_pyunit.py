# -*-coding:utf-8-*-
__author__ = "pawpawDu"
from recipe7 import *
from recipe7_legacy import *
import unittest

if __name__ == "__main__":
    tester = RomanNumeralTester()
    suite = unittest.TestSuite()
    for test in [tester.simple_test,tester.combo_test1,tester.combo_test2,
                 tester.other_test]:
        testcase = unittest.FunctionTestCase(test)#临时措施
        suite.addTest(testcase)
    unittest.TextTestRunner(verbosity=2).run(suite)
