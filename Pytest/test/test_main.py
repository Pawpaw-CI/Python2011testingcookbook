# -*-coding:utf-8-*-
__author__ = "pawpawDu"
import pytest
def test_main():
    assert 5!=5
if __name__ =="__main__":
    pytest.main("-q test_main.py")