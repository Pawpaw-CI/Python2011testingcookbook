# -*-coding:utf-8-*-
__author__ = "pawpawDu"
class Calculator:
    def add(self,x,y):
        number_types = (int,float,complex)#关键字，数据范围
        if isinstance(x,number_types) and isinstance(y,number_types):#如果想，y是归档的数据范围内的
            return x+y
        else:
            raise  ValueError