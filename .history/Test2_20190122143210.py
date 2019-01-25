#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket
ip_port = ('192.168.1.246',5050)

sk = socket.socket()
sk.connect(ip_port)

sk.sendall('请求占领地球')

server_reply = sk.recv(1024)
print server_reply

sk.close()