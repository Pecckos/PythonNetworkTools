from socket import SOCK_STREAM
from socket import AF_INET
import socket 
from concurrent.futures import ThreadPoolExecutor

#Get maximum 1024 bytes from the socket, convert to text and trim it.
def banner_grabber(ip, port):
    try:
        with socket.socket(AF_INET, SOCK_STREAM) as sock:
            sock.settimeout(3)
            sock.connect((ip, port))
            banner = sock.recv(1024).decode(errors='ignore').strip()
            if banner:
                print(f'[-] {ip}: {port} -> {banner}')
            else:
                print(f'[-] {ip}: {port} -> No banner, but port is open')
    except socket.timeout:
            print(f'[-] {ip}:{port} -> Timed out (port might be open but silent)')
    except Exception as e:
        print(f'[-] {ip}: {port} -> Error ({e})')


