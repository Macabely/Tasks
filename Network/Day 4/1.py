import socket
def resolve():
    user = input("Enter the domain: ")
    try:
        ip = socket.gethostbyname(user)
        return ip
    except socket.gaierror:
        return(f"Domain doesn't exist")
    
print(resolve())