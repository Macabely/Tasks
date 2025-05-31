import scapy.all as scapy

def test(sub, offsec):
    try:
        arp_request = scapy.ARP(pdst=sub)
        broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        arp_packet = broadcast / arp_request
        answered_list = scapy.srp(arp_packet, timeout=2, iface=offsec, verbose=False)[0]
        
        print("Devices found:")
        for t, r in answered_list:
            ip = r.psrc
            mac = r.hwsrc
            print(f"IP: {ip} <==> MAC: {mac}")
    except:
        return

sub = "192.168.1.0/24"
offsec = "Ethernet"
test(sub, offsec)    
