#!/usr/bin/python
#-*- coding:utf-8 –*-
#一、元组列表
#作用：存多个值，对比列表来说，元组不可变（是可以当做字典的key的），主要是用来读
#定义：与列表类型比，只不过[]换成()
# 变量名=tuple(字符串)
# age=tuple('hello')
# print(age,type(age))

# t=(1,2,['a','b'])
# print(id(t[2]))
# t[2][0]='A'
# print(id(t[2]))
# print(t)

#二、优先掌握的操作：
#1、按索引取值(正向取+反向取)：只能取
# age=tuple('hello')
# print(age[0])
#2、切片(顾头不顾尾，步长)
# print(age[0:3])
# print(age)
#3、长度
# print(len(age))
#4、成员运算in和not in
# print('o' in age)
# 5、循环
# for item in age:
#     print(item)

#三、掌握
#1、index
# print(age.index('o'))
#2、count
# print(age.count('l'))

#四：该类型总结
# 1 可以存多个值，值都可以是任意类型
# 2 有序
# 3 ！！！不可变：值变，id就变。不可变==可hash

#五、练习
# 简单购物车,要求如下：
# 实现打印商品详细信息，用户输入商品名和购买个数，则将商品名，价格，购买个数加入购物列表，如果输入为空或其他非法输入则要求用户重新输入
msg_dic={
'apple':10,
'tesla':100000,
'mac':3000,
'lenovo':30000,
'chicken':10,
}
order = []
while True:
    for i in msg_dic:
        print(i,msg_dic[i])
    goods=raw_input("商品==>>:").strip()
    if goods not in msg_dic or len(goods) == 0:
       print("输入有误！！！")
       continue
    number=raw_input("个数==>>:").strip()
    if not number.isdigit:
        print("输入有误！！！")
        continue
    order.append((goods,msg_dic[goods],int(number)))
    print(order)
    print("=====>>end")
    break
