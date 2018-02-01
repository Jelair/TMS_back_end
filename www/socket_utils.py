# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     zsockets
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
from www.ZRequest import ZRequest
from www import routes

def create_srv_socket(address):
    """Build and return a listening server socket."""
    listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listener.bind(address)
    listener.listen(64)
    print('Listening at {}'.format(address))
    return listener

def syn_accept_conversation_forever(listener):
    """Forever answer incoming conversation on a listening socket."""
    while True:
        sock, address = listener.accept()
        print('Accetp conversation from {}'.format(address))
        # yield sock
        handle_conversation(sock, address)

def handle_conversation(sock, address):
    """Converse with a client over "sock" until they are done talking."""
    try:
        handle_request(sock)
    except EOFError:
        print('Client socket to {} has closed'.format(address))
    except Exception as e:
        print('Client {} error:{}'.format(address, e))
    finally:
        sock.close()

def get_request(message):
    """Build a Request object, init and return."""
    request = ZRequest()
    request.method = message.split()[0]
    request.add_headers(message.split('\r\n\r\n', 1)[0].split('\r\n')[1:])
    request.body = message.split('\r\n\r\n', 1)[1]
    request.path = message.split()[1]
    return request

def handle_request(sock):
    """Receive a single client request on "sock" and send a answer."""
    msg = recv_message(sock)
    request = get_request(msg)
    print(request.method, request.path, request.body)
    # deal data and deliver data
    response = routes.response_for_request(request)
    sock.sendall(response)

def recv_message(sock):
    """Receive bytes over socket "sock"."""
    message = sock.recv(1024)
    if not message or len(message.split()) < 2:
        raise EOFError('socket closed')
    message = message.decode('utf-8')
    return message

