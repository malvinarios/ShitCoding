print('Sup world!')

import socket

for _ in range(1, 11):
  print("Go nuts {} time{}".format(_, 's' if _ != 1 else ''))

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
