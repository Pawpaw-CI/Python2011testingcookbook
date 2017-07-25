# -*-coding:utf-8-*-
__author__ = "pawpawDu"
import pytest
@pytest.fixture()#修饰器，
def fixture01():#定义测试夹具函数
    print "\n In fixture01()..."
def test_case01(fixture01):#测试夹具当做参数传给测试用例，使用了fixture01测试夹具函数，当执行用测试时fixture01作为参数传给test_case01
    print "\nIn test_case01()..."
