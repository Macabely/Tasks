from scapy.all import sniff, DNS, IP

qur = {
    1: "A",
    2: "NS",
    5: "CNAME",
    12: "PTR",
    15: "MX",
    28: "AAAA",
}

print("Sniffing starting...")
def test(pkt):
    try:
        if pkt.haslayer(DNS) and pkt.haslayer(IP):
            s = pkt[IP].src
            d = pkt[IP].dst
            dns = pkt[DNS]
            
            if dns.qr == 0 and dns.qd:
                name = dns.qd.qname.decode(errors="ignore").rstrip(".")
                typ = dns.qd.qtype
                typstr = qur.get(typ, f"Type {typ}")
                print(f"Query from {s} to {d}: {name} ({typstr})")
            else:
                pass
    except Exception as e:
        print(f"Error {e}")

sniff(iface="eth0", filter="port 53", prn=test, store=0)