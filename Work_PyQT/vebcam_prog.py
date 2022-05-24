from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
import cv2 # импорт для работы с камерой и анализа изображения
import qimage2ndarray # импорт для перевода бинарного масива в Qimage(такой тип данных)
import sys



def display_frame(): # функция для отображения кадров с камеры, с определенной скоростью
    ret, frame = cap.read() # читает поток из камеры
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # делает кадр другого цвета, потому что стандратно оно красное, а так переводит в нормальный
    image = qimage2ndarray.array2qimage(frame) # переводим его в изображение Qimage из бинарного 
    label.setPixmap(QPixmap.fromImage(image)) # и каждый раз новое изображение, по сути, новый кадр отображается в label



app = QApplication([])
window = QWidget()
layout = QVBoxLayout()
window.setLayout(layout)


cap = cv2.VideoCapture(0) # обьект для видео, в дужках нулевая камера, так как она одна

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320) # установка размера окна с камерой, мы берем вверху переменную cap в которой камера
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

timer = QTimer() # создание таймера чтобы запускать функцию постоянно с определенным количевством раз в минуту
timer.start(60) # 60 раз в минуту
timer.timeout.connect(display_frame) # какую функцию мы запускаем


label = QLabel("No Camera Feed") # если камера не запускается, тогда будет эта надпись
button = QPushButton("Exit") # кнопка для выхода


button.clicked.connect(sys.exit) # выходит из приложения

layout.addWidget(button)
layout.addWidget(label)



window.show()
app.exec_()