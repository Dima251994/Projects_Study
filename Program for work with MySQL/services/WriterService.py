from colorama import Fore 
from models import writers 
from connection_to_SQL import *
from helpers.OutputHelper import PrettyPrint # импорт prettyTable
from helpers.OutputHelper import show_id



class WriterService():
    __connectionService = None
    def __init__(self): # создаем инициализацю когда мы запускаем WriterService
        self.__connectionService = ConnectionService()

    def get_writers(self): # преедает список писателей
        cursor = self.__connectionService.get_cursor()
        cursor.execute(f""" SELECT * FROM {writers.TABLE_NAME} """)
        
        info_from_table = cursor.fetchall()
        
        columns = ["id", "name"] # названия колонок 
        PrettyPrint(writers.TABLE_NAME, columns, info_from_table) # вызываем функцию для красивого отображения таблицы

    def add_writer(self): # добавляет имя писателя
        cursor = self.__connectionService.get_cursor()

        name = input(Fore.YELLOW + "Enter name: " + Fore.RESET)

        query = (f""" INSERT INTO {writers.TABLE_NAME} (name) VALUES ('{name}') """)
        cursor.execute(query)
        connection = ConnectionService.instance() # важно соединение чтобы сделать commit что ниже
        connection.commit()
        print("SAVED!!!!!!")

    def remove_writer(self):
        cursor = self.__connectionService.get_cursor()

        name = input(Fore.YELLOW + "Enter name: " + Fore.RESET)

        query = (f""" DELETE FROM {writers.TABLE_NAME} WHERE name = '{name}' """)
        cursor.execute(query)
        
        connection = ConnectionService.instance() # важно соединение чтобы сделать commit что ниже
        connection.commit()


    def get_writer_id(self, name): # Эта функция получет id писателя по имени, которое будет прописано при вызове функции
        cursor = self.__connectionService.get_cursor()

        cursor.execute(f""" SELECT * FROM {writers.TABLE_NAME} WHERE name = "{name}" """)
        

        info_from_table = cursor.fetchmany(size=1)
        number_id = show_id(info_from_table) # сохраняем нормальный id номер
        return number_id


