# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SuperElseItemScreen.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SuperElseItemScreen(object):
    def setupUi(self, SuperElseItemScreen):
        SuperElseItemScreen.setObjectName("SuperElseItemScreen")
        SuperElseItemScreen.resize(1400, 800)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SuperElseItemScreen.sizePolicy().hasHeightForWidth())
        SuperElseItemScreen.setSizePolicy(sizePolicy)
        SuperElseItemScreen.setMinimumSize(QtCore.QSize(1400, 800))
        SuperElseItemScreen.setMaximumSize(QtCore.QSize(1400, 800))
        SuperElseItemScreen.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setUnderline(False)
        SuperElseItemScreen.setFont(font)
        SuperElseItemScreen.setToolTipDuration(-2)
        SuperElseItemScreen.setStyleSheet("background:rgb(43, 148, 209)")
        self.centralwidget = QtWidgets.QWidget(SuperElseItemScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(280, 380, 2, 2))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(750, 840, 430, 120))
        font = QtGui.QFont()
        font.setFamily("DIN Condensed")
        font.setPointSize(72)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background:url(:/newPrefix/image/continue.png)")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_EXIT = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_EXIT.setGeometry(QtCore.QRect(460, 610, 430, 120))
        self.pushButton_EXIT.setStyleSheet("background:url(:/newPrefix/exit.png)")
        self.pushButton_EXIT.setText("")
        self.pushButton_EXIT.setObjectName("pushButton_EXIT")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-40, 0, 1440, 810))
        self.label.setMinimumSize(QtCore.QSize(1440, 810))
        self.label.setMaximumSize(QtCore.QSize(1440, 810))
        self.label.setStyleSheet("background:url(:/newPrefix/teamdragon_System_NAVI_yoko.004.jpeg)")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/newPrefix/teamdragon_System_NAVI_yoko.004.jpeg"))
        self.label.setObjectName("label")
        self.gridLayoutWidget.raise_()
        self.pushButton_2.raise_()
        self.label.raise_()
        self.pushButton_EXIT.raise_()
        SuperElseItemScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SuperElseItemScreen)
        QtCore.QMetaObject.connectSlotsByName(SuperElseItemScreen)

    def retranslateUi(self, SuperElseItemScreen):
        _translate = QtCore.QCoreApplication.translate
        SuperElseItemScreen.setWindowTitle(_translate("SuperElseItemScreen", "MainWindow"))

import teamdragon_System_NAVI_rc
