# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     ZRequest
   Description :
   Author :       simplefly
   date：          2018/2/1
-------------------------------------------------
   Change Activity:
                   2018/2/1:
-------------------------------------------------
"""
__author__ = 'simplefly'

class ZRequest(object):

    def __init__(self):
        self.method = 'GET'
        self.path = ''
        self.body = ''
        self.headers = {}
        self.cookies = {}

    def add_headers(self, header):
        lines = header
        for line in lines:
            k, v = line.split(':', 1)
            self.headers[k] = v
        self.add_cookies()

    def add_cookies(self):
        cookies = self.headers.get('Cookie', '')
        kvs = cookies.split('; ')
        for kv in kvs:
            if '=' in kv:
                k, v = kv.split('=', 1)
                self.cookies[k] = v

    def form(self):
        pass