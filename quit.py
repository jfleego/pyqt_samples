#! /usr/bin/python3

import sys
from PyQt5.QtWidgets import (QApplication, QWidget,
        QToolTip, QPushButton)
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        btn = QPushButton('Quit', self)
        btn.clicked.connect(QCoreApplication.instance().quit)
        btn.setToolTip('click this button to quit')
        btn.resize(btn.sizeHint())
        btn.move(200, 170)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('quit button')
        self.setWindowIcon(QIcon('./wather.jpg'))

        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
