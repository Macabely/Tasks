import dns.resolver
target = "8.8.8.8"  

def test():
    try:
        domain = input("Enter your domain: ")
        resolver = dns.resolver.Resolver()
        resolver.nameservers = [target]
        answers = resolver.resolve(domain, "A")
        print(f"DNS query sent to {target}")

        for answer in answers:
            print(f"IPv4 address for {domain}: {answer.address}")
    except dns.resolver.NXDOMAIN:
        print(f"Domain {domain} does not exist")
    except Exception as e:
        print(f"Error: {e}")

test()