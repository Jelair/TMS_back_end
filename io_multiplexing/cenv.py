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

# 创建客户端socket对象
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 服务器IP地址和端口号元祖
server_address = ('192.168.153.132', 8888)
# 客户端连接指定的IP地址和端口号
clientsocket.connect(server_address)
while True:
    # 输入数据
    data = input('Please input:')
    # 客户端发送数据
    clientsocket.sendall(data.encode())
    # 客户端接受数据
    server_data = clientsocket.recv(1024)
    print('客户端收到的数据：', server_data)

# 关闭客户端socket
clientsocket.close()