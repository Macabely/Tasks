ports = {
    20: "TCP",    
    21: "TCP",     
    22: "TCP",      
    23: "TCP",      
    25: "TCP",    
    53: "TCP/UDP",  
    80: "TCP",     
    110: "TCP",    
    123: "UDP",     
    143: "TCP",    
    161: "UDP",   
    443: "TCP",    
    514: "UDP",    
    993: "TCP",     
    995: "TCP",  
    1433: "TCP",   
    3306: "TCP",  
    3389: "TCP",  
    5432: "TCP", 
    8080: "TCP"  
}
try:
    user = input("Enter the Port number: ")
    port = int(user)
    if 0 <= port <= 65535:
        test = ports.get(port)
        if test == 0:
            print("The port is valid but protocol is unknown (may use TCP or UDP)") 
        else:
            print(test)
    else:
        print("Out of range, must be between 0 and 65535")        
except:
    print("Invalid port must be a number and between 0 and 65535")        