import subprocess
import concurrent.futures
from ipaddress import ip_network
import os

def ping_ip(ip):
    cmd = ["ping", "-n", "1", ip] if os.name == "nt" else ["ping", "-c", "1", ip]
    result = subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return ip if result.returncode == 0 else None

def scan_network(network):
    ip_list = [str(ip) for ip in ip_network(network, strict=False).hosts()]
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        results = executor.map(ping_ip, ip_list)
        active_ips = [ip for ip in results if ip is not None]
    return active_ips

if __name__ == "__main__":
    try:
        ip_range = input("Enter IP range (e.g., 192.168.1.0/24): ")
        active_ips = scan_network(ip_range)
        if active_ips:
            print("Active IPs:")
            for ip in active_ips:
                print(ip)
        else:
            print("No active IPs found.")
    except ValueError as e:
        print(f"Error: Invalid IP range. Example: 192.168.1.0/24")