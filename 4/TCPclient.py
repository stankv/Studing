# TCP-клиент для TCPserver.py или TCPserver_sync.py
from socket import socket, AF_INET, SOCK_STREAM
 
flag = True
while(flag):
    str1 = input("-->")
    if str1.strip() == "bye":
        print("EXIT")
        flag = False
    else:
        with socket(AF_INET, SOCK_STREAM) as s:
            s.connect(('localhost', 12345))            # открываем соединение с сервером
            s.send(str1.encode())                      # отправляем серверу запрос
            server_response = s.recv(1024).decode()    # принимаем ответ сервера
            print("Server:", server_response.strip())             # выводим ответ сервера на консоль
