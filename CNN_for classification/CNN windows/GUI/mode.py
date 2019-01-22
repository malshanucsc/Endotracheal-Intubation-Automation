# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mode.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from manual import Ui_manualWindow
from automatic import Ui_autoWindow

class Ui_selectWindow(object):

    def clickProceed(self):
        print("Proceed is clicked")
        if self.radioBtnManual.isChecked() == True:
            print("Manual is checked")
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_manualWindow()
            self.ui.setupUi(self.window)
            self.window.show()
            self.selectWindow.hide()
        elif self.radioBtnAuto.isChecked() == True:
            print("Auto is checked")
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_autoWindow()
            self.ui.setupUi(self.window)
            self.window.show()
            self.selectWindow.hide()
        else:
            self.showMessagebox('Warning', 'Select the Intubation Mode')

    def showMessagebox(self, title, message):
        print("oops")
        messageBox = QtWidgets.QMessageBox()
        messageBox.setIcon(QMessageBox.Warning)
        messageBox.setWindowTitle("Warning")
        messageBox.setText("Please Select an Intubation Mode")
        messageBox.setStandardButtons(QMessageBox.Ok)
        messageBox.exec()

    def setupUi(self, selectWindow):
        self.selectWindow = selectWindow
        selectWindow.setObjectName("selectWindow")
        selectWindow.resize(698, 588)
        self.centralwidget = QtWidgets.QWidget(selectWindow)
        self.centralwidget.setObjectName("centralwidget")
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
        self.graphicsView_3 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_3.setGeometry(QtCore.QRect(200, 200, 301, 191))
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
        self.btnProceed = QtWidgets.QPushButton(self.centralwidget)
        self.btnProceed.setEnabled(True)
        self.btnProceed.setGeometry(QtCore.QRect(310, 340, 91, 31))
        self.btnProceed.clicked.connect(self.clickProceed)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnProceed.setFont(font)
        self.btnProceed.setStyleSheet("QPushButton\n"
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
        self.btnProceed.setAutoDefault(True)
        self.btnProceed.setObjectName("btnProceed")
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
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(250, 210, 421, 31))
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
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(210, 230, 281, 21))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.radioBtnManual = QtWidgets.QRadioButton(self.centralwidget)
        self.radioBtnManual.setGeometry(QtCore.QRect(250, 260, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        self.radioBtnManual.setFont(font)
        self.radioBtnManual.setObjectName("radioBtnManual")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(0, 530, 701, 41))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.radioBtnAuto = QtWidgets.QRadioButton(self.centralwidget)
        self.radioBtnAuto.setGeometry(QtCore.QRect(250, 300, 221, 21))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        self.radioBtnAuto.setFont(font)
        self.radioBtnAuto.setObjectName("radioBtnAuto")
        selectWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(selectWindow)
        self.statusbar.setObjectName("statusbar")
        selectWindow.setStatusBar(self.statusbar)

        self.retranslateUi(selectWindow)
        QtCore.QMetaObject.connectSlotsByName(selectWindow)
        selectWindow.setTabOrder(self.radioBtnManual, self.radioBtnAuto)
        selectWindow.setTabOrder(self.radioBtnAuto, self.btnProceed)
        selectWindow.setTabOrder(self.btnProceed, self.graphicsView_3)

    def retranslateUi(self, selectWindow):
        _translate = QtCore.QCoreApplication.translate
        selectWindow.setWindowTitle(_translate("selectWindow", "Select the Mode"))
        self.label_3.setText(_translate("selectWindow", "INTUBATION PROCESS"))
        self.btnProceed.setText(_translate("selectWindow", "Proceed"))
        self.label_8.setText(_translate("selectWindow", "All Right Reserved"))
        self.label_2.setText(_translate("selectWindow", "PLEASE SELECT THE MODE"))
        self.radioBtnManual.setText(_translate("selectWindow", "Manual Intubation Process"))
        self.radioBtnAuto.setText(_translate("selectWindow", "Automatic Intubation Process"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    selectWindow = QtWidgets.QMainWindow()
    ui = Ui_selectWindow()
    ui.setupUi(selectWindow)
    selectWindow.show()
    sys.exit(app.exec_())

