#!/usr/bin/python
#-*- coding:utf-8 –*-

#1 什么是生成器：只要在函数体内出现yield关键字，那么再执行函数就不会执行函数代码，会得到一个结果，该结果就是生成器
# def func():
#     print('=====>1')
#     yield 1
#     print('=====>2')
#     yield 2
#     print('=====>3')
#     yield 3

#生成器就是迭代器
# g=func()

# res1=next(g)
# print(res1)
#
#
# res2=next(g)
# print(res2)
#
#
# res3=next(g)
# print(res3)


#yield的功能：
#1、yield为我们提供了一种自定义迭代器对象的方法
#2、yield与return的区别1：yield可以返回多次值 #2：函数暂停与再继续的状态是由yield帮我们保存的

# obj=range(1,1000000000000000000000000000000000000000000000000000000000000000,2)
# obj_iter=obj.__iter__()
# print(next(obj_iter))
# print(next(obj_iter))
# print(next(obj_iter))
# print(next(obj_iter))
# print(next(obj_iter))

#练习
# 1、自定义函数模拟range(1,7,2)
#
# def my_range(start,stop,step=1):
#     while start<stop:
#             yield start
#             start+=step
#
#
# obj=my_range(1,7,2)
# print(next(obj))
# print(next(obj))
# print(next(obj))
# print(next(obj))  #StopIteration 为什么不能在函数里面加异常处理的原因是，只有在取值的时候才会有异常，函数中没涉及取值
#
# 2、模拟管道，实现功能:tail -f access.log.log | grep '404'
# def tail(file):
#     import time
#     with open(file,'rb') as f:
#         f.seek(0,2)
#         while True:
#             line = f.readline()
#             if line:
#                 # print(line)
#                 yield  line
#             else:
#                 # continue  不要直接continue，会变成死循环 消耗资源
#                 time.sleep(0.05)
#
# def grep(lines,pattern):
#     for line in lines:
#         line = line.decode('utf-8')
#         if pattern in line:
#             yield  line
#
# for line in grep( tail('access.log.log'),'404'):
#     print(line, end='')

#了解知识：yield关键字的另外一种使用形式：表达式形式的yield
# def eat(name):
#     print("%s ready to eat" %name)
#     while True:
#         food = yield
#         print("%s eat %s" %(name,food))
#
# e=eat('sb')
# e.send(None)
# e.send('面条')
# e.send('米饭')
# e.send('冒菜')


# 3、编写装饰器，实现初始化协程函数的功能
# def init(func):
#     def wrapper(*args,**kwargs):
#         g=func(*args,**kwargs)
#         next(g)
#         return g
#     return wrapper
# @init
# def eater(name):
#     print('%s 准备开始吃饭啦' %name)
#     food_list=[]
#     while True:
#         food=yield food_list
#         print('%s 吃了 %s' % (name,food))
#         food_list.append(food)
#
# g=eater('egon')
# g.send('蒸羊羔')

# 4、grep  -rl  'python'  /etc
# import os
# def init(func):
#     def wrapper(*args,**kwargs):
#         g=func(*args,**kwargs)
#         next(g)
#         return g
#     return wrapper
#
# @init
# def search(target):
#     while True:
#         filepath=yield
#         g=os.walk(filepath)
#         for dirname,_,files in g:
#             for file in files:
#                 abs_path=r'%s\%s' %(dirname,file)
#                 target.send(abs_path)
# @init
# def opener(target):
#     while True:
#         abs_path=yield
#         with open(abs_path,'rb') as f:
#             target.send((f,abs_path))
# @init
# def cat(target):
#     while True:
#         f,abs_path=yield
#         for line in f:
#             res=target.send((line,abs_path))
#             if res:
#                 break
# @init
# def grep(pattern,target):
#     tag=False
#     while True:
#         line,abs_path=yield tag
#         tag=False
#         if pattern.encode('utf-8') in line:
#             target.send(abs_path)
#             tag=True
# @init
# def printer():
#     while True:
#         abs_path=yield
#         print(abs_path)
#
#
# g=search(opener(cat(grep('你好',printer()))))
# # g.send(r'E:\CMS\aaa\db')
# g=search(opener(cat(grep('python',printer()))))
# g.send(r'E:\CMS\aaa\db')