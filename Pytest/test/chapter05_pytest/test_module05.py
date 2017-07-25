# -*-coding:utf-8-*-
__author__ = "pawpawDu"
#
import pytest
@pytest.fixture() #修饰器，
def fixture01(request):
    print "\nIn fixture01()....."

@pytest.mark.usefixtures("fixture01")#修饰器，修饰测试用例，与上述修饰器效果相同
def test_case01(fixture01):#测试夹具函数，在进行测试用例执行时被当做参数传入
    print "\n I'm the test_case01"



