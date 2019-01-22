# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signup.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import login
import sqlite3

class Ui_signUpWindow(object):

    def showMessageboxYesNo(self, title, message):
        messageBox = QtWidgets.QMessageBox()
        messageBox.setIcon(QMessageBox.Warning)
        messageBox.setWindowTitle("Warning")
        messageBox.setText(message)
        messageBox.setStandardButtons(QMessageBox.Yes, QMessageBox.No)
        messageBox.exec()

    def showMessageboxOk(self, title, message):
        print("Invalid User")
        messageBox = QtWidgets.QMessageBox()
        messageBox.setIcon(QMessageBox.Warning)
        messageBox.setWindowTitle("Warning")
        messageBox.setText(message)
        messageBox.setStandardButtons(QMessageBox.Ok)
        messageBox.exec()

    def insertData(self):
        username = self.inputUsername.text()
        email = self.inputEmailID.text()
        password = self.inputPassword.text()
        self.showMessageboxOk('Warning', 'New user added successfully')
        connection = sqlite3.connect("login.db")
        connection.execute("INSERT INTO USERS VALUES(?,?,?)", (username, email, password))
        connection.commit()
        connection.close()
        self.inputUsername.setText("")
        self.inputEmailID.setText("")
        #password = self.inputPassword.setText("")
        self.inputPassword.setText("")
        print("$$$$$$$")
        self.signUpWindow.hide()
        #login.hideSignUp()
        print("@@@@@")


    def setupUi(self, signUpWindow):
        self.signUpWindow=signUpWindow
        signUpWindow.setObjectName("signUpWindow")
        signUpWindow.resize(700, 591)
        self.centralwidget = QtWidgets.QWidget(signUpWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnOk = QtWidgets.QPushButton(self.centralwidget)
        self.btnOk.setEnabled(True)
        self.btnOk.setGeometry(QtCore.QRect(290, 400, 91, 31))
        self.btnOk.clicked.connect(self.insertData)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnOk.setFont(font)
        self.btnOk.setStyleSheet("QPushButton\n"
"{\n"
"    color: #fff;\n"
"    background-color: #00796B;\n"
"    border-width:1px;\n"
"    border-color: #00695C;\n"
"    border-style: solid;\n"
"    border-radius: 8px;\n"
"    padding: 2px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #018175, stop: 0.1 #018175, stop: 0.5 #018175, stop: 0.9 #018175, stop: 1 #018175);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"   background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #02695F, stop: 0.1 #02695F, stop: 0.5 #02695F, stop: 0.9 #02695F, stop: 1 #02695F);\n"
"}")
        self.btnOk.setAutoDefault(True)
        self.btnOk.setDefault(False)
        self.btnOk.setObjectName("btnOk")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(260, 170, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(" QLabel {\n"
"   color:#00695C;\n"
" }\n"
"")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 701, 51))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(" QLabel {\n"
"   background: #009688;\n"
"   color:#fff;\n"
" }")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(0, 550, 701, 21))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(" QLabel {\n"
" \n"
"   color:#90A4AE;\n"
" }")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(210, 350, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.inputPassword = QtWidgets.QLineEdit(self.centralwidget)
        self.inputPassword.setGeometry(QtCore.QRect(290, 340, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.inputPassword.setFont(font)
        self.inputPassword.setStyleSheet("QLineEdit\n"
"{\n"
"\n"
"    border-width:2px;\n"
"    border-color: #00796B;\n"
"    border-style: solid;\n"
"    border-radius: 2px;\n"
"}\n"
"")
        self.inputPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.inputPassword.setObjectName("inputPassword")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(210, 200, 281, 21))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.line_2.setFont(font)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 250, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setTextInteractionFlags(QtCore.Qt.TextEditorInteraction)
        self.label.setObjectName("label")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(0, 530, 701, 41))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.inputUsername = QtWidgets.QLineEdit(self.centralwidget)
        self.inputUsername.setGeometry(QtCore.QRect(290, 240, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.inputUsername.setFont(font)
        self.inputUsername.setAutoFillBackground(False)
        self.inputUsername.setStyleSheet("QLineEdit\n"
"{  \n"
"    border-width:2px;\n"
"    border-color: #00796B;\n"
"    border-style: solid;\n"
"    border-radius: 2px;\n"
"}\n"
"")
        self.inputUsername.setObjectName("inputUsername")
        self.graphicsView_3 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_3.setGeometry(QtCore.QRect(180, 160, 341, 281))
        self.graphicsView_3.setStyleSheet("QGraphicsView\n"
"{\n"
"    color: #fff;\n"
"    background-color: #fff;\n"
"    border-width:2px;\n"
"    border-color: #00796B;\n"
"    border-style: solid;\n"
"    border-radius: 2px;\n"
"}\n"
"")
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.btnCancel = QtWidgets.QPushButton(self.centralwidget)
        self.btnCancel.setEnabled(True)
        self.btnCancel.setGeometry(QtCore.QRect(400, 400, 91, 31))
        self.btnCancel.clicked.connect(self.closeWindow)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnCancel.setFont(font)
        self.btnCancel.setStyleSheet("QPushButton\n"
"{\n"
"    color: #fff;\n"
"    background-color: #00796B;\n"
"    border-width:1px;\n"
"    border-color: #00695C;\n"
"    border-style: solid;\n"
"    border-radius: 8px;\n"
"    padding: 2px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #018175, stop: 0.1 #018175, stop: 0.5 #018175, stop: 0.9 #018175, stop: 1 #018175);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"   background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #02695F, stop: 0.1 #02695F, stop: 0.5 #02695F, stop: 0.9 #02695F, stop: 1 #02695F);\n"
"}")
        self.btnCancel.setAutoDefault(True)
        self.btnCancel.setDefault(False)
        self.btnCancel.setObjectName("btnCancel")
        self.inputEmailID = QtWidgets.QLineEdit(self.centralwidget)
        self.inputEmailID.setGeometry(QtCore.QRect(290, 290, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.inputEmailID.setFont(font)
        self.inputEmailID.setAutoFillBackground(False)
        self.inputEmailID.setStyleSheet("QLineEdit\n"
"{  \n"
"    border-width:2px;\n"
"    border-color: #00796B;\n"
"    border-style: solid;\n"
"    border-radius: 2px;\n"
"}\n"
"")
        self.inputEmailID.setObjectName("inputEmailID")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(210, 300, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setTextInteractionFlags(QtCore.Qt.TextEditorInteraction)
        self.label_5.setObjectName("label_5")
        self.graphicsView_3.raise_()
        self.btnOk.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_8.raise_()
        self.label_4.raise_()
        self.inputPassword.raise_()
        self.line_2.raise_()
        self.label.raise_()
        self.line_3.raise_()
        self.inputUsername.raise_()
        self.btnCancel.raise_()
        self.inputEmailID.raise_()
        self.label_5.raise_()
        signUpWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(signUpWindow)
        self.statusbar.setObjectName("statusbar")
        signUpWindow.setStatusBar(self.statusbar)

        self.retranslateUi(signUpWindow)
        QtCore.QMetaObject.connectSlotsByName(signUpWindow)
        signUpWindow.setTabOrder(self.inputUsername, self.inputEmailID)
        signUpWindow.setTabOrder(self.inputEmailID, self.inputPassword)
        signUpWindow.setTabOrder(self.inputPassword, self.btnOk)
        signUpWindow.setTabOrder(self.btnOk, self.btnCancel)
        signUpWindow.setTabOrder(self.btnCancel, self.graphicsView_3)

    def retranslateUi(self, signUpWindow):
        _translate = QtCore.QCoreApplication.translate
        signUpWindow.setWindowTitle(_translate("signUpWindow", "SignUp"))
        self.btnOk.setText(_translate("signUpWindow", "Ok"))
        self.label_2.setText(_translate("signUpWindow", "CREATE NEW ACCOUNT"))
        self.label_3.setText(_translate("signUpWindow", "INTUBATION PROCESS"))
        self.label_8.setText(_translate("signUpWindow", "All Right Reserved"))
        self.label_4.setText(_translate("signUpWindow", "Password"))
        self.label.setText(_translate("signUpWindow", "Username"))
        self.btnCancel.setText(_translate("signUpWindow", "Cancel"))
        self.label_5.setText(_translate("signUpWindow", "Email ID"))

    def closeWindow(self):
        print("Window is closed")
        #self.showMessageboxYesNo('Warning', 'Are you sure you want to cancel adding a new user?')
        self.signUpWindow.hide()




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    signUpWindow = QtWidgets.QMainWindow()
    ui = Ui_signUpWindow()
    ui.setupUi(signUpWindow)
    signUpWindow.show()
    sys.exit(app.exec_())

