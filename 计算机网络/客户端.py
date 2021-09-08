# -*- coding: utf-8 -*-
import socket
import time

# client 发送端
from pip._vendor.distlib.compat import raw_input

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
PORT = 8000

while True:
    start = time.time()  # 获取当前时间
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start)))  # 以指定格式显示当前时间
    msg = raw_input("本客户端192.168.43.131，请输入要发送的内容：")
    server_address = ("192.168.遗传算法.7", 8080)  # 接收方 服务器的ip地址和端口号
    client_socket.sendto(msg.encode(), server_address)
    # client_socket.sendto(sendall(msg), server_address)  # 将msg内容发送给指定接收方
    now = time.time()  # 获取当前时间
    run_time = now - start  # 计算时间差，即运行时间
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(now)))
    print("run_time: %d seconds\n" % run_time)
