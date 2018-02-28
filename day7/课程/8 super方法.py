#!/usr/bin/python
#-*- coding:utf-8 –*-
#
# class Foo:
#     def f2(self):
#         print('====?>')
#
#     def f1(self):
#         print('Foo.f1')
#         # super().f2()
#         Foo.f2(123)
# class Bar:
#     def f2(self):
#         print('Bar f2')
#
# class Sub(Foo,Bar):
#     pass
#
# s=Sub()
# # print(Sub.mro())
# # [<class '__main__.Sub'>,
# # <class '__main__.Foo'>,
# # <class '__main__.Bar'>,
# #  <class 'object'>]
#
# s.f1()


class OldboyPeople:
    school = 'Oldboy'

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def tell_info(self):
        print('<名字:%s 年龄:%s 性别:%s>' %(self.name,self.age,self.sex))

class OldboyStudent(OldboyPeople):
    def __init__(self,stu_name,stu_age,stu_sex,stu_course):
        # OldboyPeople.__init__(self,name,age,sex)
        super(OldboyStudent,self).__init__(stu_name,stu_age,stu_sex)
        self.course=stu_course

    def tell_info(self):
        print('我是学生: ',end='')
        # OldboyPeople.tell_info(self)
        super(OldboyStudent,self).tell_info()


stu1=OldboyStudent('egon',18,'male','python')

# print(stu1.name,stu1.age,stu1.sex,stu1.course)
stu1.tell_info()