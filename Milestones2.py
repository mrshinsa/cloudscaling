#!/usr/bin/env python
import socket
import string
import os
import mimetypes

def handle(s):
	print s
	print repr(s.recv(4096))	
	f = open("hi.html", "rb")
	data = f.read()
	f.close()
	s.send(data)
	s.close()
  
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('', 80));
s.listen(1);
running = True
while running:
	try:
		t,_ = s.accept();
		handle(t,)
	#	threading.Thread(target = handle, args = (t,)).start()
	except:
		s.close()
		print "cleaning up";
		running = False

# http://code.activestate.com/recipes/577428-simplest-example-of-serving-a-browser-request/
