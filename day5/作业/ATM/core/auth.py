#!/usr/bin/python
#-*- coding:utf-8 –*-

import os,json
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
User_DB=os.path.join(BASE_DIR,'db','user')


# 临时的账号数据，只在内存中保留
user_data = {
    'account_id':None,
    'is_authenticated':False,
    'account_data':None
}

# 当程序启动时，这个函数将被调用
def run():
    acc_data = auth.acc_login(user_data,access_logger)  #调用账户登录函数
    if user_data['is_authenticated']:
        user_data['account_data'] = acc_data
        interactive(user_data)  #调用交互页面


# 账户登录函数
def acc_login(user_data,log_obj):
    retry_count = 0
    while user_data['is_authenticated'] is not True and retry_count < 3 :
        account = input("请输入你的账号:").strip()
        password = input("请输入你的密码:").strip()
        auth = acc_auth(account, password)   #调用优化版认证接口
        if auth:
            user_data['is_authenticated'] = True
            user_data['account_id'] = account
            return auth
        retry_count +=1
    else:
        log_obj.error("account [%s] too many login attempts" % account)
        exit()

# 账户认证接口
def acc_auth(account,password):
    db_api = db_handler.db_handler()
    data = db_api("select * from accounts where account=%s" % account)

    if data['password'] == password:
        return data
    else:
        print("\033[31;1mAccount ID or password is incorrect!\033[0m")