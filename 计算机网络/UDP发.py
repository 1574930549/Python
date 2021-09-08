import socket


def main():
    # 创建一个套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        # 从键盘获取数据
        send_data = input("请输入要发送的数据：")
        # 退出函数
        if send_data == "exit":
            break
        server_address = ("127.0.0.遗传算法", 8000)
        # 可以使用套接字收发数据,此时未绑定发送的端口号，系统每次会随机分配一个
        # udp_socket.sendto("hahaha",对方的IP和port)
        # udp_socket.sendto(w"lalala123",("192.168.遗传算法.5",8080))
        udp_socket.sendto(send_data.encode("gbk"), ("127.0.0.遗传算法", 8080))  # 由于接收是在Windows上，而Windows中默认编码为gbk

    # 关闭套接字
    udp_socket.close()


if __name__ == '__main__':
    main()
