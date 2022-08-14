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


from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, 
                            QLabel, QVBoxLayout, QHBoxLayout, QGridLayout, QLineEdit)
from PyQt5.QtGui import QIcon, QFont # дадаємо для іконки імпорт, та імпорт для шрифта

class Window(QWidget): # створення класу для роботи з вікном
    def __init__(self): # унаслідування все з QWidget
        super().__init__()

        self.setWindowTitle("My program") # встановлення назви вікна
        self.setWindowIcon(QIcon("IconCalc.png")) # додавання іконки в программу
        #self.setFixedSize(300,400) # розмір екрану, ширина і висота відповідно
        self.setGeometry(100,300,300,300) # перші два параметра це стартова позиція по осі х і у, а два інші це розміри вікна при запуску
        #self.setStyleSheet("background-color:red") # встановка кольору заднього фону
        stylesheet = ( # створюємо окремо стиль і додаємо його внизу в наші стилі
            "background-color:red"
        )
        #self.setStyleSheet(stylesheet) # ось тут додаємо

        #QPushButton("Click me 2",self) # просто добавляем кнопку через init так як ми вже ініціалізуємо через класс
        #self.btn
        
        #self.create_btn() # викликаємо функцію яка додає кнопку
        #self.create_label() # викликаємо функцію яка додає напис

        
        
        horiz_layout = QHBoxLayout() # додаємо макет (має бути self яке вказує що ми додаємо макет в наш віджет)
   
        
        self.edit_line = QLineEdit() # створюємо лінію для вводу
        self.apply_text_btn = QPushButton("Apply")
        self.apply_text_btn.clicked.connect(self.get_text)
        self.label = QLabel("Not entered")

        horiz_layout.addWidget(self.edit_line) # додаємо віджет
        horiz_layout.addWidget(self.apply_text_btn)
        horiz_layout.addWidget(self.label)
        self.setLayout(horiz_layout) # другий спосіб який додає макет
        
        

    def create_btn(self): # функція для кнопки
        btn = QPushButton("Click me",self) # сама кнопка, перший аргумент це текст а другий це віджет який ми використовуємо
        #btn.move(100,0) # змістити кнопку по х та у
        btn.setGeometry(100,100,100,100) # перші два позиція, другі 2 розмір кнопки
        btn.setIcon(QIcon("number_1.png")) # встановка іконки на кнопці
        btn.setStyleSheet("background-color:green") # встановка стилю кнопки
        btn.clicked.connect(self.btn_click) # вказуємо яку функцію ми викликаємо при нажиманні кнопки

    def create_label(self):
        self.label = QLabel("Some text", self) # додаємо self щоб можна було використовувати кнопку в классі
        self.label.setStyleSheet("background-color:red")
        self.label.setGeometry(0,0,100,100) 
        self.label.setFont(QFont("Times New Roman", 10)) # встановка шрифту і розміру
    
    def btn_click(self): # функція яка змінює текст надпису при нажиманні кнопки
        self.label.setText("Changed text") 
        self.label.setStyleSheet("background-color:green")
    
    def get_text(self): # функція для кнопки щоб прийняти текст
        edit_line_text = self.edit_line.text() # бере текст з того що ми написали
        self.label.setText(edit_line_text) # змінює текст на той що ми написали в лінію
        


app = QApplication([])
window = Window() # тепер ця змінна  відноситься до классу Window
window.show() # бере всі методи які можливо 
app.exec_()

# import hello
# print(hello.__dict__.keys()) # потрібно додавати keys тому що покаже всю інфу, там багато всього


# class FirstClass:
#     def set_data(self, value):
#         self.data = value
#     def display(self):
#         print(self.data)

# class SecondClass(FirstClass):
#     def display(self):
#         print(f"Second class value: {self.data}")

# class ThirdClass(SecondClass):
#     def __init__(self, value):
#         self.data = value
    
#     def __add__(self, other):
#         return ThirdClass(self.data + other)
    
#     def __str__(self):
#        return f"[ThirdClass: {self.data}]"
#     # def __str__(self):
#     #     print(f"Hello its me: {self.data}")
#     def mul(self,other):
#         self.data *= other

# a = ThirdClass("abc")
# # a.display() # викликає метод з SecondClass і викорстовує дані яки ми ініціалізували в ThirdClass
# # print(a) # показує що повернуто в __str__

# # b = a + "xyz" # стоврює новий екзмпляр, завдяки __add__ (після __add__ можна прописати будь які команди) (b має всі методи класу ThirdClass)
# # b.display()
# # print(b) # повертає те що є в екзмплярі b

# # a.mul(3) # змінює екземпляр на місці
# # a.display()
# print(a.__str__())


# class Test:
#     pass

# Test.name = "Bob"
# x = Test()
# print(dir(x))