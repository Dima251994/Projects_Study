from PySide2.QtWidgets import * 
from PySide2.QtCore import Qt, QSize # для манипуляции с виджетами, Qt - нужен для параметров различных
from PySide2 import QtGui


class Window(QMainWindow): # создание класса для работы с главным окном чтобы в него подьеднать подокна
    
    def __init__(self, parent=None): # инициализация для работы с окном
        super().__init__(parent)
        self.setWindowTitle("Autofill") # установка названия программы
        self.setMinimumSize(300,300) # установка минимального размера окна

        layout = QHBoxLayout() # создание схемы
        widget = QWidget() # создаем виджет так как главное окно не принимает схемы
        widget.setLayout(layout) # в виджет добавляем нашу схему
        self.setCentralWidget(widget) # добавляем виджет в главное окно
    

        label = QLabel("Test") # создание надписи

        inputField = QLineEdit()  # поле для введения чего либо
        inputField.setPlaceholderText("Enter here") # надпись на фоне пока не введены данные
        
        languages = ["Python", "C++", "C#", "JavaScript", "Java", "Ruby"]  # список для автозаполнения
        completer = QCompleter(languages, inputField) #  для автозаполенния, передаем два параметра, первый из чего мы берем автозаполение, а второй какой елемент для этого заполнителя
        inputField.setCompleter(completer) # устанавливаем комплитер на наше поле

        layout.addWidget(label)
        layout.addWidget(inputField) # добавления поля в схему
        

app = QApplication([])
window = Window()
window.show()
app.exec_()
