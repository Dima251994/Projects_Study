from colorama import Fore 
from switchlang import switch
import services.mongo_setup  as dbsetup # импортируем модуль для соединения и называем его dbsetup
from services.apartment_service import Apartment_service
from services.guest_service import Guest_Service
from services.booking_service import Booking_service


def main():
    dbsetup.global_init() # используем функцию из mongo_setup для инициалиации подключения
    apartment_service = Apartment_service() # создание переменной с классом для дальнейшего использования из нее функции и для работы с апартаментами
    guest_service = Guest_Service() # импортируем для работы с гостями
    booking_service = Booking_service() # импортируем для работы с booking


    print(Fore.BLUE,"Hotel app", Fore.RESET)
    show_menu()

    while True:
        action = get_action()
        with switch(action) as s:
            s.case("l", apartment_service.get_apartments) # добавляем функцию для отображения апартаментов 
            s.case("a", apartment_service.add_apartment) # функция для добавления апартаментов
            s.case("s", apartment_service.search_apartmnet) # функция для поиска апартаментов
            s.case("v", guest_service.guests_list) # функция для показа гостей из списка
            s.case("g", guest_service.add_guest) # функция для добавления гостя
            s.case("b", booking_service.search_booking_by_name) # функция для поиска по имени
            s.case("m", booking_service.booking_add) # фукния для добавления брониравния
            s.case("sg", guest_service.search_guest)
            s.case("bbb", booking_service.booking_list)
            s.case("?", show_menu)
            s.case("e", exit)
            s.default(lambda:print("Enter valid command"))

def get_action():
    print(Fore.YELLOW, "Enter command >", Fore.RESET, end="")
    action = input().lower().strip()
    return action

def show_menu():
    print("[L] Apartment list")
    print("[A] Add apartment")
    print("[S] Search apartment")
    print("[V] View guests list")
    print("[G] Add guest")
    print("[B] Booking info")
    print("[M] Make booking")  # бронировать номер
    print("[BBB] Booking list")
    print("[?] Help")
    print("[E] Exit")

print("For new branch!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

if __name__ == "__main__":
    main()