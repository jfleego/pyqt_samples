#! /usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QApplication, QWidget,
        QLabel, QComboBox)

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        combo = QComboBox(self)
        combo.addItem('Ubuntu')
        combo.addItem('Mandrova')
        combo.addItem('Fedora')
        combo.addItem('Arch')
        combo.addItem('Gentoo')
        combo.move(50, 50)
        combo.activated[str].connect(self.onActivated)

        self.lb = QLabel('Ubuntu', self)
        self.lb.move(50, 100)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('combo box')
        self.show()

    def onActivated(self, text):

        self.lb.setText(text)
        self.lb.adjustSize()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
