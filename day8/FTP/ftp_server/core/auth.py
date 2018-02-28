#!/usr/bin/python
#-*- coding:utf-8 –*-
import os,sys
import hashlib

# 程序主目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 添加环境变量
sys.path.append(BASE_DIR)
from conf import setting

def create_user():
    path = setting.PATH
    for key in setting.USER_DATA:
        print(setting.USER_DATA)
        user_parh = '%s/data/%s.json' %(path,key)
        if not os.path.isfile(user_parh):
            password_hash=hash(setting.USER_DATA[key])
            user_data ={
                'uasename':key,
                'password':password_hash,
                'user_path':os.path.join(setting.HOME_PATH,key)
                'max_size':setting.MAX_SIZE
            }
            # json.dump(user_data, open(user_path,"w",encoding="utf-8"))
            db_handle.user_dump(user_path, user_data)
    user_mkdir()

def user_mkdir():
    """创建用户个人目录，在home目录下"""
    for key in setting.USER_DATA:
        user_home_path = os.path.join(setting.HOME_PATH, key)
        if not os.path.isdir(user_home_path):
            os.popen("mkdir %s" % user_home_path)

def hash(data):
    m = hashlib.md5()
    m.update(data.encode())
    # 返回加密后的数据
    return m.hexdigest()