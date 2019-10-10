# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SuperScanScreen.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SuperWelcomeScreen(object):
    def setupUi(self, SuperWelcomeScreen):
        SuperWelcomeScreen.setObjectName("SuperWelcomeScreen")
        SuperWelcomeScreen.resize(1800, 1000)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SuperWelcomeScreen.sizePolicy().hasHeightForWidth())
        SuperWelcomeScreen.setSizePolicy(sizePolicy)
        SuperWelcomeScreen.setMinimumSize(QtCore.QSize(1800, 1000))
        SuperWelcomeScreen.setMaximumSize(QtCore.QSize(1800, 1000))
        SuperWelcomeScreen.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setUnderline(False)
        SuperWelcomeScreen.setFont(font)
        SuperWelcomeScreen.setToolTipDuration(-2)
        SuperWelcomeScreen.setStyleSheet("background:url(:/newPrefix/image/haikei_033.jpeg)")
        self.centralwidget = QtWidgets.QWidget(SuperWelcomeScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1250, 830, 430, 120))
        font = QtGui.QFont()
        font.setFamily("DIN Condensed")
        font.setPointSize(72)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background:url(:/newPrefix/image/start.png)")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(280, 380, 2, 2))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, -20, 1800, 1000))
        self.label_3.setMinimumSize(QtCore.QSize(1800, 1000))
        self.label_3.setMaximumSize(QtCore.QSize(1800, 1000))
        font = QtGui.QFont()
        font.setFamily("DIN Condensed")
        self.label_3.setFont(font)
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/newPrefix/teamdragon_System_NAVI_yoko_002.jpeg"))
        self.label_3.setObjectName("label_3")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(1230, 10, 461, 371))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.camera = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.camera.setContentsMargins(0, 0, 0, 0)
        self.camera.setObjectName("camera")
        self.gridLayoutWidget.raise_()
        self.label_3.raise_()
        self.pushButton.raise_()
        self.verticalLayoutWidget.raise_()
        SuperWelcomeScreen.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SuperWelcomeScreen)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1800, 22))
        self.menubar.setObjectName("menubar")
        SuperWelcomeScreen.setMenuBar(self.menubar)

        self.retranslateUi(SuperWelcomeScreen)
        QtCore.QMetaObject.connectSlotsByName(SuperWelcomeScreen)

    def retranslateUi(self, SuperWelcomeScreen):
        _translate = QtCore.QCoreApplication.translate
        SuperWelcomeScreen.setWindowTitle(_translate("SuperWelcomeScreen", "MainWindow"))

import teamdragon_System_NAVI_003_rc
