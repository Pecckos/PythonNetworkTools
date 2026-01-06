import socket 

# Function to grab banner from a given IP and port
# AF_INET = IPV4 32bits Ip adresses. 
# SOCK_STREAM = TCP
def banner_grabber(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(3)

    try:
        s.connect((ip, port))
        banner = s.recv(64)

        if banner:
            print(f"{ip}:{port} -> Banner: {banner.decode(errors="ignore")}")
        else:
            print(f"{ip}:{port} -> Port open, but no banner received.")

    except socket.timeout:
        print(f"{ip}:{port} -> Connection timed out.")

    except Exception as e:
        print(f"{ip}:{port} -> Error: {e}")

    s.close()