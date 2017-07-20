# -*-coding:utf-8-*-
__author__ = "pawpawDu"
import unittest
class RomanNumeralConverter(object):
    def __init__(self,roman_numeral):
        self.roman_numeral = roman_numeral
        self.digit_map = {"M":1000,"D":500,"C":100,"L":50,"X":10,"V":5,"I":1}
    def convert_to_deciaml(self):
        val = 0
        for char in self.roman_numeral:
            val += self.digit_map[char]
        return val

#单元测试框架的使用class名后+Test（unittest.Testcase）
#定义罗马数字的各个测试方法
class RomanNumeralConverterTest(unittest.TestCase):
    def test_parsing_millenia(self):
        value = RomanNumeralConverter("M")
        self.assertEqual(1000,value.convert_to_deciaml())

    def test_parsing_half_millenia(self):
        value = RomanNumeralConverter("D")
        self.assertEqual(500, value.convert_to_deciaml())
    def test_parsing_century(self):
        value = RomanNumeralConverter("C")
        self.assertEqual(100,value.convert_to_deciaml())
    def test_parsing_half_century(self):
        value = RomanNumeralConverter("L")
        self.assertEqual(50,value.convert_to_deciaml())
    def test_parsing_decade(self):
        value = RomanNumeralConverter("X")
        self.assertEqual(10,value.convert_to_deciaml())

    def test_parsing_half_decade(self):
        value = RomanNumeralConverter("V")
        self.assertEqual(5, value.convert_to_deciaml())
    def test_parsing_one(self):
        value = RomanNumeralConverter("I")
        self.assertEqual(1,value.convert_to_deciaml())
    def test_empty_roman_numeral(self):
        value = RomanNumeralConverter("")
        self.assertTrue(value.convert_to_deciaml()==0)
        self.assertFalse(value.convert_to_deciaml()>0)

    def test_parsing_one(self):
        value = RomanNumeralConverter("I")
        self.assertEqual(1, value.convert_to_deciaml())
if __name__ == "__main__":
    unittest.main()