# import scapy.all as scapy
# from datetime import datetime

# def test(sub, offsec):
#     try:
#         arp_request = scapy.ARP(pdst=sub)
#         broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
#         arp_packet = broadcast / arp_request
#         answered_list = scapy.srp(arp_packet, timeout=2, iface=offsec, verbose=False)[0]
#         devices = [{"ip": pkt[1].psrc, "mac": pkt[1].hwsrc} for pkt in answered_list]
        
#         print("Devices found:")
#         with open("logs.txt", "a") as f:
#             f.write(f"^^^   {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}   ^^^\n")    
#             for d in devices:
#                 print(f"IP: {d['ip']} <==> MAC: {d['mac']}")
#                 f.write(f"IP: {d['ip']} <==> MAC: {d['mac']}\n") 
#             if not devices:
#                 print("No devices found.")
#                 f.write("No devices found.\n")
#         return devices
#     except Exception as e:
#         print(f"Error: {e}")
#         return []

# sub = "192.168.1.0/24"
# offsec = "Ethernet"
# test(sub, offsec)    

import subprocess
import concurrent.futures
from ipaddress import ip_network
import os
from datetime import datetime

def ping_ip(ip):
    cmd = ["ping", "-n", "1", ip] if os.name == "nt" else ["ping", "-c", "1", ip]
    result = subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return ip if result.returncode == 0 else None

def scan_network(network):
    try:
        ip_list = [str(ip) for ip in ip_network(network, strict=False).hosts()]
        with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
            results = executor.map(ping_ip, ip_list)
            active_ips = [ip for ip in results if ip is not None]
        with open("logs.txt", "a") as f:
            f.write(f"^^^   {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}   ^^^\n")
            for ip in active_ips:
                f.write(f"IP: {ip}\n")
            if not active_ips:
                f.write("No active IPs found.\n")    
        return active_ips
    except Exception as e:
        print(f"Error: {e}")
        return []

if __name__ == "__main__":

    ip_range = input("Enter your CIDR: ")
    active_ips = scan_network(ip_range)
    if active_ips:
        print("Active IPs:")
        for ip in active_ips:
            print(ip)
    else:
         print("No active IPs found.")
