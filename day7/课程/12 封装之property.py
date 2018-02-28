#!/usr/bin/python
#-*- coding:utf-8 –*-

# 一、BMI
# 体质指数（BMI）=体重（kg）÷身高^2（m）
class People():
    def __init__(self,name,age,sex,weith,higth):
        self.name=name
        self.age=age
        self.sex=sex
        self.weith=weith
        self.higth=higth

    @property
    def BMI(self):
        return self.weith/(self.higth**2)

# 没有property之前的调用方法
# lqq=People('lqq',25,'female',55,1.65)
# print(lqq.BMI())

# 使用property之后的调用方法
lqq=People('lqq',25,'female',55,1.65)
print(lqq.BMI)

# 二、为什么要用property
# 将一个类的函数定义成特性以后，对象再去使用的时候obj.name,根本无法察觉自己的name是执行了一个函数然后计算出来的，这种特性的使用方式遵循了统一访问的原则
# ps：面向对象的封装有三种方式:
# 【public】这种其实就是不封装,是对外公开的
# 【protected】这种封装方式对外不公开,但对朋友(friend)或者子类(形象的说法是“儿子”,但我不知道为什么大家 不说“女儿”,就像“parent”本来是“父母”的意思,但中文都是叫“父类”)公开
# 【private】这种封装对谁都不公开
# class Foo:
#     def __init__(self,name):
#         self.__NAME=name #将所有的数据属性都隐藏起来
#
#     @property
#     def name(self，obj):
#         if not type(obj) str:
#         return self.__NAME #obj.name访问的是self.__NAME(这也是真实值的存放位置)
#
#     @name.setter
#     def name(self,value):
#         if not isinstance(value,str):  #在设定值之前进行类型检查
#             raise TypeError('%s must be str' %value)
#         self.__NAME=value #通过类型检查后,将值value存放到真实的位置self.__NAME
#
#     @name.deleter
#     def name(self):
#         raise TypeError('Can not delete')
#
# f=Foo('egon')
# print(f.name)
# # f.name=10 #抛出异常'TypeError: 10 must be str'
# del f.name #抛出异常'TypeError: Can not delete'