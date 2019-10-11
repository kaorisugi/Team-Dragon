# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SuperScanScreen.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SuperScanScreen(object):
    def setupUi(self, SuperScanScreen):
        SuperScanScreen.setObjectName("SuperScanScreen")
        SuperScanScreen.resize(1440, 810)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SuperScanScreen.sizePolicy().hasHeightForWidth())
        SuperScanScreen.setSizePolicy(sizePolicy)
        SuperScanScreen.setMinimumSize(QtCore.QSize(1440, 810))
        SuperScanScreen.setMaximumSize(QtCore.QSize(1440, 810))
        SuperScanScreen.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setUnderline(False)
        SuperScanScreen.setFont(font)
        SuperScanScreen.setToolTipDuration(-2)
        SuperScanScreen.setStyleSheet("background:url(:/newPrefix/teamdragon_System_NAVI_yoko.009.jpeg)")
        self.centralwidget = QtWidgets.QWidget(SuperScanScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(280, 380, 2, 2))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1240, 870, 430, 120))
        font = QtGui.QFont()
        font.setFamily("DIN Condensed")
        font.setPointSize(72)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background:url(:/newPrefix/image/cansel.png)")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(-40, -20, 1440, 810))
        self.label_3.setMinimumSize(QtCore.QSize(1440, 810))
        self.label_3.setMaximumSize(QtCore.QSize(1440, 810))
        font = QtGui.QFont()
        font.setFamily("DIN Condensed")
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background:url(:/newPrefix/teamdragon_System_NAVI_yoko.002.jpeg)")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/newPrefix/teamdragon_System_NAVI_yoko_002.jpeg"))
        self.label_3.setObjectName("label_3")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(880, 20, 431, 281))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(880, 630, 430, 120))
        self.pushButton_2.setMinimumSize(QtCore.QSize(430, 120))
        self.pushButton_2.setMaximumSize(QtCore.QSize(430, 120))
        self.pushButton_2.setStyleSheet("background:url(:/newPrefix/cansel.png)")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3.raise_()
        self.gridLayoutWidget.raise_()
        self.pushButton.raise_()
        self.verticalLayoutWidget.raise_()
        self.pushButton_2.raise_()
        SuperScanScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SuperScanScreen)
        QtCore.QMetaObject.connectSlotsByName(SuperScanScreen)

    def retranslateUi(self, SuperScanScreen):
        _translate = QtCore.QCoreApplication.translate
        SuperScanScreen.setWindowTitle(_translate("SuperScanScreen", "MainWindow"))

import teamdragon_System_NAVI_rc
