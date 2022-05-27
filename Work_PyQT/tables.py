from PySide2.QtWidgets import *
from PySide2.QtCore import Qt, QSize # для манипуляции с виджетами, Qt - нужен для параметров различных
from PySide2 import QtGui


class Window(QMainWindow): # создание класса для работы с главным окном чтобы в него подьеднать подокна
    
    def __init__(self, parent=None): # инициализация для работы с окном
        super().__init__(parent)
        self.setWindowTitle("Program table") # установка названия программы
        self.setMinimumSize(300,300) # установка минимального размера окна

        layout = QVBoxLayout() # создание схемы
        widget = QWidget() # создаем виджет так как главное окно не принимает схемы
        widget.setLayout(layout) # в виджет добавляем нашу схему
        self.setCentralWidget(widget) # добавляем виджет в главное окно


        columnsName = ["Id", "Name", "Role"]
        table = QTableWidget() # создание таблицы
        table.setColumnCount(3) # установка количества колонок, так как без этого не отобразяться названия, таблица не знает сколько отображать
        table.setHorizontalHeaderLabels(columnsName) # установка названий вверху таблицы
        
        table.setRowCount(3) # установка количевства рядков, без этого не отобразяться данные
        table.setItem(0,0, QTableWidgetItem("First cell")) # первое по горизонтали(ряд), второе по вертикали(колонка)
        table.setItem(1,0, QTableWidgetItem("Second cell"))
        table.setItem(2,0, QTableWidgetItem("Third cell"))
        
        table.resizeColumnsToContents() # когда первый раз запускаем, то подтганяет под контент кторый в колонках
        
        

        table_item = table.horizontalHeaderItem(0) # работа с определенной колонкой по номеру из названий
        table_item.setTextColor("red") # вынесли в отделуню переменную вверху чтобы было легче работать с изменением цвета
        table_item.setToolTip("Help for column") # всплывающая подсказка для колонки когда мы наводим мышку
        table_item.setTextAlignment(Qt.AlignRight) # выравнивание названия колонки вправо, будет упираться в правую сторону

        font = QtGui.QFont() # создание определенного шрифта в виде переменной чтобы далее с ним работать, чтобы не писать длинный код
        font.setBold(True) # делаем его жырным
        font.setCapitalization(font.Capitalization.AllUppercase) # устанавлияваем все буквы большыми
        font.setPointSize(13) # установка размера букв 

        table_item.setFont(font) # устанавливаем font для нашего названия нашего одного столбца

        layout.addWidget(table) # добавление таблицы в схему



app = QApplication([])
window = Window()
window.show()
app.exec_()
