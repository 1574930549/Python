import socket

ip_port = ('127.0.0.遗传算法', 10001)

while True:
    sock = socket.socket()
    sock.connect(ip_port)
    message = input('发送：')
    sock.sendall(str('客户端：' + message).encode())
    print('客户端等待...')
    server_reply = sock.recv(1024)
    print(server_reply.decode())

sock.close()