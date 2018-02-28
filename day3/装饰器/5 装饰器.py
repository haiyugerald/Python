#!/usr/bin/python
#-*- coding:utf-8 –*-

# 1、开放封闭原则：对修改封闭，对扩展开放
# 2、什么是装饰器
# 装饰器他人的器具，本身可以是任意可调用对象，被装饰者也可以是任意可调用对象。
# 强调装饰器的原则：1 不修改被装饰对象的源代码 2 不修改被装饰对象的调用方式
# 装饰器的目标：在遵循1和2的前提下，为被装饰对象添加上新功能
import time
def index():
    time.sleep(3)
    print("welcome to index")

def outter(func):
    def inner():
        start=time.time()
        func()
        stop=time.time()
        print("run time is %s" %(stop-start))
    return inner

index=outter(index)
index()