# -*- coding: utf-8 -*-
import sys
import time
from PyQt5.QtWidgets import *
from PyQt5 import*
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from UI.SuperReadResultScreen import *
from ScreensCommonFuncs import *

class ReadResultScreen(QtWidgets.QMainWindow):
    '''

    '''
    def __init__(self, parent = None, dict_names = None, dict_prices = None):
        '''

        :param parent:
        :param dict_names:
        :param dict_prices:
        '''
        super().__init__(parent)
        self.ui = Ui_SuperReadResultScreen()
        self.ui.setupUi(self)

    def draw_read_result(self, table_items=None):
        '''
        買い物リストを受け取る。
        最後にリストに加えられたものを表示する。
        リスト内の商品名、個数、金額のテーブルを表示する。
        :param table_items: 買い物リスト
        :return:
        '''
        pass
