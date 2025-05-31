from ipaddress import ip_address, IPv4Address
def ip():
    try:
        test = input("Enter your ip: ")
        ip = ip_address(test)
        if not isinstance(ip, IPv4Address):
            return 'Invalid ip! Please enter an ipv4 (e.g 192.168.1.10)'
    
        oc = test.split(".")
        bi = [format(int(i), "08b") for i in oc]
        return '.'.join(bi)
    except ValueError:
        return "Invalid ip! Please enter an ipv4 (e.g 192.168.1.10)"

print(ip())