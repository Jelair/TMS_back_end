# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     service
   Description :
   Author :       simplefly
   date：          2018/2/19
-------------------------------------------------
   Change Activity:
                   2018/2/19:
-------------------------------------------------
"""
__author__ = 'simplefly'

import socket
import threading
import time
import sys

def socket_service():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 防止socket server 重启后端口被占用
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(('', 6666))
        s.listen(10)
    except socket.error as msg:
        print(msg)
        sys.exit(1)
    print('Waiting connection...')

    while True:
        conn, addr = s.accept()
        t = threading.Thread(target=deal_data, args=(conn, addr))
        t.start()

def deal_data(conn, addr):
    print('Accept new connection from {}'.format(addr))
    conn.send(b'Hi, Welcome to the server.')
    while True:
        data = conn.recv(1024)
        print('{} client send data is {}'.format(addr, data))
        if data == 'exit' or not data:
            print('{} connection close.'.format(addr))
            conn.send(b'Connection closed.')
            break
        conn.send('Hello, {}'.format(data).encode('utf-8'))
    conn.close()

if __name__ == '__main__':
    socket_service()