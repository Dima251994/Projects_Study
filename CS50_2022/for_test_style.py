from PyQt5.QtWidgets import QApplication, QWidget

from PyQt5 import uic # для роботи з ui файлами які ми створимо в QT Designer

class UI(QWidget):
    def __init__(self):
        super().__init__()

        uic.loadUi("MyTest.ui", self) # грузимо наш ui файл, self потрібен щоб ми могли працювати з QWidget який унаслідуємо


app = QApplication([])
window = UI()
window.show()
app.exec_()