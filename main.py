
"""
PythonNetworkTools
Main entry point for the application.

Author: Jessica Bjurlerstam
Date: 2026-01-07
"""

# A simple comment from the Applied Script class partner since it is required
import sys
import platform
import socket
import logging
import argparse
from tools import ip_tracker, port_scanner, banner_grabber
from utils.logging import setup_logging
from pyfiglet import Figlet

#This function prints a stylized banner using the pyfiglet library
def print_banner():
    banner = Figlet(font="slant")
    print(banner.renderText("Pecckos CyberTools"))

#This function checks if the operating system is Linux, exiting if it is not
def check_os():
    if platform.system() != "Linux":
        print("This tool is only supported on Linux systems.")
        sys.exit(1)

    logging.info("Operating system check passed.")

#This function checks for an active internet connection by attempting to connect to a well-known DNS server, exiting if the connection fails
def check_internet_connection():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        logging.info("Internet connection check passed.")
    except OSError:
        print("No internet connection detected. Please check your connection and try again.")
        logging.error("No internet connection detected.")
        sys.exit(1)
        
def print_menu():
    print('\n')
    print('"""[MENUE]""" \n' \
    '1. IP Tracker \n' \
    '2. PortScanner \n' \
    '3. Banner Grabber \n' \
    '4. Stop the program \n'
    '"""""""""""""""""""\n')

#This function runs the IP tracker tool from an API and saves the results to a file
def run_ip_tracker():
    ip = input("Enter a IP-Adress to track: ").strip()
    ip_tracker.get_info_by_ip(ip)

    logging.info(f"IP Tracker run for IP: {ip}")

#This function runs the port scanner on a list of common ports
def run_port_scanner():
    ip = input("Enter a IP Adress to scan: ").strip()
    port = [21, 22, 23, 25, 53, 80, 110, 143, 443, 445, 
                3306, 3389, 5432, 5900, 8080, 8443, 9200, 27017, 50070]
    port = port_scanner.port_scan(ip, port)
    logging.info(f"Port Scanner run for IP: {ip}")

#This function runs the banner grabber on a list of common ports
def run_banner_grabber():
    ip = input("Enter a IP-Adress to scan: ").strip()
    ports = [21, 22, 23, 25, 53, 67, 68, 80, 110, 123, 139, 143, 443, 445, 3389, 8080]
    for port in ports:
        banner_grabber.banner_grabber(ip, port)
    logging.info(f"Banner Grabber run for IP: {ip}")
        
#This function handles the argument parsing for the script
def argument_parser():
    """
    Handles command-line arguments for the script.

    Supported arguments:
    -h / --help     Displays help and usage information
    -v / --version  Displays program version and developer information
    """
    parser = argparse.ArgumentParser(
        description=(
            "Pecckos PythonNetworkTools\n"
            "A menu-driven toolkit for basic network reconnaissance tasks.\n\n"
            "Example usage:\n"
            "  python3 main.py\n"
            "  python3 main.py --version"
        ),
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument("-v", "--version", action="version", version="Pecckos CyberTools Version 1.0 | Developed by Peccko ")
    parser.parse_args()
    logging.info("Argument parsing completed.")
    
#The main function is the execution of the script, including environment checks and user interaction
def main():
    argument_parser()
    #check_os()
    check_internet_connection()
    print("Environment check passed. Starting the tool...\n")
    setup_logging()
    logging.info("Program started.")

    print_banner()
    while True:
        print_menu()
        choice = input("Select an option: ").strip()
        logging.info(f"User selected option: {choice}")

        if choice == "1":
            run_ip_tracker()
        elif choice == "2":
            run_port_scanner()
        elif choice == "3":
            run_banner_grabber()
        elif choice == "4":
            print("Closing program")
            sys.exit()
        else:
            print("Wrong choice, try again!")

#Entry point of the script
if __name__ == "__main__":
    main()  
    
