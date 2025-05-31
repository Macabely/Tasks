import scapy.all as scapy
import time
from datetime import datetime

LOG = "lgos.txt"
devices = set()
sub = "192.168.1.0/24"
offsec = "Ethernet"

def log(msg):
    t = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    b = f"[{t}] {msg}\n"
    print(b.strip())
    with open(LOG, "a") as f:
        f.write(b)

def test(sub, offsec):
    try:
        
        arp_request = scapy.ARP(pdst=sub)
        broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        arp_packet = broadcast / arp_request
        answered_list = scapy.srp(arp_packet, timeout=2, iface=offsec, verbose=False)[0]
        
        print("Devices found:")
        for _, r in answered_list:
            ip = r.psrc
            mac = r.hwsrc
            new = f"{ip} <==> {mac}"
            if new not in devices:
                devices.add(new)
                log(f"New device detected - IP: {ip}, MAC: {mac}")
    except Exception as e:
        log(f"Error in scan: {e}")
        return

try:
    while True:
        test(sub, offsec)
        print(f"Next scan in 3 hours")
        time.sleep(3 * 60 * 60)
except KeyboardInterrupt:
    print("\nScanning stopped")
except Exception as e:
    print(f"Error: {e}")   
       