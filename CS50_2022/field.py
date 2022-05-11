from prettytable import PrettyTable  # импорт бибилиотеки для красивой таблицы

def print_table():
    print("Pretty table")
    table = PrettyTable() # создаем класс с которым мы работаем
    table.field_names = ["id", "name", "description", "year"] # имя каждой колонки
    
    table.add_row([1, "Andrew", "Friend", 21 ])
    table.add_row([2, "Kolya", "Human", 35 ])
    table.add_row([3, "Holo", "God", 800 ])
    table.add_row([4, "Star", "Princess", 17 ])

    print(table)

print_table()