# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     client
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
import sys

def socket_client():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('127.0.0.1', 6666))
    except socket.error as msg:
        print(msg)
        sys.exit(1)
    print(s.recv(1024))
    while True:
        data = input('please input word:')
        s.send(data.encode('utf-8'))
        print(s.recv(1024))
        if data == 'exit':
            break
    s.close()

if __name__ == '__main__':
    socket_client()