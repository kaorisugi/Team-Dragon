# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SuperReadResultScreen.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SuperReadResultScreen(object):
    def setupUi(self, SuperReadResultScreen):
        SuperReadResultScreen.setObjectName("SuperReadResultScreen")
        SuperReadResultScreen.resize(1440, 810)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SuperReadResultScreen.sizePolicy().hasHeightForWidth())
        SuperReadResultScreen.setSizePolicy(sizePolicy)
        SuperReadResultScreen.setMinimumSize(QtCore.QSize(1440, 810))
        SuperReadResultScreen.setMaximumSize(QtCore.QSize(1440, 810))
        SuperReadResultScreen.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setUnderline(False)
        SuperReadResultScreen.setFont(font)
        SuperReadResultScreen.setToolTipDuration(-2)
        SuperReadResultScreen.setStyleSheet("background:url(:/newPrefix/teamdragon_System_NAVI_yoko.009.jpeg)")
        self.centralwidget = QtWidgets.QWidget(SuperReadResultScreen)
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
        self.label.setGeometry(QtCore.QRect(0, -50, 1440, 281))
        self.label.setMaximumSize(QtCore.QSize(1440, 16777215))
        font = QtGui.QFont()
        font.setFamily("DIN Condensed")
        font.setPointSize(80)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 170, 1440, 261))
        self.label_2.setMaximumSize(QtCore.QSize(1440, 16777215))
        font = QtGui.QFont()
        font.setFamily("DIN Condensed")
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet("background:rgba(255, 255, 255, 0)")
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(970, 520, 430, 120))
        font = QtGui.QFont()
        font.setFamily("DIN Condensed")
        font.setPointSize(72)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background:url(:/newPrefix/finish.png)\n"
"")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(970, 650, 430, 120))
        font = QtGui.QFont()
        font.setFamily("DIN Condensed")
        font.setPointSize(72)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background:url(:/newPrefix/cansel.png)")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(40, 390, 441, 381))
        font = QtGui.QFont()
        font.setFamily("DIN Condensed")
        font.setPointSize(18)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(620, 390, 331, 381))
        font = QtGui.QFont()
        font.setFamily("DIN Condensed")
        self.textEdit_2.setFont(font)
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(480, 390, 141, 381))
        font = QtGui.QFont()
        font.setFamily("DIN Condensed")
        self.textEdit_3.setFont(font)
        self.textEdit_3.setObjectName("textEdit_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(970, 390, 430, 120))
        font = QtGui.QFont()
        font.setFamily("DIN Condensed")
        font.setPointSize(72)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background:url(:/newPrefix/continue.png)")
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayoutWidget.raise_()
        self.pushButton.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.textEdit.raise_()
        self.textEdit_2.raise_()
        self.textEdit_3.raise_()
        self.pushButton_4.raise_()
        SuperReadResultScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SuperReadResultScreen)
        QtCore.QMetaObject.connectSlotsByName(SuperReadResultScreen)

    def retranslateUi(self, SuperReadResultScreen):
        _translate = QtCore.QCoreApplication.translate
        SuperReadResultScreen.setWindowTitle(_translate("SuperReadResultScreen", "MainWindow"))
        self.label.setText(_translate("SuperReadResultScreen", "<html><head/><body><p align=\"center\"><span style=\" font-size:330pt; color:#fae984; vertical-align:sub;\">COCA COLA</span></p></body></html>"))
        self.label_2.setText(_translate("SuperReadResultScreen", "<html><head/><body><p align=\"center\"><span style=\" font-size:200pt; color:#31582d; vertical-align:sub;\">250RWF</span></p></body></html>"))
        self.textEdit.setHtml(_translate("SuperReadResultScreen", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'DIN Condensed\'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.SF NS Text\'; font-size:50pt; font-weight:600; color:#fae984;\">MINERAL WATER</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.SF NS Text\'; font-size:50pt; font-weight:600; color:#fae984;\">COFFEE</span></p></body></html>"))
        self.textEdit_2.setHtml(_translate("SuperReadResultScreen", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'DIN Condensed\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.SF NS Text\'; font-size:50pt; font-weight:600; color:#fae984;\">250RWF</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.SF NS Text\'; font-size:50pt; font-weight:600; color:#fae984;\">300RWF</span></p></body></html>"))
        self.textEdit_3.setHtml(_translate("SuperReadResultScreen", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'DIN Condensed\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.SF NS Text\'; font-size:50pt; font-weight:600; color:#31582d;\">×2</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.SF NS Text\'; font-size:50pt; font-weight:600; color:#31582d;\">×1</span></p></body></html>"))

import teamdragon_System_NAVI_rc
