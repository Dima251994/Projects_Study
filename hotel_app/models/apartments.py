# 2 создание класса Apartment и создание в meta соединения с БД которую мы инициализировали

import mongoengine # импорт монгоенджина

class Apartment(mongoengine.Document): # создания класса для работы с документами для монгоДБ
    # далее мы прописываем что добавить для БД
    # это представляет и показывает с чем мы работаем в БД
    # документ представляеться тремя полями, name, price,description
    name = mongoengine.StringField(required=True, unique=True) # это обозначает что name будет строчное значение, параметр Required - означает что значение должно быть обьязательным, unique - означает уникальное
    price = mongoengine.FloatField(required=True, min_value=15) # указываем вторую переменную для добавления в БД, min_value - означает минимальное значение которое должно быть вказано
    description = mongoengine.StringField() # описание номера 

    meta = { # это команды для mongodb, чтобы создать БД  и в дальнейшем с ней соединяться
        "db_alias":"hotel_db", # создание в нашей БД которая имеет название hoteldb и коллекцией apartments в файле mongosetup 
        "collection":"apartments"
    }