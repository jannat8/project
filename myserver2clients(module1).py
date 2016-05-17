'''
    Simple socket server using threads
'''
#!/usr/bin/python 
import socket
import sys
import threading
from thread import *

client={0,0} #to handle 2 clients

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
    #conn.send('Welcome to the server. Type something and hit enter\n') #send only takes string
    
     
    #infinite loop so that function do not terminate and thread do not end.
    while True:
         
        #Receiving from client
        if conn.client[0]==0:
          data= conn.client[0].recv(1024)
          if not data: 
                  break
          conn.client[1].sendall(data)
          
         
        elif conn.client[1]==0:
          data= conn.client[1].recv(1024)
          if not data: 
                  break
          conn.client[0].sendall(data)
          
          
        # conn.client.append(data)
        
         
        #{ print repr(data)
         #reply = 'OK...' + data
        #reply=raw_input("Reply Back: ")
         
     
        #conn.sendall(reply)}
        del client[0]
     
    #came out of loop
    conn.close()
 
#now keep talking with the client
while 1:
    #wait to accept a connection - blocking call
    conn, addr = s.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])

    #conn.recv(1024)
    #start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
    start_new_thread(clientthread ,(conn,))
       
s.close()
