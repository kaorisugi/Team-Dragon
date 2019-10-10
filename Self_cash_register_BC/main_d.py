# -*- coding: utf-8 -*-
import sys
import time
from PyQt5.QtWidgets import *
from PyQt5 import*
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from d_modules import *

from functools import partial

if __name__ == '__main__':
    # 商品の辞書をロードする
    dict_names, dict_prices = csv2dict('names_prices/BC_info.csv')
    
    app = QtWidgets.QApplication(sys.argv)
    welcome_screen = WelcomeScreen()
    pre_scan_screen = PreScanScreen()
    read_result_screen = ReadResultScreen()
    no_items_screen = NoItemsScreen()
    else_item_screen = ElseItemScreen()
    total_screen = TotalScreen()
    thank_you_screen = ThankYouScreen()

    #WelcomeScreenのボタンを関数と接続する
    #partialを使わないとどうなる？
    welcome_screen.pushButton1.clicked.connect(
        partial(ScreensCommonFunc.NextScreen, screen1 = welcome_screen, screen2 = pre_scan_screen))
    #管理者画面がない！

    #pre_scan_screen
    pre_scan_screen.pushButton1.clicked.connect(
        partial(ScreensCommonFunc.NextScreen, screen1 = pre_scan_screen, screen2 = welcome_screen))

    #ReadResultScreen
    #Continue
    read_result_screen.pushButton1.clicked.connect(
        partial(ScreensCommonFunc.NextScreen, screen1 = read_result_screen, screen2 = pre_scan_screen))
    #Finish
    read_result_screen.pushButton2.clicked.connect(
        partial(ScreensCommonFunc.NextScreen, screen1 = read_result_screen, screen2 = total_screen))
    #Cancel
    read_result_screen.pushButton2.clicked.connect(
        pre_scan_screen.pop_item())

    welcome_screen.showFullScreen()

    sys.exit(app.exec_())