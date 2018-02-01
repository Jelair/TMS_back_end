# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     app
   Description :
   Author :       simplefly
   date：          2018/2/1
-------------------------------------------------
   Change Activity:
                   2018/2/1:
-------------------------------------------------
"""
__author__ = 'simplefly'

from zlib import socket_utils

def run(address):
    listener = socket_utils.create_srv_socket(address)
    socket_utils.syn_accept_conversation_forever(listener)


if __name__ == '__main__':
    run(('', 8888))