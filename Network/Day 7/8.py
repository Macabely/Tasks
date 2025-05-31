import tldextract
import Levenshtein as lv

legit = ['test.com', 'google.com', 'facebook.com']

test = ['http://test.co', 'http://test.com', 'https://www.google.security-update.com', 'https://faceb00k.com/login', 'https://google.com']

def check(url):
    ext = tldextract.extract(url)
    return ext.subdomain, ext.domain, ext.suffix

def miss(domain_with_suffix, legit, threshold=0.75):
    for leg in legit:
        see = lv.ratio(domain_with_suffix, leg)
        if see >= threshold:
            return True
    return False 

def phishing(url, legit):    
    subdomain, domain, suffix = check(url)
    domain_with_suffix = f"{domain}.{suffix}"
    if domain_with_suffix in legit:
        print(f"link is fine: {url}")
        return False
    if miss(domain_with_suffix, legit):
        print(f"potential phishing detected: {url} (similar to legitimate domain)")
        return True
    else:
        print(f"potential phishing detected: {url} (unknown domain)")
        return True
    
if __name__ == "__main__":
    for url in test:
        phishing(url, legit)