#!/usr/bin/python

""" 
A simple echo client 
""" 
import socket
import string
import os
import mimetypes



print "Socket client!";



import socket 

host = 'localhost' 
port = 80 
size = 1024 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.connect((host,port)) 
s.send('Hello, world') 
data = s.recv(size) 
s.close() 
print 'Received:', data 