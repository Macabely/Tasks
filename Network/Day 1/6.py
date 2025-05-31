import ipaddress 
test =  "192.168.1.0/24"
ip_list = [str(test) for test in ipaddress.ip_network(test, strict=False).hosts()]

print(ip_list)