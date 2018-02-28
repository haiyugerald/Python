#!/usr/bin/python
#-*- coding:utf-8 –*-
# 三个任务
# 1、接收用户输入
# 2、将用户输入的内容格式化成大写
# 3、将格式化后的结果存入文件

from threading import Thread
msg_l=[]
format_l=[]
def talk():
    while True:
        msg=input('==>').strip()
        if not msg:continue
        msg_l.append(msg)

def format_msg():
    while True:
        if msg_l:
            # pop是从一个列表删除并拿到结果:取走一个值
            res=msg_l.pop()
            format_l.append(res.upper())

def save():
    while True:
        if format_l:
            with open('db.txt','a',encoding='utf-8') as f:
                res=format_l.pop()
                f.write('%s\n' %res)

t1=Thread(target=talk)
t2=Thread(target=format_msg)
t3=Thread(target=save)
t1.start()
t2.start()
t3.start()
