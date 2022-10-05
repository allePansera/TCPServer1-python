import socket


class Client:
    def __init__(self,host='127.0.0.1',port=4000):
        self.host = host
        self.port = port


    def send(self, content):
        """This method send to the server content inside a message"""
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        with self.s:
            self.s.connect((self.host, self.port))
            self.s.sendall(content.encode())
            #WAIT FOR EVENTUAL echo-MESSAGE
            while True:
                data = self.s.recv(1024)
                print(f"Echo-Message: {data.decode()}")
                if not data:
                    break
            #QUESTO E' SUPERFLUO
            self.s.close()
