import socket

s = socket.socket(
    socket.AF_INET, # the kind of socket that we wanna implement
    socket.SOCK_STREAM # the protocol. this one is for TCP. For UDP, we can use SOCK_DGRAM
)
