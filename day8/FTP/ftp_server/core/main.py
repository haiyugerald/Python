#!/usr/bin/python
#-*- coding:utf-8 –*-
#建立socket连接

import socket
import os
import json
import struct

SHARE_DIR='/Users/liqiongqiong/PycharmProjects/oldboy/day8/FTP/SHARE'

class FtpServer:
    def __init__(self,host,port):
        self.host=host
        self.port=port
        self.server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.server.bind((self.host,self.port))
        self.server.listen(5)

    def serve_forever(self):
        print('server starting...')
        while True:
            self.conn,self.client_addr=self.server.accept()
            print(self.client_addr)

            while True:
                try:
                    data=self.conn.recv(1024)  #params_json.encode('utf-8')
                    if not data:break
                    params=json.loads(data.decode('utf-8')) #params=['get','a.txt']
                    cmd=params[0] #
                    if hasattr(self,cmd):
                        func=getattr(self,cmd)
                        func(params)
                    else:
                        print('\033[45mcmd not exists\033[0m')
                except ConnectionResetError:
                    break
            self.conn.close()
        self.server.close()

    def get(self,params): #params=['get','a.txt']
        filename=params[1] #filename='a.txt'
        filepath=os.path.join(SHARE_DIR,filename) #
        if os.path.exists(filepath):
            #1、制作报头
            headers = {
                'filename': filename,
                'md5': '123sxd123x123',
                'filesize': os.path.getsize(filepath)
            }

            headers_json = json.dumps(headers)
            headers_bytes = headers_json.encode('utf-8')

            #2、先发报头的长度
            self.conn.send(struct.pack('i',len(headers_bytes)))

            #3、发送报头
            self.conn.send(headers_bytes)

            #4、发送真实的数据
            with open(filepath,'rb') as f:
                for line in f:
                    self.conn.send(line)

    def put(self):
        pass

    def auth_login(self):
        recv_data = self.request.recv(1024).strip()
        recv_data = recv_data.decode()
        print(recv_data, type(recv_data))
        recv_list = recv_data.split(":")
        print(recv_list)


if __name__ == '__main__':
    server=FtpServer('127.0.0.1',8080)
    server.serve_forever()

