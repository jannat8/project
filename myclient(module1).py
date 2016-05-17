#!/usr/bin/python
import socket               # Import socket module

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   
host = socket.gethostname()
port = 5188               # Reserve a port for your service.

s.connect((host, port))
while True :
  
    data=raw_input("Enter Message: ")
    #if not data: 
           # break
    print "Typing......."
    s.send(data)
    reply=s.recv(1024)
    print repr(reply)
    #print s.recv(1024)
  
  
s.close()                     # Close the socket when done 
