# # from hello import hello, main

# # main()

# name :str = "Michael"
# age:int = 24

# def print_info(name:str, age:int) -> None:
#     print(name, age)
#     #name_2 :str = "Andrew"


# class Test_class:
#     name:str = "Example"


#     def __init__(self,name: str,age: int) -> None:
#         self.class_name = name
#         self.class_age = age

#     def hello(name_func: str, age_func: int):
#         print(name_func, age_func)





# print(print_info.__code__.co_varnames) # показує аргументи функції у вигляді кортежу


# print(vars(print_info))
# print("Анотації з функції", print_info.__annotations__)
# print("Анотації з самого файлу (глобальні)",__annotations__)



# from dataclasses import dataclass, astuple, asdict # імпортуємо методи для автоматичного створення класу анотуванням, astuple та asdict потрібен для віображенням інфо по створену об'єкту класу


# @dataclass
# class Book:
#     name:str # вже створю по суті init для ініціалізації
#     year:int
#     is_bestseller:bool

#     def bestseller_check(self) -> str: # лише один метод для класу
#         if self.is_bestseller:
#             return "Bestseller"
#         else:
#             return "Not popular"


# my_book = Book("Hobbit", 1994, True)
# print(my_book.bestseller_check())
# print(astuple(my_book)) # повертає тільки аргументи які ми передали при створенні об'єкту
# print(asdict(my_book)) # повертає і анотацію і аргументи які ми передали



#print(f"{23:b}")

# import matplotlib.pyplot as plt

# x = [1,2,3,4,5]
# y = [3,5,8,1,2]
# plt.plot(x,y)

# plt.show()



from tkinter import Button, Checkbutton, Entry, Frame, IntVar, Label, Radiobutton, StringVar, Tk, font, mainloop, messagebox


class MainWindow:
    def __init__(self) -> None:
        self.main_window = Tk() # створення вікна 
        self.main_window.title("") # назва програми
        self.main_window.geometry("400x400")
        
        self.variable_day = StringVar()
        self.variable_day.set(0)
        self.list_day = ["Daytime", "Evening", "Off-Peak"]
        
        for day in self.list_day:
            radio_button = Radiobutton(self.main_window, 
                                       text=f"{day}",
                                       value=day,
                                       variable=self.variable_day)
            radio_button.pack()

        self.entry_minute = Entry(self.main_window)
        self.entry_minute.pack()

        self.accept_button = Button(self.main_window, text="Accept", command=self.accept_func)
        self.accept_button.pack()
        mainloop() # постійний запуск

    def accept_func(self):
        price = "You dont choice daytime"
        minutes = float(self.entry_minute.get())
        
        if self.variable_day.get() == self.list_day[0]:
            price = int(minutes * 0.07)
        elif self.variable_day.get() == self.list_day[1]:
            price = int(minutes * 0.12)
        elif self.variable_day.get() == self.list_day[2]:
            price = int(minutes * 0.05)
        messagebox.showinfo("Price", f"Price for {self.entry_minute.get()} is ${(price)} ")


        

window_gui = MainWindow()