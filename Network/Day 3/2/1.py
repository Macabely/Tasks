import socket
def test():
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        target = ('127.0.0.1', 8080)
        print("Connection established...")
        client.sendto("Hello".encode(), target)
        print("Massage sent")
        data , addr = client.recvfrom(4096)
        print(f"Massage from server <{addr}>: {data.decode()}")
    except Exception as e:
        print(f"Error <==> {e}")
    finally:
        client.close()
        print("Connection closed")
test()              