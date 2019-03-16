#!/usr/bin/py

# This is tcp_client.py script
# Attempts to establish connection
# to a desired server

import socket                           # Calls proper module to manipulate network connections

s = socket.socket()                     # Creates a socket object of which socket methods/functions can be enacted upon
host = socket.gethostname()             # Returns machinename/ipaddress to the host variable
port = 9999                             # Selects the port to connect to on desired server

s.connect((host, port))                 # Attempts to establish conection with server of such name and such port
print s.recv(1024)                      # 1024 is bufsize or max amount of data to be received at once

s.close()                               # Exits connection




