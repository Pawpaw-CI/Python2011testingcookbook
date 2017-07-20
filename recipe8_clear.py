# -*-coding:utf-8-*-
__author__ = "pawpawDu"
from recipe8 import *

import unittest

print "***每个断言放在单独的一个方法中，单独执行，相互之间不影响执行，那些用例失败一目了然**"
class RomanNumeralTest(unittest.TestCase):
    def setUp(self):
        self.cvt = RomanNumeralConverter()
    def test_convert_to_decimal1(self):
        self.assertEqual(0,self.cvt.convert_to_decimal(""))

    def test_convert_to_decimal2(self):
        self.assertEqual(1,self.cvt.convert_to_decimal("I"))

    def test_convert_to_decimal3(self):
        self.assertEqual(2010,self.cvt.convert_to_decimal("MMX"))

    def test_convert_to_decimal4(self):
        self.assertEqual(4000,self.cvt.convert_to_decimal("MMMM"))
        print "*****************************"
    def test_convert_to_roman1(self):
        self.assertEqual("",self.cvt.convert_to_roman(0))

    def test_convert_to_roman2(self):
        self.assertEqual("II",self.cvt.convert_to_roman(2))

    def test_convert_to_roman3(self):
        self.assertEqual("V",self.cvt.convert_to_roman(5))

    def test_convert_to_roman4(self):
        self.assertEqual("XII",self.cvt.convert_to_roman(12))

    def test_convert_to_roman5(self):
        self.assertEqual("MMX", self.cvt.convert_to_roman(2010))

    def test_convert_to_roman6(self):
        self.assertEqual("MMMM", self.cvt.convert_to_roman(4000))
        print "%%%%%%%%%%*****************************%%%%%%%%%%%%"
if __name__ == "__main__":
    unittest.main()
