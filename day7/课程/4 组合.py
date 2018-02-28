#!/usr/bin/python
#-*- coding:utf-8 –*-

# 组合是什么有什么的关系
class OldboyPeople():
    school = 'oldboy'

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    def tell_info(self):
        print('<姓名：%s 年龄：%s 性别：%s>' % (self.name,self.age,self.sex))

class OldbotStudent(OldboyPeople):

    def learn(self):
        print('%s is learning' %self.name)

class OldboyTeacher(OldboyPeople):

    def teach(self):
        print('%s is teaching' %self.name)

class Brith_date():
    def __init__(self,year,mon,day):
        self.year=year
        self.mon=mon
        self.day=day
    def tell_birth(self):
        print('出生年月日是：%s-%s-%s' %(self.year,self.mon,self.day))


stud1=OldbotStudent('lqq',25,'female')
stud1.tell_info()
date_obj1=Brith_date(1992,10,25)
stud1.birth=date_obj1
stud1.birth.tell_birth()
