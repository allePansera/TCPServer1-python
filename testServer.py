from OOP.Server.Server import Server

#s = Server('127.0.0.1',4000,'ECHO')
s = Server('127.0.0.1',4000,'ECHO')
s.initialize()
s.listen()