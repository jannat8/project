'''
    Simple socket server using threads
'''
#!/usr/bin/python 
import socket
import sys
import threading
from thread import *

conn=[] #to handle 2 clients

HOST= socket.gethostname()
PORT = 5188 # Arbitrary non-privileged port
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'
 
#Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
     
print 'Socket bind complete'
 
#Start listening on socket
s.listen(2)
print 'Socket now listening'
 
#Function for handling connections. This will be used to create threads
def clientthread(conn):
    #Sending message to connected client
    conn[0].send('Welcome to the server. Type something and hit enter\n') #send only takes string
    
     
    #infinite loop so that function do not terminate and thread do not end.
    while True:
         
        #Receiving from client
        
          data= conn[0].recv(1024)
          if not data: 
                  break
          conn[1].sendall(data) #first send
          

          data= conn[1].recv(1024)
          if not data: 
                  break
          conn[0].sendall(data) #secong send
           
          
          #{ print repr(data)
          #reply = 'OK...' + data
          #reply=raw_input("Reply Back: ")
          #conn.sendall(reply)}
        
     
    #came out of loop
    conn.close()
 
#now keep talking with the client
while 1:
    #wait to accept a connection - blocking call
    tempconn,tempaddr = s.accept()
    print 'Connected with ' + tempaddr[0] + ':' + str(tempaddr[1])
    conn.append(tempconn)  #Client1
    
     #wait to accept a connection - blocking call
    tempconn,tempaddr = s.accept()
    print 'Connected with ' + tempaddr[0] + ':' + str(tempaddr[1])
    conn.append(tempconn)   #Client2

    #conn.recv(1024)
    #start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
    start_new_thread(clientthread ,(conn,))
       
s.close()'''
    Simple socket server using threads
'''
#!/usr/bin/python 
import socket
import sys
import threading
from thread import *

conn=[] #to handle 2 clients

HOST= socket.gethostname()
PORT = 5188 # Arbitrary non-privileged port
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'
 
#Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
     
print 'Socket bind complete'
 
#Start listening on socket
s.listen(2)
print 'Socket now listening'
 
#Function for handling connections. This will be used to create threads
def clientthread(conn):
    #Sending message to connected client
    conn[0].send('Welcome to the server. Type something and hit enter\n') #send only takes string
    
     
    #infinite loop so that function do not terminate and thread do not end.
    while True:
         
        #Receiving from client
        
          data= conn[0].recv(1024)
          if not data: 
                  break
          conn[1].sendall(data) #first send
          

          data= conn[1].recv(1024)
          if not data: 
                  break
          conn[0].sendall(data) #secong send
           
          
          #{ print repr(data)
          #reply = 'OK...' + data
          #reply=raw_input("Reply Back: ")
          #conn.sendall(reply)}
        
     
    #came out of loop
    conn.close()
 
#now keep talking with the client
while 1:
    #wait to accept a connection - blocking call
    tempconn,tempaddr = s.accept()
    print 'Connected with ' + tempaddr[0] + ':' + str(tempaddr[1])
    conn.append(tempconn)  #Client1
    
     #wait to accept a connection - blocking call
    tempconn,tempaddr = s.accept()
    print 'Connected with ' + tempaddr[0] + ':' + str(tempaddr[1])
    conn.append(tempconn)   #Client2

    #conn.recv(1024)
    #start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
    start_new_thread(clientthread ,(conn,))
       
s.close()
