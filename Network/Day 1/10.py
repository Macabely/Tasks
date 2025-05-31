from ipaddress import ip_network 
    
def test(IP1, IP2): 
    
    a = ip_network(IP1, strict = False) 
    b = ip_network(IP2, strict = False)
  
    if(a == b) : 
        return "Same Network" 
  
    else : 
        return "Different Network"
    
print(test('192.168.1.0/24', '192.168.1.11/24'))    
print(test('17.53.128.0/20', '17.53.127.0/20'))    