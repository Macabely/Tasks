import ipaddress

def test():
    try:
        cidr = input("Enter the CIDR (e.g., 192.168.1.10/24): ")
        network = ipaddress.ip_network(f"{cidr.lstrip('/')}", strict=False)
        
        if not isinstance(network, ipaddress.IPv4Network):
            return "Invalid: Not an IPv4 address or mask"
        
        return f"Network address: {network.network_address}\nBroadcast address: {network.broadcast_address}"
    
    except ValueError as e:
        return f"Invalid input: {e}"

print(test())
