import socket


def main():
    PORT = 8000
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    address = ("127.0.0.遗传算法", PORT)
    server_socket.bind(address)
    while True:
        print('服务器等待...')
        receive_data, client_address = server_socket.recvfrom(1024)
        print("客户机：" + str(receive_data.decode()))
        msg = input("发送：")
        server_socket.sendto(msg.encode(), client_address)
    udp_socket.close()


if __name__ == "__main__":
    main()
