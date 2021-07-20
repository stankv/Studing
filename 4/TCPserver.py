# Простой синхронный TCP-сервер
from socketserver import BaseRequestHandler, TCPServer

class TestTCPHandler(BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address), end='')
        print(self.data)
        # just send back the same data, but upper-cased
        self.request.sendall(bytes(self.data.upper()))

HOST, PORT = "localhost", 12345
print("Server activated")
# Create the server, binding to localhost on port 12345
with TCPServer((HOST, PORT), TestTCPHandler) as server:
    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()