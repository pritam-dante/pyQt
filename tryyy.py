import csv
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5 import uic


class ApplicationWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.fileName = ""
        uic.loadUi('gui.ui', self)

        self.magFile.clicked.connect(self.loadMag)
        self.hjdFile.clicked.connect(self.loadHjd)
        self.proceed.clicked.connect(self.process)


    def readFile(self, File):
        with open(File, "r") as f:
            reader = csv.reader(f)
            data = list(reader)
            mag = len(data)
            print(mag)
        
        # self.textEdit.setText(str(mag))
        

    def loadMag(self):
        fileNameMag, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, "Open CSV", (QtCore.QDir.homePath()), "CSV (*.csv *.tsv *.txt)")

        self.fileName.setText(fileNameMag+' Loaded')
        self.readFile(fileNameMag)

                 

    def loadHjd(self,fileNameHjd):
        fileNameHjd, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, "Open CSV", (QtCore.QDir.homePath()), "CSV (*.csv *.tsv *.txt)")

        self.fileName2.setText(fileNameHjd+' Loaded')
        self.readFile(fileNameHjd)

    def process(self):
        self.div()

def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.setFixedHeight(500)
    application.setFixedWidth(700)
    application.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
