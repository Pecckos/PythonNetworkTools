from socket import AF_INET
from socket import SOCK_STREAM
from socket import socket 
from concurrent.futures import ThreadPoolExecutor

#if a connection can be made then return true. False otherwise
def test_port_number(host, port):
    #create and configure the socket
    with socket(AF_INET, SOCK_STREAM) as sock:
        #set a timeout a few seconds
        sock.settimeout(3)
        #connection may fail
        try:
            sock.connect((host, port))
            #succesful connection was made 
            return True
        except:
        #ignore the failure
            return False
        
 #scan port number on a host       
def port_scan(host, ports):
    print(f'Scanning {host}...')
    #create thread pool
    with ThreadPoolExecutor(len(ports)) as executor:
        #dispatch all tasks 
        results = executor.map(test_port_number, [host]*len(ports), ports)
        #results in order
        for port, is_open in zip(ports, results):
            if is_open:
                print(f'> {host} : {port} is open \n')

