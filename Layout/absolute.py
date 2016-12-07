#! /usr/bin/python3

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        t1 = QLabel('Zetcode', self)
        t1.move(30, 10)

        t2 = QLabel('tutorial', self)
        t2.move(50, 25)

        t3 = QLabel('for programmer', self)
        t3.move(70, 40)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Absolute')

        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
