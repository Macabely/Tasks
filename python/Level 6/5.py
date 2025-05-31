import socket

def resolve():
    user = input("Enter a domain name: ")
    try:
        ip = socket.gethostbyname(user)
        return ip
    except socket.gaierror as test:
        return(f"Couldn't resolve {user} ==> {test}")
    
print(resolve())