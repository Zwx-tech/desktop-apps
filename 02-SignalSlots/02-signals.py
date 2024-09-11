from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from random import choice, random
import sys


class MainWindow(QMainWindow):

    WINDOW_TITLES = [
        "Window 1",
        "Window 2",
        "Window 3",
        "Window 4",
        "Window 5",
        'Error'
    ]

    def __init__(self):
        super().__init__()

        self.setWindowTitle('Basic application')
        self.setMinimumSize(500, 500)

        self.button = QPushButton('Click me!')
        self.button.clicked.connect(self.button_clicked)

        self.setCentralWidget(self.button)

        self.windowTitleChanged.connect(self.title_change)

    def button_clicked(self):
        self.setWindowTitle(choice(self.WINDOW_TITLES))

    def title_change(self):
        if self.windowTitle() == "Error":
            self.button.setDisabled(True)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

if __name__ == '__main__':
    app.exec()

