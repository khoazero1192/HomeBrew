# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created: Fri Jul 21 23:05:16 2017
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(617, 749)
        self.popupWin = QtGui.QMessageBox(Form)
        self.popupWin.setWindowTitle('Warning')
        self.chiatien_dictionary = {}
        
        self.gridLayoutWidget = QtGui.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(50, 30, 481, 81))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pushButton = QtGui.QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 2, 0, 1, 1)
        self.pushButton.clicked.connect(self.add_people)
        
        
        self.lineEdit_2 = QtGui.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.lineEdit = QtGui.QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.label = QtGui.QLabel(self.gridLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.verticalLayoutWidget = QtGui.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 120, 481, 541))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.textBrowser = QtGui.QTextBrowser(self.verticalLayoutWidget)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.verticalLayout.addWidget(self.textBrowser)
        self.Chia_Tien = QtGui.QPushButton(self.verticalLayoutWidget)
        self.Chia_Tien.setObjectName(_fromUtf8("Chia_Tien"))
        self.Chia_Tien.clicked.connect(self.calculate)
        self.clear = QtGui.QPushButton()
        self.verticalLayout.addWidget(self.clear)
        self.clear.setText("Clear")
        self.clear.clicked.connect(self.clear_data)
        
        
        self.verticalLayout.addWidget(self.Chia_Tien)
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(50, 670, 111, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Chia Tien", None))
        self.pushButton.setText(_translate("Form", "Add", None))
        self.label_2.setText(_translate("Form", "Money $$", None))
        self.label.setText(_translate("Form", "Name", None))
        self.Chia_Tien.setText(_translate("Form", "Calculate", None))
        self.label_3.setText(_translate("Form", "Author:  Khoa Au", None))
    
    def add_people(self):
        if (self.lineEdit.text() == "" )| (self.lineEdit_2.text() == ""):
            self.popupWin.setText("enter missing fields")
            self.popupWin.show()
            return
        else:
            
            self.chiatien_dictionary[str(self.lineEdit.text())] = str(self.lineEdit_2.text())
            self.textBrowser.append('Added: '+ str(self.lineEdit.text()) + " and their money: "  + str(self.lineEdit_2.text() + "\n") )
            
        self.lineEdit.clear()
        self.lineEdit_2.clear()
    def calculate(self):
        total = 0.0
        count = 0.0
        for key in self.chiatien_dictionary:
            total = total +  float(self.chiatien_dictionary[key])
            count = count + 1 
        #print self.chiatien_dictionary
        #print total
        average = total/count
        self.textBrowser.append(" Total amount of money is : " + str(total))
        self.textBrowser.append(" Number of people :" + str(count))
        self.textBrowser.append(" Each person pays :" + str(average))
        #print count
        
        self.textBrowser.append("*******************************************")
        #print average
        for key in self.chiatien_dictionary:
            new_value =float(self.chiatien_dictionary[key]) - average
            self.textBrowser.append(str(key) + " : " + "%.2f" %new_value)
        
        #print self.chiatien_dictionary
    def clear_data(self):
        self.textBrowser.append("Data Cleared")
        self.chiatien_dictionary = {}
        #print self.chiatien_dictionary
            
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

