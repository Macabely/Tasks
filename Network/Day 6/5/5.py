import scapy.all as scapy

def test(ip):
    try:
        arp_request = scapy.ARP(pdst=ip)
        broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        arp_packet = broadcast / arp_request
        answered_list = scapy.srp(arp_packet, timeout=2, verbose=False)[0]
        return answered_list[0][1].hwsrc if answered_list else None
    except:
        return None

def best(pkt):
    if pkt.haslayer(scapy.ARP) and pkt[scapy.ARP].op == 2:
        real_mac = test(pkt[scapy.ARP].psrc)
        response_mac = pkt[scapy.ARP].hwsrc
        if real_mac and response_mac and real_mac != response_mac:
            print(f"[!] ARP spoofing detected! IP: {pkt[scapy.ARP].psrc}, Real MAC: {real_mac}, Spoofed MAC: {response_mac}")
        else:
            print(f"[+] ARP OK: IP {pkt[scapy.ARP].psrc}, MAC {response_mac}")

offsec = "Ethernet"
print(f"[*] Starting detection on {offsec}...")
try:
    scapy.sniff(iface=offsec, store=False, prn=best)
except KeyboardInterrupt:
    print("\n[*] Stopping...")
except:
    print(f"[!] Error sniffing on {offsec}")