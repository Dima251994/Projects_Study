# from prettytable import PrettyTable  # импорт бибилиотеки для красивой таблицы

# def print_table():
#     print("Pretty table")
#     table = PrettyTable() # создаем класс с которым мы работаем
#     table.field_names = ["id", "name", "description", "year"] # имя каждой колонки
    
#     table.add_row([1, "Andrew", "Friend", 21 ])
#     table.add_row([2, "Kolya", "Human", 35 ])
#     table.add_row([3, "Holo", "God", 800 ])
#     table.add_row([4, "Star", "Princess", 17 ])

#     print(table)

# print_table()

#import mongoengine

#print(vars(mongoengine.IntField()))


# while True:
#     n = int(input("Enter number "))
#     if n > 0: # сначала заканчиваем тут цикл если n больше нуля
#         break

# for _ in range(n): # и если n больше 0 тогда переходим сюда и делаем этот цикл
#     print("Hello")

from random import randint
data_series = [(randint(0,9999), randint(0,9999)) for i in range(5)] # создание рандомных чисел
print(data_series)
for point in data_series:
    print(point[0], point[1])


