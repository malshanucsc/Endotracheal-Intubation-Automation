# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'autoWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_autoWindow(object):
    def setupUi(self, autoWindow):
        autoWindow.setObjectName("autoWindow")
        autoWindow.resize(732, 552)
        self.centralwidget = QtWidgets.QWidget(autoWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnStart = QtWidgets.QPushButton(self.centralwidget)
        self.btnStart.setGeometry(QtCore.QRect(500, 110, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(13)
        self.btnStart.setFont(font)
        self.btnStart.setObjectName("btnStart")
        self.btnSave = QtWidgets.QPushButton(self.centralwidget)
        self.btnSave.setGeometry(QtCore.QRect(500, 180, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(13)
        self.btnSave.setFont(font)
        self.btnSave.setObjectName("btnSave")
        self.btnEnd = QtWidgets.QPushButton(self.centralwidget)
        self.btnEnd.setGeometry(QtCore.QRect(500, 440, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(13)
        self.btnEnd.setFont(font)
        self.btnEnd.setObjectName("btnEnd")
        self.displayContent = QtWidgets.QGraphicsView(self.centralwidget)
        self.displayContent.setGeometry(QtCore.QRect(40, 110, 431, 381))
        self.displayContent.setObjectName("displayContent")
        self.btnStart_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btnStart_2.setGeometry(QtCore.QRect(40, 30, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(13)
        self.btnStart_2.setFont(font)
        self.btnStart_2.setObjectName("btnStart_2")
        autoWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(autoWindow)
        self.statusbar.setObjectName("statusbar")
        autoWindow.setStatusBar(self.statusbar)

        self.retranslateUi(autoWindow)
        QtCore.QMetaObject.connectSlotsByName(autoWindow)

    def retranslateUi(self, autoWindow):
        _translate = QtCore.QCoreApplication.translate
        autoWindow.setWindowTitle(_translate("autoWindow", "Autimatic Intubation Process"))
        self.btnStart.setText(_translate("autoWindow", "Start Process"))
        self.btnSave.setText(_translate("autoWindow", "Save Snapshot"))
        self.btnEnd.setText(_translate("autoWindow", "End Process"))
        self.btnStart_2.setText(_translate("autoWindow", "Configure Camera"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    autoWindow = QtWidgets.QMainWindow()
    ui = Ui_autoWindow()
    ui.setupUi(autoWindow)
    autoWindow.show()
    sys.exit(app.exec_())

