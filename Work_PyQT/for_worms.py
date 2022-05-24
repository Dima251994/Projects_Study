from PySide2.QtWidgets import *


app = QApplication([])

class Dialog(QDialog):
    def __init__(self, parent=None): # вызваем инициализацию чтобы мы могли наследовать все из главного класса
        super().__init__(parent)
        self.setWindowTitle("Example dialog") # устанавливаем название окна
        

        layout = QVBoxLayout() # создание главной схемы

        form_layout = QFormLayout() # создание схемы для рядов
        form_layout.addRow("Name", QLineEdit()) # тут мы добавляем ряд для FormLayout, QLineEdit обозначает то что мы можем писать что то в окно
        form_layout.addRow("Age", QLineEdit()) # добавление второго ряда
        
        


        buttons = QDialogButtonBox() # создание обьекта для кнопок
        buttons.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok) # установка кнопки cancel и OK
        
        layout.addLayout(form_layout) # добавить схему в главную схему
        layout.addWidget(buttons) # добавление кнопок в схему

        self.setLayout(layout) # добавление схемы через класс и ее отображение

 
dialog = Dialog() # инициализация обьекта класса для отображения диалога
dialog.show() # вызываем метод для показа диалога
app.exec_()