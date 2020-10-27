from socket import *
import pymysql

DATABASES = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "",
    "database": "dict",
    "charset": "utf8",
}
ADDR = ("0.0.0.0", 2021)


class Database:
    def __init__(self):
        self.db = pymysql.connect(**DATABASES)
        self.cur = self.db.cursor()

    def query_word(self, word):
        sql = "select mean from words where word=%s"
        self.cur.execute(sql, [word])
        mean = self.cur.fetchone()
        if mean:
            return mean[0]
        else:
            return "Not Found"

    def close(self):
        self.cur.close()
        self.db.close()


def main():
    udp_socket = socket(AF_INET, SOCK_DGRAM)
    udp_socket.bind(ADDR)
    db = Database()  # 实例化对象
    while True:
        data, addr = udp_socket.recvfrom(1024)
        mean = db.query_word(data.decode())
        udp_socket.sendto(mean.encode(), addr)


if __name__ == '__main__':
    main()
