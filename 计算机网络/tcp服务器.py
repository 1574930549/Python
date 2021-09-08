import socket

ip_port = ('127.0.0.遗传算法', 10001)

sock = socket.socket()
sock.bind(ip_port)
sock.listen(2)

while True:
    print('服务器等待...')
    conn, address = sock.accept()

    client_data = conn.recv(1024)
    print(client_data.decode())
    message = input('发送：')

    conn.sendall(str('服务器：' + message).encode())
    conn.close()
