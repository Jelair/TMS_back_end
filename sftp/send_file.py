# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     send_file
   Description :
   Author :       simplefly
   date：          2018/2/20
-------------------------------------------------
   Change Activity:
                   2018/2/20:
-------------------------------------------------
"""
__author__ = 'simplefly'

import paramiko

'Windows 通过 ssh 给 Linux 发送文件'

transport = paramiko.Transport(('192.168.153.132', 22))
transport.connect(username='root', password='')
sftp = paramiko.SFTPClient.from_transport(transport)#如果连接需要密钥，则要加上一个参数，hostkey="密钥"
sftp.put('test.jpg', '/root/test.jpg')#将本地的test.jpg文件上传至服务器/root/test.jpg
transport.close() # 关闭连接