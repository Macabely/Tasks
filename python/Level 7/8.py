from scapy.all import sniff, IP

def packet_callback(packet):
    if IP in packet:
        layer = packet[IP]
        protocol = layer.proto
        src_ip = layer.src
        dst_ip = layer.dst

        name = ""
        if protocol == 1:
            name = "ICMP"
        elif protocol == 6:
            name = "TCP"
        elif protocol == 17:
            name = "UDP"
        else:
            name = "OUT OF RANGE"  
        print(f"Protocol: {name}")
        print(f"Source IP: {src_ip}")
        print(f"Destination IP: {dst_ip}")
        print("#" * 25)

print("Packet sniffer starting ~ Press Ctrl+C to stop.")
sniff(filter="ip", prn=packet_callback, store=0, count=10)