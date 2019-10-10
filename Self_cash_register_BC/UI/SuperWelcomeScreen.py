# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SuperWelcomeScreen.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SuperWelcomeScreen(object):
    def setupUi(self, SuperWelcomeScreen):
        SuperWelcomeScreen.setObjectName("SuperWelcomeScreen")
        SuperWelcomeScreen.resize(1440, 810)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SuperWelcomeScreen.sizePolicy().hasHeightForWidth())
        SuperWelcomeScreen.setSizePolicy(sizePolicy)
        SuperWelcomeScreen.setMinimumSize(QtCore.QSize(1440, 810))
        SuperWelcomeScreen.setMaximumSize(QtCore.QSize(1440, 810))
        SuperWelcomeScreen.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setUnderline(False)
        SuperWelcomeScreen.setFont(font)
        SuperWelcomeScreen.setToolTipDuration(-2)
        SuperWelcomeScreen.setStyleSheet("background:url(:/newPrefix/teamdragon_System_NAVI_yoko.009.jpeg)")
        self.centralwidget = QtWidgets.QWidget(SuperWelcomeScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(950, 610, 430, 120))
        self.pushButton.setMinimumSize(QtCore.QSize(430, 120))
        self.pushButton.setMaximumSize(QtCore.QSize(430, 120))
        self.pushButton.setStyleSheet("background:url(:/newPrefix/start.png)")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, -120, 1440, 411))
        self.label.setMaximumSize(QtCore.QSize(1440, 16777215))
        self.label.setBaseSize(QtCore.QSize(300, 316))
        font = QtGui.QFont()
        font.setFamily("DIN Condensed")
        font.setPointSize(85)
        self.label.setFont(font)
        self.label.setStyleSheet("background:rgba(255, 255, 255, 0)")
        self.label.setObjectName("label")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(280, 380, 2, 2))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(590, 520, 241, 251))
        self.widget_2.setStyleSheet("background:url(:/newPrefix/suraimu.png)")
        self.widget_2.setObjectName("widget_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 310, 1440, 191))
        self.label_3.setMaximumSize(QtCore.QSize(1440, 16777215))
        font = QtGui.QFont()
        font.setFamily("DIN Condensed")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        SuperWelcomeScreen.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SuperWelcomeScreen)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1440, 22))
        self.menubar.setObjectName("menubar")
        SuperWelcomeScreen.setMenuBar(self.menubar)

        self.retranslateUi(SuperWelcomeScreen)
        QtCore.QMetaObject.connectSlotsByName(SuperWelcomeScreen)

    def retranslateUi(self, SuperWelcomeScreen):
        _translate = QtCore.QCoreApplication.translate
        SuperWelcomeScreen.setWindowTitle(_translate("SuperWelcomeScreen", "MainWindow"))
        self.label.setText(_translate("SuperWelcomeScreen", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'DIN Condensed\'; font-size:85pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:450pt; color:#fae984; vertical-align:sub;\">WELCOME!</span></p></body></html>"))
        self.label_3.setText(_translate("SuperWelcomeScreen", "<html><head/><body><p align=\"center\"><span style=\" font-size:190pt; font-weight:600; color:#245928;\">DQ Register</span></p></body></html>"))

import teamdragon_System_NAVI_rc
