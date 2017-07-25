# -*-coding:utf-8-*-
__author__ = "pawpawDu"
#coding=utf-8
import pytest


# 测试相等
def test_in():
    a = "hello"
    b = "he"
    assert b in a


# 测试不相等
def test_not_in():
    a = "hello"
    b = "hi"
    assert b not in a

if __name__ == '__main__':
    pytest.main("-s test_assert2.py")