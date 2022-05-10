# Connection to DB
import mysql.connector
from models import books
from models import writers # импорт моделей из SQL файлов


class ConnectionService():
    __db_connection = None # локальные переменные, работают только внутри класса

    DB_NAME = "BooksDB"

    @staticmethod
    def instance():
        if ConnectionService.__db_connection == None: # если нет подключения, тогда создаем
            ConnectionService.__db_connection = ConnectionService.create_connection()
        return ConnectionService.__db_connection # а если уже есть подключение, тогда возвращаем его

    @staticmethod
    def create_connection():
        return mysql.connector.connect(
            user = "root",
            password = "9293709",
            host = "127.0.0.1")

    def create_db(self):
        connection = ConnectionService.instance()
        cursor = connection.cursor()
        try:
            cursor.execute(f"CREATE DATABASE {self.DB_NAME} CHARACTER SET 'utf8'")
        except mysql.connector.DatabaseError:
            print("Database exists")

        cursor.execute(f"USE {self.DB_NAME}")
        self.create_table(writers.CREATE_SQL) # а тут мы вызываем функцию create_table
        self.create_table(books.CREATE_SQL)

    def create_table(self,sql): # создаем второй параметр sql
        connection = ConnectionService.instance()
        cursor = connection.cursor()
        try:
            cursor.execute(sql) # передаем сюда в execute cursor
        except mysql.connector.DatabaseError:
            print("Table exists")

    def get_cursor(self):
        connection = ConnectionService.instance()
        cursor = connection.cursor()
        cursor.execute(f"USE {self.DB_NAME}")
        return cursor