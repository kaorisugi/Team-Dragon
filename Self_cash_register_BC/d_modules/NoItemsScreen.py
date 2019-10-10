# -*- coding: utf-8 -*-
import sys
import time
from PyQt5.QtWidgets import *
from PyQt5 import*
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from UI.SuperNoItemsScreen import *
from ScreensCommonFuncs import *

class NoItemsScreen(QtWidgets.QWidget):
    '''

    '''
    def __init__(self, parent = None):
        '''

        :param parent:
        '''
        super().__init__(parent)
        self.ui = UI_SuperNoItemsScreen()
        self.ui.setupUi(self)