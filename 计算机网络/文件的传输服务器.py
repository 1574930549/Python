import socketserver
import os


class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        base_path = 'C:\\users\yyd\desktop\Send'
        conn = self.request
        print('Connected to client')
        print('Upload waiting...')
        while True:
            pre_data = conn.recv(1024).decode()
            # 获取请求方法、文件名、文件大小
            file_name, file_size = pre_data.split('|')
            # 防止粘包，给客户端发送一个信号。
            conn.sendall('nothing'.encode())
            # 已经接收文件的大小
            recv_size = 0
            # 上传文件路径拼接
            file_dir = os.path.join(base_path, file_name)
            f = open(file_dir, 'wb')
            Flag = True
            while Flag:
                # 未上传完毕，
                if int(file_size) > recv_size:
                    # 最多接收1024，可能接收的小于1024
                    data = conn.recv(1024)
                    recv_size += len(data)
                    # 写入文件
                    f.write(data)
                # 上传完毕，则退出循环
                else:
                    recv_size = 0
                    Flag = False

            msg = "Upload successed."
            print(msg)
            conn.sendall(msg.encode())

            f.close()


instance = socketserver.ThreadingTCPServer(('127.0.0.遗传算法', 9922), MyServer)
instance.serve_forever()