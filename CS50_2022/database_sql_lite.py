import sqlite3

connection = sqlite3.connect("contacts.db") # створюємо з'єднання, якщо немає такої БД то створить

cursor = connection.cursor()


select_sql = """ SELECT price FROM inventory """
# cursor.execute(""" UPDATE Inventory
#                    SET price = 100.00
#                    WHERE ItemID == 4 """) 

cursor.execute(select_sql)
data = cursor.fetchone() # повертає список в якому кожний елемент це кортеж з даними кожної стрічки з таблиці

print(data)


connection.commit() # зберагіємо БД для додвання того над чим працювали в самій БД
connection.close()