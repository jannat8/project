'''
    Simple socket server using threads
'''
#!/usr/bin/python 
import socket
import sys
import threading
from thread import *
i=0
adr=[]
conn=[] #to handle 2 clients
string=[]
HOST= socket.gethostname()
PORT = 5188 # Arbitrary non-privileged port
n=0
j=0
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
s.listen(10)
print 'Socket now listening'

#Function for handling connections. This will be used to create threads
def clientthread(conn,string):
    #Sending message to connected client
    #conn[0].send('Welcome to the server. Type something and hit enter\n') #send only takes string
    
    
      #string.append(' ')
      #string.append(conn[i])
      #i=i+1
     
    #infinite loop so that function do not terminate and thread do not end.
    
    for i in range(n-1):  
        conn[i].sendall("people available: " + (string[i]) + "\n")
    
         #data=conn[0]
         #conn[0].send(conn) #send clients info
         #Receiving from client
    for j in range(n-1):
         conn[j-1].sendall(str(newv))
         conn[j-1].sendall(": is online")
         conn[j].sendall("Which address do you want to connect to?\n")
         address=conn[j].recv(1024)
         conn[j].sendall('you are now connected with' + address + '\n')
         print repr(address)
         adr.append(conn)
         conn[j].sendall('Type message and hit enter\n') 
    l=0    
    for l in range(m):
        if (address == string[l]):
            string[l]=conn[l]
            adr.append(string[l])
    while True:
          
          data= adr[0].recv(1024)
          if not data: 
                  break
          adr[1].sendall(data) #first send
          
          
          data= adr[1].recv(1024)
          if not data: 
                  break
          adr[0].sendall(data) #second send
         
          
          #{ print repr(data)
          #reply = 'OK...' + data
          #reply=raw_input("Reply Back: ")
          #conn.sendall(reply)}
        
     
    #came out of loop
    conn.close()
m=0
#now keep talking with the client
while 1:
    #wait to accept a connection - blocking call
    tempconn,tempaddr = s.accept()
    print 'Connected with ' + tempaddr[0] + ':' + str(tempaddr[1])
    conn.append(tempconn)  #Client1
    adr.append(tempconn)
    string.append(str(tempaddr[1])) #to save all addresses
    n=n+1
    newv=tempaddr[1]
     
    

    #conn.recv(1024)
    #start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
    start_new_thread(clientthread ,(conn,string))
    
    m += 1  
s.close()
