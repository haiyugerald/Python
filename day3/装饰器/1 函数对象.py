#!/usr/bin/python
#-*- coding:utf-8 –*-
#函数是第一类对象：指的是函数可以当做数据传递
#1、可以被引用 x=1,y=x
# def func(x,y):
#     print(x,y)
#
# f=func
# f(1,2)

#2、可当做函数的参数传入
# def foo():
#     print('from foo')
#
# def bar(func):
#     # print(func)
#     func()
#
# bar(foo)

#3、可以当做函数的返回值
# def foo():
#     print('from foo')
#
# def bar():
#     return foo
#
# f=bar()
# f()

#4、可以当做容器类型的元素
# def foo():
#     print('from foo')
#
# def bar():
#     return foo
#
# l=[foo,bar]
# print(l)
# l[0]()

# def get():
#     print('get')
#
# def put():
#     print('put')
#
# def ls():
#     print('ls')
#
# cmd=input('>>: ').strip()
# if cmd == 'get':
#     get()
# elif cmd == 'put':
#     put()
# elif cmd == 'ls':
#     ls()

# def get():
#     print('get')
#
# def put():
#     print('put')
#
# def ls():
#     print('ls')
#
# def auth():
#     print('auth')
#
# func_dic={
#     'get':get,
#     'put':put,
#     'ls':ls,
#     'auth':auth
# }

# func_dic['put']()

# cmd = input('>>: ').strip()
# if cmd in func_dic:
#     func_dic[cmd]()