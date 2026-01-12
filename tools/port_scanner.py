from socket import socket, AF_INET, SOCK_STREAM
from concurrent.futures import ThreadPoolExecutor
import logging
import ipaddress
import socket as socket_err

#if a connection can be made then return true. False otherwise
def test_port_number(ip, port):
    s = socket(AF_INET, SOCK_STREAM)
    s.settimeout(3)
    try: 
        s.connect((ip, port))
        s.close()
        return True
    except socket_err.timeout:
        logging.warning(f"Connection timed out on port {port} ({ip})")
        return False
    except socket_err.error:
        logging.warning(f"Port {port} ({ip}) is closed or unreachable.")
        return False
    
    finally:
        s.close()


#Function to scan a list of ports on a given IP address         
def port_scan(ip, ports):
    #Validate IP address
    try:
        ipaddress.ip_address(ip)
    except ValueError:
        print("[!] Invalid IP address format.")
        logging.error(f"Invalid IP address format: {ip}")
        return
    
    print(f"Scanning {ip}...\n")
    logging.info(f"Starting port scan on {ip} for ports: {ports}")

    #use threadpoolexecutor to speed up the process
    with ThreadPoolExecutor(len(ports)) as executor:
        #dispatch all tasks 
        results = executor.map(test_port_number, [ip]*len(ports), ports)
        #results in order
        for port, is_open in zip(ports, results):
            if is_open:
                print(f"> {ip} : {port} Is open \n")
                logging.info(f"Port {port} on {ip} is open.")
            else:
                print(f"> {ip} : {port } Is not open \n")
                

