#!/usr/bin/python
#-*- coding:utf-8 –*-
"""
1 练习题
1、简述编译型与解释型语言的区别，且分别列出你知道的哪些语言属于编译型，哪些属于解释型
    编译型（C、C++、Pascal/Object Pascal（Delphi））：相当于百度翻译，对程序翻译一次，拿着该翻译的结果去执行。
            优点：执行效率高
            缺点：开发效率低
    解释型（Python、JavaScript、Perl、Ruby）：相当于同声传译，可以一边解释一边执行。
            优点：开发效率高
            缺点：执行效率低

2、执行 Python 脚本的两种方式是什么
    使用python解释器(python test.py)或在系统下赋值成777，执行（./test.py）
3、Pyhton 单行注释和多行注释分别用什么?
    单行注释用#，多行注释可以用三对双引号""" """
4、布尔值分别有什么?
    True False
5、声明变量注意事项有那些?
    1)变量名只能是 字母、数字或下划线的任意组合
    2)变量名的第一个字符不能是数字
    3)关键字不能声明为变量名
6、如何查看变量在内存中的地址?
    id(变量)
7、写代码
    1 实现用户输入用户名和密码,当用户名为 seven 且 密码为 123 时,显示登陆成功,否则登陆失败!
        name = raw_input('please input your name:')
        password = raw_input('please input your password:')
        if name == 'seven' and password == '123':
            print('login success！')
        else:
            print('login faile!')
    2 实现用户输入用户名和密码,当用户名为 seven 且 密码为 123 时,显示登陆成功,否则登陆失败,失败时允许重复输入三次
        count = 0
        while count < 3:
            name = raw_input('please input your name:')
            password = raw_input('please input your password:')
            if name == 'seven' and password == '123':
                print('login success！')
                break
            else:
                count += 1    
    3 实现用户输入用户名和密码,当用户名为 seven 或 alex 且 密码为 123 时,显示登陆成功,否则登陆失败,失败时允许重复输入三次
        count = 0
        while count < 3:
            name = raw_input('please input your name:')
            password = raw_input('please input your password:')
            if ((name == 'seven' or name == 'alex') and password == '123'):
                print('login success！')
                break
            else:
                count += 1
8、写代码
    a. 使用while循环实现输出2-3+4-5+6...+100 的和
        number = 2
        sum = 0
        while number < 100:
            if number%2 == 1:
                sum += number
            else:
                sum -= number
            number += 1
        print(sum)
    b. 使用 while 循环实现输出 1,2,3,4,5, 7,8,9, 11,12 
        number = 0
        while number < 12:
            number += 1
            if number == 6 or number == 10:
                continue
            else:
                print(number)
    c.使用 while 循环实现输出 1-100 内的所有奇数
        number = 1
        sum = 0
        while number <= 100:
            if number%2 == 1:
                sum += number
            number += 1
        print(sum)
    d. 使用 while 循环实现输出 1-100 内的所有偶数
        number = 1
        sum = 0
        while number <= 100:
            if number%2 == 0:
                sum += number
            number += 1
        print(sum)
9、现有如下两个变量,请简述 n1 和 n2 是什么关系?
      n1 = 123456
      n2 = n1
      n1和n2指向同一块内存地址，数值是123456
        
"""
'''


