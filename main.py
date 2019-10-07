# coding:utf-8
import sys, time
from random import randint
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QLCDNumber, QLineEdit, QPushButton, QLabel, QApplication, QDialog, QGroupBox, QHBoxLayout, \
    QWidget, QDial, QVBoxLayout, QProgressBar, QFrame, QScrollArea, QFormLayout, QMainWindow, QSpinBox
from PyQt5.QtCore import Qt, QThread, pyqtSignal, QVariant, QObject
from  motor.common.basic import bind



class MyThread(QThread):
    change_value = pyqtSignal(int)

    def run(self):
        cnt = 0
        while cnt < 100:
            cnt += 1
            time.sleep(0.3)
            self.change_value.emit(cnt)


class Window(QDialog):
    name = bind("nameEdit", "text", str)
    pbar = bind('progressbar', 'value', float)

    def __init__(self):
        super().__init__()
        self.title = 'PyQt QLCDNumber  App'
        self.left = 500
        self.top = 400
        self.width = 400
        self.height = 300
        self.iconName = 'home.jpg'
        self.InitWindow()

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.InitUI()
        self.show()

    def InitUI(self):
        vbox = QVBoxLayout()
        self.progressbar = QProgressBar()
        self.progressbar.setStyleSheet('QProgressBar {border:2px solid grey;border-radius:9px;padding:1px}'
                                       'QProgressBar::chunk{background:red}'

                                       )
        self.progressbar.setTextVisible(True)
        self.progressbar.setObjectName('progressbar')

        # self.progressbar.setValue(50)
        vbox.addWidget(self.progressbar)

        self.button = QPushButton('RunProgress')
        self.button.clicked.connect(self.startProgressBar)
        vbox.addWidget(self.button)
        self.nameEdit = QLineEdit('I')
        self.nameEdit.setObjectName('nameEdit')
        vbox.addWidget(self.nameEdit)
        self.setLayout(vbox)

    def setProgressValue(self, val):
        self.pbar = val

        # self.progressbar.setValue(val)
        # self.progressbar.value()

    def startProgressBar(self):
        self.name = u'发安抚的'
        self.thread = MyThread()
        self.thread.change_value.connect(self.setProgressValue)
        self.thread.start()


if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
