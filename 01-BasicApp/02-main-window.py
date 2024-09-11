from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton
from PySide6.QtCore import QSize
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Basic application')
        self.setMinimumSize(QSize(500, 500))

        button = QPushButton('Click me!')
        self.setCentralWidget(button)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

if __name__ == '__main__':
    app.exec()

