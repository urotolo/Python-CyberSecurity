#!/usr/bin/py

# Connect to url/ip address and gain information on underlying server

import socket

print 'Enter Url in this format "www.example.com"'
ipAddressToExploit = str(raw_input("Enter a website Url and I will tell you about its servers: "))

request = b"GET / HTTP/1.1\nHost: " + ipAddressToExploit + "\n\n"

connectTo = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connectTo.connect((str(ipAddressToExploit), 80))
connectTo.send(request)
result = connectTo.recv(10000)
while len(result) > 0:
    print(result)
    result = connectTo.recv(10000)

print 'Connection established too', connectTo




