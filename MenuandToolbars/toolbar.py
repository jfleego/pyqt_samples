#! /usr/bin/python3

import sys
from PyQt5.QtWidgets import (QMainWindow, QApplication,
        qApp, QAction)
from PyQt5.QtGui import QIcon

class Example(QMainWindow):

    def __init__(self):

        super().__init__()
        self.initUI()

    def initUI(self):

        exitAction = QAction(QIcon('logout.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)

        self.statusBar()
        self.setGeometry(300, 300, 250, 100)
        self.setWindowTitle('MenuBar')
        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
