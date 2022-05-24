# from PySide2.QtWidgets import QApplication, QLabel # импортируем виджеты для работы. (Можно и через звездочку)

# app = QApplication([]) 

# label = QLabel("<font color=red size=40> Hello world </font>") 

# label.show() 
# app.exec_()

# from PySide2.QtCore import Qt # импорт для работы с командами различными чтобы менять интерфейс
# from PySide2.QtWidgets import *

# app = QApplication([]) # работает и когда пустое
# window = QWidget() # отдельное окошко на котором отображается то что мы добавим в него, можем задавать различные парметры, это отдельное окошко с разными виджетами, если будет еще одно такео окно то оно откроеться отдельно, как window_2 в примере внизу
# window_2 = QWidget() # второе окно

# label_2 = QLabel("For second window") # обозначения для воторого окна
# layout_2 = QVBoxLayout()
# layout_2.addWidget(label_2)

# layout = QVBoxLayout() # макет для добавления всего в дальнейшем (Q Vertical Box layout - элементы будут добавляться в стовпчик, вертикально) (есть еще QHBoxLayout- тоже самое только горизонтально)
# slider = QSlider(Qt.Horizontal) # добавляем слайдер (Qt.horizontal - горизонтальный)
# button = QPushButton("I am button") # добавляем кнопку

# layout.addWidget(QLabel("Hello world")) # добавляем надпись в наш макет который выше
# layout.addWidget(slider) # добавляем слайдера
# layout.addWidget(button) # добавляем кнопку

# window.setLayout(layout) # добавляем layout в окно наше
# window_2.setLayout(layout_2)

# window_2.show() # показ воторого окна
# window.show() # показ окна
# app.exec_() # запуск программы в цикл чтобі всегда показывалось


from PySide2.QtCore import Slot, Qt # для работы с декоратором slot
from PySide2.QtWidgets import *

label_text = "Hello world" # нужен чтобы когда мы крутим ползунок, чтобы значение когда постоянно менялось  и надпись рядом была одна и та же (Работает и без него, просто нужно парвильно сделать функцию)

@Slot() # создание декоратора который позволяет взаимодействовать с виджетами (работает и без него, пока неясно зачем он)
def onClick(): # создание функции для декоратора чтобы использовать
    label.setText(label_text)  # меняем текст на этот когда запущена функция
    

@Slot() 
def onSlider(value): # функция для показа из слайдера
    print("Value is ", value)
    tmp = f"{'Hello'} {value}" # передает значение из надписи и наше значение из ползунка каждый раз заново когда мы двигаем ползунок
    label.setText(tmp) # меняем текст прикрутке ползунка, но так как у нас текст из надписи, то он не меняется а добавляеться число только


app = QApplication([])
window = QWidget()
layout = QHBoxLayout()
window.setLayout(layout)


button = QPushButton("Click me")  # создание кнопки
button.clicked.connect(onClick) # когда нажимаем кнопку, тогда запускается функция

slider = QSlider(Qt.Horizontal) # создание слайдера
slider.valueChanged.connect(onSlider) # получение данных и их передача в функцию каждый раз когда двигаеться


label = QLabel(label_text) # создание надписи


layout.addWidget(button) # добавляем елементы в макет
layout.addWidget(label)
layout.addWidget(slider)

###################################
window.show()
app.exec_()