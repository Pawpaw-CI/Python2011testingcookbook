# -*-coding:utf-8-*-
__author__ = "pawpawDu"
def setup_module(module):#定义测试模块，初始加载
    print "\nIn setup_module()..."
def teardonw_module(module):#定义测试模块，结束后清除
    print "\nIn teardown_module()..."
def setup_function(function):#定义测试函数，初始加载
    print "\nIn setup_function()..."
def teardown_function(function):#定义测试函数，结束后清除
    print "\nIn teardown_function()..."
def test_case01():#定义测试用例，
    print "\nIn test_case01()..."
def test_case02():#定义测试用例，
    print "\nIn test_case02()..."
class TestClass02:#定义测试类，
    @classmethod
    def setup_class(cls):
        print "\nIn setup_class()..."
    @classmethod
    def teardown_class(cls):
        print "\nIn teardown()..."
    def setup_method(self,method):
        print "\nIn setup_method()..."
    def teardown_method(self,method):
        print "\nIn teardown_method()..."
    def test_case03(self):
        print "\nIn test_case03()..."
    def test_case04(self):
        print "\nIn test_case04()..."
