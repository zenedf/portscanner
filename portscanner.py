# Title: portscanner v.1 - Port Scanner
# Date: March 15, 2022
# Author: Ethan Frazier
# Version: portscanner v.1

#!/bin/usr/python3

from termcolor import colored
from socket    import socket
from os        import system, name


def scan_port(ipaddress, port):
    try:
        sock = socket() # create socket object
        sock.connect((ipaddress, port)) # attempt connection
        print("[+] Port Opened " + str(port))
        sock.close()
    except: 
        pass # it didn't connect {closed, filtered, or ignored ports}

def scan(target, ports):
    print(colored(('\n' + '[>] Starting Scan For ' + str(target)),'green'))
    for port in range(1,ports+1):
        scan_port(target,port)

def clear_screen():
    if name != "posix": # if windows
         system("cls")
         return
    system("clear")

def introduction():
    clear_screen()
    print(colored(("Port Scanner v.1 by Ethan Frazier \n"), 'cyan'))

def end_program():
    n = input('\nPRESS ENTER TO EXIT...')

def main():
    introduction()
    targets = input("[*] Target(s) To Scan: ")
    ports = int(input("[*] How Many Ports: "))
    if ',' in targets:
        print("[*] Scanning Multiple Targets")
        for ip_addr in targets.split(','):
            scan(ip_addr.strip(' '),ports)
    else:
        scan(targets,ports)
    end_program()

if __name__ == '__main__':
    main()