from models import books
from connection_to_SQL import *


class BooksService():
    __connectionService = None
    def __init__(self):
        self.__connectionService = ConnectionService()

    def get_books_list(self):
        cursor = self.__connectionService.get_cursor()
        cursor.execute(f""" SELECT * FROM {books.TABLE_NAME} """)
        info_from_cursor = cursor.fetchall()
        print(info_from_cursor)

    def add_book(self):
        cursor = self.__connectionService.get_cursor()
        
        name_of_books = input("ENter book name: ")
        description = input("ENter description (not necesarry): ")
        writer_id = input("Enter writer id: ")
        
        query = (f""" INSERT INTO {books.TABLE_NAME} (name, description, writer_id) 
                    VALUES ('{name_of_books}', '{description}', {writer_id}) """)
        cursor.execute(query)
        
        connection = ConnectionService.instance()
        connection.commit()

    def show_book_info(self):
        cursor = self.__connectionService.get_cursor()
        name_of_book = input("Enter name of book: ")
        #try:
        query = (f""" SELECT description FROM {books.TABLE_NAME} WHERE name = '{name_of_book}' """)
        cursor.execute(query)
        info = cursor.fetchall()
        print(info)
        #except:
         #   print("Dont have this book in list")


