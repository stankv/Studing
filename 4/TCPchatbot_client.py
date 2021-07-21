# TCP-клиент для асинхронного чат-бота TCPchatbot_server.py
from socket import socket, AF_INET, SOCK_STREAM
 
flag = True
while(flag):
    NickName = input("Ваше имя/ник:")
    if NickName == "":
        flag = True
    else:
        flag = False
NickName = NickName + ": "

flag = True
while(flag):
    str1 = input(NickName)
    if str1.strip() == "bye":
        print("EXIT")
        flag = False
    else:
        with socket(AF_INET, SOCK_STREAM) as s:
            s.connect(('localhost', 12345))            # открываем соединение с сервером
            str1 = NickName + str1
            s.send(str1.encode())                      # отправляем серверу запрос
            server_response = s.recv(1024).decode()    # принимаем ответ сервера
            print(server_response.strip())             # выводим ответ сервера на консоль