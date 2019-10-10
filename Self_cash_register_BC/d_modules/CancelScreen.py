# -*- coding: utf-8 -*-
import sys
import time
from PyQt5.QtWidgets import *
from PyQt5 import*
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from UI.SuperCancelScreen import *
from ScreensCommonFuncs import *

class CancelScreen(QtWidgets.QWidget):
    '''

    '''
    def __init__(self, parent = None):
        '''

        :param parent:
        '''
        super().__init__(parent)
        self.ui = UI_SuperCancelScreen()
        self.ui.setupUi(self)