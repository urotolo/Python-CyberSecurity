#!/usr/bin/py



import nmap


host = str(raw_input("Enter a ip address that you wish to scan: "))
ports = str(raw_input("Enter a port or port(s) that you wish to scan: "))

nmScan = nmap.PortScanner()
nmScan.scan(host, ports)

print ' '
print "Type of scan conducted: " + str(nmScan.scaninfo())
print " "

portList = ports.split(',')
for port in portList:
    print "Scan results for port: " + port + str(' ') + str(nmScan[host]['tcp'][int(port)])


