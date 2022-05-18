# 1 Запуск инициализации соединения

import mongoengine 


def global_init(): 
    mongoengine.register_connection("hotel_db", name="hotel_db") # создаем соединение к БД (Там где name можно писать какое угодно название)
                                                                # тут мы можем прописывать домены, пароли, и т.д, если это все не локально находиться


