#! /usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox
from PyQt5.QtCore import Qt

class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        cb = QCheckBox('change title', self)
        cb.move(50,50)
        cb.toggle()
        cb.stateChanged.connect(self.changeTitle)
        self.statusBar()

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Change title')

        self.show()

    def changeTitle(self, state):

        if state == Qt.Checked:
            self.statusBar().showMessage('select')
        else:
            self.statusBar().showMessage('not select')

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
