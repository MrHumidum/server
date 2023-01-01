import socket

port = 1000

message = input()
if message == 'POST':
    book = 'POST' + input("Введите название книги: ")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', port))
if message == 'POST':
    s.sendall(book.encode('utf-8'))
else:
    s.sendall(message.encode('utf-8'))
data = s.recv(1024)
