import socket

def test():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    message = "Hello, Broadcast!".encode()
    client.sendto(message, ("255.255.255.255", 12345))
    client.close()
    print("Broadcast message sent")


test()