import socket


class Server:
    def __init__(self,host='127.0.0.1',port=4000,mode='ECHO'):
        self.host = host
        self.port = port
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.mode = mode #-> ECHO/BASIC ACCEPTED

    def initialize(self):
        """This method initialize server side of the connection"""
        self.s.bind((self.host,self.port))
        self.s.listen()

    def listen(self):
        """This method serves all incoming request."""
        try:
            with self.s:
                conn, addr = self.s.accept()
                print('Start listening for incoming connection....')
                with conn:
                    print(f'Connected by {addr}')
                    while True:
                        data = conn.recv(1024)
                        print(f"Received Message: {data}")
                        if not data:
                            break
                        #ECHO-SERVER BEHAVIOUR
                        if self.mode=='ECHO':
                            conn.sendall(data)
        except KeyboardInterrupt as e:
            print("Server has been closed manually")
        except Exception as e:
            print("Error while listening for incoming connection")