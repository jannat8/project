#!/usr/bin/python
import socket               # Import socket module
import sys
import threading
from thread import *
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   
host = socket.gethostname()
port = 5188    
s.connect((host, port))

def receive():
    #data=string.split(' ']
    
    while True :
      #print "Typing......."
      reply=s.recv(1024)
      if not reply:
              break
      print "\nRecieved: ",repr(reply)
      
    #print s.recv(1024)



start_new_thread(receive,())

while True :
  data=raw_input("Enter Message: ")
  s.send(data)


s.close()                     # Close the socket when done 
