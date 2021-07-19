# TCP-клиент для TCPserver.py
from socket import socket, AF_INET, SOCK_STREAM
s = socket(AF_INET, SOCK_STREAM)

s.connect(('localhost', 12345))    # открываем соединение с сервером
s.send(b'Hello, server')           # отправляем серверу запрос
server_response = s.recv(1024).decode()    # принимаем ответ сервера
print(server_response.strip())     # выводим ответ сервера на консоль

flag = True
while(flag):
    str1 = input("-->")
    if str1.strip() == "bye":
        print("EXIT")
        flag = False
    else:
        s.send(str1.encode())
        server_response = s.recv(1024).decode()
        print(server_response.strip())

s.close()    # закрываем соединение с сервером