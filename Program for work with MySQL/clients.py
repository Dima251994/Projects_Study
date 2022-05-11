from switchlang import switch # импорт свича 
from colorama import Fore # импорт цветов из колорамы 
from connection_to_SQL import * # импорт соединения из файла
from services.WriterService import * # импорт из сервисов 
from services.BooksService import *
from prettytable import PrettyTable # импорт бибилиотеки для красивой таблицы



books_service = BooksService()
writer_service = WriterService()

def main():
    show_menu()

    

    while True: # цикл чтобы всегда работало
        action = input(Fore.YELLOW + "Enter action for work: " + Fore.RESET).lower().strip() # в инпуте нужно плюсовать, так как принимает только один параметр
        
        with switch(action) as s: # создание свича в котором передаем значение action и идет выбор
            s.case("b", lambda: books_service.get_books_list()) # каждый случай в зависимости от выбора
            s.case("i", lambda: books_service.show_book_info())
            s.case("r", lambda: books_service.add_book())
            s.case("w", lambda: writer_service.get_writers()) # показать писателей
            s.case("a", lambda: writer_service.add_writer()) # добавить писателелй
            s.case("wr", lambda: writer_service.remove_writer()) # удалить поета
            s.case("?", show_menu) # показ меню 
            s.case("t", writer_service.get_writer_id)
            s.case("e", exit)    # выход из программы по умолчанию в python
            s.default(lambda: print("Sorry, enter command")) # это запуститься если ни один из вариантов не подойдет, должна быть только функция


def show_menu():
    print(Fore.GREEN,"Choose action for work: ", Fore.RESET)
    print("[B]Book list")
    print("[I]Book info")
    print("[R]Register book")
    print("[W]Writer list")
    print("[A]Add writer")
    print("[WR]Remove writer")
    print("[?] Help")
    print("[E] Exit")
if __name__ == "__main__":
    #service = ConnectionService() # идет импорт класса ConnectionService
    #service.create_db() 
    main()

