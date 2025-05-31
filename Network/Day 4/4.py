import dns.resolver
try:
    domain = input("Enter the domain: ")
    query = dns.resolver.resolve(domain, "NS")
    for server in query:
        print(server)
except dns.resolver.NXDOMAIN:
    print(f"{domain} doesn't exist")
