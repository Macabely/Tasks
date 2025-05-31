from ipaddress import ip_address, IPv4Address
def ip():
    test = input("Enter your ip: ")
    try:
        return f"{test} is ipv4" if type(ip_address(test)) is IPv4Address else f"{test} is ipv6"
    except ValueError as e:
       return "Invalid IP!",str(e)
print(ip())