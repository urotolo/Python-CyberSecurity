#!/usr/bin/py

# This client-side script is the sending counter part 
# to the add_server script: Which stays on the receiving end of data.
# Sends a couple numbers in string format to be summarized.

import socket

s = socket.socket()                         # Create TCP connection object
numericGiftForGenerousHostServer = "55, 34" # Servers dont get paid enough, a gift with numberic value.
                                            # In string format, all the server has to do is cash it to int value
                                            # and count up the money I have sent for generously hosting and personally connecting with me.
host = socket.gethostname()                 # Chooses machine to chat with
port = 12345                                # Chooses machine:port to access

s.connect((host, port))

s.send(numericGiftForGenerousHostServer)    # Send gift
data = s.recv(1024)                         # receive server response
print data

s.close()    


