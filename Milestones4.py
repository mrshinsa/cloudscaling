#!/usr/bin/env python
import socket
import string
import os
import mimetypes

def viewFolder(File):	
	if os.path.isdir(File):
		os.chdir(File)	
		return viewFolder("")
	elif not File: 
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
	return html

def handle(s):		
	data = s.recv(1024) 	
	File = data[len("GET /"):1024]
	File = File[0:File.find(" HTTP")]
	print File	
	html = viewFolder(File)			
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


# http://docs.python.org/2/library/os.html#files-and-directories
# http://lookherefirst.wordpress.com/2007/12/03/check-if-an-entry-is-a-file-or-directory-in-python/
