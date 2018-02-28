
#!/usr/bin/python
#-*- coding:utf-8 –*-

import json

# data={'test':{'password': 'abc','locked': 0}}
# print(json.dumps(data))

# data={'888888':'123','666666':'123'}
# print(json.dumps(data))
# data1={"test": {"password": "abc", "locked": 0}}

# data={"888888": "123", "666666": "123"}
# print(json.load(data))


# def wrapper():
#     # res = func()
#     res = ''
#     username = input("\33[34;0m请输入用户名：\33[0m")
#     password = input("\33[34;0m请输入密码：\33[0m")
#     if len(username.strip()) > 0:
#         with open('a', "r+") as f_users_dict:
#             users_dict = json.loads(f_users_dict.read())
#             print(users_dict)
#             # jsom.load:解码(把Json格式字符串解码转换成Python对象)
#             if username in users_dict.keys():
#                 if password == users_dict[username]["password"]:
#                     if users_dict[username]["locked"] == 0:
#                         print("\33[31;0m用户 %s 认证成功\33[0m" % (username))
#                         return res, username
#                     else:
#                         print("\33[31;0m用户 %s 已经被锁定 认证失败\33[0m" % (username))
#                 else:
#                     print("\33[31;0m输入的密码不匹配 认证失败\33[0m")
#             else:
#                 print("\33[31;0m输入的用户名不存在 认证失败\33[0m")
#     else:
#         print("\33[31;0m输入的用户名为空 认证失败\33[0m")
#
# wrapper()

# users_dict={'test': {'password': 'abc', 'locked': 0}}
# print(users_dict.keys())



def wrapper():
    # res = func()
    res = ''
    creditcard = input("\33[34;0m输入信用卡卡号(6位数字)：\33[0m")
    password = input("\33[34;0m输入信用卡的密码：\33[0m")
    if len(creditcard.strip()) > 0:
        with open('b', "r+") as f_creditcard_dict:
            creditcard_dict = json.loads(f_creditcard_dict.read())
            if creditcard in creditcard_dict.keys():
                if password == creditcard_dict[creditcard]["password"]:
                    if creditcard_dict[creditcard]["locked"] == 0:
                        print("\33[31;0m信用卡 %s 认证成功\33[0m" % (creditcard))
                        return res, creditcard
                    else:
                        print("\33[31;0m信用卡 %s 已经被冻结 认证失败\33[0m" % (creditcard))
                else:
                    print("\33[31;0m输入的密码不匹配 认证失败\33[0m")
            else:
                print("\33[31;0m输入的信用卡卡号不存在 认证失败\33[0m")
    else:
        print("\33[31;0m输入的信用卡卡号为空 认证失败\33[0m")

wrapper()




