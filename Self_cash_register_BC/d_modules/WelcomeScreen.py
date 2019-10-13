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
from play_sound import SoundPlayer #階層に注意

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
        self.table_items = None

    def showEvent(self, _):
        '''
        :param _: 使わない
        :return:
        '''
        SoundPlayer.play('sound/thema.mp3', stop=True)
        self.table_items.clear()

    def hideEvent(self, _):
        '''

        :param _: 使わない
        :return:
        '''
        SoundPlayer.play('sound/zoma.mp3', stop=True)

    def keyPressEvent(self, e):
        # Escを押すとバーコード読み取り画面が現れる
        if e.key() == Qt.Key_Escape:
#            product_registration.add_main()
            self.close()
#        ellif e.key() == Qt.Key_Escape:
