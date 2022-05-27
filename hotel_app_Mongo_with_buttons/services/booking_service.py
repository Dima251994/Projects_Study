from datetime import datetime
from helper.output_helper import pretty_print
from models.booking import Booking
from services.guest_service import Guest_Service
from services.apartment_service import Apartment_service
from models.apartments import Apartment

class Booking_service():

    def get_int(self, message): # функция для получения номера апартаментов
        while True:
            input_string = input(message) # принмает возраст
            
            try:
                input_string = int(input_string) # пытается пеервести то что ввели в цифру
                return input_string
            except:
                print("Enter number not letter")


    def booking_add(self):
        print("Add booking")

        guest_service = Guest_Service() # для подключения к гостям,  чтобы использовать функцию для поиска гостя
        apartment_service = Apartment_service() # для работы с апартаментами
        booking = Booking() # для работы с бронированием

        guest = guest_service.search_guest() # функция для поиска клиентов и функция возвращает обьект документа
        apartments = apartment_service.search_apartmnet() # функция для поиска апартаментов и возвращает апартамент

        row_idx = self.get_int("Please enter number of apartment ") # функция для получения индекса для апартаментов
        apartment = apartments[row_idx] # сохранение индекса апартаментов



        booking.guest_id = guest.id
        booking.booked_date = datetime.now() # поточная дата
        booking.check_in_date = datetime.now() 
        booking.check_out_date = datetime.now() 

        apartment.booking.append(booking) # берет из apartments models переменную booking, там список созданный специально для внутреннего вложения
        apartment.save()

    def search_booking_by_name(self):
        guest_service = Guest_Service()
        guest = guest_service.search_guest() # вызываем функцию для поиска и возвращения обьекта гостя 
        print(f"Name {guest['name']}, age {guest['age']}") # выбираем определенные елементы и выводим их значения
        #print(f"Name {guest.name}, age {guest.age}") # выбираем определенные елементы и выводим их значения, второй вариант
        apartments = Apartment.objects(booking__guest_id=guest.id)
        for apartment in apartments:
            print(f"Name apartment: {apartment.name}, price apartment: {apartment.price}")


        
