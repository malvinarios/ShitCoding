print('Sup world!')

import socket
import time # Just for now, we will improve later.

for _ in range(1, 11):
  print("Go nuts {} time{}".format(_, 's' if _ != 1 else ''))

class Bot:
    def __init__(self):
        self.server = "irc.provisionweb.org"
        self.port = 6667
        self.nick = "ShitCodedBot"
        self.ident = "shit"
        self.sock = socket.socket()
        self.read = 0

    def run(self):
        self.sock.connect((self.server, self.port))
        print('Connected')
        self.read = 1
        self.reg_client()
        self.listen() # Starting listening.

    def reg_client(self):
        self.raw(f'NICK {self.nick}')
        self.raw(f'USER {self.ident} 0 0 :Shit bot')

    def raw(self, data):
        self.sock.send(bytes(data, 'utf-8'))

    def disconnect(self):
        self.read = 0
        try:
            self.sock.shutdown(socket.SHUT_WR)
        except:
            pass
        self.sock.close()
        print('Socket gracefully closed.')

    def listen(self):
        # Here we will read the socket.
        while (self.read):
            recv = self.sock.recv(4096).decode('utf-8')
            if not recv:
                print('Unable to read socket.')
                self.disconnect()
                return

            print(recv) # Let's print out all the incoming data, we can work with this later.

            time.sleep(0.1) # Temporary solution.

b = Bot()
b.run()
