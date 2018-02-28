#!/usr/bin/python
#-*- coding:utf-8 –*-

#一、列表
#作用：多个装备，多个爱好，多门课程，多个女朋友等
#定义：[]内可以有多个任意类型的值，逗号分隔
#变量l= list('字符串')
# l=list('hello')
# print(l)

#二、优先掌握的操作：
#1、按索引存取值(正向存取+反向存取)：即可存也可以取
# my_girl_friends=['alex','wupeiqi','yuanhao',4,5]
# print(my_girl_friends[0])

#2、切片(顾头不顾尾，步长)
# print(my_girl_friends[1:3])
# print(my_girl_friends[1:5:2])

#3、长度
# print(my_girl_friends.__len__())
# print(len(my_girl_friends))

#4、成员运算in和not in
# print('wupeiqi' in my_girl_friends)

#5、追加
# my_girl_friends.append(6)
# print(my_girl_friends)

#6、删除

#单纯的删除
# del my_girl_friends[5]
# print(my_girl_friends)

# print(my_girl_friends)
# res=my_girl_friends.remove('yuanhao')
# print(res)
# print(my_girl_friends)

#删除并拿到结果:取走一个值
# res=my_girl_friends.pop(2)
# print(res)
#
# print(my_girl_friends.pop(0)) #'alex'
# print(my_girl_friends.pop(0)) #'wupeqi'
# print(my_girl_friends.pop(0)) #'yuanhao'

#7、循环
# my_girl_friends=['alex','wupeiqi','yuanhao',4,5]
# i=0
# while i < len(my_girl_friends):
#     print(my_girl_friends[i])
#     i+=1
#
# for item in my_girl_friends:
#     print(item)
#
# for i in range(10):
#     if i== 3:
#         break
#         # continue
#     print(i)
# else:
#     print('===>')


#三、掌握的方法
#1、insert
my_girl_friends=['alex','wupeiqi','yuanhao','yuanhao',4,5]
# my_girl_friends.insert(1,'egon')
# print(my_girl_friends)

#2、clear python2 没有这个方法
# my_girl_friends.clear()
# print(my_girl_friends)

#3、copy
# l=my_girl_friends.copy()
# print(l)

#4、count
# print(my_girl_friends.count('yuanhao'))

#5、extend
# l=['egon1','egon2']
# my_girl_friends.extend(l)
# my_girl_friends.extend('hello')
# print(my_girl_friends)

#6、index
# print(my_girl_friends.index('wupeiqi'))

#7、reverse
# my_girl_friends.reverse()
# print(my_girl_friends)

#8、sort
# l=[1,10,4,11,2,]
# l.sort(reverse=True)
# print(l)

# l=['egon','alex','wupei']
# l.sort()
# print(l)

#二：该类型总结
# 1 可以存多个值，值都可以是任意类型
# 2 有序
# 3 ！！！可变：值变，id不变。可变==不可hash


#练习
# 1. 有列表data=['alex',49,[1900,3,18]]，分别取出列表中的名字，年龄，出生的年，月，日赋值给不同的变量
# data=['alex',49,[1900,3,18]]
# name = data[0]
# age = data[1]
# year = data[2][0]
# month = data[2][1]
# day = data[2][2]
# print(name,age,year,month,day)
#
# 2. 用列表模拟队列（先进先出）
# l=list()
# l.append('a')
# l.append('b')
# l.append('c')
# l.append('d')
# print(l)
#
# print(l.pop(0))
# print(l.pop(0))
# print(l.pop(0))
# print(l.pop(0))
#
# 3. 用列表模拟堆栈(先进后出，后进先出)
# l=list()
# l.insert(0,'e')
# l.insert(0,'f')
# l.insert(0,'g')
# print(l)
#
# print(l.pop(0))
# print(l.pop(0))
# print(l.pop(0))
#
# 4. 有如下列表，请按照年龄排序（涉及到匿名函数）
# l=[
#     {'name':'alex','age':84},
#     {'name':'oldboy','age':73},
#     {'name':'egon','age':18},
# ]
# l.sort(key=lambda item:item['age'])
# print(l)