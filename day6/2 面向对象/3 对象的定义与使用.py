#!/usr/bin/python
#-*- coding:utf-8 –*-

class Student:

    school = 'oldboy'

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def  learn(self):
        print('%s is learning' % self)  # 新增self.name

    def eat(self):
        print('%s is eating' % self)

    def sleep(self):
        print('%s is sleeping' % self)


# 调用类的过程又称为实例化的过程，主要发生下面的两件事情
# 1、得到一个返回值即对象，该对象是一个空对象 s1
s1 = Student('李坦克', '男', 18)
s2 = Student('王大炮', '女', 28)
s3 = Student('牛榴弹', '男', 38)

print(s1.name)