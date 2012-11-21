#!/usr/bin/env python
import socket, threading, time

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
while 1:
	try:
		t,_ = s.accept();
		threading.Thread(target = handle, args = (t,)).start()
	except:
		client.close()
		print "cleaning up";

# http://code.activestate.com/recipes/577428-simplest-example-of-serving-a-browser-request/
