#!/usr/bin/python
#-*- coding:utf-8 –*-
from multiprocessing import Process,Queue
import time,random,os
def consumer(q):
    while True:
        res=q.get()
        time.sleep(random.randint(1,3))
        print('%s 吃 %s' %(os.getpid(),res))

def producer(q):
    for i in range(10):
        time.sleep(random.randint(1,3))
        res='包子%s' %i
        print(res)
        q.put(res)
        print('%s 生产了 %s' %(os.getpid(),res))

    q.put(None)
q=Queue()
#生产者们:即厨师们
p1=Process(target=producer,args=(q,))

#消费者们:即吃货们
c1=Process(target=consumer,args=(q,))

#开始
p1.start()
c1.start()
# p1.join()
# q.put(None) #发送结束信号
print('主')