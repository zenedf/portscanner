# Title: portscanner v.1 - Port Scanner
# Date: March 15, 2022
# Author: Ethan Frazier
# Version: portscanner v.1

#!/bin/usr/python3

from socket    import socket
from os        import system, name

def which_os():
    if name == 'nt':
        return 'windows'
    if name == 'posix':
        return 'linux' # mac/linux/BSD

def clear_screen():
    if which_os() == 'windows':
        system("cls")
    if which_os() == 'linux':
        system("clear")

def introduction():
    clear_screen()
    print("Port Scanner v.1 by Ethan Frazier \n")

def scan(target, ports):
    print('\n' + ' Starting Scan For ' + str(target))
    for port in range(1,ports):
        scan_port(target,port)

def scan_port(ipaddress, port):
    try: # to connect to a certain address and port
        sock = socket() # new socket object
        sock.connect((ipaddress, port))
        print("[+] Port Opened " + str(port))
        sock.close()
    except: # it didn't connect {closed, filtered, or ignored ports}
        pass

def main():
    ''' Main logic of the program '''
    introduction()

    targets = input("[*] Target(s) To Scan: ")
    ports = int(input("[*] How Many Ports: "))
    if ',' in targets:
        print("[*] Scanning Multiple Targets")
        for ip_addr in targets.split(','):
            scan(ip_addr.strip(' '),ports)
    else:
        scan(targets,ports)

if __name__ == '__main__':
    main()
