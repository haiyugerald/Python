#!/usr/bin/python
#-*- coding:utf-8 –*-
#
# from multiprocessing import Process
# import time
#
# def task(name):
#     print('%s is running' %name)
#     time.sleep(3)
#     print('%s is done' %name)
#
#
# p=Process(target=task,args=('Alex',))
# p.daemon=True #一定要在p.start()前设置,设置p为守护进程,禁止p创建子进程,并且父进程代码执行结束,p即终止运行
# p.start()
# print('主函数')


from multiprocessing import Process
import time
def foo():
    print(123)
    time.sleep(1)
    print("end123")

def bar():
    print(456)
    time.sleep(3)
    print("end456")


p1=Process(target=foo)
p2=Process(target=bar)

p1.daemon=True
p1.start()
p2.start()
print("main-------")
#打印该行则主进程代码结束,则守护进程p1应该被终止,可能会有p1任务执行的打印信息123,因为主进程打印main时,p1也执行了,但是随即被终止