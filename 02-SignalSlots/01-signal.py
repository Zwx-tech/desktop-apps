from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton
from PySide6.QtCore import QSize
import PySide6.QtGui as QtGui
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Basic application')
        self.setMinimumSize(QSize(500, 500))

        self.button = QPushButton('Click me!')
        self.button.clicked.connect(self.button_clicked)
        self.button.setFont(QtGui.QFont('Verdana', 16))
        self.button.setStyleSheet('color: red')

        self.setCentralWidget(self.button)

    def button_clicked(self):
        self.button.setText('U have clicked me!')
        self.button.setEnabled(False)

        self.setWindowTitle("Button cliecked")

app = QApplication(sys.argv)

window = MainWindow()
window.show()

if __name__ == '__main__':
    app.exec()

