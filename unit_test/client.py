# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     client
   Description :
   Author :       simplefly
   date：          2018/2/1
-------------------------------------------------
   Change Activity:
                   2018/2/1:
-------------------------------------------------
"""
__author__ = 'simplefly'

import socket

if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('127.0.0.1', 8888))
    sock.sendall(b'test client')
    sock.close()