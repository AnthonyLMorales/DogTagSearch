
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from src.PDFReader import PDFReader
import os

class combo():
    def __init__(self):
        super(combo,self).__init__()
        self.app = QApplication(sys.argv)
        self.win = QMainWindow()
        self.win.setGeometry(200,200,300,300)
        self.win.setWindowTitle("Preproccess files")
        bt = QtWidgets.QPushButton(self.win)
        bt.setText("Click here")
        self.label = QtWidgets.QLabel(self.win)
        self.label.setText("Click button and wait")
        self.label.move(100,175)
        bt.move(100,200)
        bt.clicked.connect(self.clicked)
        self.nameLabel = QtWidgets.QLabel(self.win)
        self.nameLabel.setText('Enter Name of File:')
        self.line = QtWidgets.QLineEdit(self.win)
        self.line.move(40, 125)
        self.line.resize(200, 32)
        self.nameLabel.move(40, 100)
        self.win.show()
        sys.exit(self.app.exec_())
    def clicked(self):
        self.label.setText("Clicked")
        self.getFiles()
        self.label.setText("Proccessing over")
        
    def getFiles(self):
        fs = os.listdir("./UnProccessedFiles")
        file = str(self.line.text())+ ".csv"
        PDFReader(fs,file).open_pdf()


combo()