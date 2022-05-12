from models import books
from connection_to_SQL import * 
from helpers.OutputHelper import PrettyPrint
from services.WriterService import * 


class BooksService():
    __connectionService = None
    __writerService = None
    def __init__(self):
        self.__connectionService = ConnectionService()
        self.__writerService = WriterService() # нужно инициализировать его как обьект класса, это такой переключатель на рахные классы

    def get_books_list(self):
        cursor = self.__connectionService.get_cursor()
        cursor.execute(f""" SELECT * FROM {books.TABLE_NAME} """)
        info_from_cursor = cursor.fetchall()
        
        columns = ["id", "name", "description", "writer_id"] # названия колонок когда мы будем использовать функцию для красивого вывдедения таблицы
        PrettyPrint(books.TABLE_NAME, columns, info_from_cursor)

    def show_books_with_authors(self): # функция которая показывает и книгу и имя автора
        cursor = self.__connectionService.get_cursor()
        cursor.execute(f""" SELECT
                                {books.TABLE_NAME}.name,
                                {books.TABLE_NAME}.description,
                                {writers.TABLE_NAME}.name' 
                            FROM {books.TABLE_NAME} 
                            JOIN {writers.TABLE_NAME}
                            ON writers.id = books.writer_id """)
        info_from_cursor = cursor.fetchall()
        
        columns = ["Book name","Description","Author name"]
        PrettyPrint("Author and books", columns, info_from_cursor)
        #print(info_from_cursor)


    # def get_books_list_return(self):
    #     cursor = self.__connectionService.get_cursor()
    #     cursor.execute(f""" SELECT * FROM {books.TABLE_NAME} """)
    #     return cursor.fetchall()

    def add_book(self):
        cursor = self.__connectionService.get_cursor()
        
        name_of_books = input("ENter book name: ")
        description = input("ENter description (not necesarry): ")
        author_name = input("Enter name for id: ")
        #writer_id = input("Enter writer id: ")
        writer_id = self.__writerService.get_writer_id(author_name)
        

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

    def book_only_one_author(self): # отображает книги только того автора которого мы пропишем имя
        cursor = self.__connectionService.get_cursor()
        author_name = input("Enter name for show author books: ") # вот тут пропишем имя
        cursor.execute(f""" SELECT
                                {books.TABLE_NAME}.name,
                                {books.TABLE_NAME}.description,
                                {writers.TABLE_NAME}.name 
                            FROM {books.TABLE_NAME} 
                            JOIN {writers.TABLE_NAME}
                            ON writers.id = books.writer_id
                            WHERE writers.name = '{author_name}' """)
        info_from_cursor = cursor.fetchall()
        columns = ["Book name","Description","Author name"]
        PrettyPrint(author_name + " books", columns, info_from_cursor)


