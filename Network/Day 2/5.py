import socket
import random

ports = random.sample(range(1024, 65536), 5)
t = []

try:

    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            s.bind(("127.0.0.1", port))
            s.listen(5)
            t.append(s)
            print(f"Opened port {port}")
        except socket.error:
            print(f"Port {port} in use")
            s.close()

    print(f"Listening on ports: {[p.getsockname()[1] for p in t]}")
    print("Press ctrl+c to stop")


    while True:
        pass

except KeyboardInterrupt:
    print("\nClosing ports...")
    for s in t:
        s.close()
    print("Done")