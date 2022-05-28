# -*- coding: cp1251 -*-

from PySide2.QtWidgets import *
from PySide2.QtCore import Slot
from views.landing_window import LandingWindow # импорт подокна из папки

class MainWindow(QMainWindow): # создание класса для работы с главным окном чтобы в него подьеднать подокна
    def __init__(self, parent=None): # инициализация для работы с окном
        super().__init__(parent)
    

        self.setWindowTitle("Hotel app") # установка названия программы
        self.setMinimumSize(640,480) # установка минимального размера окна
        self.setMaximumSize(800,800) # установка максимального размера окна

        self.mdi = QMdiArea() # для работы с различными маленькими окнами которые будут в главноем окне, так как мы добавлии через self (MDI - многодокументальный интерфейс)
        self.setCentralWidget(self.mdi)
        self._createMenu() # вызываем функцию для меню
        self.showLandingWindow() # вызываем функцию подокна

        

    def _createMenu(self): # создаем функцию отдельно для меню
        self.menu = self.menuBar() # создание меню бара

        apartments = self.menu.addMenu("Apartments") # добавление в меню бар, пункта вверху бара apartments
        aptAdd = apartments.addAction("Add apartment") # добавление действия в виде подпункта меню
        aptAdd.setShortcut("Ctrl+N") # горячие клавишы, они рабочие, просто нужно писать название кнопок без пробела
        aptAdd.triggered.connect(lambda:print("Adding apartment")) # создание для работы с функциями
        

        apartments.addAction("View apartment")
        apartments.addAction("Search apartment")

        
        booking = self.menu.addMenu("Bookings") # добавляем пункта бронирования
        booking.addAction("Add booking") # добавления действия в один из пунктов менюбара
        booking.addAction("View booking")


        users = self.menu.addMenu("Users") # добалвление пункта пользователей
        users.addAction("Add user")
        users.addAction("View user") 

    def showLandingWindow(self): # функция для показа одного из подокон для отображения
        self.main_window = LandingWindow(self.mdi) # создаем класс который мы импортируем из файла landing_window из папки view нашего одного из многих окон внутри главного окна и привязываем его к mdi который работает с небольшыми окнами. В self.mdi мы передаем аргумент когда мы вызываем класс и таким образом у нас есть подокно
        self.main_window.showMaximized()


app = QApplication([])
main_window = MainWindow()

main_window.show()
app.exec_()
