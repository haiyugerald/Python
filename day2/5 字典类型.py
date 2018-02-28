#!/usr/bin/python
#-*- coding:utf-8 –*-

#一、作用：存放多个值，key:value,存取速度快

#二、定义：key必须是不可变类型（int，float，str，tuple），value可以是任意类型
# 变量=dict(name='egon',age=18,)
#info={'name':'egon','age':18,'sex':'male'} #info=dict({'name':'egon','age':18,'sex':'male'})

#了解
# info=dict(age=18,sex='male',name='egon')
# print(info)

# info=dict([('name','egon'),('age',18),('sex','male')])
# info=dict([['name','egon'],['age',18],['sex','male']])
# print(info)

# info={}.fromkeys(['name','age','sex'],None)
# info={}.fromkeys('hello',None)
# print(info)

#三、常用操作+内置方法
#优先掌握的操作：
#1、按key存取值：可存可取
# d={'a':1,'b':2}
# print(d['a'])
#
# d['a']=3
# print(d)

#2、长度len
# print(len(d))

#3、成员运算in和not in
# print('a' in d)

#4、删除
# print(d.pop('a')) #输出的是删除的key对应的value值
# print(d)

# print(d.popitem()) #输出的是删除的key对应的key:value键值对
# print(d)

#5、键keys()，值values()，键值对items() #了解
# print(d.keys())
# print(list(d.keys())[0])
#
# print(list(d.values()))
# print(list(d.items()))

#6、循环
# info={'name':'egon','age':18,'sex':'male'}
# for k in info:
#     print(k,info[k])

# 四、练习
# 1 有如下值集合 [11,22,33,44,55,66,77,88,99,90...]，将所有大于 66 的值保存至字典的第一个key中，将小于 66 的值保存至第二个key的值中
# 即： {'k1': 大于66的所有值, 'k2': 小于66的所有值}
# dict = {'k1':[],'k2':[]}
# list = [11,22,33,44,55,66,77,88,99,90]
# for i in list:
#     if i > 66:
#         dict['k1'].append(i)
#     if i < 66:
#         dict['k2'].append(i)
# print(dict)
#
# 2 统计s='hello alex alex say hello sb sb'中每个单词的个数
# 结果如：{'hello': 2, 'alex': 2, 'say': 1, 'sb': 2}
# s='hello alex alex say hello sb sb'
# words = s.split()
# print(words)
# dic={}
# for i in words:
#     if i in dic:
#         dic[i]+=1
#     else:
#         dic[i]=1
# print(dic)

