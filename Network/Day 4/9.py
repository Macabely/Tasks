import dns.resolver

def test(domain):
    try:
        ips = dns.resolver.resolve(domain, 'A')
        return [i.address for i in ips]
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        print("Invalid domain")
        return []
    except Exception as e:
        print(f"Error {e}")
        return []

def best():
    domain = input("Enter domain name: ")
    ips = test(domain)
    if not ips:
        return
    if len(ips) > 1:
        t = ips[0]
        s = all(ip == t for ip in ips)
        if not s:
            print("Domain's ip has been changed over time")    
        else:
            print("Domain's ip hasen't been changed over time")
    else:
        print("Domain's ip hasen't been changed over time")
best()                   
