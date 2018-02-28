#!/usr/bin/python
#-*- coding:utf-8 –*-

# 1、
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
# p.join()
# print('主函数')

# 2、
# from multiprocessing import Process
# import time
#
# class task(Process):
#     def __init__(self,name):
#         super().__init__()
#         self.name=name
#     def run(self):
#         print('%s is running' %self.name)
#         time.sleep(3)
#         print('%s is done' %self.name)
#
#
# p=task('Alex')
# p.start()
# p.join()
# print('主函数')

# 3、
# from multiprocessing import Process
# import time
# import random
# def run(name):
#     print('%s is running' %name)
#     time.sleep(random.randint(1,3))
#     print('%s is ending' %name)
#
# p1=Process(target=run,args=('egon',))
# p2=Process(target=run,args=('alex',))
# p3=Process(target=run,args=('yuanhao',))
# p4=Process(target=run,args=('wupeiqi',))
#
# p1.start()
# p2.start()
# p3.start()
# p4.start()
#
# p1.join()
# p2.join()
# p3.join()
# p4.join()
#
# print('主线程')

# 4、
from multiprocessing import Process
import time
import random
def run(name):
    print('%s is running' %name)
    time.sleep(random.randint(1,3))
    print('%s is ending' %name)

p1=Process(target=run,args=('egon',))
p2=Process(target=run,args=('alex',))
p3=Process(target=run,args=('yuanhao',))
p4=Process(target=run,args=('wupeiqi',))

p_l=[p1,p2,p3,p4]
for p in p_l:
    p.start()
    # p.join() 这样写会造成四个人完全变成串行，第一个开始到结束
for p in p_l:
    p.join()

print('主线程')