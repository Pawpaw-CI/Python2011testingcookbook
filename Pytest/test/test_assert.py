# -*-coding:utf-8-*-
__author__ = "pawpawDu"
#coding=utf-8
import pytest

# 功能
def add(a,b):
    return a + b

# 测试相等
def test_add():
    assert add(3,4) == 7

# 测试不相等
def test_add2():
    assert add(17,22) != 50

# 测试大于
def test_add3():
    assert add(17,22) <= 50

# 测试小于
def test_add4():
    assert add(17,22) >= 50


if __name__ == '__main__':
    pytest.main("-s test_assert.py")