#!/usr/bin/python
#-*- coding:utf-8 –*-
# 版本1
# from socket import *
#
# server=socket(AF_INET,SOCK_STREAM)
# server.bind(('127.0.0.1',8080))
# server.listen(5)
#
#
# while True:
#     conn,client_addr=server.accept()
#
#     while True:
#         try:
#             data=conn.recv(1024)
#             if not data:break
#             server.send(data.upper())
#             conn.close()
#         except ConnectionResetError:
#             break
#     server.close()

# 版本2
# from socket import *
# def comunicate(conn):
#     while True:
#         try:
#             data=conn.recv(1024)
#             if not data:break
#             conn.send(data.upper())
#         except ConnectionResetError:
#             break
#     conn.close()
#
# def server(ip,port):
#     server=socket(AF_INET,SOCK_STREAM)
#     server.bind(ip,port)
#     server.listen(5)
#
#     while True:
#         conn,client_addr=server.accept()
#         comunicate(conn)
#     server.close()
#
# if __name__ == '__main__':
#     server('127.0.0.1', 8081)

# 版本3
from socket import *
from threading import Thread, current_thread
# def comunicate(conn):
#     print('子线程：%s' % current_thread().getName())
#     while True:
#         try:
#             data = conn.recv(1024)
#             if not data: break
#             conn.send(data.upper())
#         except ConnectionResetError:
#             break
#     conn.close()
#
#
# def server(ip, port):
#     print('主线程：%s' % current_thread().getName())
#     server = socket(AF_INET, SOCK_STREAM)
#     server.bind((ip, port))
#     server.listen(5)
#
#     while True:
#         conn, addr = server.accept()
#         print(addr)
#         # comunicate(conn)
#         t = Thread(target=comunicate, args=(conn,))
#         t.start()
#     server.close()
#
# if __name__ == '__main__':
#     server('127.0.0.1', 8081)
import multiprocessing
import threading

import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',8080))
s.listen(5)

def action(conn):
    while True:
        data=conn.recv(1024)
        print(data)
        conn.send(data.upper())

if __name__ == '__main__':

    while True:
        conn,addr=s.accept()

        p=threading.Thread(target=action,args=(conn,))
        p.start()
