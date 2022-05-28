from PySide2.QtWidgets import *
from PySide2.QtCore import Slot, Qt
from PySide2.QtGui import * # импорт для qtfont
from services.booking_service import Booking_service
import services.mongo_setup  as dbsetup # импорт соединения

class LandingWindow(QMdiSubWindow): # создаем класс для работы с подокном только он унаследует от другого подкласса 
    def __init__(self, mdi): # инициализация для работы с окном
        super().__init__()
        dbsetup.global_init() # создание соединения с монго бд
        
        self.booking = Booking_service()
        self.bookings = self.booking.booking_list() # берем список booking и делаем глобальным этот список

        
    
        widget = QWidget() # создаем виджет
        layout = QHBoxLayout() # создаем схему

        widgetLeft = self.renderLeftSide() # рендерим нормально левую сторону
        layout.addWidget(widgetLeft) # добавлем виджет в главную схему
        

        widgetRight = self.renderRightSide() # вызываем функцию и сохраняем в переменную
        layout.addWidget(widgetRight) # добавляем правый виджет который в переменной в главную схему
        
        widget.setLayout(layout) # добавление главного виджета в главную схему

        self.setWidget(widget) # устанавливаем виджет на наш класс окна
        mdi.addSubWindow(self) # мы подьеднали LandingWindow окно в mdi который находиться в классе Main_Window, чтобы оно было в главном внутри
        self.setWindowFlags(~Qt.WindowMinimizeButtonHint) # удаляет кнопки самого окна
        self.setAttribute(Qt.WA_DeleteOnClose, True) # закрывает окно если основное закрылось

    
    def renderLeftSide(self): # функция для левой стороны 
        widgetLeft = QWidget() # левый виджет
        widgetLeft.setMinimumWidth(270) # минимальный размер виджета
        layoutLeft = QVBoxLayout() # левая схема

        label = QLabel("<b>Booking list</b>")
        layoutLeft.addWidget(label)

        

        booking_list_view = QListWidget() # добавление списка в виде виджета
        for booking in self.bookings:
            item = QListWidgetItem()
            widget = self.render_item(
                booking["apartment_name"],
                booking["check_in_date"],
                booking["check_out_date"]
            )
            item.setSizeHint(widget.sizeHint())
            booking_list_view.addItem(item)
            booking_list_view.setItemWidget(item, widget)


        layoutLeft.addWidget(booking_list_view)
        
        #QListWidgetItem(f"Number one {bookings}", booking_list_view)

        widgetLeft.setLayout(layoutLeft)
        return widgetLeft
        

    def renderRightSide(self):
        widgetRight = QWidget() # правый виджет
        layoutRight = QVBoxLayout() # правая схема

        calendar = QCalendarWidget() # создание виджета календаря

        font = QFont("Helvetice", 14, 1) # создание определенного шрифта, первый аргумент шрифт, второй размер, третье жирность, четвертое курсив
        available_apartment_label = QLabel("Apartments available: <i>5</i>") # надпись для схемы, там где i будет только курсив
        available_apartment_label.setFont(font) # устанвока шрифта

        bookings_count = len(self.bookings) # количевство бронирований
        booking_created_label = QLabel(f"Booking created: <i>{bookings_count}</i>")
        booking_created_label.setFont(font)
        
        layoutRight.addWidget(calendar) # добавление календаря в правую схему
        layoutRight.addWidget(available_apartment_label) #  добавление надписей
        layoutRight.addWidget(booking_created_label)
        
        widgetRight.setLayout(layoutRight) # добавляем правую схему в правый виджет, правый виджет создан специально для правой схемы
        return widgetRight # наполняем информацией наш виджет и возвращаем наполненный виджет при вызове функции


    def render_item(self, guest_id, check_in_date, check_out_date): # Функция для парсинга елементов для добалвения в таблицу
        widget = QWidget()
        layout = QHBoxLayout()
        widget.setLayout(layout)
        
        layout.addWidget(QLabel(guest_id))
        
        dateIn = check_in_date.strftime("%Y-%m-%d")
        dateOut = check_out_date.strftime("%Y-%m-%d")

        
        layout.addWidget(QLabel(f"{dateIn}, {dateOut}"))

        return widget