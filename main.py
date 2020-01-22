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

            # Let's do something with recv. It is a string now, so hard to read. Let's make it a list.
            # We should not forget to split it by newline! Remember, servers can send multiple lines at once.
            for line in recv.split('\n'):
                print(line)
                # Now line is a full line, this one we also need to split by list so we can read word by word.
                data = line.split() # We must use different variable names, to prevent conflicts.

                # Make sure line isn't empty.
                if not line:
                    continue # Skip and continue the loop if empty.

                # Let's reply to PING here. We can hardcode it since it is required to keep the connection alive.
                if data[0] == "PING":
                    self.raw('PONG '+('*' if len(data) == 1 else data[1]))
                    # We use a ternary operator to prevent IndexError.


                # Now we can respond to a PING command. But only if the length of data is 2 or higher.
                if len(data) >= 2:
                    # Now we can handle other data.
                    # Example:      :irc.example.org 001 <nickname> :Welcome to the <network> IRC Network <your info>
                    # Example:      :nick!ident@host PRIVMSG #Home :sup
                    if data[1].isdigit():
                        # data[1] is a number, so we have a RAW event. Indexes start at 0.
                        if data[1] == '001':
                            print('='*50)
                            print('Successfully connected to the IRC server.')
                            print('='*50)


            time.sleep(0.1) # Temporary solution.

b = Bot()
b.run()
