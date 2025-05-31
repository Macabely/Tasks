import socket
def test():
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind(('127.0.0.1', 8080))
        server.listen(5)
        print("Server established....")
    
        conn, addr = server.accept()
        data = conn.recv(4096)
        print (f'Massage from client <{addr[0]}:{addr[1]}>: {data.decode()}')
        conn.send("Hello back".encode())
        print("Response sent")
        conn.close()
        print ('Connection disconnected')
    except Exception as e:
        print(f"Error <==> {e}")

test()        