#!/usr/bin/python
#-*- coding:utf-8 –*-
from socket import *

client=socket(AF_INET,SOCK_DGRAM)  #基于数据报传输 TCP是SOCK_STREAM基于数据流传输
# server.bind(('127.0.0.1',8080))
# server.listen(5)  #UDP 协议不需要建立连接，所以也就不需要监听
# server.accept() #UDP 协议不需要建立连接，所以也就不需要等待接收连接

while True:
    msg=input('===>')
    client.sendto(msg.encode('utf-8'),('127.0.0.1',8080))
    data,server_addr=client.recvfrom(1024)
    print(data.decode('utf-8'))