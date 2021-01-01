import socket
import threading
from queue import Queue

queue = Queue()
open_ports = []


def scan(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        return True
    except:
        return False


def fill_queue(ports):
    for port in ports:
        queue.put(port)


def worker():
    empty = queue.empty()
    while not empty:
        port = queue.get()
        if scan('localhost', port):
            open_ports.append(port)
            print(open_ports)


fill_queue(range(1, 100))

thread_list = []

for i in range(1, 100):
    thread = threading.Thread(target=worker)
    thread_list.append(thread)

for thread in thread_list:
    thread.start()
