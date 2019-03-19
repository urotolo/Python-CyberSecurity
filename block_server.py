#!/usr/bin/py 

# Block server

import socket

sock = socket.socket()

host = socket.gethostname()
port = 12345

sock.bind((host, port))
sock.listen(5)

while True:
    print "Waiting on connection..."
    conn, addr = sock.accept()     # Accept the connection from block_client.py
    data = conn.recv(1024)
    while data:                    # While data != empty
        print data
        data = conn.recv(1024)
    print "All data received"      # Will execute when all data is received: data variable is empty of its content
    conn.close()
    break

