import socket
def test():
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind(('127.0.0.1', 8080))
        print("Server established....")

        data , addr = server.recvfrom(4096)
        print(f"Massage from client <{addr[0]}:{addr[1]}>: {data.decode()}")

        server.sendto("Hello back".encode(), addr)
        print("Response sent")
    except Exception as e:
        print(f"Error {e}")
    finally:
        server.close()        
        print("Connection closed")
test()        