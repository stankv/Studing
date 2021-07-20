# Простой асинхронный TCP-сервер. Реализация подсказана на
# https://docs-python.ru/standart-library/modul-socketserver-python/klassy-forkingmixin-threadingmixin-modulja-socketserver/
from socketserver import BaseRequestHandler, TCPServer, ThreadingMixIn
from threading import Thread

# Класс обработчика клиентских запросов
class TestTCPHandler(BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address), end='')
        print(self.data)
        self.request.sendall(bytes(self.data.upper()))

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