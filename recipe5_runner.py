# -*-coding:utf-8-*-
__author__ = "pawpawDu"
if __name__ == "__main__":
    import unittest
    from recipe5 import *#引用测试用例文件

    suite1 = unittest.TestLoader().loadTestsFromTestCase(RomanNumeralConverterTest)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(RomanNumeralComboTest)
    suite = unittest.TestSuite([suite1,suite2])
    unittest.TextTestRunner(verbosity=2).run(suite)
