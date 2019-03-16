#!/usr/bin/py

# State - Currently being worked on
# Design plan: So it functions well, only problem is I cannot figure out how to 
# return the state of the scanned ports.
# Potential solution: Go to google and look up how to use python-nmap so it returns
# whether a port is open or closed. How to make python-nmap return the 'state' of each scanned port.
# Note - python-nmap has the same function as bash nmap, but has different design vectors. Keep this in mind.

import nmap
# import optparse


def nmapScan(tgtHost, tgtPort):
    nmScan = nmap.PortScanner()
    nmScan.scan(tgtHost, tgtPort)
    # state=nmapScan[tgtHost]['tcp'][int(tgtPort)]['state']
    print " [*] " + tgtHost + "tcp/" + tgtPort + " "                # + state 

def main():
    ipAddress = str(raw_input("Enter ip address of victim target: "))
    portsToCrush =str(raw_input("Enter ports of victim target: "))
    portList = portsToCrush.split(",")
    for port in portList:
        nmapScan(ipAddress, port)

if __name__ == '__main__':
    main()

        


