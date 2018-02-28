#!/usr/bin/python
#-*- coding:utf-8 –*-
# 1、比较谁的开启速度快
# from threading import  Thread
# from multiprocessing import Process
#
# def task():
#     print('hello')
#
# t1=Thread(target=task)
# t1.start()
# print('主函数/线程')
#
# p1=Process(target=task)
# p1.start()
# print('主函数/进程')
#
# 2、查看pid
# from threading import  Thread
# from multiprocessing import Process
# import os
# def task():
#     print('hello', os.getpid())
#
# # 在主进程下开多个线程,每个线程都跟主进程的pid一样
# t1=Thread(target=task)
# t2=Thread(target=task)
# t1.start()
# t2.start()
# print('主函数pid/线程',os.getpid())
#
# # 在主进程下开多个进程,每个进程都有不同的pid
# p1=Process(target=task)
# p2=Process(target=task)
# p1.start()
# p2.start()
# print('主函数pid/进程',os.getpid())
#
# 3、同一进程内的线程共享改进程内的数据
from  threading import Thread
from  multiprocessing import Process
def task():
    global n
    n=0

n=1
p=Process(target=task)
p.start()
p.join()
print('主函数/进程',n)

t=Thread(target=task)
t.start()
t.join()
print('主函数/线程',n)