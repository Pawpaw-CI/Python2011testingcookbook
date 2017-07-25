# -*-coding:utf-8-*-
__author__ = "pawpawDu"
from calculator import Calculator#导入被测类
import pytest#导入测试框架
class TestClass01:
    def test_case01(self):
        calc = Calculator()
        result = calc.add(2,2)
        assert  4 == result
    def test_case02(self):#新增一个测试用例
        with pytest.raises(ValueError):
            result = Calculator().add(2,"Two")
    def test_case03(self):
        with pytest.raises(ValueError):
            result = Calculator().add("two",2)
    def test_stradd04(self):#测试用例名称最好能体现用例功能
        with pytest.raises(ValueError):
            result = Calculator().add("two","two")