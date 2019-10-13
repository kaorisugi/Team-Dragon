# -*- coding: utf-8 -*-
import sys
import time
from PyQt5.QtWidgets import *
from PyQt5 import*
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from UI.SuperThankYouScreen import *
from ScreensCommonFuncs import *
from play_sound import SoundPlayer #階層に注意

class ThankYouScreen(QtWidgets.QMainWindow):
    '''

    '''
    def __init__(self, parent = None):
        '''

        :param parent:
        '''
        super().__init__(parent)
        self.ui = Ui_SuperThankYouScreen()
        self.ui.setupUi(self)
    
    def showEvent(self, _):
        total = 0
        for item in self.table_items:
            total += self.dict_prices[item]
        if total >= 300:
            SoundPlayer.play('sound/levelup.mp3', stop=True)
        else:
            SoundPlayer.play('sound/fin.mp3', stop=True)
        self.table_items.clear()

