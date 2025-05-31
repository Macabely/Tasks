from scapy.all import TCP, UDP, sniff, IP, Ether
from datetime import datetime

offsec = "lo"
packets = set()
def log(msg):
    t = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    b = f"[{t}] {msg}\n"
    print(b.strip())

def test(pkt):

    if Ether in pkt and pkt[Ether].dst == "ff:ff:ff:ff:ff:ff":
        print("Broadcast packet")
        
    if IP in pkt:
        d = pkt[IP].dst
        if d == "255.255.255.255":
            return True
        if d.endswith(".255"):
            return True
    return False
                   
def best(pkt):

    try:
        if not test(pkt):
            return
        
        if Ether in pkt and IP in pkt:
            id = (pkt[Ether].src, pkt[Ether].dst, pkt[IP].src, pkt[IP].dst, pkt[IP].id if IP in pkt else 0)
            if id in packets:
                return
            packets.add(id)

        if IP in pkt and Ether in pkt:
            s = pkt[IP].src
            d = pkt[IP].dst
            smac = pkt[Ether].src
            dmac = pkt[Ether].dst
        proto = "unknown"
        data = ""
        if UDP in pkt and IP in pkt:
            proto = "UDP"
            sport = pkt[UDP].sport
            dport = pkt[UDP].dport
            data = f"From port: {sport} to: {dport}"
            if dport == 67 or dport == 68:
                data += f"DHCP"

        elif TCP in pkt:
            proto = "TCP"
            sport = pkt[TCP].sport
            dport = pkt[TCP].dport
            data = f"TCP packet "
        elif pkt.haslayer("ARP"):
            proto = "ARP"
            data = f"Operation: {pkt['ARP'].op}"

        log(f"Broadcast packet petected")
        log(f"Source MAC: {smac}, Destination MAC: {dmac}")
        log(f"Source IP: {s}, Destination IP: {d}")
        log(f"Protocol: {proto}")
        if data:
            log(f"Details: {data}")
        log("-" * 50)
    except Exception as e :
        print(f"Error {e}")

def monitor():

    log(f"Listening for broadcast messages on {offsec}...")
    try:
        sniff(iface=offsec, filter="udp or tcp or arp", prn=best, store=0, timeout=10)
        log("Finished listening for broadcast messages")
    except Exception as e:
        log(f"Error during packet capture: {e}")

    except KeyboardInterrupt:
        log("Stopped")	    

monitor()