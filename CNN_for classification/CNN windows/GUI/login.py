# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import mode
import signup
import sqlite3

class Ui_loginWindow(object):


    def showMessageboxOk(self, title, message):
        messageBox = QtWidgets.QMessageBox()
        messageBox.setIcon(QMessageBox.Warning)
        messageBox.setWindowTitle("Warning")
        messageBox.setText(message)
        messageBox.setStandardButtons(QMessageBox.Ok)
        messageBox.exec()

    def loginCheck(self):
        print("Login Button Clicked! ")
        username = self.inputUsername.text()
        password = self.inputPassword.text()

        connection = sqlite3.connect("login.db")
        result = connection.execute("SELECT USERNAME FROM USERS WHERE USERNAME =?", (username,))

        if (len(result.fetchall()) > 0):
            for resultPassword in connection.execute("SELECT PASSWORD FROM USERS WHERE USERNAME =?", (username,)):
                if(resultPassword[0] == password):
                    print("User Found !")
                    loginWindow.hide()
                    self.mode_window = QtWidgets.QMainWindow()
                    self.ui = mode.Ui_selectWindow()
                    self.ui.setupUi(self.mode_window)
                    self.mode_window.show()
                else:
                    self.showMessageboxOk('Warning', 'Credentials are incorrect')
                    self.inputPassword.setText("")
        else:
            print("Incorrect")
            self.showMessageboxOk('Warning', 'User not found. Please Sign Up')
            self.inputUsername.setText("")
            self.inputPassword.setText("")

    def signUpCheck(self):
        print("Sign Up Button Clicked! ")
        self.signup_window = QtWidgets.QMainWindow()
        self.ui = signup.Ui_signUpWindow()
        self.ui.setupUi(self.signup_window)
        self.signup_window.show()


    def hideSignUp(self):
        self.signup_window.hide()

    def setupUi(self, loginWindow):
        loginWindow.setObjectName("loginWindow")
        loginWindow.resize(700, 591)
        loginWindow.setMinimumSize(QtCore.QSize(700, 591))
        loginWindow .setMaximumSize(QtCore.QSize(700, 591))
        self.centralwidget = QtWidgets.QWidget(loginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnLogin = QtWidgets.QPushButton(self.centralwidget)
        self.btnLogin.setEnabled(True)
        self.btnLogin.setGeometry(QtCore.QRect(290, 350, 91, 31))
        self.btnLogin.clicked.connect(self.loginCheck)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnLogin.setFont(font)
        self.btnLogin.setStyleSheet("QPushButton\n"
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
        self.btnLogin.setAutoDefault(True)
        self.btnLogin.setDefault(False)
        self.btnLogin.setObjectName("btnLogin")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(220, 170, 281, 31))
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
        self.label_4.setGeometry(QtCore.QRect(210, 300, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.inputPassword = QtWidgets.QLineEdit(self.centralwidget)
        self.inputPassword.setGeometry(QtCore.QRect(290, 290, 201, 31))
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
        self.graphicsView_3.setGeometry(QtCore.QRect(180, 160, 341, 251))
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
        self.btnSignUp = QtWidgets.QPushButton(self.centralwidget)
        self.btnSignUp.setEnabled(True)
        self.btnSignUp.setGeometry(QtCore.QRect(400, 350, 91, 31))
        self.btnSignUp.clicked.connect(self.signUpCheck)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnSignUp.setFont(font)
        self.btnSignUp.setStyleSheet("QPushButton\n"
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
        self.btnSignUp.setAutoDefault(True)
        self.btnSignUp.setDefault(False)
        self.btnSignUp.setObjectName("btnSignUp")
        self.graphicsView_3.raise_()
        self.btnLogin.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_8.raise_()
        self.label_4.raise_()
        self.inputPassword.raise_()
        self.line_2.raise_()
        self.label.raise_()
        self.line_3.raise_()
        self.inputUsername.raise_()
        self.btnSignUp.raise_()
        loginWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(loginWindow)
        self.statusbar.setObjectName("statusbar")
        loginWindow.setStatusBar(self.statusbar)

        self.retranslateUi(loginWindow)
        QtCore.QMetaObject.connectSlotsByName(loginWindow)
        loginWindow.setTabOrder(self.inputUsername, self.inputPassword)
        loginWindow.setTabOrder(self.inputPassword, self.btnLogin)
        loginWindow.setTabOrder(self.btnLogin, self.btnSignUp)
        loginWindow.setTabOrder(self.btnSignUp, self.graphicsView_3)

    def retranslateUi(self, loginWindow):
        _translate = QtCore.QCoreApplication.translate
        loginWindow.setWindowTitle(_translate("loginWindow", "Login"))
        self.btnLogin.setText(_translate("loginWindow", "Login"))
        self.label_2.setText(_translate("loginWindow", "PLEASE ENTER THE LOGIN DETAILS"))
        self.label_3.setText(_translate("loginWindow", "INTUBATION PROCESS"))
        self.label_8.setText(_translate("loginWindow", "All Right Reserved"))
        self.label_4.setText(_translate("loginWindow", "Password"))
        self.label.setText(_translate("loginWindow", "Username"))
        self.btnSignUp.setText(_translate("loginWindow", "SignUp"))


if __name__ == "__main__":
    print("hgg")
    import sys
    app = QtWidgets.QApplication(sys.argv)
    loginWindow = QtWidgets.QMainWindow()
    ui = Ui_loginWindow()
    ui.setupUi(loginWindow)
    loginWindow.show()
    sys.exit(app.exec_())

