# -*- coding: utf-8 -*-
import sys
import time
from PyQt5.QtWidgets import *
from PyQt5 import*
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from UI.SuperThankYouScreen import *
from ScreensCommonFuncs import *

class TotalScreen(QtWidgets.QWidget):
    '''

    '''
    def __init__(self, parent = None):
        '''

        :param parent:
        '''
        super().__init__(parent)
        self.ui = UI_SuperThankYouScreen()
        self.ui.setupUi(self)

