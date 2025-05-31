import socket
import concurrent.futures

def test():
    target = input("Target to scan: ")
    try:
        ip = socket.gethostbyname(target)
    except:
        return "Invalid target"

    print(f"Scanning {ip} for all TCP ports...")
    try:
        with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
            for port in range(1, 65536):
                executor.submit(lambda p: print(f"Open port: {p}") 
                if socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect_ex((ip, p)) == 0 
                else None, port)
    except KeyboardInterrupt:
        print("\nScan stopped by user")
        executor._threads.clear()

print(test())