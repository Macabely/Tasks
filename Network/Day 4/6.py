import dns.resolver
import concurrent.futures
domain = input("Enter your domain: ")
wordlist = input("Enter the wordlist path: ")
subdomains = []

def test(sub, domain):
    f = f"{sub}.{domain}"
    try:
        dns.resolver.resolve(f, "A")
        subdomains.append(f)
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        pass
    except Exception as e:
        print(f"Error! {e}")                   

def thread():
    try:
        with open(wordlist, 'r') as w:
            t = [line.strip() for line in w]
        print(f"Getting subs for {domain}")
        with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
            executor.map(lambda sub: test(sub, domain), t)
        if subdomains:
            print("Found subdomains: ")
            for sub in sorted(subdomains):
                print(sub) 
        else:
            print("No subs found")  
    except FileNotFoundError:
        print("Wordlist does not exist")                                    

thread()                        