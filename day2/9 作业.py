#!/usr/bin/python
#-*- coding:utf-8 –*-

#博客地址
#http://blog.51cto.com/10630401/2049359
#http://blog.51cto.com/10630401/2049413


# 作业一: 三级菜单
# 要求:
# 打印省、市、县三级菜单
# 可返回上一级
# 可随时退出程序
# menu = {
#     '北京':{
#         '海淀':{
#             '五道口':{
#                 'soho':{},
#                 '网易':{},
#                 'google':{}
#             },
#             '中关村':{
#                 '爱奇艺':{},
#                 '汽车之家':{},
#                 'youku':{},
#             },
#             '上地':{
#                 '百度':{},
#             },
#         },
#         '昌平':{
#             '沙河':{
#                 '老男孩':{},
#                 '北航':{},
#             },
#             '天通苑':{},
#             '回龙观':{},
#         },
#         '朝阳':{},
#         '东城':{},
#     },
#     '上海':{
#         '闵行':{
#             "人民广场":{
#                 '炸鸡店':{}
#             }
#         },
#         '闸北':{
#             '火车战':{
#                 '携程':{}
#             }
#         },
#         '浦东':{},
#     },
#     '山东':{},
# }
# province_list=list(menu.keys())           #省列表
# while True:
#     print(" 省 ".center(50, '='))
#     for x in province_list:    #打印省份列表
#         print(x)
#     province = input("请输入省份,或输入q(quit)退出：").strip()
#     if len(province) > 0 and province in province_list:
#         city_list = list(menu[province].keys())
#         while True:
#             print(" 市 ".center(50, '='))
#             for y in city_list:   #打印市列表
#                 print(y)
#             city = input("请输入市,或输入b(back)返回上级菜单，或输入q(quit)退出：").strip()
#             if len(city) > 0 and city  in city_list:
#                 town_list = menu[province][city]
#                 while True:
#                     print(" 县 ".center(50, '='))
#                     for z in town_list:  # 打印县列表
#                         print(z)
#                     back_or_quit = input("输入b(back)返回上级菜单，或输入q(quit)退出：")
#                     if back_or_quit == 'b':
#                         break  # 终止此层while循环，跳转到上一层While。
#                     elif back_or_quit == 'q':
#                         exit()
#                     else:
#                         print("输入非法！")
#             elif city == 'b':
#                 break
#             elif city == 'q':
#                 exit()
#             else:
#                 print("输入的市有误，请重新输入！！！")
#                 continue
#     elif province == 'q':
#         break
#     else:
#         print("输入的省份有误，请重新输入！！！")
#         continue

# 作业二：请闭眼写出购物车程序
# 需求:
# 用户名和密码存放于文件中，格式为：egon|egon123
# 启动程序后，先登录，登录成功则让用户输入工资,然后打印商品列表，失败则重新登录，超过三次则退出程序
# 允许用户根据商品编号购买商品   完成
# 用户选择商品后，检测余额是否够，够就直接扣款，不够就提醒  完成
# 可随时退出，退出时，打印已购买商品和余额  完成
product_list = [
        ["Iphone",5800],
        ["MAC PRO",16800],
        ["Bike",800],
        ["Coffee",30],
]

shopping_list = []

#f = open('a','r+')
with open('a','r+') as f:
    db = list()
    for line in f.readlines():
        line  = line.rstrip('\n')
        arr = line.split('|')
        db.append(arr)
print(db)

count = 0
while count < 3:
    input_name = input('名字==>>: ')
    input_password = input('密码==>>: ')
    for i in range(len(db)):
        if input_name == db[i][0] and  input_password == db[i][1]:
            print('登录成功！！！')
            while True:
                salary = input("请输入你的工资或者输入‘q’退出>>：")
                if salary.isdigit():  # 判断是否为数字
                    salary = int(salary)
                    while True:
                        for index, item in enumerate(product_list):
                            print(index, item[0], item[1])  # 打出菜单
                        choice = input("请选择要购买的商品编号或者输入‘q’退出>>：")
                        if choice.isdigit():
                            choice = int(choice)
                            if choice >= 0 and choice < len(product_list):
                                p = product_list[choice]
                                if p[1] <= salary:  # 判断钱是否够用
                                    shopping_list.append(p)
                                    salary -= p[1]
                                    print("[%s]已加进你的购物车,所剩余额为[%s]" % (p, salary))
                                else:
                                    print("钱不够，你只有[%s] \033[0m " % salary)
                            else:
                                print("没有此商品！！！")
                        elif choice == "q":
                            print("已购买的商品".center(50, "-"))
                            for i in shopping_list:
                                print(i)
                            print("所剩余额为[%s]" % salary)
                            exit()
                        else:
                            print("请输入正确的序号！！！")
                elif salary == 'q':
                    exit()
                else:
                    print("请输入正确的工资数！！！")
                    continue
        else:
            print('输入的账号密码有误！！')
            count += 1
            break