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

# while True:
#     try:
#         x = int(input("Enter number: "))
#     except ValueError:
#         print("Enter number not letter")
#     else: # это происходит если выполниться try
#         break
# print("x is", x)



# import sys


# for arg in sys.argv[1:]: 
#     print("Hello my name:", arg)


some_list = ["Hello", "My", "Darlling", "Amazing", "Stuff"]
print(some_list[0:-1]) # отображаем все елементы кроме последнего, если мы не значем сколько елементов в списке
