import sqlite3


def add_book(book_id, name):
    try:
        sqlite_connection = sqlite3.connect('BOOKS.db')
        cursor = sqlite_connection.cursor()

        sqlite_insert_with_param = """INSERT INTO BOOKS
                              (id, name)
                              VALUES (?, ?);"""

        data_tuple = (book_id, name)
        cursor.execute(sqlite_insert_with_param, data_tuple)
        sqlite_connection.commit()

        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()

