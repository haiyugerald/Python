#!/usr/bin/python
#-*- coding:utf-8 –*-
'''
站在老男孩学校的角度
现实中的对象：
    对象1：
        特征
            学校=老男孩
            名字=egon
            性别=男
            年龄=18
        技能
            教学
            备课
    对象2：
        特征
            学校=老男孩
            名字=alex
            性别=男
            年龄=28
        技能
            教学
            备课
    对象3：
        特征
            学校=老男孩
            名字=june
            性别=女
            年龄=28
        技能
            教学
            备课

现实中的老男孩教师类：
        相似的特征
            学校=老男孩
        相似的技能
            教学
'''
class Teacher():

    def __init__(self,name,age,sex,salary):  #定制独有的特征
        self.Name = name
        self.Age = age
        self.Sex = sex
        self.Salary = salary
        # Teacher+=1

    def teach(self):
        print('%s is teaching' % self)

    def beike(self):
        print('%s is beikeing' % self)

print(Teacher)
print(Teacher.__dict__)

teacher1=Teacher('egon','18','男','50000')
teacher2=Teacher('alex','28','男','60000')
teacher3=Teacher('june','28','女','35000')

print(teacher1.Name)