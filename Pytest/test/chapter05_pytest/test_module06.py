# -*-coding:utf-8-*-
__author__ = "pawpawDu"
import pytest
@pytest.fixture()
def fixture01(request):#测试夹具函数，在进行测试用例执行时被当做参数传入
    print "\nIn fixture01()....."

@pytest.mark.usefixtures("fixture01")#修饰器，修饰测试类，测试夹具函数在进行测试用例执行时被当做参数传入
class TestClass03:
    def test_case01(self):
        print "\n I'm the test_case01"
    def test_case02(self):
        print "\nI'm the test_case02"

