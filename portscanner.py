# Title: portscanner v.1 - Port Scanner
# Date: March 15, 2022
# Author: Ethan Frazier
# Version: portscanner v.1

#!/bin/usr/python3

from termcolor import colored
from socket    import socket
from os        import system

def scan(target, ports):
    print('\n' + ' Starting Scan For ' + str(target))
    for port in range(1,ports):
        scan_port(target,port)

def scan_port(ipaddress, port):
    try: # to connect to a certain address and port
        sock = socket() # initalize the socket object
        sock.connect((ipaddress, port))
        print("[+] Port Opened " + str(port))
        sock.close()
    except: # it didn't connect {closed, filtered, or ignored ports}
        pass

def main():
    ''' Main logic of the program '''
    system("clear")
    print(colored(("Port Scanner v.1 by Ethan Frazier \n"), 'red'))

    targets = input("[*] Target(s) To Scan: ")
    ports = int(input("[*] How Many Ports: "))
    if ',' in targets:
        print(colored(("[*] Scanning Multiple Targets"), 'green'))
        for ip_addr in targets.split(','):
            scan(ip_addr.strip(' '),ports)
    else:
        scan(targets,ports)

if __name__ == '__main__':
    main()
