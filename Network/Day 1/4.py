from IPy import IP
try:
    test = IP(input("Enter your ip: "))
    print("This ip is:",test.iptype())
except ValueError as e:
    print(f"Invalid ip: {e}")