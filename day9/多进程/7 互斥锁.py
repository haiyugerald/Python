#!/usr/bin/python
#-*- coding:utf-8 –*-
#1、并发运行,效率高,但竞争同一打印终端,带来了打印错乱
# from multiprocessing import Process,Lock
# import time,os
# def task():
#     print('%s is running' %os.getpid())
#     time.sleep(3)
#     print('%s is done' %os.getpid())
#
# for i in range(3):
#     p=Process(target=task)
#     p.start()

# 2、由并发变成了串行,牺牲了运行效率,但避免了竞争
# from multiprocessing import Process,Lock
# import time
# import os
# def task(lock):
#     lock.acquire()
#     print('%s is running' %os.getpid())
#     time.sleep(3)
#     print('%s is done' %os.getpid())
#     lock.release()
#
# lock=Lock()
# for i in range(3):
#     p=Process(target=task,args=(lock,))
#     p.start()

# 3、购票练习（并发运行,效率高,但竞争同一文件,数据写入错乱）
# from multiprocessing import Process
# import time,json,random
# def search():
#     dic=json.load(open('db.txt'))
#     print('剩余票数%s' %dic['count'])
#
# def get():
#     dic=json.load(open('db.txt'))
#     time.sleep(0.1) #模拟读数据的网络延迟
#     if dic['count'] >0:
#         dic['count']-=1
#         time.sleep(0.2) #模拟写数据的网络延迟
#         json.dump(dic,open('db.txt','w'))
#         print('购票成功')
#
# def task():
#     search()
#     get()
#
# for i in range(3): #模拟并发100个客户端抢票
#     p=Process(target=task)
#     p.start()

# 4、加锁：由并发变成了串行,牺牲了运行效率,但保证了数据的安全
from multiprocessing import  Process,Lock
import json,time
def search():
    dic=json.load(open('db.txt'))
    print('剩余票数%s' %dic['count'])

def get():
    dic = json.load(open('db.txt'))
    time.sleep(0.1)
    if dic['count']>0:
        dic['count']-=1
        time.sleep(0.1)
        json.dump(dic,open('db.txt','w'))
        print('购票成功')
    else:
        print('没票了')

def task(lock):
    search()
    lock.acquire()
    get()
    lock.release()

lock=Lock()
for i in range(3):
    p=Process(target=task,args=(lock,))
    p.start()