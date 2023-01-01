import sqlite3

def show_books():
    try:
        sqlite_connection = sqlite3.connect('BOOKS.db')
        cursor = sqlite_connection.cursor()

        sqlite_select_query = """SELECT * from BOOKS"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        print("Всего строк:  ", len(records))
        print("Id:Name")
        print()
        for row in records:
            print(row[0], row[1], sep=':')

        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()


