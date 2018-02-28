#!/usr/bin/python
#-*- coding:utf-8 –*-
import random
print(random.random()) #(0,1)----float    大于0且小于1之间的小数
print(random.randint(1,3)) #[1,3]    大于等于1且小于等于3之间的整数
print(random.randrange(1,3)) #[1,3)    大于等于1且小于3之间的整数
print(random.choice([1,'23',[4,5]]))#1或者23或者[4,5]
print(random.sample([1,'23',[4,5]],2)) #列表元素任意2个组合
print(random.uniform(1,3)) #大于1小于3的小数，如1.927109612082716





# 练习写验证码模块
import random
def make_code(n):
    res=''
    for i in range(n):
        s1=str(random.randint(0,9))    #随机取到的是一个数字，为了后面方便拼接 转华为字符串
        s2=chr(random.randint(65,90)) #取到的数字刚好对应的是ASCII表中的大写字母
        res+=random.choice([s1,s2])
    return res

print(make_code(6))
