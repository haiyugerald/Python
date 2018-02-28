#!/usr/bin/python
#-*- coding:utf-8 –*-
# f=open(r'C:\Users\Administrator\PycharmProjects\python20期\day2\a.txt')

# f=open('a.txt','r',encoding='utf-8')
# data=f.read()
# print(data)
# print(f)
# f.close() #文件关闭，回收操作系统的资源
# print(f)
# f.read()

# with open('a.txt','r',encoding='utf-8') as f: #f=open('a.txt','r',encoding='utf-8')
#     pass


#读操作:r只读模式，默认是rt文本读
# f=open('a.txt','r',encoding='utf-8')
# # data1=f.read()
# # print('=1===>',data1)
# # data2=f.read()
# # print('=2===>',data2)
#
# # print(f.readlines())
#
# # print(f.readline(),end='')
# # print(f.readline(),end='')
# # print(f.readline(),end='')
#
#
# f.close()


#写操作:w只写模式，默认是wt文本写，如果文件不存在则创建，存在则清空+覆盖
f=open('a.txt','w',encoding='utf-8')
# f.write('11111\n')
# f.write('222222\n')
# f.write('1111\n2222\n3333\n')
# f.writelines(['哈哈哈哈\n','你好','alex'])
f.close()



# 练习
# 1、利用b模式，编写一个cp工具，要求如下：
# 1）既可以拷贝文本又可以拷贝视频，图片等文件
# 2）用户一旦参数错误，打印命令的正确使用方法，如usage: cp source_file target_file
# 提示：可以用import sys，然后用sys.argv获取脚本后面跟的参数

#2、基于seek实现tail -f功能

#3、文件a.txt内容：每一行内容分别为商品名字，价钱，个数，求出本次购物花费的总钱数
apple 10 3
tesla 100000 1
mac 3000 2
lenovo 30000 3
chicken 10 3

#4、修改文件内容，把文件中的alex都替换成SB