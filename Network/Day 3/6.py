from scapy.all import TCP, sniff, IP
from datetime import datetime
import socket, threading

HOST, PORT, LOG = "127.0.0.1", 9999, "tcp.log"

def log(msg):
    t = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    b = f"[{t}] {msg}\n"
    print(b.strip())
    with open(LOG, "a") as f:
        f.write(b)

def monitor():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(5)
    log(f"Listening on {HOST}:{PORT}")

    def completed():
        while True:
            c, (ip, port) = s.accept()
            log(f"Completed from {ip}:{port}")
            c.close()

    def raw(pkt):
        if pkt.haslayer(TCP) and pkt[IP].dst == HOST and pkt[TCP].dport == PORT and pkt[TCP].flags & 0x02:
            log(f"SYN from {pkt[IP].src}:{pkt[TCP].sport}")

    threading.Thread(target=completed, daemon=True).start()
    try:
        sniff(filter=f"tcp and dst port {PORT}", prn=raw, store=0, iface="lo")
    except KeyboardInterrupt:
        log("Stopped")


open(LOG, "w").close()
monitor()