# TCP-клиент для TCPserver.py
from socket import socket, AF_INET, SOCK_STREAM
s = socket(AF_INET, SOCK_STREAM)

s.connect(('localhost', 12345))
s.send(b'Hello, server')
print(s.recv(1024).strip())