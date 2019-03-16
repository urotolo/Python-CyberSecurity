#!/usr/bin/py

# Incomplete program.

import socket
import sys

ipAddress = str(raw_input("Enter a ipAddress to be scanned: "))
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print s

server = 'pythonprogramming.net'
port = 80

server_ip = socket.gethostbyname(server)
print server_ip

request = "GET / HTTP/1.1\nHOST: " + server + "\n\n"

s.connect((server, port))
s.send(request.encode())
result = s.recv(4096)

#print result

while (len(result) > 0):
    print(result)
    result = s.recv(4096)



# Code below this point was taken a more dynamicbut complicated approach

host = ipAddress
portList = (20,21,22,23,25,80,156,443)

def iteratePortsPerHost(inHost, inPortList):
   s = socket.socket()
   for i in range(0,256):
       ip = inHost + '.' + str(i)
       for port in inPortList:
           s.connect((ip, port))
           banner = s.recv(1024)
           return banner



print iteratePortsPerHost(host, portList)
    
    

