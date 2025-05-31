from scapy.all import TCP, IP, sniff, threading, Raw
from datetime import datetime

offsec = "eth0" 

def test(pkt):
    try:
        t = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if IP in pkt and TCP in pkt:
            s = pkt[IP].src
            d = pkt[IP].dst
            sport = pkt[TCP].sport
            dport = pkt[TCP].dport
            if dport == 80:
                if Raw in pkt:
                    p = pkt[Raw].load.decode('utf-8', errors='ignore')
                    methods = ['GET', 'POST', 'HEAD', 'PUT', 'DELETE', 'OPTIONS']
                    if any(p.startswith(method) for method in methods):
                        lines = p.split('\r\n')
                        if lines:
                            print(t)
                            req = lines[0]
                            headers = [line for line in lines[1:] if line and ': ' in line]  
                            bd = p.find('\r\n\r\n') + 4
                            body = p[bd:] if bd < len(p) else ""
                            print(f"Request from {s}:{sport} To {d}:{dport}")
                            print(req)
                            if headers:
                                for header in headers:
                                    print(f"{header}")
                            elif body:
                                print(f"{body}")                                    
                            print('^' * 30)
            if sport == 80:
                if Raw in pkt:
                    p = pkt[Raw].load.decode('utf-8', errors='ignore')
                    if p.startswith("HTTP/"):
                        lines = p.split('\r\n')
                        if lines:
                            res = lines[0]
                            headers = [line for line in lines[1:] if line and ': ' in line]
                            bd = p.find('\r\n\r\n') + 4
                            body = p[bd:bd+100] if bd < len(p) else ""
                            print(f"Response from {s}:{sport} To {d}:{dport}")
                            print(f"{res}")
                            if headers:
                                for header in headers:
                                    print(f"{header}")
                            if body:
                                print(f"{body}")
                            print("*" * 30)                                
    except Exception as e:
        print(f"Error {e}")
                             
def best():
    print(f"Capturing packets running")
    try:
        sniff(iface=offsec, prn=lambda pkt: threading.Thread(target=test, args=(pkt,), daemon=True).start(), store=0)
    except KeyboardInterrupt:
        print(f"script Stopped")
    except Exception as e:
        print(f"Error: {e}")
best()                      