# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     cenv
   Description :
   Author :       simplefly
   date：          2018/2/20
-------------------------------------------------
   Change Activity:
                   2018/2/20:
-------------------------------------------------
"""
__author__ = 'simplefly'

import socket

def generate_str():
    l = 'abcdefghijklmnopqrstuvwxyz'
    i = 0
    while True:
        yield str(l[i % 26])
        i+=1

# 创建客户端socket对象
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 服务器IP地址和端口号元祖
server_address = ('192.168.153.132', 8888)
# 客户端连接指定的IP地址和端口号
clientsocket.connect(server_address)
s = generate_str()
while True:
    # 输入数据
    data = next(s)
    print('Send Message:', data)
    # 客户端发送数据
    clientsocket.sendall(data.encode())
    # 客户端接受数据
    server_data = clientsocket.recv(1024)
    print('Receive Message：', server_data)

# 关闭客户端socket
clientsocket.close()

