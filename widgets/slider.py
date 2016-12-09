#! /usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QSlider, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        slide = QSlider(Qt.Horizontal, self)
        slide.setFocusPolicy(Qt.NoFocus)
        slide.setGeometry(30, 40, 100, 30)
        slide.valueChanged[int].connect(self.changeValue)

        self.label = QLabel(self)
        self.label.setGeometry(160, 40, 100, 100)
        self.label.setPixmap(QPixmap('../image/mute.png'))

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Slider volume')

        self.show()

    def changeValue(self, value):

        if value == 0:
            self.label.setPixmap(QPixmap('../image/mute.png'))
        elif value > 0 and value <= 30:
            self.label.setPixmap(QPixmap('../image/low-volume.png'))
        elif value > 30 and value <= 80:
            self.label.setPixmap(QPixmap('../image/medium-volume.png'))
        else:
            self.label.setPixmap(QPixmap('../image/high-volume.png'))


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
