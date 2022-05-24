from PySide2.QtCore import Qt, Slot
from PySide2.QtWidgets import *

app = QApplication([])
window = QWidget()
layout_grid = QGridLayout() # схема с колонками в которіе мі можем в определенное место вставлять
window.setLayout(layout_grid)


label = QLabel("Test")
button_1 = QPushButton("Button 1")
button_2 = QPushButton("Button 2")
button_3 = QPushButton("Button 3")


layout_grid.addWidget(label,0,0) # распологаем кнопки по различных местах
layout_grid.addWidget(button_1,1,1) # первое число по горизонтали, второе по вертикали
layout_grid.addWidget(button_2,2,2)
layout_grid.addWidget(button_3,3,3)


window.show()
app.exec_()