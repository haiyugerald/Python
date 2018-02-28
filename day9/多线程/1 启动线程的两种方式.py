#!/usr/bin/python
#-*- coding:utf-8 –*-

# 方式一：
# from threading import Thread
# import time
# import random
#
# def task(name):
#     print('%s is running' %name)
#     time.sleep(random.randint(1,3))
#     print('%s is end' %name)
#
# 注意：在windows中Process()必须放到# if __name__ == '__main__':下
# if __name__ == '__main__':
#     t1=Thread(target=task,args=('ALex',))
#     t1.start()
#     print('主函数')
#
# linux下的就不需要if __name__ == '__main__':
# t1=Thread(target=task,args=('renwu1',))
# t1.start()
# print('主函数')
#
# 方式二：
from threading import Thread
import time
import random

class task(Thread):
    def __init__(self,name):
        super().__init__()
        self.name=name
    def run(self):
        print('%s is runnging' %self.name)
        time.sleep(random.randint(1,3))
        print('%s is end' %self.name)

t1=task('renwu1')
t1.start()
print('主函数')

