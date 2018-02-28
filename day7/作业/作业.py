#!/usr/bin/python
#-*- coding:utf-8 –*-
#!/usr/bin/python
#-*- coding:utf-8 –*-

# 站在老男孩学校的角度

# 角色:学校、学员、课程、讲师
# 要求:
# 1. 创建北京、上海 2 所学校
# 2. 创建linux , python , go 3个课程 ， linux\py 在北京开， go 在上海开
# 3. 课程包含，周期，价格，通过学校创建课程
# 4. 通过学校创建班级， 班级关联课程、讲师
# 5. 创建学员时，选择学校，关联班级
# 5. 创建讲师角色时要关联学校，
# 6. 提供两个角色接口
# 6.1 学员视图， 可以注册， 交学费， 选择班级，
# 6.2 讲师视图， 讲师可管理自己的班级， 上课时选择班级， 查看班级学员列表 ， 修改所管理的学员的成绩
# 6.3 管理视图，创建讲师， 创建班级，创建课程
# 7. 上面的操作产生的数据都通过pickle序列化保存到文件里
import json

# 学校：创建班级、课程、老师、学生
class School():
    def __init__(self,school_name):
        self.school_name = school_name

    def create_class(self):   #创建班级
        print('创建班级'.center(50,'*'))
        classroom_name=input('请输入班级名称：')
        classroom_period=input('请输入班级周期：')
        classroom_obj=Clsaaroom(classroom_name,classroom_period)  #班级实例化
        print('班级%s创建成功' %classroom_name)
        print('班级信息如下：')
        classroom_obj.show_classroom_info()
        # classroom[classroom_name]=classroom_obj #将班级名和班级实例关联起来
        classroom_dict={
            '班级名称': classroom_name,
            '班级周期':classroom_period
        }
        with open('班级信息.txt','a',encoding='utf-8') as f:
            f.write(json.dumps(classroom_dict))
        # control_view() # 从新调用选择功能函数

    def create_course(self):  #创建课程
        print('创建课程'.center(50, '*'))
        course_name=input('请输入课程名称：')
        course_period=input('请输入课程周期：')
        course_pay=input('请输入课程价格：')
        course_obj=Course(course_name,course_period,course_pay) #课程实例化
        print('课程%s创建成功' %course_name)
        print('课程信息如下：')
        course_obj.show_course_info()
        # course[course_name]=course_name # 将课程名和课程实例关联起来
        courses_dic={
            '课程名称':course_name,
            '课程周期':course_period,
            '课程价格':course_pay
        }
        with open('课程信息.txt','a',encoding='utf-8') as f:
            f.write(json.dumps(courses_dic))
        # control_view() # 从新调用选择功能函数

    def create_teacher(self):
        print('创建老师'.center(50,'*'))
        teacher_name=input('请输入老师的姓名：')
        teacher_age=input('请输入老师的年龄：')
        teacher_sex=input('请输入老师的性别：')
        teacher_course=input('请输入老师的课程：')
        teacher_school=input('请输入老师的学校：')
        teacher_class=input('请输入老师的班级：')
        teacher_obj=Teacher(teacher_name,teacher_age,teacher_sex,teacher_course,teacher_school,teacher_class)
        #老师实例化
        print('老师%s创建成功' %teacher_name)
        print('老师的信息如下：')
        teacher_obj.show_teacher_info()
        # teacher[teacher_name]=teacher_obj
        teachers_dic={
            '老师姓名':teacher_name,
            '老师年龄':teacher_age,
            '老师性别':teacher_sex,
            '老师课程':teacher_course,
            '老师学校':teacher_school,
            '老师班级':teacher_class
        }
        # with open('老师信息','a',encoding='utf-8') as f:
        #     f.write(json.dumps(teachers_dic))
        control_view() # 从新调用选择功能函数

    def creat_student(self):
        print('创建学生'.center(50,'*'))
        student_name = input('请输入学生的姓名：')
        student_age = input('请输入学生的年龄：')
        student_sex = input('请输入学生的性别：')
        student_id = input('请输入学生的学号：')
        student_course = input('请输入学生的课程：')
        student_school = input('请输入学生的学校：')
        student_class = input('请输入学生的班级：')
        student_obj = Student(student_name,student_age,student_sex,student_id,student_course,student_school,student_class)
        print('学生%s创建成功' % student_name)
        print('学生的信息如下：')
        student_obj.show_student_info()
        # student[student_name]=student_obj
        students_dic = {"学生姓名": student_name,
                         "学生年龄": student_age,
                         "学生性别": student_sex,
                         "学生学号": student_id,
                         "学生课程": student_course,
                         "学生学校":student_school,
                         "学生班级": student_class
                         }
        with open('学生信息.txt','a',encoding='utf-8') as f:
            f.write(json.dumps(students_dic))

# 班级：班级名和周期
class Clsaaroom():
    def __init__(self, classroom_name, classroom_period):
        self.classroom_name = classroom_name
        self.classroom_period = classroom_period

    def show_classroom_info(self):
        print('''
        ----------班级信息---------
        班级名称：%s
        班级周期：%s''' % (self.classroom_name, self.classroom_period))

