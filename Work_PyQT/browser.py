from PySide2.QtWidgets import *
from PySide2.QtCore import Qt, QSize, QUrl # для манипуляции с виджетами, Qt - нужен для параметров различных
from PySide2 import QtGui
from PySide2.QtWebEngineWidgets import * # импорт для работы с интернет виджетами

class Window(QMainWindow): # создание класса для работы с главным окном чтобы в него подьеднать подокна
    
    def __init__(self, parent=None): # инициализация для работы с окном
        super().__init__(parent)
        self.setWindowTitle("My browser") # установка названия программы
        self.setMinimumSize(300,300) # установка минимального размера окна

        widget = QWidget() # создаем виджет так как главное окно не принимает схемы
        self.setCentralWidget(widget) # добавляем виджет в главное окно

        layout = QVBoxLayout() # создание схемы
        widget.setLayout(layout) # в виджет добавляем нашу схему


        browser = QWebEngineView() # создание браузера
        url = QUrl("https://www.google.com") # создаем с адресом переменную
        browser.setUrl(url) #  добавляем адрес в наш браузер 

        layout.addWidget(browser) # обавление брауера в нашу схему
        
    



app = QApplication([])
window = Window()
window.show()
app.exec_()
