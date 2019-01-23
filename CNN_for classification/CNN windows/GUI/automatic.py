# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'automatic.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from threading import Thread
import time
import cv2
import os
import sys
from PyQt5.QtGui import QPixmap,QImage
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsPixmapItem
import mode

sys.path.insert(0, '../')
import label2

class Ui_autoWindow(object):
    def __init__(self):
        self.thread_exit = False
        self.UICount = 0
        self.scene = QGraphicsScene();
        self.imagelist=[]
        self.started = False


    def setupUi(self, autoWindow):
        self.autoWindow = autoWindow
        autoWindow.setObjectName("autoWindow")
        autoWindow.resize(730, 863)
        self.centralwidget = QtWidgets.QWidget(autoWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 120, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.viewTubeLocation = QtWidgets.QGraphicsView(self.centralwidget)
        self.viewTubeLocation.setGeometry(QtCore.QRect(40, 300, 428, 484))
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
        self.btnCancel = QtWidgets.QPushButton(self.centralwidget)
        self.btnCancel.setGeometry(QtCore.QRect(560, 160, 102, 21))
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
        self.btnCancel.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        self.btnCancel.setFont(font)
        self.btnCancel.setStyleSheet("QPushButton\n"
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
        self.btnCancel.setObjectName("btnCancel")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(550, 260, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(0, 800, 841, 41))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 190, 771, 21))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(0, 820, 841, 21))
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
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 851, 51))
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
        self.btnStartProcess = QtWidgets.QPushButton(self.centralwidget)
        self.btnStartProcess.setEnabled(True)
        self.btnStartProcess.setGeometry(QtCore.QRect(550, 220, 161, 31))
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
        self.progressBarAuto = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBarAuto.setGeometry(QtCore.QRect(40, 160, 341, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.progressBarAuto.setFont(font)
        self.progressBarAuto.setStyleSheet("QProgressBar\n"
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
        self.progressBarAuto.setProperty("value", 0)
        self.progressBarAuto.setObjectName("progressBarAuto")
        self.btnEndProcess = QtWidgets.QPushButton(self.centralwidget)
        self.btnEndProcess.setGeometry(QtCore.QRect(550, 780, 161, 31))
        self.btnEndProcess.clicked.connect(self.endProcess)
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
        self.btnEndProcess.setObjectName("btnEndProcess")


        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(510, 200, 20, 621))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.btnChooseCamera = QtWidgets.QPushButton(self.centralwidget)
        self.btnChooseCamera.setEnabled(True)
        self.btnChooseCamera.setGeometry(QtCore.QRect(400, 160, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnChooseCamera.setFont(font)
        self.btnChooseCamera.setStyleSheet("QPushButton\n"
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
        self.btnChooseCamera.setObjectName("btnChooseCamera")
        self.progressBarSnaps = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBarSnaps.setGeometry(QtCore.QRect(550, 290, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.progressBarSnaps.setFont(font)
        self.progressBarSnaps.setStyleSheet("QProgressBar\n"
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
        self.progressBarSnaps.setProperty("value", 0)
        self.progressBarSnaps.setObjectName("progressBarSnaps")
        self.graphicsViewSavedSnaps = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsViewSavedSnaps.setGeometry(QtCore.QRect(550, 330, 161, 341))
        self.graphicsViewSavedSnaps.setStyleSheet("QGraphicsView\n"
"{\n"
"    color: #fff;\n"
"    background-color: #fff;\n"
"    border-width:0px;\n"
"    border-color: #00796B;\n"
"    border-style: solid;\n"
"    border-radius: 2px;\n"
"}\n"
"")
        self.graphicsViewSavedSnaps.setObjectName("graphicsViewSavedSnaps")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 70, 421, 31))
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
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 100, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btnSaveSnaps = QtWidgets.QPushButton(self.centralwidget)
        self.btnSaveSnaps.setEnabled(True)
        self.btnSaveSnaps.setGeometry(QtCore.QRect(210, 790, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnSaveSnaps.setFont(font)
        self.btnSaveSnaps.setStyleSheet("QPushButton\n"
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
        self.btnSaveSnaps.setObjectName("btnSaveSnaps")
        self.btnSaveSnaps.clicked.connect(self.saveImage)
        self.lblLoadImage = QtWidgets.QLabel(self.centralwidget)
        self.lblLoadImage.setGeometry(QtCore.QRect(40, 300, 428, 484))
        self.lblLoadImage.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lblLoadImage.setText("")
        self.lblLoadImage.setObjectName("lblLoadImage")
        self.lblLandmark = QtWidgets.QLabel(self.centralwidget)
        self.lblLandmark.setGeometry(QtCore.QRect(40, 210, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lblLandmark.setFont(font)
        self.lblLandmark.setObjectName("lblLandmark")
        self.lblNavigationTopic = QtWidgets.QLabel(self.centralwidget)
        self.lblNavigationTopic.setGeometry(QtCore.QRect(40, 250, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lblNavigationTopic.setFont(font)
        self.lblNavigationTopic.setObjectName("lblNavigationTopic")
        self.lblTubePosition = QtWidgets.QLabel(self.centralwidget)
        self.lblTubePosition.setGeometry(QtCore.QRect(210, 210, 191, 31))
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
        self.lblNavigation.setGeometry(QtCore.QRect(140, 250, 361, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lblNavigation.setFont(font)
        self.lblNavigation.setText("")
        self.lblNavigation.setObjectName("lblNavigation")
        self.btnOpenFolder = QtWidgets.QPushButton(self.centralwidget)
        self.btnOpenFolder.setEnabled(True)
        self.btnOpenFolder.setGeometry(QtCore.QRect(550, 680, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnOpenFolder.setFont(font)
        self.btnOpenFolder.setStyleSheet("QPushButton\n"
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
        self.btnOpenFolder.setObjectName("btnOpenFolder")
        self.btnOpenFolder.clicked.connect(self.openSanpsFolder)
        self.verticalScrollBar_2 = QtWidgets.QScrollBar(self.centralwidget)
        self.verticalScrollBar_2.setGeometry(QtCore.QRect(695, 330, 21, 341))
        self.verticalScrollBar_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar_2.setObjectName("verticalScrollBar_2")
        autoWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(autoWindow)
        self.statusbar.setObjectName("statusbar")
        autoWindow.setStatusBar(self.statusbar)

        self.retranslateUi(autoWindow)
        QtCore.QMetaObject.connectSlotsByName(autoWindow)

    def retranslateUi(self, autoWindow):
        _translate = QtCore.QCoreApplication.translate
        autoWindow.setWindowTitle(_translate("autoWindow", "Automatic Intubation"))
        self.label_4.setText(_translate("autoWindow", "CameraResource 001"))
        self.btnCancel.setText(_translate("autoWindow", "Cancel"))
        self.label_7.setText(_translate("autoWindow", "Genarating the images"))
        self.label_8.setText(_translate("autoWindow", "All Right Reserved"))
        self.label_3.setText(_translate("autoWindow", "AUTOMATIC INTUBATION PROCESS"))
        self.btnStartProcess.setText(_translate("autoWindow", "Start the Process"))
        self.btnEndProcess.setText(_translate("autoWindow", "End Process"))
        self.btnChooseCamera.setText(_translate("autoWindow", "Choose the Camera"))
        self.label_2.setText(_translate("autoWindow", "CHOOSE THE VIDEO CAMERA RESOURCE HERE"))
        self.label.setText(_translate("autoWindow", "Configuring the camera"))
        self.btnSaveSnaps.setText(_translate("autoWindow", "Save Snapshot"))
        self.lblLandmark.setText(_translate("autoWindow", "Anatomical Location :"))
        self.lblNavigationTopic.setText(_translate("autoWindow", "Navigation :"))
        self.btnOpenFolder.setText(_translate("manualWindow", "Open Folder"))

    def saveImageProgrezz(self):
        self.completed = 0
        while self.completed < 100:
            self.completed += 0.0001
            self.progressBarSnaps.setValue(self.completed)

    def saveImage(self):
        save_name="D:/Academic/4th Year/1st Semester/Project SCS- 4123/Endotracheal-Intubation-Automation/CNN_for classification/CNN windows/Snapshot/"+str(time.time())+".jpg"
        save_img = cv2.cvtColor(self.display_img, cv2.COLOR_BGR2RGB)
        cv2.imwrite(save_name,save_img)

        r = 150.0 / self.display_img.shape[1]
        dim = (150, int(self.display_img.shape[0] * r))

        # perform the actual resizing of the image and show it
        resized_save_image = cv2.resize(self.display_img, dim, interpolation=cv2.INTER_AREA)

        save_height, save_width, save_channel = resized_save_image.shape
        bytesPerLine = 3 * save_width
        save_qImg = QtGui.QImage(resized_save_image.data, save_width, save_height, bytesPerLine, QImage.Format_RGB888)

        item = QGraphicsPixmapItem(QPixmap(save_qImg))
        self.scene.addItem(item)
        #print(self.scene)
        self.graphicsViewSavedSnaps.setScene(self.scene)
        self.saveImageProgrezz()

    def startIntubation(self):
        if (self.started):
            print("End the Processs first")
        else:
            self.started = True
            print("Process is being started...")
            self.thread2 = Thread(target=self.runvideo, args=())
            self.thread2.start()
            self.run.video_file = "D:/Academic/4th Year/1st Semester/Project SCS- 4123/Endotracheal-Intubation-Automation/CNN_for classification/CNN windows/sam2.mp4"

            time.sleep(1)

            self.thread = Thread(target=self.threaded_function, args=())

            if self.UICount == 1:
                self.thread.start()

    def runvideo(self):
        self.run = label2.prediction()
        self.UICount = 1
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

                    self.display_img = cv2.cvtColor(list_obj[2], cv2.COLOR_RGB2BGR)
                    height, width, channel = self.display_img.shape
                    midy=height/2
                    midx=width/2
                    xcor=list_obj[3]
                    ycor=list_obj[4]



                    #xs=str(xcor)
                    #ys=str(ycor)
                    string="x:  "+xcor+"  y: "+ycor
                    #self.lblTubePosition.setText(string)
                    print(string)
                    #self.lblNavigation.setText(list_obj[1])



                    bytesPerLine = 3 * width
                    qImg = QtGui.QImage(self.display_img.data, width, height, bytesPerLine, QImage.Format_RGB888)
                    pixmap = QPixmap(qImg)
                    self.lblLoadImage.setPixmap(pixmap)
                    time.sleep(0.1)
    def openSanpsFolder(self):
        path = "D:/Academic/4th Year/1st Semester/Project SCS- 4123/Endotracheal-Intubation-Automation/CNN_for classification/CNN windows/Snapshot"
        path = os.path.realpath(path)
        os.startfile(path)

    def endProcess(self):

        if (self.started):
            self.thread_exit = True
            # self.thread2._stop()
            # self.thread._stop()
            #print(self.run.sess)
            # del self.run
            del self.run.sess

        self.autoWindow.hide()
        self.newMode_window = QtWidgets.QMainWindow()
        self.ui = mode.Ui_selectWindow()
        self.ui.setupUi(self.newMode_window)
        self.newMode_window.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    autoWindow = QtWidgets.QMainWindow()
    ui = Ui_autoWindow()
    ui.setupUi(autoWindow)
    autoWindow.show()
    sys.exit(app.exec_())

