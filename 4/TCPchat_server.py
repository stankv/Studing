# КОНСОЛЬНЫЙ TCP-ЧАТ-СЕРВЕР
import socket
import threading

# Функция отправки сообщений всем клиентам
def broadcast(message, current_client):
    for client in clients:    # отправляем всем, кроме того, кто прислал
        if client == current_client:
            continue
        client.send(message)

# Функция обработки сообщений от клиентов
def handle(client):
    while True:
        try:
            # Отправка сообщения клиентам
            message = client.recv(1024)    # получаем сообщение от клиента
            broadcast(message, client)    # рассылаем его всем другим клиентам
            print(message.decode('utf-8'))
        except:
            # Если ошибка, удаляем из списков объект типа сокет клиента и его ник
            index = clients.index(client)
            clients.remove(client)
            client.close()    # закрываем объект типа сокет клиента
            nickname = nicknames[index]
            broadcast('{} is disconnect!'.format(nickname).encode('utf-8'), None)
            print(nickname, "is disconnect")
            nicknames.remove(nickname)
            break

# Основная функция программы. Прослушивание порта, подключение новых клиентов
def receive():
    while True:
        # Принимаем подключение клиента
        client, address = server.accept()    # ожидаем и принимаем соединение с клиентом
        print("Connected with {}".format(str(address)))

        # Запрашиваем имя/ник клиента, сохраняем данные клиента в списках
        client.send('NICK'.encode('utf-8'))    # отправляем клиенту запрос его имени/ника
        nickname = client.recv(1024).decode('utf-8')    # ожидаем и получаем ответ клиента
        nicknames.append(nickname)
        clients.append(client)

        # Сообщаем о подключении нового клиента
        print("Nickname is {}".format(nickname))
        broadcast("{} joined!".format(nickname).encode('utf-8'), None)
        client.send('Connected to server!'.encode('utf-8'))

        # Запуск отдельного потока приема/отправки сообщений для подключившегося клиента
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

# функция запуска отключения сервера
def server_off():
    while True:
        comm = input()
        if comm == 'bye':
            if len(clients) != 0:    # если есть подключенные клиенты, то закрываем соединения
                broadcast('Server shutdown!'.encode('utf-8'), None)
                for client in clients:
                    client.close()
            #server.shutdown(socket.SHUT_RDWR)
            server.close()
            print("Server Deactivated!")
            break



# Данные для подключения к серверу
host = 'localhost'
port = 12345

# Запуск сервера
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    # создаем TCP-сокет
server.bind((host, port))    # привязываем сокет к адресу и порту
server.listen()    # перевод сокета в режим сервера и прослушивания порта
print("Server Activated!")

# Списки объектов типа сокет подключенных клиентов и ников клиентов
clients = []
nicknames = []
# Запуск потока для функции отключения сервера
thread_off = threading.Thread(target=server_off)
thread_off.start()
receive()