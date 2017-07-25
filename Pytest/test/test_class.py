# -*-coding:utf-8-*-
__author__ = "pawpawDu"
#一个测试类中创建多个测试用例
class TestClass:
    def test_one(self):
        x = "hello"
        assert 'h'in x
    def test_two(self):
        x = "123"
        assert hasattr(x,"check")