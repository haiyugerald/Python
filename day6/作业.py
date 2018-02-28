#!/usr/bin/python
#-*- coding:utf-8 –*-
# 角色:学校、学员、课程、讲师
# 站在老男孩学校的角度
'''
1、现实中的老男孩学校类：
    老男孩学校类
        相似的特征
            名称=老男孩
        相似的技能
            创建课程
            创建班级
            创建讲师
学校：
    对象1：
        特征
            名称=老男孩
            地址=北京
        技能
            创建课程
            创建班级
            创建讲师
    对象2：
        特征
            名称=老男孩
            地址=上海
        技能
            创建课程
            创建班级
            创建讲师
'''
class School():
    def __init__(self,school_name,school_addr):
        self.school_name = school_name
        self.school_addr = school_addr

    def create_class(self):
        pass

    def create_course(self):
        pass

    def create_teacher(self):
        pass

'''
2、现实中的老男孩学员类：
    老男孩学员类
        相似的特征
            学校=老男孩
        相似的技能
            选择学校
            选择班级
学员：
    对象1：
        特征
            学校=老男孩
            名字=张三
            性别=男
            年龄=18
            课程=linux
        技能
            选择学校
            选择班级
    对象2：
        特征
            学校=老男孩
            名字=李四
            性别=女
            年龄=28
            课程=go
        技能
            选择学校
            选择班级
'''
class Student():
    def __init__(self, student_name,student_age,student_sex,student_course):
        self.student_name = student_name
        self.student_age = student_age
        self.student_sex = student_sex
        self.student_course = student_course

    def choice_school(self):
        pass

    def choice_cousre(self):
        pass
'''
3、现实中的老男孩课程类：
    老男孩课程类
        相似的特征
            学校=老男孩
        相似的技能
课程：
    对象1：
        特征
            学校=老男孩
            课程名=python
            课时=23
            价格=10000
        技能

    对象2：
        特征
            学校=老男孩
            课程名=go
            课时=20
            价格=9000
        技能

    对象3：
        特征
            学校=老男孩
            课程名=linux
            课时=25
            价格=12000
        技能
'''
class Course():
    def __init__(self,course_name, course_time, course_pay):
        self.course_name = course_name
        self.course_time = course_time
        self.course_pay = course_pay

'''
4、现实中的老男孩讲师类：
    老男孩课程类
        相似的特征
            学校=老男孩
        相似的技能
            管理自己的班级
            上课时选择班级
            查看班级学员列表
            修改所管理的学员的成绩
讲师：
    对象1：
        特征
            学校=老男孩
            名字=egon
            性别=男
            年龄=18
        技能
            管理自己的班级
            上课时选择班级
            查看班级学员列表
            修改所管理的学员的成绩

    对象2：
        特征
            学校=老男孩
            名字=alex
            性别=男
            年龄=28
        技能
            管理自己的班级
            上课时选择班级
            查看班级学员列表
            修改所管理的学员的成绩
'''
class Teacher():
    def __init__(self, teacher_name, teacher_age, teacher_sex, teacher_course, teacher_school, teacher_classroom):
        self.teacher_name = teacher_name
        self.teatch_age = teacher_age
        self.teacher_sex = teacher_sex
        self.teacher_course = teacher_course
        self.teacher_school = teacher_school
        self.teacher_classroom = teacher_classroom

    def manager_class(self):
        pass
    def choice_class(self):
        pass
    def view_studentlist(self):
        pass
    def change_grade(self):
        pass
