# -*-coding:utf-8-*-
"""assertEquals
　　函数原型1： assertEquals([String message],expected,actual)
参数说明：
       message是个可选的消息，假如提供，将会在发生错误时报告这个消息。
　　 expected 是期望值，通常都是用户指定的内容。
       actual 是被测试的代码返回的实际值。
　　函数原型2：assertEquals([String message],expected,actual,tolerance)
参数说明：
      message是个可选的消息，假如提供，将会在发生错误时报告这个消息。
　　expected是期望值，通常都是用户指定的内容。
　　actual是被测试的代码返回的实际值。
　　tolerance是误差参数，参加比较的两个浮点数在这个误差之内则会被认为是
　　相等的。
"""
__author__ = "pawpawDu"
class RomanNumeralConverter(object):
    def __init__(self):
        self.digit_map = {"M":1000,"D":500,"C":100,"L":50,"X":10,"V":5,"I":1}
    #罗马数字转换为十进制
    def convert_to_decimal(self,roman_numeral):
        val = 0
        for char in roman_numeral:
            val += self.digit_map[char]
        if val > 4000:
            #异常，当大于4000后输出
            raise Exception("We don't handle values over 4000")
        return val

    # 十进制转换为罗马数字
    def convert_to_roman(self,decimal):
        if decimal > 4000:
            # 异常，当大于4000后输出
            raise Exception("We don't handle values over 4000")
        val = ""
        mappers = [(1000,"M"),(500,"D"),(100,"C"),(50,"L"),(10,"X"),(5,"V"),(1,"I")]
        for (mappers_dec,mappers_rom) in mappers:
            while decimal >= mappers_dec:
                val += mappers_rom
                decimal -=mappers_dec
        return val
import unittest
class RomanNumeralTest(unittest.TestCase):
    def setUp(self):
        self.cvt = RomanNumeralConverter()
    def test_to_roman_bottom(self):
        self.assertEquals("I",self.cvt.convert_to_roman(1))

    print "低于目标值"
    def test_to_roman_below_bottom(self):
        self.assertEquals("",self.cvt.convert_to_roman(0))
    def test_to_roman_negative_value(self):
        self.assertEquals("",self.cvt.convert_to_roman(-1))
    def test_to_roman_top(self):
        self.assertEquals("MMMM",self.cvt.convert_to_roman(4000))
    def test_to_roman_above_top(self):
        #异常值
        self.assertRaises(Exception,self.cvt.convert_to_roman,4001)
    def test_to_decimal_bottom(self):
        self.assertEquals(1,self.cvt.convert_to_decimal("I"))

    def test_to_decimal_below_bottom(self):
        self.assertEquals(0, self.cvt.convert_to_decimal(""))

    def test_to_decimal_top(self):
        self.assertEquals(4000, self.cvt.convert_to_decimal("MMMM"))
        #函数原型1： assertEquals([String message],expected,actual),[String message],可选输入，期望值，实际值
        print "高于目标值"
    def test_to_decimal_above_top(self):
        self.assertRaises(Exception, self.cvt.convert_to_decimal,"MMMMI")
     #self.assert_raises(Exception, self.cvt.convert_to_decimal,"MMMMI") 这一句话就是说，函数self.cvt.convert_to_decimal(MMMMI)确保它一定会出现Exception这个异常

    def test_to_roman_tier1(self):
        self.assertEquals("V",self.cvt.convert_to_roman(5))

    def test_to_roman_tier2(self):
        self.assertEquals("X", self.cvt.convert_to_roman(10))

    def test_to_roman_tier3(self):
        self.assertEquals("L", self.cvt.convert_to_roman(50))

    def test_to_roman_tier4(self):
        self.assertEquals("C", self.cvt.convert_to_roman(100))

    def test_to_roman_tier5(self):
        self.assertEquals("D", self.cvt.convert_to_roman(500))

    def test_to_roman_tier6(self):
        self.assertEquals("M", self.cvt.convert_to_roman(1000))
    print "非常规输入检测"
    def test_to_roman_bad_inputs(self):

        self.assertEquals("",self.cvt.convert_to_roman(None))
        self.assertEquals("I", self.cvt.convert_to_roman(1.2))
    def test_to_decimal_bad_inputs(self):
        self.assertRaises(TypeError,self.cvt.convert_to_decimal,None)
        self.assertRaises(TypeError,self.cvt.convert_to_decimal,1.2)
if __name__ == "__main__":
    unittest.main()
















