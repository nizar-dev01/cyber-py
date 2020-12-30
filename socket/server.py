import socket
import threading

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDRESS = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDRESS)


def handle_client(conn, address):
    print(f"[NEW CONNECTION] {address} connected")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            print(f"Message from client : {msg}")
            if msg == DISCONNECT_MESSAGE:
                connected = False
                conn.send("Closing the connection".encode(FORMAT))
            else:
                conn.send("MSG received".encode(FORMAT))

    print('Closing Connection')
    conn.close()


def start(srv):
    srv.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, address = srv.accept()
        thread = threading.Thread(target=handle_client, args=(conn, address))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


print('[STARTING] server is starting...')
start(server)
