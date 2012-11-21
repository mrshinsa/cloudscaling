#!/usr/bin/env python
import socket
import string
import os
import mimetypes

def handle(s):
		
	data = s.recv(1024) 	
	
	File = data[len("GET /"):1024]
	File = File[0:File.find(" HTTP")]
	print File
	
	if not File: 
		dirs = os.listdir(".")	
		html = "<HTML><HEAD><TITLE>Milestone 3</TITLE></HEAD><BODY>"
		for file in dirs:
			html += "<tr><td><a href=" + file + ">" + file + "</a></td></tr><br>"
		html += "</BODY></HTML>"
	else:	
		try:
			f = open(File, "rb")	
			html = f.read()
			f.close()	
		except:			
			html = "File Excetption!"
				
	s.send(html)
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

# http://www.astro.ufl.edu/~warner/prog/python.html
