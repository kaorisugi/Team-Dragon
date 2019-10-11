# -*- coding: utf-8 -*-
import sys
import time
from PyQt5.QtWidgets import *
from PyQt5 import*
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from UI.SuperTotalScreen import *
from ScreensCommonFuncs import *

class TotalScreen(QtWidgets.QMainWindow):
    '''

    '''
    def __init__(self, parent = None):
        '''

        :param parent:
        '''
        super().__init__(parent)
        self.ui = Ui_SuperTotalScreen()
        self.ui.setupUi(self)

