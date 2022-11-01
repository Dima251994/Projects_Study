from PySide2.QtCore import Qt # импорт для работы с командами различными чтобы менять интерфейс 
from PySide2.QtWidgets import *
from PySide2 import QtGui

app = QApplication([]) # работает и когда пустое
window = QWidget() # отдельное окошко на котором отображается то что мы добавим в него, можем задавать различные парметры, это отдельное окошко с разными виджетами, если будет еще одно такео окно то оно откроеться отдельно, как window_2 в примере внизу
#layout = QVBoxLayout() # макет для добавления всего в дальнейшем (Q Vertical Box layout - элементы будут добавляться в стовпчик, вертикально) (есть еще QHBoxLayout- тоже самое только горизонтально)
#window.setLayout(layout) # добавляем layout в окно наше

label_1 = QLabel("Hello")
font = QtGui.QFont()
font.setBold(True)

label_1.setFont(font)
slider = QSlider(Qt.Vertical) # добавляем слайдер (Qt.horizontal - горизонтальный)
button = QPushButton("I am button") # добавляем кнопку


#layout.addWidget(QLabel("Hello world")) # добавляем надпись в наш макет который выше
#layout.addWidget(slider) # добавляем слайдера
#layout.addWidget(button) # добавляем кнопку
#layout.addWidget(label_1)


window.show() # показ окна
app.exec_() # запуск программы в цикл чтобі всегда показывалось



