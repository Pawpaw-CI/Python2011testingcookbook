# -*-coding:utf-8-*-
__author__ = "pawpawDu"
#coding=utf-8
import pytest

# 功能函数
def multiply(a,b):
    return a * b

# =====fixtures========
def setup_module(module):
    print ("\n")
    print ("<===******************************setup_module******************************===>")

def teardown_module(module):
    print ("<====**************************teardown_module**************************====>")

def setup_function(function):
    print ("<@@@@@@@@@@@@@@@@setup_function_____@@@@@@@@@@@@@@@@>")

def teardown_function(function):
    print ("<@@@@@@@@@@@@@@@@teardown_function_____@@@@@@@@@@@@@@>")

# =====测试用例========
def test_numbers_3_4():
    print 'test_numbers_3_4'
    assert multiply(3,4) == 12


def test_strings_a_3():
    print 'test_strings_a_3'
    assert multiply('a',3) == 'aaa'

if __name__ == '__main__':
    pytest.main("-s test_fixtures.py")#执行详细打印-s