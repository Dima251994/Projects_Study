from prettytable import PrettyTable

def pretty_print(data, columns): # функция для красивого выведения таблицы, принимает два аргумента, данные для работы и имена колонок
    if not data or len(data) == 0: # проверяет есть ли данные в таблице
        print("Dont have data in document")
        return 
    else:
        output_table = PrettyTable(columns) 
        for item in data: # первым циклом мы заходим в обьект
            row_data = [] # создаем список для данных по которых мы прошлись
            for column in columns: # вторым циклом мы проходимся по списку columns что выше и каждое значение используем для того,
                                   # чтобы через append добавить в список row_data подписанные значения из БД  
               row_data.append(item[column.lower()])
            output_table.add_row(row_data) # добавляем значения в колонку таблички output_table, из списка row_data
         # а тут первый цикл  перейдет ко второму обьекту и будет добавлять новую строку в output_table
        print(output_table)

