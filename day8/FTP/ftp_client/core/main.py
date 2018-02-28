#!/usr/bin/python
#-*- coding:utf-8 –*-
import socket
import struct
import json
import os
import hashlib


DOWNLOAD_DIR='/Users/liqiongqiong/PycharmProjects/oldboy/day8/FTP/DOWNLOAD'

class FtpClient:
    def __init__(self,host,port):
        self.host=host
        self.port=port
        self.client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.client.connect((self.host,self.port))

    def interactive(self):
        while True:
            data=input('>>: ').strip() #get a.txt
            if not data:continue
            params=data.split() #parmas=['get','a.txt']
            cmd=params[0] #cmd='get'
            if hasattr(self,cmd):
                func=getattr(self,cmd)
                func(params) #func(['get','a.txt'])

    def get(self,params):
        params_json=json.dumps(params)
        self.client.send(params_json.encode('utf-8'))

        # 1、先接收报头的长度
        headers_size = struct.unpack('i', self.client.recv(4))[0]

        # 2、再收报头
        headers_bytes = self.client.recv(headers_size)
        headers_json = headers_bytes.decode('utf-8')
        headers_dic = json.loads(headers_json)
        print('========>', headers_dic)
        filename = headers_dic['filename']
        filesize = headers_dic['filesize']
        filepath = os.path.join(DOWNLOAD_DIR, filename)

        # 3、再收真实的数据
        with open(filepath, 'wb') as f:
            recv_size = 0
            while recv_size < filesize:
                line = self.client.recv(1024)
                recv_size += len(line)
                f.write(line)
            print('===>下载成功')

    def send_auth(self):
        user_name = input('请输入用户名：')
        password = input('请输入密码：')
        # 客户端发送用户名与密码(列表)
        password_hash = hash(password)
        user_data = '用户信息：%s,%s' % (user_name, password_hash)
        self.client.send(user_data.encode())
        # 接收服务端返回，认证成功True，认证失败False
        auth_recv=self.client.recv(1024).decode()
        if auth_recv == '200':
            print('Welocome Login'.center(50,'*'))
            return auth_recv
        elif auth_recv == '400':
            print('usename or password is error')
            return auth_recv


def hash(data):
    m=hashlib.md5()
    m.update(data.encode())
    return m.hexdigest

if __name__ == '__main__':
    client=FtpClient('127.0.0.1',8080)

    client.send_auth()

    client.interactive()