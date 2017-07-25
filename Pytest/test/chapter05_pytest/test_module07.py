# -*-coding:utf-8-*-
__author__ = "pawpawDu"
import pytest
@pytest.fixture()
def fixture01(request):
    print "\nIn fixture....."
    def fin():#结束方法
        print "\nFinalized..."
    request.addfinalizer(fin) #测试夹具函数增加一个结束方法，在进行测试用例执行时被当做参数传入
@pytest.mark.usefixtures("fixture01")
def test_case01():
    print "\n I'm the test_case01"
