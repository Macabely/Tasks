import whois
test = input("Enter your domain: ")
s = whois.whois(test)
print(s)