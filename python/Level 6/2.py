import socket

target = "scanme.nmap.org"

for port in range(20, 101):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ports = s.connect_ex((target, port))
    if ports == 0:
        print(f"Port {port} is open")
    s.close()
print("Scan finished successfully")    