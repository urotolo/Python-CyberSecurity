#!/usr/bin/py

# This server script takes to numbers from a connected client
# adds the two values, then returns the sum to the connected client

import socket

host = socket.gethostbyname(socket.gethostname())
port = 12345

s = socket.socket()                                               # Example of TCP socket object

s.bind((host,port))
print 'Waiting for guest connection'
s.listen(5)

conn,addr = s.accept()

print 'Connected by', addr
while True:
    data = conn.recv(1024)
    dlist = data.split(",")
    sum = int(dlist[0]) + int(dlist[1])
    conn.send(str(sum))

conn.close()

