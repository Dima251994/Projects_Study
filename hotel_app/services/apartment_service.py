# 3 из models импортируем апартмент и по сути инициализируем класс Apartment  из модуля models.apatments

from colorama import Fore 
from models.apartments import Apartment # импортируем модель для работы и для создания обьектов в документе из models.apartment
from helper.helper_app import (get_price) # импортируем функцию помощника. В дужках мы можем указать какие функции мы хотим импортировать
from helper.output_helper import pretty_print

class Apartment_service():
   def get_apartments(self): # благодаря запуску этой функции мы инициализиурем Apartment из models
         print(Fore.GREEN, "Get apartment", Fore.RESET )

         apartments = Apartment.objects() # создаем переменную с классом для отображения обьектов в БД
         #print(apartments[0]["name"]) # так как apartment возвращает нам обьекты, то нам нужно сначала указать индекс обьекта а потом какое значение мы хотим использовать
         
         columns = ("Name", "Price", "Description") # колонки для названия в PrettyTable
         pretty_print(apartments,columns) # функция для отображения таблицы, импортирована
         

   def add_apartment(self): # функция для добавления апартаментов в БД
         print(Fore.GREEN, "Add apartment", Fore.RESET)

         apartment = Apartment() # создаем переменную класса Apartment
         
         apartment.name = input("Enter apartment name: ") # 
         apartment.price =  get_price("Enter price :") # используем функцию из helper для принятия числа
         apartment.description = input("Enter description: ")

         apartment.save() # сохраняет данные в БД

         print(Fore.BLUE, "Apartment saved", Fore.RESET)

   def search_apartmnet(self): # функция для поиска апартаментов
      print("Searh apartment")

      name = input("Enter name for search: ")

      apartments = Apartment.objects().filter(name=name) # получаем обьекты из БД и выбираем определенные по методу filter
      
      columns = ("Name", "Price", "Description") # колонки для названия в PrettyTable
      pretty_print(apartments,columns) # функция для отображения таблицы, импортирована
      





    
