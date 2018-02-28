#!/usr/bin/python
#-*- coding:utf-8 –*-
'''
multiprocessing模块支持进程间通信的两种主要形式:管道和队列
都是基于消息传递实现的,但是队列接口
'''

# from multiprocessing import Process,Queue
# import time
# q=Queue(3)  #3是队列中允许最大项数，省略则表示无大小限制
#
#
# #put ,get ,put_nowait,get_nowait,full,empty
# # q.put方法用以插入数据到队列中，put方法还有两个可选参数：blocked和timeout。
# # 如果blocked为True（默认值），并且timeout为正值，该方法会阻塞timeout指定的时间，直到该队列有剩余的空间。
# # 如果超时，会抛出Queue.Full异常。
# # 如果blocked为False，但该Queue已满，会立即抛出Queue.Full异常。
# q.put(3)
# q.put(3)
# q.put(3)
# print(q.full()) #满了
#
# print(q.get())
# print(q.get())
# print(q.get())
# print(q.empty()) #空了


from multiprocessing import Queue

q=Queue(3)

q.put('first')
q.put(2)
q.put({'count':3})
# q.put('fourth',block=False) #q.put_nowait('fourth')
# q.put('fourth',block=True,timeout=3)

print(q.get())
print(q.get())
print(q.get())
# print(q.get(block=False)) #q.get_nowait()
# print(q.get(block=True,timeout=3))
