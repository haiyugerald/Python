#!/usr/bin/python
#-*- coding:utf-8 –*-


# pythons=['egon','axx','ysb','wxx']
# linuxs=['egon','oldboy','oldgirl','smallboy','smallgirl']
#
# python_linux=[]
#
# for student in pythons:
#     if student in linuxs:
#         python_linux.append(student)
#
# print(python_linux)

#一、作用：关系运算，去重
#二、定义集合：{}内用逗号分割每个元素都必须是不可变类型,元素不能重复,无序
# s={1,'a',[1,2]} #TypeError: unhashable type: 'list'
# s={1,2,3,1} #s=set({1,2,3,1})
# print(s,type(s))


#三、优先掌握的操作：
#1、长度len
# s=set({'a','b','c','d'})
# print(s,type(s))
# print(len(s))

#2、成员运算in和not in
# print('a' in s)
# print('a' not in s)

#3、&交集:同时报名两门课程的学生
# pythons={'egon','axx','ysb','wxx'}
# linuxs={'egon','oldboy','oldgirl','smallboy','smallgirl'}
# print(pythons,type(pythons))
# print(pythons & linuxs)
# print(pythons.intersection(linuxs))

#4、|合集:老男孩所有的学生
# print(pythons | linuxs)
# print(pythons.union(linuxs))

#5、^对称差集:没有同时报名两门课程
# print(pythons ^ linuxs)
# print(pythons.symmetric_difference(linuxs))

#6.1  -差集：只报名python课程的学生
# print(pythons - linuxs)
# print(pythons.difference(linuxs))

#6.2  -差集：只报名linux课程的学生
# print(linuxs-pythons)

#7 父集:>,>=,子集：<，<=
# s1={1,2,3}
# s2={1,2,}
# print(s1 >= s2)
# print(s1.issuperset(s2))
# print(s2.issubset(s1))

#8 循环
# linuxs={'egon','oldboy','oldgirl','smallboy','smallgirl'}
# for student in linuxs:
#     print(student)

#四、了解的知识点
#1 difference_update
# s1={1,2,3}
# s2={1,2,}
# print(s1-s2)  #s1与s2的差集
# print(s1.difference(s2))
# s1.difference_update(s2) #s1=s1.difference(s2)
# print(s1)

#2 pop
#s2={1,2,3,4,5,'a'}
# print(s2.pop())
# print(s2)

#3 add
# s2.add('b')
# print(s2)

#4 删除
# s2.discard('c')#删除的元素不存在不会报错
# s2.remove('b') #删除的元素不存在则报错
# print(s2)

#5 判断两个集合是否有共同的部分
# s1={1,2,3,4,5,'a'}
# s2={'b','c',}
# print(s1.isdisjoint(s2)) #两个集合没有共同部分时，返回值为True

#6 update
# s2={1,2,3,4,5,'a'}
# s2.update({6,7,8})
# print(s2)

#7 集合中元素的唯一性
# l=['a','b',1,'a','a']
# print(list(set(l)))

# print(set('hello'))
# print(set({'a':1,'b':2,'c':3}))

# s1=set('hello')
# print(s1,type(s1),id(s1))
# s1=set('helle')
# print(s1[0],type(s1),id(s1))

# 五、练习
# 一.关系运算
# 有如下两个集合，pythons是报名python课程的学员名字集合，linuxs是报名linux课程的学员名字集合
# pythons={'alex','egon','yuanhao','wupeiqi','gangdan','biubiu'}
# linuxs={'wupeiqi','oldboy','gangdan'}
# 1. 求出即报名python又报名linux课程的学员名字集合
# print(pythons & linuxs)
# 2. 求出所有报名的学生名字集合
# print(pythons | linuxs)
# 3. 求出只报名python课程的学员名字
# print(pythons - linuxs)
# 4. 求出没有同时这两门课程的学员名字集合
# print(pythons ^ linuxs)

# 二.去重
# 1.有列表l=['a','b',1,'a','a']，列表元素均为可hash类型，去重，得到新列表,且新列表无需保持列表原来的顺序
l=['a','b',1,'a','a']
s=set(l)
print(s)
# 2.在上题的基础上，保存列表原来的顺序
l2=[]
for i in l:
    if i not in l2:
        l2.append(i)
print(l2)

# 3.去除文件中重复的行，肯定要保持文件内容的顺序不变
import os
f =
# 4.有如下列表，列表元素为不可hash类型，去重，得到新列表，且新列表一定要保持列表原来的顺序
l=[
    {'name':'egon','age':18,'sex':'male'},
    {'name':'alex','age':73,'sex':'male'},
    {'name':'egon','age':20,'sex':'female'},
    {'name':'egon','age':18,'sex':'male'},
    {'name':'egon','age':18,'sex':'male'},
]