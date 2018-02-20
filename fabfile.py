# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     fabfile
   Description :
   Author :       simplefly
   date：          2018/2/20
-------------------------------------------------
   Change Activity:
                   2018/2/20:
-------------------------------------------------
"""
__author__ = 'simplefly'

import os,re
from datetime import datetime
from fabric.api import *

# 服务器登录用户名
env.user = 'root'
# sudo用户为root
env.sudo_user = 'root'
# 服务器地址，可以有多个，依次部署
env.hosts = ['39.108.230.15']
# 服务器MySQL用户名和口令
db_user = 'root'
db_password = 'root'

_TAR_FILE = 'dist-microblog.tar.gz'

def build():
    includes = ['static', 'templates', 'transwarp', 'favicon.ico', '*.py']
    excludes = ['test', '.*', '*.pyc', '*.pyo']
    local('rm -f dist/%s' % _TAR_FILE)
    with lcd(os.path.join(os.path.abspath('.'), 'async_www')):
        cmd = ['tar', '--dereference', '-czvf', '../dist/%s' % _TAR_FILE]
        cmd.extend(['--exclude=\'%s\'' % ex for ex in excludes])
        cmd.extend(includes)
        local(' '.join(cmd))