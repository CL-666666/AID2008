import socket

# 172.40.91.108
sockfd = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sockfd.bind(('0.0.0.0', 2020))
data, addr = sockfd.recvfrom(1024)
sockfd.close()
