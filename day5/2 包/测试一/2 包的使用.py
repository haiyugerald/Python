#!/usr/bin/python
#-*- coding:utf-8 –*-


import  sys
# print(sys.path)
# sys.path.append('/Users/liqiongqiong/PycharmProjects/oldboy/day5/2 包/package1')
print(sys.path)
#
#
# from  package1  import m1
# print(m1.fun1)

# from package1 import package2  错误的导入

import package1

package1.package2.m2.func2()