#!/usr/bin/python
#-*- coding:utf-8 –*-
'''
2 FTP：编写登陆接口
基础需求：
    让用户输入用户名密码
    认证成功后显示欢迎信息
    输错三次后退出程序
升级需求：
    可以支持多个用户登录(提示，通过列表存多个账户信息)
    用户3次认证失败后，退出程序，再次启动程序尝试登录时，还是锁定状态（提示:需把用户锁定的状态存到文件里)
'''
#=========================================================================
count = 0

while count < 3:
    name = raw_input('请输入你的账号：')
    password = raw_input('请输入你的密码：')
    if name == 'test' and password == 'test':
        print('恭喜你!登录成功')
        break
    else:
        print('账号或者密码有误!')
        count += 1
#==========================================================================
dic = {
    'test1':{'password':'test1','count':0},
    'test2':{'password':'test2','count':0},
    'test3':{'password':'test3','count':0}
}
count = 0
while True:
    name = raw_input('请输入你的账号：')
    if name not in dic:
        print ('没有该用户！')
        continue
    if dic[name]['count'] > 2:
        print('错误次数已达上限！')
        continue

    password = raw_input('请输入你的密码：')
    if password == dic[name]['password']:
        print('恭喜你!登录成功')
        break
    else:
        print('用户名或者密码错误')
        dic[name]['count'] += 1
#==========================================================================
dic={
    'egon1':{'password':'123','count':0},
    'egon2':{'password':'123','count':0},
    'egon3':{'password':'123','count':0},
}

count=0
while True:
    name=input('u>>: ')
    if name not in dic:
        print('用户不存在')
        continue

    with open('db.txt','r') as f:
        lock_users=f.read().split('|')
        if name  in lock_users:
            print('用户%s已经被锁定' %name)
            break

    if dic[name]['count'] > 2:
        print('尝试次数过多,锁定')
        with open('db.txt','a') as f:
            f.write('%s|' %name)
        break

    password=input('p>>: ')

    if password == dic[name]:
        print('登录成功')
        break
    else:
        print('用户名或密码错误')
        dic[name]['count']+=1


