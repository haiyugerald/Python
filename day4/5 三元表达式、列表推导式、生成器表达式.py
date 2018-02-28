#!/usr/bin/python
#-*- coding:utf-8 –*-

# 1、三元表达式
# def my_max(x,y):
#     if x>y:
#         return x
#     else:
#         return y
# res=my_max(10,12)
# print(res)
#
#
# x=10
# y=12
# res=x if x>y else y
# print(res)

# 2、列表推导式
# l=[]
# for i in range(1,11):
#     res='egg'+str(i)
#     l.append(res)
# print(l)
#
# l=['egg'+str(i) for i in range(1,11) ]
# print(l)
#
# l=['egg'+str(i) for i in range(1,11) if i>5]
# print(l)

# 3、生成器表达式  可以存放无穷多个值
# g=('egg'+str(i) for i in range(1,11) )
# print(g)
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

# 4、声明式编程练习题
# 1将names=['egon','alex_sb','wupeiqi','yuanhao']中的名字全部变大写
# names=['egon','alex_sb','wupeiqi','yuanhao']
# names=[name.upper() for name in names]
# print(names)
# 2将names=['egon','alex_sb','wupeiqi','yuanhao']中以sb结尾的名字过滤掉，然后保存剩下的名字长度
# names=['egon','alex_sb','wupeiqi','yuanhao']
# names=[name for name in names if name.endswith('sb') ]
# print(names)
# 3求文件a.txt中最长的行的长度（长度按字符个数算，需要使用max函数）
# with open('a.txt','r',encoding='utf-8') as f:
#     print(max(len(line) for line in f))
# 4求文件a.txt中总共包含的字符个数？思考为何在第一次之后的n次sum求和得到的结果为0？（需要使用sum函数）
# with open('a.txt', 'r', encoding='utf-8') as f:
#     print(sum(len(line) for line in f))
#
#     print(sum(len(line) for line in f))  #求包换换行符在内的文件所有的字符数，为何得到的值为0?
# 5、思考题
# with open('a.txt') as f:
#     g=(len(line) for line in f)
# print(sum(g)) #为何报错？
#
#
# 6、文件shopping.txt内容如下
# mac,20000,3
# lenovo,3000,10
# tesla,1000000,10
# chicken,200,1
# 求总共花了多少钱？
# 打印出所有商品的信息，格式为[{'name':'xxx','price':333,'count':3},...]
# 求单价大于10000的商品信息,格式同上
