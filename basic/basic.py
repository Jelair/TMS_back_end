# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     basic
   Description :
   Author :       simplefly
   date：          2018/2/19
-------------------------------------------------
   Change Activity:
                   2018/2/19:
-------------------------------------------------
"""
__author__ = 'simplefly'

# Transport bytes by socket
import socket

def server(address):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(address)
    sock.listen(3)
    print('Listening at {}'.format(address))
    while True:
        s, addre = sock.accept()
        print('Accept from {}'.format(addre))
        msg = s.recv(1024)


