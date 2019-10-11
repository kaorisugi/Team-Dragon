# -*- coding: utf-8 -*-
import sys
import time
from PyQt5.QtWidgets import *
from PyQt5 import*
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from UI.SuperScanScreen import *
from ScreensCommonFuncs import *

class ScanScreen(QtWidgets.QMainWindow):
    '''

    '''
    def __init__(self, parent = None):
        '''

        :param parent:
        '''
        super().__init__(parent)
        self.ui = Ui_SuperScanScreen()
        self.ui.setupUi(self)
        self.table_items =[]
        self.read_result_screen = None

    def showEvent(self, _):
        '''

        :param _: 使わない
        :return:
        '''
        # self.register_main()


    def register_main(self, draw_read_result_func = None):
        '''

        :return:
        '''
        data = read_BC()
        if len(data) == 0:
            print("バーコードが読み取れていない！！！！") # 例外処理について後で考える！
        bc_num = data[0][0].decode('utf-8', 'ignore') if data[0][0].decode('utf-8', 'ignore') in self.dict_names.keys() else "その他" #"その他"よりも任意の英数字の方が良い？
        self.table_items.append(bc_num)
        #read_result.draw_read_result_func(table_items)
        self.hide()
        self.read_result_screen.showFullScreen()

    def check_table_items(self):
        '''
        table_items（お買い物リスト）をチェックして、
        アイテムがあれば、精算画面へ遷移する。
        アイテムがなければ、開始画面へ遷移する。
        :return:
        '''
        if len(self.tabel_items) != 0:
            pass
        else:
            pass

    def pop_item(self):
        '''
        table_items（お買い物リスト）に最後に加えられたものを取り除く
        :return:
        '''
        pass