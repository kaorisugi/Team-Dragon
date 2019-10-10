# -*- coding: utf-8 -*-
import sys
import time
from PyQt5.QtWidgets import *
from PyQt5 import*
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from UI import *

class WelcomeScreen(QtWidgets.QMainWindow):
    '''
    開始画面
    '''
    def __init__(self,parent=None):
        '''

        :param parent:
        '''
        super(StartWindow, self).__init__(parent)
        self.ui = SsuperWelcomeScreen()
        self.ui.setupUi(self)
    def showEvent(self, _):
        '''
        ScanScreenを初期化する。
        :param _: 使わない
        :return:
        '''
        pass