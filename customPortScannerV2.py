#!/usr/bin/py

# A improved version from the port scanner I wrote
# in bash located in /root/usefulBashScripts.
# However nmap standard is still a more effective tool
# then my port scanner here I have built.
# I learned that this was inferior to nmap after 
# running a few comparative open/close port 
# status test in order to see which port scanner was
# more accurate and more able to detect open ports.
# My calculations tell me that it is the case that
# nmap, the port scanner to rule all port scanners
# remains supreme.

from socket import *
from threading import *



screenLock = Semaphore(value=1)
def connScan(tgtHost, tgtPort):
    try:
        connSkt = socket(AF_INET, SOCK_STREAM)
        connSkt.connect((tgtHost, tgtPort))
        connSkt.send('ViolentPython\r\n')
        results = connSkt.recv(100)
        screenLock.acquire()
        print '[+]%d/tcp open'% tgtPort
        print '[+] ' + str(results)
        connSkt.close()
    except:
        screenLock.acquire()
        print '[-]%d/tcp closed: ' +  str(tgtPort)
    finally:
        screenLock.release()
        connSkt.close()

def portScan(tgtHost, tgtPort):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print "[-] Cannot resolve '%s': Unknown host"%tgtHost
        return
    try:
        tgtName = gethostbyaddr(tgtIP)
        print '\n[+] scan Results for: ' + tgtName[0]
    except:
        print '\n[+] Scan Results for: ' + tgtIP
    setdefaulttimeout(1)
    t = Thread(target=connScan, args=(tgtHost, int(tgtPort)))  # Error
    t.start()
        
def main():
    print 'Enter IP address to investigate: '
    ipAddress = str(raw_input())
    print 'Enter port(s) to investigate: '
    ports = str(raw_input())
    portList = ports.split(',')
    for port in portList:
        portScan(ipAddress, port)  # Error
    
if __name__ == '__main__':
    main()                         # Error
