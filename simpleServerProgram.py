#!/usr/bin/py

# This is a tcp_server.py script:
# This is server side code that
# is intended to receive socket 
# connections from clients attemting
# to establish a connection

import socket                     
                                                             # Imports proper module/file with socket scripts and functions

s = socket.socket()                                          # Creates a socket object
                                                             # test = socket.gethostbyname()
host = socket.gethostbyname(socket.gethostname())                      # Returns machine name/ip address
port = 9999                                                  # Selects port number for receiving connections

s.bind((host, port))                                         # Binds with the address encapsulated in the duet argument

print "Waiting for connection..."
s.listen(5)                                                  # Listens for connection - Amount of conection attempts allowed before connection attempt is confirmed as failure

while True:
    conn,addr = s.accept()                                   # Connection from client is accepted, and returns that client-server connection is success/fail, along with client                                                              # ip address. Assuming connection succes
    print 'Got connection from', addr
    conn.send('Server saying Hello')
    conn.close()                                             # Close the connection



