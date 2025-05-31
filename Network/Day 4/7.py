import dns.resolver
try:
    domain = input("Enter you domain: ")
    a = dns.resolver.resolve(domain, "TXT")
    for text in a:
        s = text.to_text()
        if "v=spf1" in s :
            print(f"SPF record for the domain: {s}")
except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
    print("No SPF records for this domain")
except Exception as e:
    print(f"Error! {e}")