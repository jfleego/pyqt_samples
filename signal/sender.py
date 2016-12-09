#! /usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        qb1 = QPushButton('Button 1', self)
        qb1.move(20, 50)
        qb2 = QPushButton('Button 2', self)
        qb2.move(150, 50)

        qb1.clicked.connect(self.buttonClicked)
        qb2.clicked.connect(self.buttonClicked)

        self.statusBar()

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Event sender')
        self.show()

    def buttonClicked(self):

        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed!')

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
