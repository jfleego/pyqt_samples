#! /usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow,
        QPushButton, QFrame)
from PyQt5.QtGui import QColor

class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.col = QColor(0, 0, 0)

        redb = QPushButton('Red', self)
        redb.setCheckable(True)
        redb.move(10, 10)
        redb.clicked[bool].connect(self.setColor)

        greenb = QPushButton('Green', self)
        greenb.setCheckable(True)
        greenb.move(10, 60)
        greenb.clicked[bool].connect(self.setColor)

        blueb = QPushButton('Blue', self)
        blueb.setCheckable(True)
        blueb.move(10, 110)
        blueb.clicked[bool].connect(self.setColor)

        self.frm = QFrame(self)
        self.frm.setGeometry(150, 25, 100, 100)
        self.frm.setStyleSheet("QWidget { background-color: %s }"
                % self.col.name())

        self.setGeometry(300, 300, 280, 160)
        self.setWindowTitle('Toggle button')

        self.show()

    def setColor(self, pressed):

        source = self.sender()

        if pressed:
            val = 255
        else:
            val = 0

        if source.text() == 'Red':
            self.col.setRed(val)
        if source.text() == 'Green':
            self.col.setGreen(val)
        if source.text() == 'Blue':
            self.col.setBlue(val)

        self.frm.setStyleSheet("QFrame { background-color: %s }"
                % self.col.name())


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
