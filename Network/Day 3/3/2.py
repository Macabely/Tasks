import socket
def test():
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind(('127.0.0.1', 9999))
        server.listen(5)
        t= server.getsockname()
        print(f"Server established on port {t[1]}....")
    
        conn, addr = server.accept()
        conn.send("Hello, Client!".encode())
        print("Massage sent")
        data = conn.recv(4096)
        if data:
            print (f'Massage from client <{addr[0]}:{addr[1]}>: {data.decode()}')
        conn.close()
        print ('Connection closed')
    except Exception as e:
        print(f"Error <==> {e}")
test()        