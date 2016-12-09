#! /usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout,
        QPushButton, QLabel, QFontDialog, QSizePolicy)

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        vbox = QVBoxLayout()

        self.btn = QPushButton('Dialog', self)
        self.btn.move(20, 20)
        self.btn.setSizePolicy(QSizePolicy.Fixed,
                QSizePolicy.Fixed)
        self.btn.clicked.connect(self.showDialog)

        self.lb = QLabel('Knowledge only matters', self)
        self.lb.move(10, 60)

        vbox.addWidget(self.btn)
        vbox.addWidget(self.lb)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Input dialog')

        self.show()

    def showDialog(self):

        font, ok = QFontDialog.getFont()
        if ok:
            self.lb.setFont(font)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
