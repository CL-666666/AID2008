from socket import *

ADDR = ("172.40.83.107", 2021)
udp_socket = socket(AF_INET, SOCK_DGRAM)
while True:
    word = input(">>请输入要查询的单词:")
    if not word:
        break
    udp_socket.sendto(word.encode(), ADDR)
    data, addr = udp_socket.recvfrom(1024)
    print(addr)
    print(word, ':', data.decode())

udp_socket.close()
