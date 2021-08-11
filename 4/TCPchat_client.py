# КОНСОЛЬНЫЙ TCP-ЧАТ-КЛИЕНТ
import socket
import threading

# Функция получения сообщений с сервера (и отправки ника)
def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')    # получение сообщения с сервера
            if message == 'NICK':    # если сервер запрашивает ник то отправляем ему его
                client.send(nickname.encode('utf-8'))
            else:
                print(message)       # иначе просто выводим в консоль сообщение с сервера
        except:
            # Закрываем соединение, если возникла ошибка (исключение) приема данных
            print("An error occured, or maked exit from chat!")
            client.close()    # закрытие сокета
            break

# Функция отправки сообщений пользователя
def write():
    while True:
        mess = input('')
        message = '{}: {}'.format(nickname, mess)
        if mess.strip() == 'bye':    # команда выхода из чата
            client.close()    # закрытие сокета
            break
        else:
            try:
                client.send(message.encode('utf-8'))
            except:
                break

# Запрос имени/ника и проверка его корректности
flag = True
while flag:
    nickname = input("Choose your nickname: ")    # запрос имени/ника клиента
    if nickname == "":                   # можно добавить ряд проверок на корректность ника
        continue
    else:
        flag = False

# Соединение с сервером
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    # создаем TCP-сокет
client.connect(('localhost', 12345))    # подключаемся к удаленному сокету по адресу

# Запуск потоков для получения и отправки сообщений
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()

while True:
    if write_thread.is_alive() or receive_thread.is_alive():
        continue
    else:
        break
print("Exit from chat")
print("Server is disconnected")