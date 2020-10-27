from socket import *

udp_socket = socket(AF_INET, SOCK_DGRAM)
udp_socket.bind(("0.0.0.0", 2020))
while True:
    data, addr = udp_socket.recvfrom(1024)
    print(addr, "接收到:", data.decode())
    n = udp_socket.sendto(b"Thanks", addr)
    print("共发送%d bytes" % n)
