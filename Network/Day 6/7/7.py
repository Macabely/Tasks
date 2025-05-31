from scapy.all import TCP, select, sniff, IP
from datetime import datetime
import socket

HOST, PORT, LOG = "127.0.0.1", 9999, "tcp.log"
packets = set()
def log(msg):
    t = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    b = f"[{t}] {msg}\n"
    print(b.strip())
    with open(LOG, "a") as f:
        f.write(b)

def test(pkt):
    try:
        if IP in pkt and TCP in pkt:
            s = pkt[IP].src
            d = pkt[IP].dst
            sport = pkt[TCP].sport
            dport = pkt[TCP].dport
            seq = pkt[TCP].seq
            ack = pkt[TCP].ack
            flags = pkt[TCP].flags
            if dport == PORT or sport == PORT:
                id = (s, d, sport, dport, seq, ack, flags)
                if id in packets:
                    return 
                packets.add(id)

                syn = 0x02      
                synack = 0x12  
                ackk = 0x10    

                if flags == syn:
                    log(f"SYN from {s}:{sport} To {d}:{dport}")
                    log(f"SYN packet")
                    log(f"seq number: {seq}")
                    log(f"ack number: {ack}")
                
                if flags == synack:
                    log(f"SYN-ACK from {s}:{sport} To {d}:{dport}")
                    log(f"SYN-ACK packet")
                    log(f"seq number: {seq}")
                    log(f"ack number: {ack}")
                
                if flags == ackk:
                    if sport == PORT:
                        return
                    log(f"ACK from {s}:{sport} To {d}:{dport}")
                    log(f"ACK packet")
                    log(f"seq number: {seq}")
                    log(f"ack number: {ack}")
    except Exception as e:
         print(f"Error {e}")                     


def monitor():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(5)
    log(f"Listening for TCP packets on {HOST}:{PORT}")

    try:

        sniff(filter=f"tcp and (dst port {PORT} or src port {PORT})", prn=test, store=1, iface="lo", timeout=10)
        
        r, _, _ = select.select([s], [], [], 0)
        if s in r:
            c, (ip, port) = s.accept()
            log(f"TCP Connection from {ip}:{port}")
            data = c.recv(4096)
            if data:
                log(f"Data received: {data.decode()}")
            c.close()

    except KeyboardInterrupt:
        log("Stopped")	    

open(LOG, "w").close()
monitor()