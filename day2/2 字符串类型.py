#!/usr/bin/python
#-*- coding:utf-8 –*-
#一、字符串
#1、用途：姓名，性别，住址等描述性的数据
#2、定义方式：‘’ ，“”，''' '''内定义的一串字符
# str='hello world'


#3、优先掌握的操作：
#1、按索引取值(正向取+反向取) ：只能取
# print(str[0],type(str[0]))
# print(str[-1])

#2、切片(顾头不顾尾，步长)
# print(str[0:6])
# print(str[0:6:2])
# print(str[5:0:-1])

#3、长度len
# print(str.__len__())
# print(len(str)) #str.__len__()

#4、成员运算in和not in
# print('hello' in str)
# print('hello' not in str)

#5、移除空白strip
# password='  liqiongqiong    '
# print(password.strip())
#日常用法 password=input('>>: ').strip()

#6、切分split
# dir='/root/bin/bash'
# res=dir.split('/')
# print(res)

#默认是空格符做切割符号，不指定切割次数的话，默认整个字符串都会切完
# cmd='get /root/a/b/c/d.txt'
# print(cmd.split())
#
# file_path='C:\\a\\d.txt'
# print(file_path.split('\\',1))
#
# file_path='C:\\a\\d.txt'
# print(file_path.rsplit('\\',1)) #rsplit是按照倒序的方式切割

#7、循环（逐个取出字符串中的字符）
# str = 'hello world'
# n = 0
# while n<len(str):
#     print(str[n])
#     n+=1
#
# for n in str:
#     print(n)
#
# for n in range(len(str)):
#     print(n)


#二：该类型总结
# 1 存一个值or存多个值
#     只能存一个值
# 2 有序
# 3 可变or不可变
#     ！！！不可变：值变，id就变。不可变==可hash

#需要掌握的
#1、strip,lstrip,rstrip
# strip默认是移除空白，非空格的需要指定；lstrip是移除左边的；rstrip是移除右边的；
# print("**alex****".strip('*'))
# print("**alex****".lstrip('*'))
# print("**alex****".rstrip('*'))

#2、lower,upper
#lower是把字符串中的大写字母转换成小写，upper是小写换成大写
# print('ALeX'.lower())
# print('aaa'.upper())

#3、startswith,endswith
#判断字符串是否是以什么开头或者结尾，结果是布尔值
# msg='alex is SB'
# print(msg.startswith('alex'))
# print(msg.startswith('a'))
# print(msg.endswith('SB'))

#4、format的三种玩法
#占位符是{}
# print('my name is %s my age is %s' %('alex',18))
# print('this is {} this is a {}'.format('test','pen'))
# print('my name is {} my age is {}'.format('alex',18))
# print('my name is {} my age is {}'.format(18,'alex'))
# print('{0} {1} {0}'.format('alex',18))
# print('my name is {name} my age is {age}'.format(age=18,name='male'))

#5、split,rsplit
# info='root:x:0:0'
# l=info.split(':')
# print(l)

#6、join
# info='root:x:0:0'
# l=info.split(':')
# print(l)
# print(':'.join(l))

#l=[1,2,3]
# ' '.join(l)
#报错：只有在列表内的元素全是字符串类型，才能用join拼接

#7、replace
# msg='alex say my name is alex ,alex have on tesla'
# msg=msg.replace('alex','SB',1)
# print(msg)

#8、isdigit
# age=raw_input('>>: ').strip()
# print(age.isdigit()) #age='123'
# if age.isdigit():
#     age=int(age)
# else:
#     print('必须输入数字')


#了解
#1、find,rfind,index,rindex,count
#2、center,ljust,rjust,zfill
#3、expandtabs
#4、captalize,swapcase,title
#5、is数字系列
#6、is其他





#
# 三、练习　　　
#
# 写代码,有如下变量,请按照要求实现每个功能
# 1)    移除 name 变量对应的值两边的空格,并输出处理结果
# name = " aleX"
# res = name.strip()
# print(res)
# 2)    判断 name 变量对应的值是否以 "al" 开头,并输出结果
# print(name.startswith('al'))
# 3)    判断 name 变量对应的值是否以 "X" 结尾,并输出结果 
# print(name.endswith('X'))
# 4)    将 name 变量对应的值中的 “l” 替换为 “p”,并输出结果
# print(name.replace('l','p'))
# 5)    将 name 变量对应的值根据 “l” 分割,并输出结果。
# print(name.split('l'))
# 6)    将 name 变量对应的值变大写,并输出结果 
# print(name.upper())
# 7)    将 name 变量对应的值变小写,并输出结果 
# print(name.lower())
# 8)    请输出 name 变量对应的值的第 2 个字符?
# print(name[1])
# 9)    请输出 name 变量对应的值的前 3 个字符?
# print(name[:3])
# 10)    请输出 name 变量对应的值的后 2 个字符? 
# print(name[-2:])
# 11)    请输出 name 变量对应的值中 “e” 所在索引位置? 
# print(name.index('e'))
# 12)    获取子序列,去掉最后一个字符。如: oldboy 则获取 oldbo。
# print(name[:-1])
