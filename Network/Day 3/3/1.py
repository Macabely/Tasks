import socket
def test():
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(('127.0.0.1', 9999))
        print("Connection established...")
        # client.send("Hello".encode())
        # print("massage sent")
        server = client.recv(4096)
        s = client.getpeername()
        print(f"Massage from server <{s[0]}:{s[1]}>: {server.decode()}")
    except Exception as e:
        print(f"Error <==> {e}")
    finally:
        client.close()         
        print("Connection disconnected")

test()  