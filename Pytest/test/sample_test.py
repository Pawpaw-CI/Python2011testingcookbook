# -*-coding:utf-8-*-
__author__ = "pawpawDu"
import pytest
def func(x):
    return x+1
def test_answer():
    assert func(3)==5