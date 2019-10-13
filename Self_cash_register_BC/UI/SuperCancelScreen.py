# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SuperCancelScreen.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SuperCanselScreen(object):
    def setupUi(self, SuperCanselScreen):
        SuperCanselScreen.setObjectName("SuperCanselScreen")
        SuperCanselScreen.resize(1440, 810)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SuperCanselScreen.sizePolicy().hasHeightForWidth())
        SuperCanselScreen.setSizePolicy(sizePolicy)
        SuperCanselScreen.setMinimumSize(QtCore.QSize(1440, 810))
        SuperCanselScreen.setMaximumSize(QtCore.QSize(16777207, 16777215))
        SuperCanselScreen.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setUnderline(False)
        SuperCanselScreen.setFont(font)
        SuperCanselScreen.setToolTipDuration(-2)
        SuperCanselScreen.setStyleSheet("background:rgb(5, 165, 250)")
        self.centralwidget = QtWidgets.QWidget(SuperCanselScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 1381, 781))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 80, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem)
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
        self.pushButton_yes = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_yes.setMinimumSize(QtCore.QSize(420, 120))
        self.pushButton_yes.setMaximumSize(QtCore.QSize(420, 120))
        font = QtGui.QFont()
        font.setFamily("DIN Condensed")
        font.setPointSize(80)
        self.pushButton_yes.setFont(font)
        self.pushButton_yes.setStyleSheet("background:rgb(250, 233, 132);\n"
"color:rgb(49, 88, 45)")
        self.pushButton_yes.setObjectName("pushButton_yes")
        self.horizontalLayout.addWidget(self.pushButton_yes)
        spacerItem3 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.pushButton_no = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_no.sizePolicy().hasHeightForWidth())
        self.pushButton_no.setSizePolicy(sizePolicy)
        self.pushButton_no.setMinimumSize(QtCore.QSize(420, 120))
        self.pushButton_no.setMaximumSize(QtCore.QSize(420, 120))
        self.pushButton_no.setStyleSheet("background:rgb(250, 233, 132);\n"
"color:rgb(49, 88, 45);\n"
"font: 80pt \"DIN Condensed\";")
        self.pushButton_no.setObjectName("pushButton_no")
        self.horizontalLayout.addWidget(self.pushButton_no)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        spacerItem5 = QtWidgets.QSpacerItem(20, 80, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        SuperCanselScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SuperCanselScreen)
        QtCore.QMetaObject.connectSlotsByName(SuperCanselScreen)

    def retranslateUi(self, SuperCanselScreen):
        _translate = QtCore.QCoreApplication.translate
        SuperCanselScreen.setWindowTitle(_translate("SuperCanselScreen", "CanselScreen"))
        self.label_3.setText(_translate("SuperCanselScreen", "<html><head/><body><p align=\"center\"><span style=\" font-size:200pt; color:#fae984;\">CANCEL?</span></p></body></html>"))
        self.pushButton_yes.setText(_translate("SuperCanselScreen", "YES"))
        self.pushButton_no.setText(_translate("SuperCanselScreen", "NO"))

import teamdragon_System_NAVI_rc
