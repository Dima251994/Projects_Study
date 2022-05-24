# Графики

from PySide2 import QtGui
from PySide2.QtWidgets import *
from PySide2.QtCharts import QtCharts # отвечает за вывод графиков
from PySide2.QtGui import QPainter # отвечает за цвет
from random import randint

app = QApplication([])
window = QWidget()
layout = QVBoxLayout()
window.setLayout(layout)

chart = QtCharts.QChart() # создание обьекта графика, он абстрактный, его еще нужно добавить для отображения
line_series = QtCharts.QLineSeries() # сбор точок которые будут выведены на экран,  тоесть создание линии. (их может быть и больше одной)


data_series = [(i+1, randint(0,9999)) for i in range(200)] # создание рандомных чисел, будет списко из двох чисел(там где i+1- первое число, randint - второе)
                                                          # вот такой список с кортежом из двух елементов внутри - [(1, 1904), (2, 2692), (3, 4611), (4, 1070), (5, 438)]
for point in data_series: # перебираем список и выбираем из кортежа числа в переменную point
    line_series.append(point[0], point[1]) # добавлеям точки по X и по Y осях из созданного списка data series 


chart.addSeries(line_series) # тут мы добавляем наши точки которые были выбраны выше


chartView = QtCharts.QChartView(chart) # добавления самого обьекта графика, чтобы его отобразить

# Стилизация рафика
chart.setTitle("Random numbers") # Название графика
chart.createDefaultAxes() # Создание отображения осей чтобы мы видели какие числа и в каком промежутке мы отображаем

chartView.setRenderHint(QPainter.Antialiasing) # Более мягкая отрисовка линий
line_series.setColor(QtGui.QColor("red")) # установка цвета линии, QtGui назначает цвет
chartView.chart().setBackgroundBrush(QtGui.QColor("black")) # установка фона графика

layout.addWidget(chartView)

window.show()
window.resize(600,400) # отображения определенногo размера окна
app.exec_()


