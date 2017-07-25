# -*-coding:utf-8-*-
__author__ = "pawpawDu"
import pytest

@pytest.fixture()
def before():
    print '\nbefore each test'

def test_1(before):
    print 'test_1()'

def test_2(before):
    print 'test_2()'
    assert 0