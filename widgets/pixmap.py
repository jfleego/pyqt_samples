#! /usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QApplication, QWidget,
        QLabel, QHBoxLayout)
from PyQt5.QtGui import QPixmap

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        hbox = QHBoxLayout(self)
        lb = QLabel(self)
        lb.move(30, 30)
        lb.setPixmap(QPixmap('../image/laptop.png'))
        hbox.addWidget(lb)
        self.setLayout(hbox)
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Pixmap')

        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
