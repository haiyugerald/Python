#!/usr/bin/python
#-*- coding:utf-8 –*-
#1、进程对象的其他方法一:terminate,is_alive
# from multiprocessing import Process
# import time
#
# def task(name):
#     print('%s is running' %name)
#     time.sleep(3)
#     print('%s is done' %name)
#
# p=Process(target=task,args=('Alex',))
# p.start()
#
# #关闭进程,不会立即关闭,所以is_alive立刻查看的结果可能还是存活，过一会就就不存活了
# p.terminate()
# print(p.is_alive())
#
# print('开始')
# print(p.is_alive())

# 2、pid
# from multiprocessing import Process
# import time
#
# def task(name):
#     print('%s is running' %name)
#     time.sleep(3)
#     print('%s is done' %name)
#
# p=Process(target=task,args=('Alex',))
# p.start()
# print(p.pid)

# 3、孤儿进程与僵尸进程
# import os
# import sys
# import time
#
# pid = os.getpid()
# ppid = os.getppid()
# print('im father', 'pid', pid, 'ppid', ppid)
# pid = os.fork()
# #执行pid=os.fork()则会生成一个子进程
# #返回值pid有两种值：
# #    如果返回的pid值为0，表示在子进程当中
# #    如果返回的pid值>0，表示在父进程当中
# if pid > 0:
#     print('father died..')
#     sys.exit(0)
#
# # 保证主线程退出完毕
# time.sleep(1)
# print('im child', os.getpid(), os.getppid())
