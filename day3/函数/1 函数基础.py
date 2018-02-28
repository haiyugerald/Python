#!/usr/bin/python
#-*- coding:utf-8 –*-
'''
1 为什么要有函数？没有函数带来的困扰？
    组织结构不清晰，可读性差
    代码冗余
    可扩展性差

2 什么是函数
    具备某一个功能的工具---》函数

    事先准备工具-》函数的定义
    拿来就用、重复使用-》函数的调用
    ps：先定义后调用

3 函数的分类：
    内置函数：len，max(10,11)，help(函数名)
    自定义函数：def
        语法：
            def 函数名(参数1，参数2，...):
                """注释"""
                函数体
                return 返回值
'''

#1、'函数即是变量'
# def print_tag():
#     print('*'*20)
#
# def print_msg(): #print_msg=<function print_msg at 0x00000000027EA8C8>
#     print('hello world')
#
#
# print(print_msg)  #打印出来的是这个函数在内存上的空间地址
# print(print_tag)
#
# print_tag()
# print_msg()
# print_tag()

#2、定义函数阶段都发生了什么事：只检测语法，不执行代码
#定义阶段
# def auth():
#     name=input('name>>: ').strip()
#     password=input('password>>: ').strip()
#     if name =='egon' and password == '123':
#         print('login successfull')
#     else:
#         print('user or password err')
#
#调用阶段
# auth()

#3、函数的使用：先定义后调用

# def bar():
#     print('from bar')
#
# def foo():
#     print('from foo')
#     bar()
#
# foo()

#4 定义函数的三种形式
#第一种：无参函数
# def auth():
#     name=input('name>>: ').strip()
#     password=input('password>>: ').strip()
#     if name =='egon' and password == '123':
#         print('login successfull')
#     else:
#         print('user or password err')

#第二种：有参函数
# def my_max(x,y):
#     if x >= y:
#         print(x)
#     else:
#         print(y)
#
# my_max(1,2)

# def auth(name,password):
#     if name =='egon' and password == '123':
#         print('login successfull')
#     else:
#         print('user or password err')
#
# def interactive():
#     name=input('name>>: ').strip()
#     password=input('password>>: ').strip()
#     auth(name,password)
#
# interactive()

#第三种：空函数
# def auth():
#     pass
#
# def put():
#     pass
#
# def get():
#     pass
#
# def ls():
#     pass

#5、返回值：return
#1）、函数可以有多个return，但是只执行一个
#2）、return的值不限类型

# def max_number(x,y):
#     if x>y:
#         print(x)
#     else:
#         print(y)
#
# res=max_number(1,2)
# print(res)

# def max_number(x,y):
#     if x>y:
#         return x
#     else:
#         return y
#
# res=max_number(1,2)
# print(res)

# 6、函数的参数：
# 形参：位置形参、默认参数
#   位置形参：必须被传值（用于经常会发生变化的参数）
#   默认参数：定义阶段已经有值，调用阶段可以不用传值（使用于不经常变动的参数）
#     PS:当形参中同时含有位置形参和默认参数时，默认参数必须放在位置形参的后边
#        默认参数的值只在定义时被赋值一次
#        默认参数的值通常应该是不可变类型（并非强制）
#     命名关键字参数：定义在*后面的参数(了解，传参的时候必须使用关键字实参)
# def auth(name,age,sex):
#     print(name,age,sex)
#
# def auth(name,age,sex='male'):
#     print(name,age,sex)
#
# sex='male'
# def auth(name,age,sex):
#     print(name,age,sex)
# sex='female'
# 实参：位置实参、关键字实参
#     位置实参：与位置形参一一对应，依赖于位置
#     关键字实参：不依赖位置，指定关键字
#     可变长参数：*(元组) **(字典)  形参的解决方案（*args，**kwargs）
#
# def auth(name,age,sex):
#     print(name,age,sex)
#
# auth('test',18,'male')
# auth(name='test',sex='male',age=18)
#
# def number(x,y,*args):
#     print(x,y)
#     print(args)
#
# number(1,2,3,4,5,6)
# number(1,2,*(3,4,5,6))
#
#
# def auth(name,age,sex='male',**kwargs):
#     print(name,age,sex)
#     print(kwargs)
#
# auth('test',18,'male',addr='shanxi')

# 练习题
# 1、写函数，用户传入修改的文件名，与要修改的内容，执行函数，完成批了修改操作
# 2、写函数，计算传入字符串中【数字】、【字母】、【空格] 以及 【其他】的个数
# 3、写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5。
# 4、写函数，检查传入列表的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
# 5、写函数，检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新列表返回给调用者。
# 6、写函数，检查字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
# dic = {"k1": "v1v1", "k2": [11,22,33,44]}
# PS:字典中的value只能是字符串或列表
#
#
# 1、
# def change(filename,oldsb,newsb):
#     import os
#     with open(filename,'r',encoding='utf-8') as read_f,\
#             open('.filename.swap','w',encoding='utf-8') as write_f:
#             for line in  read_f:
#                 if oldsb in line:
#                     line=line.replace(oldsb,newsb)
#                 write_f.write(line)
#
#     os.remove(filename)
#     os.rename('.filename.swap','filename')
#
# change('filename','somebady','sb')
#
# 2、
# def count(str):
#     res={
#         'string':0,
#         'num':0,
#         'space':0,
#         'qita':0
#     }
#     for s in str:
#         if s.isdigit():
#             res['num']+=1
#         elif s.isalpha():
#             res['string']+=1
#         elif s.isspace():
#             res['space']+=1
#         else:
#             res['qita']+=1
#     return  res
# res=count('hello world 123 : nihao ? ma ')
# print(res)
#
# 3、
# def long(str):
#     if len(str)>5:
#         print('长度大于5')
#     else:
#         print('长度小于5')
# res=long('hello')
#
# 4、
# def func1(list1):
#     if len(list1)>2:
#         list1=list1[0:2]
#     return  list1
#
# res=func1((1,2,3,4,5))
# print(res)
#
# 5、
# def func2(list2):
#     list2=list2[::2]
#     return  list2
# res=func2((1,2,3,4,5))
# print(res)
#
# 6、
# def func3(dic1):
#     for k,v in dic1.items():
#         if len(v) >2:
#             dic1[k] = v[0:2]
#         return  dic1
# print(func3({'k1':'abcdef','k2':[1,2,3,4],'k3':('a','b','c')}))