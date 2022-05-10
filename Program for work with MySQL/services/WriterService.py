from colorama import Fore
from models import writers
from connection_to_SQL import *



class WriterService():
    __connectionService = None
    def __init__(self): # создаем инициализацю когда мы запускаем WriterService
        self.__connectionService = ConnectionService()

    def get_writers(self): # преедает список писателей
        cursor = self.__connectionService.get_cursor()
        cursor.execute(f""" SELECT * FROM {writers.TABLE_NAME} """)
        
        info_from_table = cursor.fetchall()
        print(info_from_table)

    def add_writer(self): # добавляет имя писателя
        cursor = self.__connectionService.get_cursor()

        name = input(Fore.YELLOW + "Enter name: " + Fore.RESET)

        query = (f""" INSERT INTO {writers.TABLE_NAME} (name) VALUES ('{name}') """)
        cursor.execute(query)
        connection = ConnectionService.instance() # важно соединение чтобы сделать commit что ниже
        connection.commit()
        print("SAVED!!!!!!")
