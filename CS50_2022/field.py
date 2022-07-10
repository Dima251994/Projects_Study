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

# name = input("Enter name: ")

# with open("names.txt", "a") as file:
#      file.write(f"{name}\n")


# import sys # для доступу до командної строки аргументів

# from PIL import Image # імпорт бібліотеки

# load_image_file = ["11.png", "22.png"]
# images = [] # для збирання всіх картинок з командної строки

# for arg in load_image_file: # проходиться по всіх аргументах в в терміналі де ми вказали назви картинок, окрім назви файли, відлік йде з першого елементу щоб не попала назва файлу, яка йде першою в коді терміналу
#     image = Image.open(arg) # кожну картинку відкриває в PIL файл
#     images.append(image) # додаємо в список


# images[0].save( # зберігаємо картинку нову у вигляді гіфки, стартова нульова зі списку
#     "costumes.gif", save_all=True, append_images=[images[1]], duration=200, loop=0 # перше це назва, друге все зберегти, третє які картинки додати до гіфки, duration - тривалість, loop - безкінечно
# )




#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# import re
# check_email = "@dd"
# email = "some_namemail@@@@@.com"

# if re.search(".+@.*\.com", email): # тут вказує що ми хочемо знайти, а другий аргумент в чому шукаємо
#     print("Valid")
# else:
#     print("Invalid")
    
# L = [1, 2, 4, 8, 16, 32, 64]
# X = 5
# found = False
# i = 0
# while not found and i < len(L) :
#     if 2 ** X == L[i] :
#         found = True
#     else:
#         i = i + 1
# if found:
#     print("at index", i)
# else:
#     print(X, "not found")

#CAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

def test_func():
    return 2 + 2


def test_func_from_branch():
    return 2*566666676767676767677
