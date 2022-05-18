import mongoengine

class Guest(mongoengine.Document):
    name = mongoengine.StringField(required=True)
    age = mongoengine.IntField(required=True, min_value=16)
    is_card = mongoengine.BooleanField(required=True, default=True) # для определения хочет ли опалитьт кредиткой, тут будет булевое значение(По умолчанию всегда кредиткой)

    meta = {
        "db_alias":"hotel_db",
        "collection":"guests"
    }