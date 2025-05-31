import random

def test():
    test = [random.randint(0, 255) for i in range(6)]
    best = [f"{byte:02X}" for byte in test]
    mac_address = "-".join(best)
    
    return mac_address
print(test())