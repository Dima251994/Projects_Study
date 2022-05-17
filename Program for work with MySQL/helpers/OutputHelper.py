# Файл для нормального вывдения елементов из БД 

from colorama import Fore 
from prettytable import PrettyTable


def PrettyPrint(table_name, columns, rows):
    print(Fore.GREEN, table_name.center(20, "*"), Fore.RESET) # отображаем только название таблицы
    output_table = PrettyTable(columns) # тут мы сразу передаем названия колонок
    for tuple_0 in rows: # это нужно для правильного добавления и отображения строк
        work_list = [item for item in tuple_0]
        output_table.add_row(work_list)

    print(output_table)


def show_id(sql_info):
    for tuple_0 in sql_info: # для того чтобы показать номер из sql запроса 
        for item in tuple_0:
            return item # возвращение елемента из первого столбца из списка по SQL запросу



