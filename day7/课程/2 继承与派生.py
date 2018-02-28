#!/usr/bin/python
#-*- coding:utf-8 –*-

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

stu1=OldbotStudent('lqq',25,'female')
stu1.learn()
print(stu1.name)
stu1.tell_info()

tea1=OldboyTeacher('egon',28,'male')
tea1.teach()
print(tea1.name)



#找的顺序是：先对象，再子类，最后再父类
# 继承是什么是什么的关系