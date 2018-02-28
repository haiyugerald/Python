#!/usr/bin/python
#-*- coding:utf-8 –*-

import sys,os


BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)

sys.path.append(BASE_DIR)
# print(sys.path)

# from core import src
#
# if __name__ == '__main__':
#     src.run()

while True:
    print("\33[35;1m欢迎进入信用卡购物模拟程序\33[0m".center(50, "#"),
          "\n1 购物中心\n"
          "2 信用卡中心\n"
          "3 后台管理\n"
          "q 退出程序\n")

    choice=input("\33[34;0m请输入你的选择ID\33[0m:").strip()

    res = authentication.user_auth()

    if  choice == 0:continue
    if choice == '1':
        shopping()
    elif choice =='2':
        check_balance()
    elif choice== '3':
        transfer()
    elif choice == '4':
        pay_back()
    elif choice =='5':
        exit()
