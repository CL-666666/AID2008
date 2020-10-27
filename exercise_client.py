from socket import *

ADDR = ("127.0.0.1", 2021)
udp_socket = socket(AF_INET, SOCK_DGRAM)
while True:
    msg = input("请输入要查询的单词:")
    if not msg:
        break
    udp_socket.sendto(msg.encode(), ADDR)
    data, addr = udp_socket.recvfrom(1024)
    print(msg, ":", data.decode())
udp_socket.close()
