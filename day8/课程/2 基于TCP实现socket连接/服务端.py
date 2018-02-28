#!/usr/bin/python
#-*- coding:utf-8 –*-
import socket

#1、买手机
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #tcp协议

#2、绑定手机
# phone.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
phone.bind(('127.0.0.1',8082)) #0-65535

#3、开机
phone.listen(5)

#4、等待电话连接
print('starting...')
while True:   #连接循环
    conn,client_addr=phone.accept() #(conn,client_addr)
    print(conn,client_addr)

    #5、收\发消息
    while True:  #通信循环
        # try:  #针对windows
        data=conn.recv(1024) #1024bytes?
        if not data:break    #针对linux
        print('客户端发的:%s' %data)
        conn.send(data.upper())
        # except ConnectionResetError:
        #     break
#6、挂电话连接
    conn.close()

#7、关机
phone.close()

