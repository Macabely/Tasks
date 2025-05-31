import socket
import concurrent.futures
import os

def test():
    target = input("Target to scan: ")
    try:
        ip = socket.gethostbyname(target)
    except:
        return "Invalid target"

    print(f"Scanning {ip} for all UDP ports...")
    def scan(p):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.settimeout(1.5)
            s.sendto(b"", (ip, p)) 
            s.recvfrom(1024)  
            s.close()
            return True
        except (socket.timeout, socket.error):
            s.close()
            return False

    try:
       
        with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
            for port in range(1, 65536):
                executor.submit(lambda p: print(f"Open port: {p}") if scan(p) else None, port)
    except KeyboardInterrupt:
        print("\nScan stopped by user")
        executor._threads.clear()
        os._exit(0)
test()