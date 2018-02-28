#!/usr/bin/python
#-*- coding:utf-8 –*-
# 方式1：用已有的python类
# from multiprocessing import Process
# import time
#
# def task(name):
#     print('%s is running' %name)
#     time.sleep(3)
#     print('%s is done' %name)
#
# 注意：在windows中Process()必须放到# if __name__ == '__main__':下
# if __name__=='__main__':
#     p=Process(target=task,args=('Alex',))
#     p.start()
#     print('主函数')

# linux下的就不需要if __name__ == '__main__':
# p=Process(target=task,args=('Alex',))
# p.start()
# print('主函数')

# 方式2：继承现有的类，自己写一个类
from multiprocessing import Process
import time

class task(Process):
    def __init__(self,name):
        super().__init__()
        self.name=name
    def run(self):
        print('%s is running' %self.name)
        time.sleep(3)
        print('%s is done' %self.name)

# if __name__=='__main__':
#     p=task('Alex')
#     p.start()
#     print('主函数')

p=task('Alex')
p.start()
print('主函数')