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
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(750, 840, 430, 120))
        font = QtGui.QFont()
        font.setFamily("DIN Condensed")
        font.setPointSize(72)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background:url(:/newPrefix/image/continue.png)")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 1381, 781))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 80, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 180))
        font = QtGui.QFont()
        font.setFamily("DIN Condensed")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 180))
        font = QtGui.QFont()
        font.setFamily("DIN Condensed")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.pushButton_EXIT = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_EXIT.setMinimumSize(QtCore.QSize(420, 120))
        font = QtGui.QFont()
        font.setFamily("DIN Condensed")
        font.setPointSize(80)
        self.pushButton_EXIT.setFont(font)
        self.pushButton_EXIT.setStyleSheet("background:rgb(250, 233, 132);\n"
"color:rgb(49, 88, 45)")
        self.pushButton_EXIT.setObjectName("pushButton_EXIT")
        self.horizontalLayout.addWidget(self.pushButton_EXIT)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        spacerItem4 = QtWidgets.QSpacerItem(20, 80, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        SuperNoItemsScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SuperNoItemsScreen)
        QtCore.QMetaObject.connectSlotsByName(SuperNoItemsScreen)

    def retranslateUi(self, SuperNoItemsScreen):
        _translate = QtCore.QCoreApplication.translate
        SuperNoItemsScreen.setWindowTitle(_translate("SuperNoItemsScreen", "SuperNoItemsScreen"))
        self.label_2.setText(_translate("SuperNoItemsScreen", "<html><head/><body><p align=\"center\"><span style=\" font-size:200pt; color:#fae984;\">BARCODE</span></p></body></html>"))
        self.label_3.setText(_translate("SuperNoItemsScreen", "<html><head/><body><p align=\"center\"><span style=\" font-size:200pt; color:#fae984;\">NOT FOUND</span></p></body></html>"))
        self.pushButton_EXIT.setText(_translate("SuperNoItemsScreen", "EXIT"))

import teamdragon_System_NAVI_rc