#!/usr/bin/python
#-*- coding:utf-8 –*-
#spam.py

print('from the spam.py')

money=1000

def read1():
    print('spam模块：',money)

def read2():
    print('spam模块')
    read1()

def change():
    global money
    money=0

print(__name__)
if __name__ == '__main__':
    read1()
    read2()
    change()
    print('调试功能')