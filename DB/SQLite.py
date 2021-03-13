import sqlite3
from sqlite3 import Error


def create_connection(path):
    connect = None
    try:
        connect = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
        print(e.__class__)
    else:
        print("All right!")
    finally:
        connect.close()
        print("Connection to SQLite DB is closed")

    return connect


create_connection("D:/PROJECTS/Python/PyCharm_project/DB/bd.db")
