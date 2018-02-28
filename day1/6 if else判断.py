#!/usr/bin/python
#-*- coding:utf-8 –*-

#1、如果：女人的年龄>30岁，那么：叫阿姨
# age_of_girl=31
# if age_of_girl > 30:
#   print('阿姨好')

# 2、如果：女人的年龄>30岁，那么：叫阿姨，否则：叫小姐
# age_of_girl=18
# if age_of_girl > 30:
#   print('阿姨好')
# else:
#   print('小姐好')

# 3、如果：女人的年龄>=18并且<22岁并且身高>170并且体重<100并且是漂亮的，那么：表白，否则：看不上
# age_of_girl=18
# height=171
# weight=99
# is_pretty=True
# if age_of_girl >= 18 and age_of_girl < 22 and height >170 and weight < 100 and is_pretty == True:
#     print ('去表白')
# else:
#     print ('看不上')

# 4、if嵌套，在表白的基础上继续：如果表白成功，那么变白成功  否则：打印表白失败
# age_of_girl=18
# height=171
# weight=99
# is_pretty=True
# seccess=True
#
# if age_of_girl >= 18 and age_of_girl < 22 and height >170 and weight < 100 and is_pretty == True:
#     print ('去表白')
#     if seccess:
#         print ('表白成功')
#     else:
#         print ('表白失败')
# else:
#     print ('看不上')

# 5、如果：成绩>=90，那么：优秀
#    如果成绩>=80且<90,那么：良好
#    如果成绩>=70且<80,那么：普通
#    其他情况：很差
# grade = input('pleade input your grade >>: ')
# if grade >= 90:
#     print('优秀')
# elif grade >= 80:
#     print('良好')
# elif grade >= 70:
#     print ('普通')
# else:
#     print ('很差')

#6、验证登录
# name = raw_input('please input your name:')
# password = raw_input('please input your password:')
# if name == 'test':
#      if password == 'test':
#          print('login success！')
#      else:
#          print('password is error！')
# else:
#     print('name is error!')

#7、根据用户输入内容打印其权限
'''
root --> 超级管理员
test  --> 普通管理员
test1,test2 --> 业务主管
其他 --> 普通用户
'''
# name = raw_input('please input your name:')
# if name == 'root':
#     print('超级管理员')
# elif name == 'test':
#     print('普通管理员')
# elif name == 'test1' or name == 'test2':
#     print('业务主管')
# else:
#     print('普通用户')

#8、根据星期几决定做什么事情
'''
如果:今天是Monday,那么:上班
如果:今天是Tuesday,那么:上班
如果:今天是Wednesday,那么:上班
如果:今天是Thursday,那么:上班
如果:今天是Friday,那么:上班
如果:今天是Monday,那么:出去浪
如果:今天是Sunday,那么:出去浪
'''
# today = raw_input('please input today is : ')
# if today == 'Monday' or today == 'Tuesday' or today == 'Wednesday' or today == 'Thursday' or today == 'Friday':
#     print('上班')
# elif today == 'Saturday' or today == 'Sunday':
#     print ('出去浪')
# else:
#     print('请输入正确的星期几！！')