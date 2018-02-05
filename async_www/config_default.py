# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     config_default
   Description :
   Author :       simplefly
   date：          2018/2/5
-------------------------------------------------
   Change Activity:
                   2018/2/5:
-------------------------------------------------
"""
__author__ = 'simplefly'

configs = {
    'debug': True,
    'db': {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'www',
        'password': 'www',
        'db': 'awesome'
    },
    'session': {
        'secret': 'Awesome'
    }
}