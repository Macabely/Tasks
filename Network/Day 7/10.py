import scapy.all as scapy
from datetime import datetime, timedelta
from collections import defaultdict

max_length = 50
max_queries = 100
susqtype = ['TXT', 'CNAME', 'NULL']
offsec = 'eth0'
query_counts = defaultdict(list)

def alert(message):
    print(f"[ALERT!!!] ==> {message}")

def subdomain(domain):
    return len(domain) > max_length

def rate(src_ip):
    now = datetime.now()
    query_counts[src_ip] = [t for t in query_counts[src_ip] if now - t < timedelta(minutes=1)]
    query_counts[src_ip].append(now)
    return len(query_counts[src_ip]) > max_queries

def process(packet):
    if packet.haslayer(scapy.DNSQR):
        src_ip = packet[scapy.IP].src
        query = packet[scapy.DNSQR].qname.decode().lower()
        qtype = packet[scapy.DNSQR].qtype
        qtype_str = scapy.DNS.get_rr(qtype, 'UNKNOWN')

        if subdomain(query):
            alert(f"Suspicious subdomain length detected: {query} from {src_ip}")

        if qtype_str in susqtype:
            alert(f"Suspicious query type {qtype_str} for {query} from {src_ip}")

        if rate(src_ip):
            alert(f"High query rate from {src_ip}: {len(query_counts[src_ip])} queries/min")

def main():
    print("Starting DNS tunneling detection on interface eth0... Press Ctrl+C to stop.")
    try:

        scapy.sniff(iface=offsec, filter="udp port 53", prn=process, store=0)
    except KeyboardInterrupt:
        print("\nStopped DNS tunneling detection.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()