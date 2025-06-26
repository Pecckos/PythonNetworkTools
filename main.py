import sys
from tools import ip_tracker
from tools import port_scanner
from tools import banner_grabber
from pyfiglet import Figlet

def print_banner():
    banner = Figlet(font='slant')
    print(banner.renderText('Pecckos CyberTools'))

def print_menu():
    print('"""[MENUE]""" \n' \
    '1. IP Tracker \n' \
    '2. PortScanner \n' \
    '3. Banner Grabber \n' \
    '4. Stop the program \n'
    '"""""""""""""""""""')

def run_ip_tracker():
    ip = input('Enter a IP-Adress to track: 3').strip()
    ip_tracker.get_info_by_ip(ip)

def run_port_scanner():
    ip = input('Enter a IP Adress to scan: ').strip()
    port = range(1024)
    port = port_scanner.port_scan(ip, port)

def run_banner_grabber():
    ip = input('Enter a IP-Adress to scan: ').strip()
    ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445, 3389, 8080]
    for port in ports:
        banner_grabber.banner_grabber(ip, port)

def main():
    print_banner()
   
    while True:
        print_menu()
        choice = input('Select an option: ').strip()

        if choice == "1":
            run_ip_tracker()
        elif choice == "2":
            run_port_scanner()
        elif choice == "3":
            run_banner_grabber()
        elif choice == "4":
            print('Closing program')
            sys.exit(3)
        else:
            print('Wrong choice, try again!')

if __name__ == "__main__":
    main()  