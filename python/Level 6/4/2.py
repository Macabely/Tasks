import socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 8080))
server.listen(5)
print("Server established....")
t = True
while t:
  conn, addr = server.accept()
  client = ''
  while True:
    data = conn.recv(4096)
    if not data: break
    client += data.decode()
    print (f'Massage from client: {client}')
    conn.send("Hello back".encode())
  conn.close()
  print ('Connection disconnected')
  t = False