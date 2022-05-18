import mongoengine

class Booking(mongoengine.EmbeddedDocument): # создаем класс который позвоялет создавать струкуту внутри обьекта
    guest_id = mongoengine.ObjectIdField() # принимает id
    booked_date = mongoengine.DateTimeField() # для даты, когда бронировали
    check_in_date = mongoengine.DateTimeField(required=True) # дата когда заселились
    check_out_date = mongoengine.DateTimeField(required=True) # дата выселения

    @property # позволяет использовать функции при форматированнии  строк без вызова самой функции
    def duration(self): # функция для вычесления сколько жыл клиент
        dates_diff = self.check_out_date - self.check_in_date
        return dates_diff.days # возвращает разницу в днях


    # тут meta не нужен, так как мы работаем с другими документами
