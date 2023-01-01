import socket
from read import show_books
from lib import add_book
import sqlite3

port = 1000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', port))
s.listen()
conn, addr = s.accept()
while True:
    data = conn.recv(1024)
    if not data:
        break
    conn.sendall(data)
    if data.decode('utf-8') == 'GET':
        show_books()
    if data.decode('utf-8')[:4] == 'POST':
        sqlite_connection = sqlite3.connect('BOOKS.db')
        cursor = sqlite_connection.cursor()

        sqlite_select_query = """SELECT * from BOOKS"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        add_book(len(records) + 1, data.decode('utf-8')[4:])
        cursor.close()
        if sqlite_connection:
            sqlite_connection.close()
        print('Книга', data.decode('utf-8')[4:], 'добавлена')

