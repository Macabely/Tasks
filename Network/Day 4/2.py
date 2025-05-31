import socket
try:
    test = input("Enter the ip: ")
    best = socket.gethostbyaddr(test)[0]
    print(best)
except:
    print("No data found on that ip!")    