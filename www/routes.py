# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     routes
   Description :
   Author :       simplefly
   date：          2018/2/1
-------------------------------------------------
   Change Activity:
                   2018/2/1:
-------------------------------------------------
"""
__author__ = 'simplefly'



def error(request, code=404):
    e = {
        404: b'HTTP/1.1 404 NOT FOUND\r\n\r\n<h1>NOT FOUND</h1>',
    }
    return e.get(code, b'')

def response_for_request(request):
    response = route_dict.get(request.path, error)
    return response(request)

def route_index(request):
    header = 'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n'
    body = 'Hello'
    response = header + '\r\n' + body
    return response.encode(encoding='utf-8')

route_dict = {
    '/': route_index,
}