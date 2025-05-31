import dns.resolver
try:
    domain = input("Enter the domain: ")
    query = dns.resolver.resolve(domain, "MX")
    for server in query:
        print(server.exchange)
except dns.resolver.NXDOMAIN:
    print(f"{domain} doesn't exist")
