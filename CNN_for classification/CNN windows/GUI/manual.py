# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'manual.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

import ntpath
import time
from threading import Thread

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap,QImage

import cv2

import sys

from PyQt5.QtWidgets import QGraphicsScene, QGraphicsPixmapItem

sys.path.insert(0, '../')

import label2





class Ui_manualWindow(object):
    def __init__(self):
        self.thread_exit = False
        self.UICount = 0
        self.scene = QGraphicsScene();
        self.imagelist=[]

    def setupUi(self, manualWindow):
        manualWindow.setObjectName("manualWindow")
        manualWindow.resize(844, 863)
        manualWindow.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.centralwidget = QtWidgets.QWidget(manualWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.viewTubeLocation = QtWidgets.QGraphicsView(self.centralwidget)
        self.viewTubeLocation.setGeometry(QtCore.QRect(100, 270, 428, 484))
        self.viewTubeLocation.setStyleSheet("QGraphicsView\n"
"{\n"
"    color: #fff;\n"
"    background-color: #fff;\n"
"    border-width:2px;\n"
"    border-color: #00796B;\n"
"    border-style: solid;\n"
"    border-radius: 2px;\n"
"}\n"
"")
        self.viewTubeLocation.setObjectName("viewTubeLocation")
        self.btnEndProcess = QtWidgets.QPushButton(self.centralwidget)
        self.btnEndProcess.setGeometry(QtCore.QRect(670, 770, 151, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 105, 92))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 105, 92))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 105, 92))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 105, 92))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 105, 92))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 105, 92))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.btnEndProcess.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        self.btnEndProcess.setFont(font)
        self.btnEndProcess.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.btnEndProcess.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: #ffffff;\n"
"    border-width:1px;\n"
"    border-color: #00695C;\n"
"    border-style: solid;\n"
"    border-radius: 8px;\n"
"    padding: 2px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"}")
        self.btnEndProcess.setAutoDefault(True)
        self.btnEndProcess.setObjectName("btnEndProcess")
        self.viewSavedSnaps = QtWidgets.QGraphicsView(self.centralwidget)
        self.viewSavedSnaps.setGeometry(QtCore.QRect(670, 320, 151, 351))
        self.viewSavedSnaps.setStyleSheet("QGraphicsView\n"
"{\n"
"    color: #fff;\n"
"    background-color: #fff;\n"
"    border-width:0px;\n"
"    border-color: #00796B;\n"
"    border-style: solid;\n"
"    border-radius: 2px;\n"
"}\n"
"")
        self.viewSavedSnaps.setObjectName("viewSavedSnaps")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(-1, 0, 851, 51))
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
        self.progressBarFileUpload = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBarFileUpload.setGeometry(QtCore.QRect(39, 130, 341, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 61, 92))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 61, 92))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 61, 92))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 61, 92))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 61, 92))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 61, 92))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.progressBarFileUpload.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.progressBarFileUpload.setFont(font)
        self.progressBarFileUpload.setStyleSheet("QProgressBar\n"
"{\n"
"    background-color: #ffffff;\n"
"    border-width:2px;\n"
"    border-color: #008071;\n"
"    border-style: solid;\n"
"    border-radius: 8px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"     background-color: #4DB6AC;\n"
"     width: 24%;\n"
" }")
        self.progressBarFileUpload.setProperty("value", 0)
        self.progressBarFileUpload.setObjectName("progressBarFileUpload")
        self.progressBarSnapshots = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBarSnapshots.setGeometry(QtCore.QRect(670, 280, 151, 16))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 61, 92))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 61, 92))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 61, 92))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 61, 92))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.progressBarSnapshots.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.progressBarSnapshots.setFont(font)
        self.progressBarSnapshots.setStyleSheet("QProgressBar\n"
"{\n"
"    background-color: #ffffff;\n"
"    border-width:2px;\n"
"    border-color: #008071;\n"
"    border-style: solid;\n"
"    border-radius: 8px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"     background-color: #4DB6AC;\n"
"     width: 24%;\n"
" }")
        self.progressBarSnapshots.setProperty("value", 0)
        self.progressBarSnapshots.setObjectName("progressBarSnapshots")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(0, 800, 851, 41))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.btnSaveSnapshot = QtWidgets.QPushButton(self.centralwidget)
        self.btnSaveSnapshot.setEnabled(True)
        self.btnSaveSnapshot.setGeometry(QtCore.QRect(250, 770, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnSaveSnapshot.setFont(font)
        self.btnSaveSnapshot.setStyleSheet("QPushButton\n"
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
        self.btnSaveSnapshot.setObjectName("btnSaveSnapshot")
        self.btnSaveSnapshot.clicked.connect(self.saveImage)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(39, 60, 421, 31))
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
        self.btnStartProcess = QtWidgets.QPushButton(self.centralwidget)
        self.btnStartProcess.setEnabled(True)
        self.btnStartProcess.setGeometry(QtCore.QRect(670, 190, 161, 31))
        self.btnStartProcess.clicked.connect(self.startIntubation)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnStartProcess.setFont(font)
        self.btnStartProcess.setStyleSheet("QPushButton\n"
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
        self.btnStartProcess.setObjectName("btnStartProcess")
        self.lblVideoName = QtWidgets.QLabel(self.centralwidget)
        self.lblVideoName.setGeometry(QtCore.QRect(39, 90, 130, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lblVideoName.setFont(font)
        self.lblVideoName.setObjectName("lblVideoName")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(650, 170, 20, 651))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.btnFileSelect = QtWidgets.QPushButton(self.centralwidget)
        self.btnFileSelect.setEnabled(True)
        self.btnFileSelect.setGeometry(QtCore.QRect(399, 130, 141, 21))
        self.btnFileSelect.clicked.connect(self.openFileNameDialog)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnFileSelect.setFont(font)
        self.btnFileSelect.setStyleSheet("QPushButton\n"
"{\n"
"    color: #fff;\n"
"    background-color: #4DB6AC;\n"
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
        self.btnFileSelect.setObjectName("btnFileSelect")
        self.btnCancelUploading = QtWidgets.QPushButton(self.centralwidget)
        self.btnCancelUploading.setGeometry(QtCore.QRect(559, 130, 102, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 105, 92))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 105, 92))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 105, 92))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 105, 92))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 105, 92))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 105, 92))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.btnCancelUploading.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        self.btnCancelUploading.setFont(font)
        self.btnCancelUploading.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: #ffffff;\n"
