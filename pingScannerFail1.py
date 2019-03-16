#!/usr/bin/py

# Incomplete program.

import socket
import sys

ipAddress = str(raw_input("Enter a ipAddress to be scanned: "))

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
    
    

