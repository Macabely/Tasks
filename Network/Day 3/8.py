import socket

def test():
    host = "127.0.0.1"
    port = 23
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect(host, port)
        print(f"Telnet is rachable through {host}")
        s.close()
    except:
        print("Telnet is not reachable")
        s.close
test()        