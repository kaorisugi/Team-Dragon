# -*- coding: utf-8 -*-
import sys
import time
from PyQt5.QtWidgets import *
from PyQt5 import*
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from UI.SuperWelcomeScreen import *
from ScreensCommonFuncs import *
import product_registration

class WelcomeScreen(QtWidgets.QMainWindow):
    '''
    開始画面
    商品登録画面を設定する必要がある。
    '''
    def __init__(self,parent=None):
        '''

        :param parent:
        '''
        super().__init__(parent)
        self.ui = Ui_SuperWelcomeScreen()
        self.ui.setupUi(self)
    def showEvent(self, _):
        '''
        ScanScreenを初期化する。
        :param _: 使わない
        :return:
        '''
        pass

    def hideEvent(self, _):
        '''

        :param _: 使わない
        :return:
        '''
        #read_BC()
        pass

    def keyPressEvent(self, e):
        # Escを押すとバーコード読み取り画面が現れる
        if e.key() == Qt.Key_Escape:
            product_registration.add_main()
            #self.close()
        ellif e.key() == Qt.Key_Escape:
