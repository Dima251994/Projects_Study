from models.guests import Guest 
from helper.output_helper import pretty_print

class Guest_Service(): 
    def guests_list(self): # функция для отобажения гостей
        print("Guests list")
        guest = Guest.objects()
        columns = ["Name", "Age", "Is_card"]
        pretty_print(guest, columns)


    def add_guest(self): # функция для добавления гостей
        print("Add guest")


        min_age = Guest.age.min_value # тут сохраняется минимальный возраст который мы указали в models
        guest = Guest()
         

        guest.name = input("Enter name: ")
        guest.age = self.get_age(f"Enter age: (min age = 16) ", min_age) # тут мы вызываем функцию для проверки корректоности возраста и введены ли цифры
        guest.is_card = False
        guest.save()

        print("Guest saved")

    def search_guest(self):
        name = input("Enter name for search guest: ")

        guest = Guest.objects().filter(name=name) # получаем обьекты из БД и выбираем определенные по методу filter

        if guest:
            return guest[0]
        # else:
        #     print("Not found")


        columns = ("Name", "Age") # колонки для названия в PrettyTable
        pretty_print(guest,columns) # функция для отображения таблицы, импортирована



    def get_age(self, message, minimum_age): # функция для обработки возраста
        while True:
            input_string = input(message) # принмает возраст
            
            try:
                input_string = int(input_string) # пытается пеервести то что ввели в цифру
                if input_string < minimum_age: # проверяет введенное число не меньше ли минимального возраста
                    print("ENter age more than 16 ")
                else:
                    return input_string
            except:
                print("Enter number not letter")


