import mysql.connector
from PySide2.QtCore import Slot # для работы с декоратором slot
from PySide2.QtWidgets import *

connection = mysql.connector.connect(
    user = "root",
    password = "9293709",
    host = "127.0.0.1",
    database = "sql_store"
)

@Slot() # создание декоратора который позволяет взаимодействовать с виджетами (работает и без него, пока неясно зачем он)
def for_show_info():
    cursor = connection.cursor()
    cursor.execute("""SELECT 
                        customer_id,
                        first_name,
                        last_name
                    FROM customers
                    WHERE customer_id = 1""")
    info_from_sql = cursor.fetchall()
    for item in info_from_sql:
        list_sql = list(item)
        end_list = []
        for converted in list_sql:
            end_list.append(str(converted))
        my_string = ", ".join(end_list)
        label.setText(my_string)
        
        
    
app = QApplication([])
window = QWidget()
layout = QVBoxLayout()
window.setLayout(layout)


button = QPushButton("Click me for info")  # создание кнопки
button.clicked.connect(for_show_info) # когда нажимаем кнопку, тогда запускается функция

label = QLabel("No info") # создание надписи


layout.addWidget(button) # добавляем елементы в макет
layout.addWidget(label)


window.show()
app.exec_()


