#!/usr/bin/python
#-*- coding:utf-8 –*-

#默认打开的文件类型是文本模式
#w：文件不存在则创建，文件存在那么在打开文件后会清空已有的文件，重新写
# f=open(r'a.txt','w',encoding='utf-8')
# # print(f.writable())
# f.write('1111\n')
# f.write('2222\n')
# f.writelines(['3333\n','444\n'])
# f.close()

#a：文件不存在则创建，文件存在那么在打开文件后立刻将光标移动到文件末尾，进行追加写
# f=open(r'b.txt','a',encoding='utf-8')
# # print(f.writable())
# f.write('4444\n')
# f.write('5555\n')
# f.writelines(['66666\n','7777\n'])
# f.close()

#r：文件必须存在，不存在则抛出异常
# f=open(r'b.txt','r',encoding='utf-8')
# # print(f.writable())
# # print(f.read())
# # print(f.readlines())
# print(f.readline(),end='')
# print(f.readline(),end='')
# f.close()


# with open('b.txt','r',encoding='utf-8') as f:
#     # while True:
#     #     line=f.readline()
#     #     if len(line) == 0:break
#     #     print(line)
#
#     # print(f.readline())
#     # print(f.readline())
#     # print(f.readline())
#     # print(f.readline())
#     # print(f.readline())
#     # print(f.readline())
#     # print(f.readline())
#     # print('第八次',f.readline())
#
#     for line in f:
#         print(line)


#b:bytes  对于非文本文件，我们只能使用b模式，"b"表示以字节的方式操作（而所有文件也都是以字节的形式存储的，使用这种模式无需考虑文本文件的字符编码、图片文件的jgp格式、视频文件的avi格式）
#以b方式打开时，读取到的内容是字节类型，写入时也需要提供字节类型，不能指定编码

# with open('111.png','rb') as f:
#     print(f.read())

# with open('b.txt','rb',) as f:
#     print(f.read().decode('utf-8'))

# with open('b.txt','rt',encoding='utf-8') as f:
#     print(f.read())


# with open('b.txt','wb') as f:
#     res='中问'.encode('utf-8')
#     print(res,type(res))
#     f.write(res)


# with open('b.txt','ab') as f:
#     res='哈哈哈'.encode('utf-8')
#     print(res,type(res))
#     f.write(res)



#练习：
# 1、用python实现cp命令
# import sys
# _,src_file,des_file=sys.argv
#
# with open(src_file,'rb') as read_f,\
#         open(des_file,'wb') as write_f:
#
#         for line in read_f:
#             write_f.write(line)



# with open('a.txt','rb') as read_f,\
#         open('b.txt','wb') as write_f:
#
#         for line in read_f:
#             write_f.write(line)

#2、文件的修改
# import os
#
# with open('a.txt','r',encoding='utf-8') as read_f,\
#         open('.a.txt.swap','w',encoding='utf-8') as write_f:
#
#     for line in read_f:
#         if 'sb' in line:
#             line=line.replace('sb','somebady')
#         write_f.write(line)
#
# os.remove('a.txt')
# os.rename('.a.txt.swap','a.txt')