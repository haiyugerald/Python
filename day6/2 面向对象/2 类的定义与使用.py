#!/usr/bin/python
#-*- coding:utf-8 –*-


class Student:

    school = 'oldboy'  #类定义的变量是共享给对象用的

    def __init__(self, name, age, sex):  #__init__是为对象初始化的
        self.name = name
        self.age = age
        self.sex = sex

    def  learn(self): #类定义的函数是绑定给对象用的(self会自动作为第一个参数)，类本身是可以调的，但是必须遵循函数的调用规则(传参)
        print('%s is learning' % self)  # 新增self.name

    def eat(self):
        print('%s is eating' % self)

    def sleep(self):
        print('%s is sleeping' % self)

# 类体代码在类的定义阶段就会立刻执行，

Student.sleep('lqq')

# print(Student)
# print(Student.__dict__)  #查看类的名称空间，以字典的形式
#
# #查看
# print(Student.school) #数据属性
# print(Student.learn) #函数属性
#
# #增加
# Student.country='China'
# print(Student.country)
#
# #修改
# Student.school='Oldboy'
# print(Student.school)
#
# #删除
# # del Student.country
# # print(Student.country)   #删除之后在打印 会报错
#
# print(Student.learn)
Student.learn('egon')

