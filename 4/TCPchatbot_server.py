# Простой асинхронный TCP-чат-бот-сервер.
import json
import os.path
from socketserver import BaseRequestHandler, TCPServer, ThreadingMixIn
from threading import Thread

# Класс обработчика клиентских запросов
class TestTCPHandler(BaseRequestHandler):

    def handle(self):
        # задаем путь к json-файлу со словарем ответов чат-бота
        dict_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '../4/data/forChatBot.json')
        with open(dict_path, "r") as json_file:
            jsonFile = json.load(json_file)    # считываем словарь из файла

        self.data = self.request.recv(1024).decode()    # получаем сообщение клиента
        self.data = self.data.strip()                   # удаляем из него лишние пробелы слева и справа
        k = self.data.find(": ")
        NickName = self.data[:k+2]                      # выделяем из тела сообщения ник клиента
        self.data = self.data[k+2:]                     # выделяем из тела сообщения само сообщение
        self.data = self.data.lower()                   # переводим строку сообщения в нижний регистр
        print(NickName, self.data)
        if self.data in jsonFile:    # ищем в словаре ключ, равный сообщению клиента
            key_answer = jsonFile.get(self.data)
        else:
            key_answer = "Я Вас не понял..."
        print("Server to " + NickName + key_answer)
        key_answer = "Server: " + key_answer
        self.request.sendall(key_answer.encode())    # отправляем ответ клиенту
        

# Класс асинхронного сервера, который обрабатывает запросы клиентов в отдельных потоках
class ThreadedTCPServer(ThreadingMixIn, TCPServer):
    pass

print("Server activated")
with ThreadedTCPServer(('localhost', 12345), TestTCPHandler) as server:
    # Запускаем поток с сервером - этот поток затем 
    # запустит еще один поток для каждого запроса
    server_thread = Thread(target=server.serve_forever())
    # Выйдем из потока сервера, когда основной поток завершится
    server_thread.daemon = True
    server_thread.start()