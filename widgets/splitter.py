#! /usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QApplication, QWidget,
        QLabel, QLineEdit)

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.lb = QLabel(self)
        le = QLineEdit(self)

        self.lb.move(40, 40)
        le.move(40, 100)
        le.textChanged[str].connect(self.onChanged)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Line edit')
        self.show()

    def onChanged(self, text):

        self.lb.setText(text)
        self.lb.adjustSize()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
