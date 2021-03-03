import os
from socket import socket as Socket

from config import ADDRESS, PORT, MESSAGE_SIZE

def startServer():
    socket = Socket()
    socket.bind((ADDRESS, PORT))
    socket.listen()
    print(f"Listening on '{ADDRESS}:{PORT}'")
    
    while 1:
        connection, clientInfo = socket.accept()
        print(f"Client {clientInfo} connected")
        
        if listenClient(connection, clientInfo):
            return 

def listenClient(connection: Socket, clientInfo):
    while 1:
        try:
            data = connection.recv(MESSAGE_SIZE)
        except ConnectionError:
            break
        if not data:
            break
        os.system("cls")
        print(data.decode())
    print(f"Client {clientInfo} has disconnected")
    
startServer()