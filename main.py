print('Sup world!')

import socket

for _ in range(1, 11):
  print("Go nuts {} time{}".format(_, 's' if _ != 1 else ''))

class Bot:
    def __init__(self):
        self.server = "irc.provisionweb.org"
        self.port = 6667
        self.nick = "ShitCodedBot"
        self.ident = "shit"
        self.sock = socket.socket()

    def run(self):
        self.sock.connect((self.server, self.port))
        print('Connected')
        self.reg_client()

    def reg_client(self):
        self.raw('NICK '+self.nick)
        self.raw('USER {} 0 0 :Shit bot'.format(self.ident))

    def raw(self, data):
        self.sock.send(bytes(data, 'utf-8'))


    def read_sock(self):
        pass
        # Here we will read the socket.

b = Bot()
b.run()
