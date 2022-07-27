from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculator")
        self.setWindowIcon(QIcon("IconCalc.png"))
        self.setFixedSize(300,400)  

app = QApplication([])
window = Window()
window.show()
app.exec_()


