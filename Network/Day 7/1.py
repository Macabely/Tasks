import subprocess
import concurrent.futures
from ipaddress import ip_network
import socket
import os

def ping_ip(ip):
    cmd = ["ping", "-n", "1", ip] if os.name == "nt" else ["ping", "-c", "1", ip]
    result = subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return ip if result.returncode == 0 else None

def scan_port(ip: str) -> list:
    open_ports = []
    print(f"Scanning {ip} for open ports...")
    try:
        with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
            futures = {
                executor.submit(
                    lambda p: (p, socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect_ex((ip, p))),
                    port
                ): port
                for port in range(1, 65536)
            }
            for future in concurrent.futures.as_completed(futures):
                port = futures[future]
                try:
                    port, result = future.result()
                    if result == 0:
                        open_ports.append(port)
                        print(f"Open port: {ip}:{port}")
                except Exception as e:
                    print(f"Error scanning ports for {ip} : {e}")
    except KeyboardInterrupt:
        print(f"\nPort scan for {ip} stopped by user")
    return open_ports        

def scan_network(network):
    try:    
        ip_list = [str(ip) for ip in ip_network(network, strict=False).hosts()]
        if not ip_list:
            print("No host IPs in the given CIDR range")
            return [], []
    except ValueError as e:
        print(f"Invalid CIDR notation: {e}")
        return [], []
    
    print(f"Searching active IPs...")
    active_ips = []
    open_ports = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        results = executor.map(ping_ip, ip_list)
        active_ips = [ip for ip in results if ip is not None]
        if active_ips:
            print("Active IPs:")
            for ip in active_ips:
                print(ip) 
                ip_open_ports = scan_port(ip)
                open_ports.extend([(ip, port) for port in ip_open_ports])  
                if open_ports:
                    print("\nOpen ports found:")
                    for ip, port in open_ports:
                        print(f"{ip}:{port}")
                else:
                    print(f"\nNo open ports found for {ip}.") 
            return active_ips, open_ports           
        else:
            print("No active IPs found.")
            return [], []   

if __name__ == "__main__":
    try:
        ip_range = input("Enter IP range (e.g., 192.168.1.0/24): ")
        scan_network(ip_range)
    except ValueError as e:
        print(f"Error: {e}")