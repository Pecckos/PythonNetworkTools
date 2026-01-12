from socket import socket, AF_INET, SOCK_STREAM
from concurrent.futures import ThreadPoolExecutor

#if a connection can be made then return true. False otherwise
def test_port_number(ip, port):
    s = socket(AF_INET, SOCK_STREAM)
    s.settimeout(3)
    try: 
        s.connect((ip, port))
        s.close()
        return True
    except:
        return False
        
  #Function to scan a list of ports on a given IP address         
def port_scan(ip, ports):
    print(f"Scanning {ip}...\n")
    #use threadpoolexecutor to speed up the process
    with ThreadPoolExecutor(len(ports)) as executor:
        #dispatch all tasks 
        results = executor.map(test_port_number, [ip]*len(ports), ports)
        #results in order
        for port, is_open in zip(ports, results):
            if is_open:
                print(f"> {ip} : {port} Is open \n")
            else:
                print(f"> {ip} : {port } Is not open \n")

