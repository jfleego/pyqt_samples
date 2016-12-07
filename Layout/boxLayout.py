#! /usr/bin/python3

import sys
from PyQt5.QtWidgets import (QApplication, QWidget,
        QLabel, QPushButton, QHBoxLayout, QVBoxLayout)

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        qb1 = QPushButton('Yes')
        qb2 = QPushButton('No')

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(qb1)
        hbox.addWidget(qb2)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Box layout')

        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
