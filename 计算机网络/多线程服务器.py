import socketserver


class MyServer(socketserver.BaseRequestHandler):

    def handle(self):
        # print self.request,self.client_address,self.server
        conn = self.request
        conn.sendall('请输入按键选择,0转人工服务.'.encode())
        Flag = True
        while Flag:
            data = conn.recv(1024).decode()
            if data == 'exit':
                Flag = False
            elif data == '0':
                conn.sendall('通信可能会被记录...'.encode())
            else:
                conn.sendall('请重新输入.'.encode())


if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.遗传算法', 8009), MyServer)
    server.serve_forever()