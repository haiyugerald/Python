#!/usr/bin/python
#-*- coding:utf-8 –*-

# 多线程性能测试
# 1、计算密集型：多进程效率高
# from multiprocessing import Process
# from threading import Thread
# import os,time
# def work():
#     res=0
#     for i in range(100000000):
#         res*=i
# l=[]
# print(os.cpu_count()) #本机为4核
# start=time.time()
# for i in range(4):
#     # p=Process(target=work) #耗时18s多
#     p=Thread(target=work) #耗时26s多
#     l.append(p)
#     p.start()
# for p in l:
#     p.join()
# stop=time.time()
# print('run time is %s' %(stop-start))

# 2、i/o密集型：多线程效率高
# from multiprocessing import Process
# from threading import Thread
# import threading
# import os,time
#
# def work():
#     time.sleep(2)
#     print('===>')
#
# l=[]
# print(os.cpu_count()) #本机为4核
# start=time.time()
# for i in range(400):
#     p=Process(target=work) #耗时4s多,大部分时间耗费在创建进程上
#     # p=Thread(target=work) #耗时2s多
#     l.append(p)
#     p.start()
# for p in l:
#     p.join()
# stop=time.time()
# print('run time is %s' %(stop-start))