# 课程：名称、周期和价格
class Course():
    def __init__(self,course_name,course_period,course_pay):
        self.course_name=course_name
        self.course_period=course_period
        self.course_pay=course_pay

    def show_course_info(self):
        print('''
        ----------课程信息---------
        课程名：%s
        课程周期：%s
        课程价格：%s ''' %(self.course_name,self.course_period,self.course_pay))


# 人：姓名、年龄、性别
class Person():
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex

# 老师：姓名、年龄、性别、课程、学校、班级
class Teacher(Person):
    def __init__(self,teacher_name,teacher_age,teacher_sex,teacher_course,teacher_school,teacher_class):
        super(Teacher,self).__init__(teacher_name,teacher_age,teacher_sex)
        self.teacher_course = teacher_course
        self.teacher_school = teacher_school
        self.teacher_class = teacher_class

    def show_teacher_info(self):
        print('''
        ----------老师信息---------
        姓名：%s
        年龄：%s
        性别：%s
        课程：%s
        学校：%s
        班级：%s
        ''' %(self.name,self.age,self.sex,self.teacher_course,self.teacher_school,self.teacher_class))

# 学生：姓名、年龄、性别、学号、课程、班级
class Student(Person):
    def __init__(self, student_name,student_age,student_sex,student_id,student_course,student_school,student_class):
        super(Student,self).__init__(student_name,student_age,student_sex)
        self.student_id = student_id
        self.student_course = student_course
        self.student_school = student_school
        self.student_class = student_class

    def show_student_info(self):
        print('''
        ----------学生信息---------
        姓名：%s
        年龄：%s
        性别：%s
        学号：%s
        课程：%s
        学校：%s
        班级：%s
        ''' %(self.name,self.age,self.sex,self.student_id,self.student_course,self.student_school,self.student_class))

# 学生视图：可以注册， 交学费， 选择班级
def Student_view():
    while True:
        print('欢迎进入学生视图'.center(50,'*'),
                '\n1.注册\n'
                '2.缴费\n'
                '3.选择班级\n'
                '4.返回\n'
                '5.退出\n')
        student_choice_id = input('选择要进入模式的id:')
        if student_choice_id == '1':
           schoolid.creat_student()
        elif student_choice_id =='2':
            print('该功能正在开发中……')
        elif student_choice_id =='3':
            print('该功能正在开发中……')
        elif student_choice_id =='4':
            break
        elif student_choice_id =='5':
            exit()
        else:
            print('输入的ID无效，请重新选择')

# 老师视图：可管理自己的班级，选择班级，查看班级学员列表，修改所管理的学员的成绩
def Teacher_view():
    while True:
        print('欢迎进入老师视图'.center(50,'*'),
                '\n1.选择班级\n'
                '2.查看班级学员\n'
                '3.修改班级学员成绩\n'
                '4.返回\n'
                '5.退出\n')
        teacher_choice_id = input('选择要进入模式的id:')
        if teacher_choice_id == '1':
            print('该功能正在开发中……')
        elif teacher_choice_id =='2':
            print('该功能正在开发中……')
        elif teacher_choice_id =='3':
            print('该功能正在开发中……')
        elif teacher_choice_id =='4':
            break
        elif teacher_choice_id =='5':
            exit()
        else:
            print('输入的ID无效，请重新选择')

# 管理视图，创建讲师， 创建班级，创建课程
def control_view():

    while True:
        print('欢迎进入管理视图'.center(50, '*'),
              '\n1.创建老师\n'
              '2.创建班级\n'
              '3.创建课程\n'
              '4.返回\n'
              '5.退出\n')
        control_choice_id = input('选择要进入模式的id:')
        if control_choice_id =='1':
            schoolid.create_teacher()
        elif control_choice_id =='2':
            schoolid.create_class()
        elif control_choice_id =='3':
            schoolid.create_course()
        elif control_choice_id =='4':
            break
        elif control_choice_id =='5':
            exit()
        else:
            print('输入的ID无效，请重新选择')

# 选择学校
def select_school():
    global schoolid
    print('欢迎进入老男孩选课系统,请先选择学校:'
            '\n1.北京\n'
            '2.上海\n'
            '3.退出\n')
    choice_school_id = input('选择要进入模式的id:')
    if choice_school_id == '1':
        schoolid = school1
    elif choice_school_id == '2':
        schoolid = school2
    elif choice_school_id == '3':
        exit()
    else:
        print('输入的ID无效，请重新选择')

def select_fun():
    while True:
        print('欢迎进入老男孩选课系统'.center(50, '='),
              '\n1.管理视图\n'
              '2.学生视图\n'
              '3.老师视图\n'
              '4.返回\n'
              '5.退出\n')
        select_choice_id = input('选择要进入模式的id:')
        if select_choice_id == '1':
            control_view()
        elif select_choice_id == '2':
            Student_view()
        elif select_choice_id == '3':
            Teacher_view()
        elif select_choice_id == '4':
            break
        elif select_choice_id == '5':
            exit()
        else:
            print('输入的ID无效，请重新选择')

def main():
    while True:
        select_school()
        while True:
            select_fun()

if __name__ == '__main__':
    classrooms = {}
    courses = {}
    teachers = {}
    students = {}
    school1 = School("北京")
    school2 = School("上海")
    main()
