#!/usr/bin/python
#-*- coding:utf-8 –*-
# import sys
# sys.argv     命令行参数List，第一个元素是程序本身路径
# sys.exit(n)  退出程序，正常退出时exit(0)
# sys.version  获取Python解释程序的版本信息
# sys.maxint   最大的Int值
# sys.path     返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
# sys.platform 返回操作系统平台名



# 练习：打印进度条

# =========知识储备==========
# 进度条的效果
# [#             ]
# [##            ]
# [###           ]
# [####          ]
#
# 指定宽度
# print('[%-15s]' %'#')  #-是左对齐 15是宽度
# print('[%-15s]' %'##')
# print('[%-15s]' %'###')
# print('[%-15s]' %'####')
#
# 打印%
# print('%s%%' %(100)) #第二个%号代表取消第一个%的特殊意义 100%
#
# 可传参来控制宽度
# print(('[%-%ds]' %50) %'#')#这个是错误的，这里这么想，先把50传值给%d，但是第一个%也会被认为要接受值，所以这里要保留他的本意，给下一次传值使用
#
# print('[%%-%ds]' %50) #[%-50s]
# print(('[%%-%ds]' %50) %'#')
# print(('[%%-%ds]' %50) %'##')
# print(('[%%-%ds]' %50) %'###')


#=========实现打印进度条函数==========
import time
def func1(percent, width=50):
    if percent >= 1:
        percent = 1
    jindu = (('[%%-%ds]' % width) % ('#' * int(width * percent)))
    print('\r%s %d%%' % (jindu, int(100 * percent)), end='')


#=========应用==========
recv_size=0
total_size=10241
while recv_size< total_size:
    time.sleep(0.1)
    recv_size+=1024
    func1(recv_size/total_size)

