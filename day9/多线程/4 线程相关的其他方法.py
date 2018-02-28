#!/usr/bin/python
#-*- coding:utf-8 –*-

# Thread实例对象的方法
#   isAlive(): 返回线程是否活动的。
#   getName(): 返回线程名。
#   setName(): 设置线程名。
#
# threading模块提供的一些方法：
#   threading.currentThread(): 返回当前的线程变量。
#   threading.enumerate(): 返回一个包含正在运行的线程的list。正在运行指线程启动后、结束前，不包括启动前和终止后的线程。
#   threading.activeCount(): 返回正在运行的线程数量，与len(threading.enumerate())有相同的结果。

# from threading import Thread
# import threading
# import time
#
# def work():
#     time.sleep(3)
#     print(threading.current_thread().getName())
#
# t=Thread(target=work)
# t.start()
#
# print(threading.current_thread().getName())
# print(threading.current_thread())
# print(threading.enumerate())
# print(threading.active_count())
# print('主线程/主进程')


# 主线程等待子线程结束
from threading import Thread
import time

def sayhi(name):
    time.sleep(2)
    print('%s say hello' %name)

t=Thread(target=sayhi,args=('egon',))
t.start()
t.join()
print('主线程')
print(t.is_alive())