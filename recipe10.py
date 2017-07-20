# -*-coding:utf-8-*-

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
#生成一个测试类
class RomanNumeralTest(unittest.TestCase):
    def setUp(self):
        self.cvt = RomanNumeralConverter()
        #创建一个对象，被测类的实例
    #测试方法
    def test_edges(self):
        r =  self.cvt.convert_to_roman
        d = self.cvt.convert_to_decimal
        edges = [("equals",r,"I",1),("equals",r,"",0),("equals",r,"",-1),("equals",r,"MMMM",4000),("equals",r,Exception,4001),
                 ("equals",d,1,"I"),("equals",d,0,""),("equals",d,4000,"MMMM"),("equals",d,Exception,"MMMMI"),]
        [self.checkout_edge(edge) for  edge in  edges]













