# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     get_file
   Description :
   Author :       simplefly
   date：          2018/2/20
-------------------------------------------------
   Change Activity:
                   2018/2/20:
-------------------------------------------------
"""
__author__ = 'simplefly'

'Windows 通过 ssh 接受从 Linux 发送的文件'

import paramiko
transport = paramiko.Transport(('192.168.153.132',22))
transport.connect(username='root', password='')
sftp = paramiko.SFTPClient.from_transport(transport)
sftp.get('/root/Linux.txt', 'Linux.txt')#将Linux上的/root/Linux.txt下载到本地
transport.close()