import socket

target = "127.0.0.1"

for port in range(0, 1000):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ports = s.connect_ex((target, port))
    if ports == 0:
        print(f"Port {port} is open")
        print("Scan starting...")
    s.close()
print("Scan finished successfully")    