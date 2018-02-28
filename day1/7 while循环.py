#!/usr/bin/python
#-*- coding:utf-8 –*-

#1、猜数字游戏(为何要使用循环语句)
'''
上节课我们已经学会用if .. else 来猜年龄的游戏啦，
但是只能猜一次就中的机率太小了，如果我想给玩家3次机会呢？
就是程序启动后，玩家最多可以试3次，这个怎么弄呢？
你总不会想着把代码复制3次吧。。。。
'''
# number = 25
#
# #第一次
# guess = input('please input your number: ')
# if guess == number:
#     print('哇塞！猜对了')
# elif guess > number:
#     print('猜大了')
# else:
#     print('猜小了')
#
# #第二次
# guess = input('please input your number: ')
# if guess == number:
#     print('哇塞！猜对了')
# elif guess > number:
#     print('猜大了')
# else:
#     print('猜小了')
#
# #第三次
# guess = input('please input your number: ')
# if guess == number:
#     print('哇塞！猜对了')
# elif guess > number:
#     print('猜大了')
# else:
#     print('猜小了')
'''
记住，写重复的代码是程序员最不耻的行为。
那么如何做到不用写重复代码又能让程序重复一段代码多次呢？ 循环语句就派上用场啦
上面的问题下面用循环语句的实现
'''
# number = 25
# guess = 1
# while guess:
#     if guess == number:
#         print('哇塞！猜对了')
#         break
#     elif guess > number:
#         print('猜大了')
#     else:
#         print('猜小了')
#     guess = input('please input your number: ')

# 2、打印0-10
# number = 0
# while number <= 10:
#     print (number)
#     number += 1
# 打印0-10之间的偶数
# number = 0
# while number <= 10:
#     if number%2 == 0:
#         print (number)
#     number += 1
# 打印0-10之间的奇数
# number = 0
# while number <= 10:
#     if number%2 != 0:
#         print (number)
#     number += 1

#3、死循环（只要条件一直为True，循环就一直继续）
# import time
# number = 0
# while True:
#     print(number)
#     time.sleep(1)
#     number += 1

# 4、循环嵌套与tag
# 练习，要求如下：
#     1 循环验证用户输入的用户名与密码
#     2 认证通过后，运行用户重复执行命令
#     3 当用户输入命令为quit时，则退出整个程序
#
# 第一种办法
# name = 'test'
# passport = 'test'
#
# while True:
#     input_name = raw_input('Please input your name: ')
#     input_password = raw_input('Please input your password: ')
#     if input_name == name and input_password == passport:
#         print('login success!!!')
#         while True:
#             input_cmd = raw_input('input your cmd: ')
#             if not input_cmd:
#                 continue
#             if input_cmd != 'quit':
#                 print('run <%s>' %input_cmd)
#                 continue
#             else:
#                 break
#
#     else:
#         print('your name or passport is error: ')
#         continue
#     break
#
# 第二种办法
# name = 'test'
# passport = 'test'
#
# tag = True
#
# while tag:
#     input_name = raw_input('请输入你的名字：')
#     input_passport = raw_input('请输入你的密码：')
#     if input_name == name and input_passport == passport:
#         print('恭喜你 登录成功！！！')
#         while tag:
#             cmd = raw_input('请输入你的命令：')
#             if not cmd:
#                 continue
#             if cmd == 'quit':
#                 tag = False
#             else:
#                 print('运行 <%s>' %cmd)
#                 continue
#     else:
#         print('账户名或者密码有误！请重新尝试')

# 以上程序有个不好的地方是账户密码错误的输入次数是无限次

# 5、while循环练习题
#     1 使用while循环输出1 2 3 4 5 6     8 9 10 （done）
#     2 求1-100的所有数的和
# number = 1
# sum = 0
# while number <= 100:
#     sum += number
#     number += 1
# print(sum)
#     3 输出 1-100 内的所有奇数
# number = 1
# sum = 0
# while number <= 100:
#     if number%2 == 1:
#         sum += number
#     number += 1
# print(sum)
#     4 输出 1-100 内的所有偶数
# number = 1
# sum = 0
# while number <= 100:
#     if number%2 == 0:
#         sum += number
#     number += 1
# print(sum)
#     5 求1-2+3-4+5 ... 99的所有数的和
# number = 1
# sum = 0
# while number < 100:
#     if number%2 == 1:
#         sum += number
#     else:
#         sum -= number
#     number += 1
# print(sum)
#     6 用户登陆（三次机会重试）
# number = 0
# name = 'test'
# passport = 'test'
# while number < 3:
#     input_name =raw_input('请输入你的账号：')
#     input_passport =raw_input('请输入你的密码：')
#     if input_name == name and input_passport == passport:
#         print('恭喜你!登录成功')
#         break
#     else:
#         print('账号或者密码有误!')
#         number += 1
#     7 猜年龄游戏
#         允许用户最多尝试3次，3次都没猜对的话，就直接退出，如果猜对了，打印恭喜信息并退出
# count = 0
# age = 18
# while count < 3:
#     input_age = input('请输入你猜的年龄：')
#     if input_age == age:
#         print('哇塞！猜对啦。。。')
#         break
#     print('猜错了，再试试')
#     count += 1
#     8 猜年龄游戏升级版
#         允许用户最多尝试3次
#         每尝试3次后，如果还没猜对，就问用户是否还想继续玩，如果回答Y或y, 就继续让其猜3次，以此往复，如果回答N或n，就退出程序
#         如果猜对了，就直接退出
#
# count = 0
# age = 18
#
# while True:
#     if count == 3:
#         Ans = raw_input('还想继续续玩吗？输入Y或者N:')
#         if Ans == 'Y' or Ans == 'y':
#             count = 0
#         else:
#             break
#
#     input_age = input('请输入你猜的年龄：')
#     if input_age == age:
#         print('哇塞！猜对啦。。。')
#         break
#     print('猜错了，再试试')
#     count += 1


