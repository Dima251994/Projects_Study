# def next_number(numbers):
#     index = 1
#     for iter in numbers:
#         if len(numbers) > index and numbers[index] - numbers[index - 1] !=1:
#             return numbers[index]
#         index += 1
#     return None


# print(next_number([1,2,3,4,5]))



import mysql.connector

connection = mysql.connector.connect(
    user = "root",
    password = "9293709",
    host = "127.0.0.1",
    database = "work"
    )

connection.close()