#!/usr/bin/python

""" 
A simple echo server 
""" 

import socket
import string
import os
import mimetypes



print "Socket server!";

host = '' 
port = 50000 
backlog = 5 
size = 1024 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.bind((host,port)) 
s.listen(backlog) 
while 1: 
    client, address = s.accept() 
    data = client.recv(size) 
    if data: 
        client.send(data) 
    client.close() 