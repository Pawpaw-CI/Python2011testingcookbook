# -*-coding:utf-8-*-
__author__ = "pawpawDu"
from recipe8 import *

import unittest

class RomanNumeralTest(unittest.TestCase):
    def setUp(self):
        self.cvt = RomanNumeralConverter()
    def test_convert_to_decimal(self):
        self.assertEqual(0,self.cvt.convert_to_decimal(""))
        self.assertEqual(1,self.cvt.convert_to_decimal("I"))
        self.assertEqual(2010,self.cvt.convert_to_decimal("MMX"))
        self.assertEqual(4000,self.cvt.convert_to_decimal("MMMM"))
        print "***多个断言放在一个方法中，只要有一个失败其他不在执行，具体哪些失败模糊不清***"
    def test_convert_to_roman(self):
        self.assertEqual("",self.cvt.convert_to_roman(0))
        self.assertEqual("II",self.cvt.convert_to_roman(2))
        self.assertEqual("V",self.cvt.convert_to_roman(5))
        self.assertEqual("XII",self.cvt.convert_to_roman(12))
        self.assertEqual("MMX", self.cvt.convert_to_roman(2010))
        self.assertEqual("MMMM", self.cvt.convert_to_roman(4000))
        print "%%%%%%%%%%*****************************%%%%%%%%%%%%"
if __name__ == "__main__":
    unittest.main()
