# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SuperNoItemsScreen.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SuperNoItemsScreen(object):
    def setupUi(self, SuperNoItemsScreen):
        SuperNoItemsScreen.setObjectName("SuperNoItemsScreen")
        SuperNoItemsScreen.resize(1400, 800)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SuperNoItemsScreen.sizePolicy().hasHeightForWidth())
        SuperNoItemsScreen.setSizePolicy(sizePolicy)
        SuperNoItemsScreen.setMinimumSize(QtCore.QSize(1400, 800))
        SuperNoItemsScreen.setMaximumSize(QtCore.QSize(1400, 800))
        SuperNoItemsScreen.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setUnderline(False)
        SuperNoItemsScreen.setFont(font)
        SuperNoItemsScreen.setToolTipDuration(-2)
        SuperNoItemsScreen.setStyleSheet("background:rgb(43, 148, 209)")
        self.centralwidget = QtWidgets.QWidget(SuperNoItemsScreen)
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
        self.label.setStyleSheet("background:url(:/newPrefix/UI/teamdragon_System_NAVI_yoko.003.jpeg)")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/newPrefix/teamdragon_System_NAVI_yoko.003.jpeg"))
        self.label.setObjectName("label")
        self.gridLayoutWidget.raise_()
        self.pushButton_2.raise_()
        self.label.raise_()
        self.pushButton_EXIT.raise_()
        SuperNoItemsScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SuperNoItemsScreen)
        QtCore.QMetaObject.connectSlotsByName(SuperNoItemsScreen)

    def retranslateUi(self, SuperNoItemsScreen):
        _translate = QtCore.QCoreApplication.translate
        SuperNoItemsScreen.setWindowTitle(_translate("SuperNoItemsScreen", "MainWindow"))

import teamdragon_System_NAVI_rc
