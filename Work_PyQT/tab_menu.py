from PySide2.QtWidgets import *
from PySide2.QtGui import QPixmap 
import sys

class Window(QMainWindow): # создание класса для работы с главным окном чтобы в него подьеднать подокна
    
    def __init__(self, parent=None): # инициализация для работы с окном
        super().__init__(parent)
        self.setWindowTitle("Program tab") # установка названия программы
        self.setCentralWidget(QLabel("Some text")) # установка надписи
        
####################################################################################
        file = self.menuBar().addMenu("File") # добавление таб меню вверху
        edit = self.menuBar().addMenu("Edit") # и еще несколько
        info = self.menuBar().addMenu("Info")
        file.addAction("Exit", sys.exit) # добавление кнопки в таб меню и действия чтобы выходить
        edit.addAction("Cut", self.cut_som) # добавление кнопки в другое таб меню и нашей функции


        # menu_name = ["File", "Edit", "Info"]
        # for name in menu_name: # можно добавить и через цикл
        #     self.menuBar().addMenu(name)

##########################################################################
        pixmap = QPixmap("Work_PyQT/google.png") # картинка для добавления
        label = QLabel() # инициализация надписи
        label.setPixmap(pixmap) # добавление картинки в надпись



        toolbar = QToolBar() # создание меню вверху под табом
        self.addToolBar(toolbar) # добавлению тулбара в наше окно класса 
        toolbar.addAction("Test") # добавления действия в наш тулбар 

        toolbar.addWidget(label) # добавление в виде виджета в наш тулбар
###########################################################
        status_bar = QStatusBar() # создание статус бара внизу
        status_bar.showMessage("Hello here") # что показать
        self.setStatusBar(status_bar) # установка статус бара в наше окно
        
        
######################################################################
        window = QWidget() # создание виджета так как не добавляется в главное окно класса
        layout = QVBoxLayout() # установка схемы
        window.setLayout(layout) # добавление схемы в окно виджет
        self.setCentralWidget(window) # добавление в наше окно класса

        checkbox = QCheckBox("For choose") # виджет для выбора чего то
        checkbox.stateChanged.connect(self.for_checkbox) # вызов функции когда мы выбираем что то
        layout.addWidget(checkbox) # добавление в схему

        self.resize(600, 600) # размер окна

    def cut_som(self):
        print("Cut")
    
    def for_checkbox(self, state):
        print("Hello", state) # отображает значение в state - если выбрано то там 2 а если нет то 0

app = QApplication([])
window = Window() # инициализация класса для окна
window.show() # показ окна

app.exec_()