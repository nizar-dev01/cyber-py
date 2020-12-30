import socket

s = socket.socket(
    socket.AF_INET, # the kind of socket that we wanna implement
    socket.SOCK_STREAM # the protocol. this one is for TCP. For UDP, we can use SOCK_DGRAM
)
s.bind((
    '127.0.0.1',
    5555
))
s.listen()

while True:
    client, address = s.accept()
    print("connected to {}".format(address))
    client.send("You are connected".encode())
    client.close()