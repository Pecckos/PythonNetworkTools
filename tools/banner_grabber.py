import socket 
import logging
import ipaddress

#Function to grab banner from a given IP and port
#AF_INET = IPV4 32bits Ip adresses. 
#SOCK_STREAM = TCP
def banner_grabber(ip, port):
    #Validate IP address
    try:
        ipaddress.ip_address(ip)
    except ValueError:
        print("[!] Invalid IP address format.")
        logging.error(f"Invalid IP address format: {ip}")
        return
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(3)

    try:
        s.connect((ip, port))
        banner = s.recv(64)

        if banner:
            decoded = banner.decode(errors="ignore")
            print(f"{ip}:{port} -> Banner: {banner.decode(errors="ignore")}")
            logging.info(f"Banner from {ip}:{port}: {banner.decode(errors='ignore')}")
        else:
            print(f"{ip}:{port} -> Port open, but no banner received.")
            logging.warning(f"No banner received from {ip}:{port}")

    except socket.timeout:
        print(f"{ip}:{port} -> Connection timed out.")
        logging.warning(f"Connection to {ip}:{port} timed out.")

    except socket.error as e:
        print(f"{ip}:{port} -> Socket error: {e}")
        logging.warning(f"Connection failed on {ip}:{port} -> {e}")

    except Exception as e:
        print(f"{ip}:{port} -> Error: {e}")
        logging.error(f"Error grabbing banner from {ip}:{port} -> {e}")

    finally:
        s.close()