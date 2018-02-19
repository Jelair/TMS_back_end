# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     send
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
import os
import sys
import struct
# 192.168.153.132
def socket_client():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('192.168.153.132', 6666))
    except socket.error as msg:
        print(msg)
        sys.exit(1)
    print(s.recv(1024))

    while True:
        filepath = 'E:\python_projects\TMS_back_end\socket_transport/recv.py'
        if os.path.isfile(filepath):
            # 定义文件信息。128s表示文件名为128bytes长，l表示一个int或log文件类型，在此为文件大小
            fileinfo_size = struct.calcsize('128sl')
            # 定义文件头信息，包含文件名和文件大小
            fhead = struct.pack('128sl', os.path.basename(filepath).encode(), os.stat(filepath).st_size)
            s.send(fhead)
            print('client filepath: {}'.format(filepath))
            fp = open(filepath, 'rb')
            while True:
                data = fp.read(1024)
                if not data:
                    print('{} file send over...'.format(filepath))
                    fp.close()
                    break
                s.send(data)
        s.close()
        break

if __name__ == '__main__':
    socket_client()