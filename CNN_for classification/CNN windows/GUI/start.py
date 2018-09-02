# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'startWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from manual import Ui_manualWindow
from auto import Ui_autoWindow

class Ui_startWindow(object):
    def setupUi(self, startWindow):
        startWindow.setObjectName("startWindow")
        startWindow.resize(436, 282)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(13)
        startWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(startWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lblTopic = QtWidgets.QLabel(self.centralwidget)
        self.lblTopic.setGeometry(QtCore.QRect(40, 20, 261, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.lblTopic.setFont(font)
        self.lblTopic.setObjectName("lblTopic")
        self.rbManual = QtWidgets.QRadioButton(self.centralwidget)
        self.rbManual.setGeometry(QtCore.QRect(90, 80, 121, 51))
        self.rbManual.setObjectName("rbManual")
        self.rbAuto = QtWidgets.QRadioButton(self.centralwidget)
        self.rbAuto.setGeometry(QtCore.QRect(90, 130, 171, 41))
        self.rbAuto.setObjectName("rbAuto")
        self.btnNext = QtWidgets.QPushButton(self.centralwidget)
        self.btnNext.setGeometry(QtCore.QRect(290, 180, 101, 51))
        self.btnNext.setObjectName("btnNext")
        self.btnNext.clicked.connect(self.clickNext)

        startWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(startWindow)
        self.statusbar.setObjectName("statusbar")
        startWindow.setStatusBar(self.statusbar)

        self.retranslateUi(startWindow)
        QtCore.QMetaObject.connectSlotsByName(startWindow)

    def retranslateUi(self, startWindow):
        _translate = QtCore.QCoreApplication.translate
        startWindow.setWindowTitle(_translate("startWindow", "Intubation Mode"))
        self.lblTopic.setText(_translate("startWindow", "Select Intubation Mode"))
        self.rbManual.setText(_translate("startWindow", "Manual"))
        self.rbAuto.setText(_translate("startWindow", "Automatic"))
        self.btnNext.setText(_translate("startWindow", "Next"))

    def clickNext(self):
        print("Next is clicked")
        if self.rbManual.isChecked() == True:
            print("Manual is checked")
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_manualWindow()
            self.ui.setupUi(self.window)
            startWindow.hide()
            self.window.show()
        elif self.rbAuto.isChecked() == True:
            print("Auto is checked")
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_autoWindow()
            self.ui.setupUi(self.window)
            startWindow.hide()
            self.window.show()
        else:
            self.showMessagebox('Warning', 'Select the Intubation Mode')

    def showMessagebox(self, title, message):
        print("oops")
        messageBox = QtWidgets.QMessageBox()
        messageBox.setIcon(QMessageBox.Warning)
        messageBox.setWindowTitle("Warning")
        messageBox.setText("Select an Intubation Mode")
        messageBox.setStandardButtons(QMessageBox.Ok)
        messageBox.exec()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    startWindow = QtWidgets.QMainWindow()
    ui = Ui_startWindow()
    ui.setupUi(startWindow)
    startWindow.show()
    sys.exit(app.exec_())

