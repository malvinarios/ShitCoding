print('Sup world!')

import socket

class Bot:
    def __init__(self):
        self.server = "irc.provisionweb.org"
        self.port = 6667
        self.nick = "ShitCodedBot"
        self.sock = socket.socket()

    def run(self):
        self.sock.connect((self.server, self.port))
        print('Connected')

b = Bot()
b.run()
