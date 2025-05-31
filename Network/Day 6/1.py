from scapy.all import TCP, IP, UDP, ICMP, sniff, threading
from datetime import datetime

offsec = "eth0" 

def test(pkt):

    try:
        if IP in pkt:
            pr = "Unknown"
            sport, dport = "N/A", "N/A"
            
            if TCP in pkt:
                pr = "TCP"
                sport = pkt[TCP].sport
                dport = pkt[TCP].dport
            elif UDP in pkt:
                pr = "UDP"
                sport = pkt[UDP].sport
                dport = pkt[UDP].dport
            elif ICMP in pkt:
                pr = "ICMP"
            
            t = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"[{t}] {pr} packet. {pkt[IP].src}:{sport} -> {pkt[IP].dst}:{dport} (Size: {len(pkt)} bytes)")
    except Exception as e:
        print(f"Error: {e}")

def best():
    print(f"Capturing packets running")
    try:
        sniff(iface=offsec, prn=lambda pkt: threading.Thread(target=test, args=(pkt,), daemon=True).start(), store=0)
    except KeyboardInterrupt:
        print(f"script Stopped")
    except Exception as e:
        print(f"Error: {e}")
best()