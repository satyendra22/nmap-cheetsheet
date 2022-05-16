#!/usr/bin/python3

import nmap

scanner = nmap.PortScanner()

print("Welcome, NAMP SCANNER AUTOMATION TOOL")
print("---------------------------------------------")

ipAddr = input("ENTER IP ADDRESS FOR SCAN: ")
print("IP ADDRESS ENTERED AS: ", ipAddr)
type(ipAddr)

scanType = input("""\nPLEASE ENTER TYPE OF SCAN YOU WANT TO RUN:
                1)SYN ACK SCAN
                2)UDP SCAN
                3)Comprehensive SCAN \n""")
print("YOUR SELECTED OPTION IS: ", scanType)

if scanType == '1':
    print("NMAP VERSION: ", scanner.nmap_version())
    scanner.scan(ipAddr, '1-65535', '-v -sS')
    print(scanner.scaninfo())
    print("IP STATUS: ", scanner[ipAddr].state())
    print(scanner[ipAddr].all_protocols())
    print("OPEN PORTS: ", scanner[ipAddr]['tcp'].keys())
elif scanType == '2':
    print("NMAP VERSION: ", scanner.nmap_version())
    scanner.scan(ipAddr, '1-65535', '-v -sU')
    print(scanner.scaninfo())
    print("IP STATUS: ", scanner[ipAddr].state())
    print(scanner[ipAddr].all_protocols())
    print("OPEN PORTS: ", scanner[ipAddr]['udp'].keys())
elif scanType == '3':
    print("NMAP VERSION: ", scanner.nmap_version())
    scanner.scan(ipAddr, '1-65535', '-v -sS -sV -sC -A -O')
    print(scanner.scaninfo())
    print("IP STATUS: ", scanner[ipAddr].state())
    print(scanner[ipAddr].all_protocols())
    print("OPEN PORTS: ", scanner[ipAddr]['tcp'].keys())
elif scanType >= '4':
    print("PLEASE ENTER VALID OPTION")

