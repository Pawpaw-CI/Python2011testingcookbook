# -*-coding:utf-8-*-
#使用列表，元素、字典、迭代
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
        if decimal > 4000: # 异常，当大于4000后输出
            raise Exception("We don't handle values over 4000")
        val = ""
        mappers = [(1000,"M"),(500,"D"),(100,"C"),(50,"L"),(10,"X"),(5,"V"),(1,"I")]
        for (mappers_dec,mappers_rom) in mappers:
            while decimal >= mappers_dec:
                val += mappers_rom
                decimal -=mappers_dec
        return val
import unittest

class RomanNumeralTest(unittest.TestCase):     #生成一个测试类
    def setUp(self):
        self.cvt = RomanNumeralConverter() #创建一个对象，被测类的实例
    def test_edges(self):       #测试方法,测试方法必须是以小写test开头的方法;#被测对象的类中的方法调用
        r =  self.cvt.convert_to_roman
        d = self.cvt.convert_to_decimal
        edges = [("equals",r,"I",1),("equals",r,"",0),
                 ("equals",r,"",-1),("equals",r,"MMMM",4000),
                 ("raises",r,Exception,4001),("equals",d,1,"I"),
                 ("equals",d,0,""),("equals",d,4000,"MMMM"),
                 ("raises",d,Exception,"MMMMI")] #异常要用raises捕获
        [self.checkout_edge(edge) for edge in edges]
    def test_tiers(self):
        r = self.cvt.convert_to_roman#下列列表[],中的元组（）内部元素不可变，

        edges = [("equals", r, "V", 5), ("equals", r, "VIIII", 9),
                 ("equals", r, "X", 10), ("equals", r, "XI", 11),
                 ("equals", r, "L", 50),("equals", r, "LI", 51),
                 ("equals", r, "LXXXXVIIII", 99),("equals", r, "C", 100),
                 ("equals", r, "CI", 101),("equals", r, "CCCCLXXXXVIIII", 499),
                 ("equals", r, "D", 500),("equals", r, "DI", 501),
                 ("equals", r, "M", 1000) ]

        [self.checkout_edge(edge) for edge in edges] #循环检测


    def test_bad_inputs(self):        # 无效输入集合
        r = self.cvt.convert_to_roman
        d = self.cvt.convert_to_decimal
        edges = [("equals", r, "", None),
                 ("equals", r, "I", 1.1),
                 ("raises", d, TypeError, None),
                 ("raises", d, TypeError, 1.1)]
        [self.checkout_edge(edge) for edge in edges]


    def checkout_edge(self,edge):
        if edge[0]=="equals":
            f,output,input =edge[1],edge[2],edge[3]
            print ("Converting %s to %s..."%(input,output))
            self.assertEquals(output,f(input))
        elif edge[0] == "raises":
            f, exception, args = edge[1], edge[2], edge[3:]
            print ("Converting %s expecting %s..." % (args, exception))
            self.assertRaises(exception,f,*args)
if __name__ == "__main__":
    #加载测试用例到测试套件
    suite = unittest.TestLoader().loadTestsFromTestCase(RomanNumeralTest)
    #执行测试套件
    unittest.TextTestRunner(verbosity=2).run(suite)









