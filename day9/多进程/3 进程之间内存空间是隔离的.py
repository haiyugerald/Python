#!/usr/bin/python
#-*- coding:utf-8 –*-
# from multiprocessing import Process
# n=100 #在windows系统中应该把全局变量定义在if __name__ == '__main__'之上就可以了
# def work():
#     global n
#     n=0
#     print('子进程内: ',n)
#
# if __name__ == '__main__':
#     p=Process(target=work)
#     p.start()
#     print('主进程内: ',n)

from multiprocessing import Process
x=100
def task():
    global x
    x=0
    print('子进程x值是：',x)

p=Process(target=task)
p.start()
print('主进程x值是：',x)
