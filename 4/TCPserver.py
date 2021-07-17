# Простой синхронный TCP-сервер
from socketserver import BaseRequestHandler, TCPServer

class TestTCPHandler(BaseRequestHandler):
    def handle(self):
        print("handle activated", self.client_address)
        self.data = self.request.recv(1024).strip()
        print(self.data)
        self.request.send(b"privet, client")


server = TCPServer(('localhost', 12345), TestTCPHandler)
print("Server activated")
server.serve_forever()