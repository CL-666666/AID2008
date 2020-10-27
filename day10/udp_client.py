from socket import *

# ADDR = ('172.40.91.108', 8888)
ADDR = ('172.40.83.108', 12345)
udp_socket = socket(AF_INET, SOCK_DGRAM)
while True:
    msg = input(">>")
    if not msg:
        break
    udp_socket.sendto(msg.encode(), ADDR)
    data, addr = udp_socket.recvfrom(1024)
    print("from server:", data.decode())

udp_socket.close()