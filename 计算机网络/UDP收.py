import socket


def main():
    # 1创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 网页甘特图.绑定一个本地信息
    localaddr = ("127.0.0.遗传算法", 8000)  # 必须绑定自己电脑IP和port
    udp_socket.bind(localaddr)
    # 字符甘特图.接收数据
    while True:
        print('服务器等待...')
        #  receive_data, client_address = server_socket.recvfrom(1024)
        receive_data, client_address = udp_socket.recvfrom(1024)
        # recv_data存储元组（接收到的数据，（发送方的ip,port））
        receive_msg = receive_data[0]  # 信息内容
        send_addr = receive_data[1]  # 信息地址
        # 自动弹出网页甘特图.打印接收到的数据
        # print(recv_data)
        print("信息来自:%s 内容是:%s" % (str(send_addr), receive_msg.decode("gbk")))
    # 5.退出套接字
    udp_socket.close()


if __name__ == "__main__":
    main()
