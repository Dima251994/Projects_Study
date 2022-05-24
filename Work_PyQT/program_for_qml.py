from PySide2.QtWidgets import QApplication
from PySide2.QtCore import QUrl 
from PySide2.QtQuick import QQuickView # для работы с Qml что мы написали в файле который грузим


app = QApplication([]) # основная программа
view = QQuickView() # модель чтобы подгружать инфо из файла url
url = QUrl("Work_PyQT\design.qml") # подтягивает инфо из файла по адресу

view.setSource(url) # тут задает это загруженное инфо в view, чтобы отобразить это
view.show() # отображает наше окно
app.exec_()