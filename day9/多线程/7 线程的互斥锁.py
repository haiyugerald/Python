#!/usr/bin/python
#-*- coding:utf-8 –*-
from threading import Thread,Lock
import time

n=100

def task():
    global  n
    with mutex:
        temp=n
        time.sleep(0.1)
        n=temp-1

t_l=[]
start_time=time.time()
mutex=Lock()
for i in range(100):
    t=Thread(target=task)
    t_l.append(t)
    t.start()

for t in t_l:
    t.join()
stop_time=time.time()
print('主函数',n)






print('time',stop_time-start_time)