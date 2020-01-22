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
        self.sock = socket.socket() # We assign a new socket object to this class' sock attribute. (self.sock)
        self.read = 0

    def run(self):
        self.sock.connect((self.server, self.port)) # A socket object takes a tuple as argument, so don't be alarmed by the double parenthesis around the insertion.
        print('Connected')
        self.read = 1
        self.reg_client()
        self.listen() # Starting listening.

    def reg_client(self):
        self.raw(f'NICK {self.nick}')
        self.raw(f'USER {self.ident} 0 0 :Shit bot')

    def raw(self, data):
        self.sock.send(bytes(data+'\n', 'utf-8'))
        print('<< '+data) # Visualising output to the server. Handy for debugging.

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

            # Let's do something with recv. It is a string now, so hard to read. Let's make it a list.
            # We should not forget to split it by newline! Remember, servers can send multiple lines at once.
            for line in recv.split('\n'):
                # Now line is a full line, this one we also need to split by list so we can read word by word.
                print(line)
                data = line.split() # We must use different variable names, to prevent conflicts.
                # Now we can respond to a PING command. But only if the length of data is 2 or higher.
                if len(data) >= 2:
                    if data[0] == 'PING':
                        self.raw('PONG '+data[1]) # Reply with the same random string as you received.
                        print('Replied to PING command from server. We should be connected now.')

            time.sleep(0.1) # Temporary solution.

b = Bot()
b.run()
