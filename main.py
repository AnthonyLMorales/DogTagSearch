from tkinter import CENTER
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QLabel, QFileDialog, QTextEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import search
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class ScrollLabel(QScrollArea):
 
    # constructor
    def __init__(self, *args, **kwargs):
        QScrollArea.__init__(self, *args, **kwargs)
 
        # making widget resizable
        self.setWidgetResizable(True)
 
        # making qwidget object
        content = QWidget(self)
        self.setWidget(content)
 
        # vertical box layout
        lay = QVBoxLayout(content)
 
        # creating label
        self.label = QLabel(content)
 
        # setting alignment to the text
        self.label.setAlignment(Qt.AlignLeft | Qt.AlignTop)
 
        # making label multi-line
        self.label.setWordWrap(True)
 
        # adding label to the layout
        lay.addWidget(self.label)

    # the setText method
    def setText(self, text):
        # setting text to the label
        self.label.setText(text)
class UI(QMainWindow):
    

    def __init__(self):
        self.dictt = { 'PetName':'0', 'Line1': '0', "Line2": '0', "Line3": '0', "Line4": '0', "Line5": '0'}
        self.outputt = []
        self.file = []
        self.name = ""
        self.file_to_write = ""
        self.textEdit = QTextEdit()
        super(UI, self).__init__()

        uic.loadUi("dialog.ui", self)

        self.label = QLabel('nas;lkdjf;lkajsdf;lkja;lskdjf;lkajds;flkja;lskdjf;lakjsdf;lkjasd;lfkja;lksjdf;lkja;dslfkja;lskdjf;lkajsdf;lkjasd;flkja;lskdfj;lkajsdf;lkajsdf', self)
        self.label.setGeometry(QtCore.QRect(190, 250, 281, 31))
        self.label.setObjectName("label")
        #self.label.setText(_translate("MainWindow", "Output"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        #self.label.adjustSize()


        text = "**Potentional dog tags will show here**"
 
        # creating scroll label
        self.label10 = ScrollLabel(self)
 
        # setting text to the label
        self.label10.setText(text)
 
        # setting geometry
        self.label10.setGeometry(190, 250, 281, 231)


        self.label2 = QLabel('Line 1', self)
        self.label2.setGeometry(QtCore.QRect(140, 60, 281, 31))

        self.label3 = QLabel('Line 2', self)
        self.label3.setGeometry(QtCore.QRect(140, 115, 281, 31))

        self.label4 = QLabel('Line 3', self)
        self.label4.setGeometry(QtCore.QRect(140, 165, 281, 31))

        self.label5 = QLabel('Line 4', self)
        self.label5.setGeometry(QtCore.QRect(475, 60, 281, 31))

        self.label6 = QLabel('Line 5', self)
        self.label6.setGeometry(QtCore.QRect(475, 115, 281, 31))

        self.label7 = QLabel('Pet Name', self)
        self.label7.setGeometry(QtCore.QRect(475, 165, 281, 31))
       
        self.label8 = QLabel('# of tags: ', self)
        self.label8.setGeometry(QtCore.QRect(75, 265, 281, 31))

        # Create textbox
        self.textbox1 = QLineEdit(self)
        self.textbox1.move(20, 20)
        self.textbox1.resize(280,40)
        self.textbox1.setGeometry(QtCore.QRect(190, 60, 131, 41))
        

        # Create textbox
        self.textbox2 = QLineEdit(self)
        self.textbox2.move(20, 20)
        self.textbox2.resize(280,40)
        self.textbox2.setGeometry(QtCore.QRect(190, 110, 131, 41))

        # Create textbox
        self.textbox3 = QLineEdit(self)
        self.textbox3.move(20, 20)
        self.textbox3.resize(280,40)
        self.textbox3.setGeometry(QtCore.QRect(190, 160, 131, 41))

        # Create textbox
        self.textbox4 = QLineEdit(self)
        self.textbox4.move(20, 20)
        self.textbox4.resize(280,40)
        self.textbox4.setGeometry(QtCore.QRect(340, 60, 131, 41))

        # Create textbox
        self.textbox5 = QLineEdit(self)
        self.textbox5.move(20, 20)
        self.textbox5.resize(280,40)
        self.textbox5.setGeometry(QtCore.QRect(340, 110, 131, 41))

        # Create textbox
        self.textbox6 = QLineEdit(self)
        self.textbox6.move(20, 20)
        self.textbox6.resize(280,40)
        self.textbox6.setGeometry(QtCore.QRect(340, 160, 131, 41))

        # Create a button in the window
        self.button1 = QPushButton('Cancel', self)
        self.button1.move(20,80)
        self.button1.setGeometry(QtCore.QRect(200, 210, 113, 32))

        # Create a button in the window
        self.button2 = QPushButton('Enter', self)
        self.button2.move(20,80)
        self.button2.setGeometry(QtCore.QRect(350, 210, 113, 32))

        # Create a button in the window
        self.button5 = QPushButton('Get Final CSV', self)
        self.button5.move(20,80)
        self.button5.setGeometry(QtCore.QRect(275, 510, 113, 32))
        
        # Create a button in the window
        self.button3 = QPushButton('Incorrect Info', self)
        self.button3.move(20,80)
        self.button3.setGeometry(QtCore.QRect(200, 480, 113, 32))

        # Create a button in the window
        self.button4 = QPushButton('Correct Info', self)
        self.button4.move(20,80)
        self.button4.setGeometry(QtCore.QRect(350, 480, 113, 32))


        self.button = self.findChild(QPushButton, "pushButton")

        # connect button to function on_click
        self.button2.clicked.connect(self.on_enter)
        self.button1.clicked.connect(self.on_cancel)
        self.button.clicked.connect(self.on_openfile)
        self.button4.clicked.connect(self.on_correct_info)
        self.button5.clicked.connect(self.on_download)
        self.show()

        
        self.show()

    def on_download(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            print(fileName)

        search.download(fileName)

    def on_cancel(self):
        self.textbox1.setText("")
        self.textbox2.setText("")
        self.textbox3.setText("")
        self.textbox4.setText("")
        self.textbox5.setText("")
        self.textbox6.setText("")
        self.label.setText("")
        self.dictt = { 'PetName':'0', 'Line1': '0', "Line2": '0', "Line3": '0', "Line4": '0', "Line5": '0'}
    def on_enter(self):
        #dictt = { 'PetName':'0', 'Line1': '0', "Line2": '0', "Line3": '0', "Line4": '0', "Line5": '0'}
        textboxValue1 = self.textbox1.text()
        textboxValue2 = self.textbox2.text()
        textboxValue3 = self.textbox3.text()
        textboxValue4 = self.textbox4.text()
        textboxValue5 = self.textbox5.text()
        textboxValue6 = self.textbox6.text()

        if textboxValue1 != "":
            self.dictt["Line1"] = textboxValue1
        if textboxValue2 != "":
            self.dictt["Line2"] = textboxValue2
        if textboxValue3 != "":
            self.dictt["Line3"] = textboxValue3
        if textboxValue4 != "":
            self.dictt["Line4"] = textboxValue4
        if textboxValue5 != "":
            self.dictt["Line5"] = textboxValue5
        if textboxValue6 != "":
            self.dictt["PetName"] = textboxValue6
        print(self.dictt)

        self.outputt = search.search(self.dictt, self.file_to_write)
        realoutput = ""
        for tag in self.outputt:
            realoutput += "Petname: "
            realoutput += str(tag[1])
            realoutput += "\n\n"
            realoutput += "Line 1: "
            realoutput += str(tag[4])
            realoutput += "\n\n"
            realoutput += "Line 2: "
            realoutput += str(tag[5])
            realoutput += "\n\n"
            realoutput += "Line 3: "
            realoutput += str(tag[6])
            realoutput += "\n\n"
            realoutput += "Line 4: "
            realoutput += str(tag[7])
            realoutput += "\n\n"
            realoutput += "Line 5: "
            realoutput += str(tag[8])
            realoutput += "\n\n"
            realoutput += "SKU: "
            realoutput += str(tag[2])
            realoutput += "\n"
            realoutput += "**NEXT TAG**\n\n"
        #self.label10.setText(str(self.outputt[0]))
        self.label10.setText(str(realoutput))
        self.label8.setText("# of tags:"+str(len(self.outputt)))

    def on_correct_info(self):
        search.right_entries.append(self.outputt)
        print("right entries ", search.right_entries)


    def on_openfile(self):
        self.file = QFileDialog.getOpenFileName(self," Open File", "", "All Files (*);;Python Files (*.py)")
        outputfile = self.file[0].split("/")
        print(self.file)
        self.file_to_write = "./ProccessFiles/"+ outputfile[len(outputfile) - 1] 
        print(self.file_to_write)
        
        
#initialize
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
