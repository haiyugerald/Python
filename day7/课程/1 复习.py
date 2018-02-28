#!/usr/bin/python
#-*- coding:utf-8 –*-
import json


teachers_dic={
            '老师姓名':'egon',
            '老师年龄':18,
            '老师性别':'male',
        }

with open('老师信息', 'a', encoding='utf-8') as f:
    f.write(json.dumps(teachers_dic))
