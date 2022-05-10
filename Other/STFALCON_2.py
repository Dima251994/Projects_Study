# def next_number(numbers):
#     index = 1
#     for iter in numbers:
#         if len(numbers) > index and numbers[index] - numbers[index - 1] !=1:
#             return numbers[index]
#         index += 1
#     return None


#print(next_number([1,2,3,4,5]))



import mysql.connector

connection = mysql.connector.connect(
    user = "root",
    password = "9293709",
    host = "127.0.0.1",
    database = "sql_store")
    

cursor = connection.cursor() 

def get_data(func_cursor): # создание функции для получения данных
    func_cursor.execute(""" SELECT * FROM new_name """)
    info_from_new_name = func_cursor.fetchall()
    for employee in info_from_new_name:
        print(employee)


def add_data(cursor, connection):
    add_command = (""" INSERT INTO new_name()
                        VALUES (%(first_name)s, %(salary)s)""") # создаем форматирование строк для добавления инфо из словаря

    info_for_insert = { # словарь из которого берем инфо
        "first_name":"Dertovvv",
        "salary":2222}
    cursor.execute(add_command, info_for_insert ) # добавление инфо в БД

    connection.commit() # нужно для того чтобы добавить инфо в БД

#add_data(cursor, connection)
#get_data(cursor)

def get_data_my(my_cursor):
    my_cursor.execute(""" SELECT points FROM customers WHERE points > 2000 """)
    result = my_cursor.fetchall()
    for row_customers in result:
        print(row_customers)

def update_data(my_cursor, my_connection):
    my_cursor.execute(""" UPDATE customers SET points = 9999 WHERE customer_id = 1 """)
    my_connection.commit()


def delete_from_sql(my_cursor, my_connection):
    my_cursor.execute(""" DELETE FROM customers WHERE customer_id = 1 """)
    my_connection.commit()

#get_data_my(cursor)
#update_data(cursor, connection)
#delete_from_sql(cursor, connection)
connection.close()



def some_func():
    return print("Hello")


some_func()