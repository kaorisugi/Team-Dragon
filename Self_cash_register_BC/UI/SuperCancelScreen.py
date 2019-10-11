# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SuperCancelScreen.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SuperCancelScreen(object):
    def setupUi(self, SuperCancelScreen):
        SuperCancelScreen.setObjectName("SuperCancelScreen")
        SuperCancelScreen.resize(1440, 810)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SuperCancelScreen.sizePolicy().hasHeightForWidth())
        SuperCancelScreen.setSizePolicy(sizePolicy)
        SuperCancelScreen.setMinimumSize(QtCore.QSize(1440, 810))
        SuperCancelScreen.setMaximumSize(QtCore.QSize(1440, 810))
        SuperCancelScreen.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setUnderline(False)
        SuperCancelScreen.setFont(font)
        SuperCancelScreen.setToolTipDuration(-2)
        SuperCancelScreen.setStyleSheet("background:url(:/newPrefix/teamdragon_System_NAVI_yoko.009.jpeg)")
        self.centralwidget = QtWidgets.QWidget(SuperCancelScreen)
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
        self.label.setGeometry(QtCore.QRect(0, 130, 1440, 281))
        self.label.setMaximumSize(QtCore.QSize(1440, 16777215))
        font = QtGui.QFont()
        font.setFamily("DIN Condensed")
        font.setPointSize(80)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(780, 570, 430, 120))
        font = QtGui.QFont()
        font.setFamily("DIN Condensed")
        font.setPointSize(72)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background:url(:/newPrefix/no.png)")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(220, 570, 430, 120))
        font = QtGui.QFont()
        font.setFamily("DIN Condensed")
        font.setPointSize(72)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background:url(:/newPrefix/yes.png)")
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayoutWidget.raise_()
        self.pushButton.raise_()
        self.label.raise_()
        self.pushButton_2.raise_()
        self.pushButton_4.raise_()
        SuperCancelScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SuperCancelScreen)
        QtCore.QMetaObject.connectSlotsByName(SuperCancelScreen)

    def retranslateUi(self, SuperCancelScreen):
        _translate = QtCore.QCoreApplication.translate
        SuperCancelScreen.setWindowTitle(_translate("SuperCancelScreen", "MainWindow"))
        self.label.setText(_translate("SuperCancelScreen", "<html><head/><body><p align=\"center\"><span style=\" font-size:330pt; color:#fae984; vertical-align:sub;\">CANCEL?</span></p></body></html>"))

import teamdragon_System_NAVI_rc
