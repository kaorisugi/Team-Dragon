# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SuperThankYouScreen.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SuperThankYoulScreen(object):
    def setupUi(self, SuperThankYoulScreen):
        SuperThankYoulScreen.setObjectName("SuperThankYoulScreen")
        SuperThankYoulScreen.resize(1440, 810)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SuperThankYoulScreen.sizePolicy().hasHeightForWidth())
        SuperThankYoulScreen.setSizePolicy(sizePolicy)
        SuperThankYoulScreen.setMinimumSize(QtCore.QSize(1440, 810))
        SuperThankYoulScreen.setMaximumSize(QtCore.QSize(1440, 810))
        SuperThankYoulScreen.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setUnderline(False)
        SuperThankYoulScreen.setFont(font)
        SuperThankYoulScreen.setToolTipDuration(-2)
        SuperThankYoulScreen.setStyleSheet("background:url(:/newPrefix/teamdragon_System_NAVI_yoko.009.jpeg)")
        self.centralwidget = QtWidgets.QWidget(SuperThankYoulScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1290, 820, 430, 120))
        font = QtGui.QFont()
        font.setFamily("DIN Condensed")
        font.setPointSize(72)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background:url(:/newPrefix/image/cansel.png)")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(280, 380, 2, 2))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 50, 1440, 411))
        self.label.setMaximumSize(QtCore.QSize(1440, 16777215))
        font = QtGui.QFont()
        font.setFamily("DIN Condensed")
        font.setPointSize(80)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(500, 570, 430, 120))
        font = QtGui.QFont()
        font.setFamily("DIN Condensed")
        font.setPointSize(72)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background:url(:/newPrefix/exit.png)")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayoutWidget.raise_()
        self.pushButton.raise_()
        self.label.raise_()
        self.pushButton_2.raise_()
        SuperThankYoulScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SuperThankYoulScreen)
        QtCore.QMetaObject.connectSlotsByName(SuperThankYoulScreen)

    def retranslateUi(self, SuperThankYoulScreen):
        _translate = QtCore.QCoreApplication.translate
        SuperThankYoulScreen.setWindowTitle(_translate("SuperThankYoulScreen", "MainWindow"))
        self.label.setText(_translate("SuperThankYoulScreen", "<html><head/><body><p align=\"center\"><span style=\" font-size:400pt; color:#fae984; vertical-align:sub;\">THANK YOU!</span></p></body></html>"))

import teamdragon_System_NAVI_rc
