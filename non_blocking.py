#!/usr/bin/py

# non_blocking_client.py
# Blocking v non blocking concept: When sending buffers
# if I set blocking on then blocking will send data to the
# server in segments. Only when the server signals back to
# the client that it has processed the last segment of data
# and is ready to receive more. Turning off blocking on the other
# hand, as this program does, attempts to send in as much data
# through the buffer as possible. Could cause buffer overflow in
# certain context. This is why this program sends all its data far
# quicker then the blocking client. Test and see for yourself!
# first run 'python block_server.py'

import socket

s = socket.socket()

host = socket.gethostname()
port = 12345

s.connect((host, port))
s.setblocking(0)                          # Now setting to non-blocking mode [0] is non-blocking
                                          # [1] will set it to blocking mode


data = "Hello Python\n" *10*1024*1024     # Huge amount of data to be sent
assert s.send(data)                       # Send data till true... Will send data until
                                          # A coonection is established. #assertCommand



