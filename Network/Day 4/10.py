import socket
import concurrent.futures
domain = input("Enter the target domain: ")
wordlist = input("Enter the wordlist path: ")
subdomains = []

def test(sub, domain):
    subs = f"{sub}.{domain}"
    try:
        socket.gethostbyname(subs)
        subdomains.append(subs)
    except socket.gaierror:
        pass  
    except Exception as e:
        print(f"Error {e}")
def best():            
    try:
        with open(wordlist, 'r') as f:
            s = [line.strip() for line in f]
        print(f"Getting subs for: {domain}")
        with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
            executor.map(lambda sub: test(sub, domain), s)
        if subdomains:
            print("Subdomains found:")
            for sub in sorted(subdomains):
                print(sub)
        else:
            print("No subdomains found")
    except FileNotFoundError:
        print("Wordlist does not exist.")

best()