"    border-width:1px;\n"
"    border-color: #00695C;\n"
"    border-style: solid;\n"
"    border-radius: 8px;\n"
"    padding: 2px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"}")
        self.btnCancelUploading.setObjectName("btnCancelUploading")
        self.lblLandmark = QtWidgets.QLabel(self.centralwidget)
        self.lblLandmark.setGeometry(QtCore.QRect(40, 180, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lblLandmark.setFont(font)
        self.lblLandmark.setObjectName("lblLandmark")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(670, 240, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(70, 820, 701, 21))
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
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(-1, 160, 841, 21))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalScrollBarSnaps = QtWidgets.QScrollBar(self.centralwidget)
        self.verticalScrollBarSnaps.setGeometry(QtCore.QRect(810, 320, 20, 351))
        self.verticalScrollBarSnaps.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBarSnaps.setObjectName("verticalScrollBarSnaps")
        self.lblLoadImage = QtWidgets.QLabel(self.centralwidget)
        self.lblLoadImage.setGeometry(QtCore.QRect(100, 270, 428, 484))
        self.lblLoadImage.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lblLoadImage.setText("")
        self.lblLoadImage.setObjectName("lblLoadImage")
        self.lblNavigationTopic = QtWidgets.QLabel(self.centralwidget)
        self.lblNavigationTopic.setGeometry(QtCore.QRect(40, 220, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lblNavigationTopic.setFont(font)
        self.lblNavigationTopic.setObjectName("lblNavigationTopic")
        self.lblTubePosition = QtWidgets.QLabel(self.centralwidget)
        self.lblTubePosition.setGeometry(QtCore.QRect(220, 180, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lblTubePosition.setFont(font)
        self.lblTubePosition.setText("")
        self.lblTubePosition.setObjectName("lblTubePosition")
        self.lblNavigation = QtWidgets.QLabel(self.centralwidget)
        self.lblNavigation.setGeometry(QtCore.QRect(140, 220, 511, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lblNavigation.setFont(font)
        self.lblNavigation.setText("")
        self.lblNavigation.setObjectName("lblNavigation")
        manualWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(manualWindow)
        self.statusbar.setObjectName("statusbar")
        manualWindow.setStatusBar(self.statusbar)

        self.retranslateUi(manualWindow)
        QtCore.QMetaObject.connectSlotsByName(manualWindow)

    def retranslateUi(self, manualWindow):
        _translate = QtCore.QCoreApplication.translate
        manualWindow.setWindowTitle(_translate("manualWindow", "Manual Intubation"))
        self.btnEndProcess.setText(_translate("manualWindow", "End Process"))
        self.label_3.setText(_translate("manualWindow", "MANUAL INTUBATION PROCESS"))
        self.btnSaveSnapshot.setText(_translate("manualWindow", "Save Snapshot"))
        self.label_2.setText(_translate("manualWindow", "CHOOSE THE VIDEO FILE TO START THE PROCESS"))
        self.btnStartProcess.setText(_translate("manualWindow", "Start the Process"))
        self.lblVideoName.setText(_translate("manualWindow", "SampleVideo.mp4"))
        self.btnFileSelect.setText(_translate("manualWindow", "Choose to Upload"))
        self.btnCancelUploading.setText(_translate("manualWindow", "Cancel"))
        self.lblLandmark.setText(_translate("manualWindow", "Anatomical Location :"))
        self.label_7.setText(_translate("manualWindow", "Genarating the images"))
        self.label_8.setText(_translate("manualWindow", "All Right Reserved"))
        self.lblNavigationTopic.setText(_translate("manualWindow", "Navigation :"))

    def progrezz(self):
        self.completed = 0
        if str(self.lblVideoName.text()) != "" :
            while self.completed < 100:
                self.completed += 0.0001
                self.progressBarFileUpload.setValue(self.completed)

    def saveImageProgrezz(self):
        self.completed = 0
        while self.completed < 100:
            self.completed += 0.0001
            self.progressBarSnapshots.setValue(self.completed)

    def openFileNameDialog(self):
        print("File is being uploaded...")
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        self.fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()", "", "All Files (*);;Python Files (*.py)", options=options)
        videoName = ntpath.basename(self.fileName)
        self.lblVideoName.setText(videoName)
        self.progrezz()

    def saveImage(self):
        save_name="E:/Degree/4th year 1st semester/Project/Endotracheal-Intubation-Automation/CNN_for classification/CNN windows/Snapshots/"+str(time.time())+".jpg"
        save_img = cv2.cvtColor(self.display_img, cv2.COLOR_BGR2RGB)
        cv2.imwrite(save_name,save_img)





        r = 150.0 / self.display_img.shape[1]
        dim = (150, int(self.display_img.shape[0] * r))

        # perform the actual resizing of the image and show it
        resized_save_image = cv2.resize(self.display_img, dim, interpolation=cv2.INTER_AREA)


        #resized_save_image=cv2.resize(self.display_img,(175,100))

        save_height, save_width, save_channel = resized_save_image.shape
        bytesPerLine = 3 * save_width
        save_qImg = QtGui.QImage(resized_save_image.data, save_width, save_height, bytesPerLine, QImage.Format_RGB888)

        item = QGraphicsPixmapItem(QPixmap(save_qImg))
        self.scene.addItem(item)
        #print(self.scene)
        self.viewSavedSnaps.setScene(self.scene)
        self.saveImageProgrezz()



    def startIntubation(self):
        print("Process is being started...")
        thread2 = Thread(target=self.runvideo, args=())
        thread2.start()
        self.run.video_file = self.fileName

        time.sleep(1)

        thread = Thread(target=self.threaded_function, args=())

        if self.UICount == 1:

            thread.start()




    def runvideo(self):
        self.run = label2.prediction()
        self.UICount = 1

        # print(self.run.video_file)

        self.run.main2()


    def threaded_function(self):

        while (True):
            if self.thread_exit:
                return

            """if(isinstance(str(self.run.output_location),str)):
                self.lblTubePosition.setText(str(self.run.output_location))
            if(isinstance(self.run.navigation_message,str)):
                self.lblNavigation.setText(self.run.navigation_message)"""

            if(not(self.run.queue is None)):


                if (self.run.queue.isEmpty() == False):
                    list_obj=self.run.queue.dequeue()

                    self.lblTubePosition.setText(str(list_obj[0]))
                    self.lblNavigation.setText(list_obj[1])


                    self.display_img = cv2.cvtColor(list_obj[2], cv2.COLOR_RGB2BGR)
                    # cv2.imshow("kjkj",img)
                    height, width, channel = self.display_img.shape
                    bytesPerLine = 3 * width
                    qImg = QtGui.QImage(self.display_img.data, width, height, bytesPerLine, QImage.Format_RGB888)

                    pixmap = QPixmap(qImg)

                    # pixmap = QPixmap('C:\\Users\\Sandunika\\Downloads\\img\\{n}.jpg'.format(n=str((i % 5) + 1)))
                    self.lblLoadImage.setPixmap(pixmap)
                    time.sleep(0.1)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    manualWindow = QtWidgets.QMainWindow()
    ui = Ui_manualWindow()
    ui.setupUi(manualWindow)
    manualWindow.show()
    sys.exit(app.exec_())

