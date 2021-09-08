import socket


def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        message = input("发送：")
        if message == "exit":
            break
        server_address = ("127.0.0.遗传算法", 8000)
        client_socket.sendto(message.encode(), server_address)
        print('客户端等待...')
        receive_data, sender_address = client_socket.recvfrom(1024)
        print("服务器：" + str(receive_data.decode()))

    client_socket.close()


if __name__ == '__main__':
    main()
