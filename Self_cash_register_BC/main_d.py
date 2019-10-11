# -*- coding: utf-8 -*-
import sys
import time
from PyQt5.QtWidgets import *
from PyQt5 import*
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from d_modules.WelcomeScreen import *
from d_modules.ScanScreen import *
from d_modules.ReadResultScreen import *
from d_modules.NoItemsScreen import *
from d_modules.ElseItemScreen import *
from d_modules.TotalScreen import *
from d_modules.CancelScreen import *
from d_modules.ThankYouScreen import *
from ScreensCommonFuncs import *
from BC_video_copy import csv2dict

from functools import partial

import sys



if __name__ == '__main__':
    # 商品の辞書をロードする
    dict_names, dict_prices = csv2dict('names_prices/BC_info.csv')

    print()

    app = QtWidgets.QApplication(sys.argv)
    welcome_screen = WelcomeScreen()
    scan_screen = ScanScreen()
    read_result_screen = ReadResultScreen()
    no_items_screen = NoItemsScreen()
    else_item_screen = ElseItemScreen()
    total_screen = TotalScreen()
    cancel_screen = CancelScreen()
    thank_you_screen = ThankYouScreen()

    #グローバル変数で買い物リストを定義する
    #直接参照しているのではなく、引数として渡せば結合度に問題ないのか？
    table_items = []

    #WelcomeScreenが表示された時にScanScreenを初期化するようにする
    #これでできるのか？
    '''
    welcome_screen.showEvent = scan_screen.__init__
    '''

    #引数を固定して関数を定義する
    #必要ないかも知れない。
    partial_read_result_screen = partial(register_main, dict_names = dict_names
                                         , table_items = table_items, scan_screen = scan_screen, read_result_screen = read_result_screen)



    #WelcomeScreenのボタンを関数と接続する
    #partialを使わないとどうなる？
    welcome_screen.ui.pushButton.clicked.connect(
        partial(next_screen, screen1 = welcome_screen, screen2 = scan_screen))
    #管理者画面がない！

    #scan_screen
    scan_screen.ui.pushButton.clicked.connect(
        partial(next_screen, screen1 = scan_screen, screen2 = welcome_screen))
    #cancelボタン必要かも
    #Finishボタン必要かも

    #ReadResultScreen
    #Continue
    read_result_screen.ui.pushButton.clicked.connect(
        partial(next_screen, screen1 = read_result_screen, screen2 = scan_screen))
    #Finish
    read_result_screen.ui.pushButton_2.clicked.connect(
        partial(next_screen, screen1 = read_result_screen, screen2 = total_screen))
    #Cancel
    read_result_screen.ui.pushButton_3.clicked.connect(
        partial(table_items.pop, -1))

    #NoItemsScreen
    #Exit(?)
    no_items_screen.ui.pushButton_EXIT.clicked.connect(
        partial(next_screen, screen1 = no_items_screen, screen2 = scan_screen))

    #ElseItemScreen
    #Exit(?)
    else_item_screen.ui.pushButton_EXIT.clicked.connect(
        partial(next_screen, screen1 = else_item_screen, screen2 = scan_screen))

    #TotalScreen
    #PayMoney
    total_screen.ui.pushButton.clicked.connect(
        partial(next_screen, screen1 = total_screen, screen2 = scan_screen))
    #Cancel
    total_screen.ui.pushButton_2.clicked.connect(
        partial(next_screen, screen1 = total_screen, screen2 = total_screen))

    #CancelScreen
    #No
    cancel_screen.ui.pushButton.clicked.connect(
        partial(next_screen, screen1 = cancel_screen, screen2 = total_screen))
    #Yes
    cancel_screen.ui.pushButton_2.clicked.connect(
        partial(next_screen, screen1 = cancel_screen, screen2 = welcome_screen))


    #ThankYouScreen
    #Exit(?)
    thank_you_screen.ui.pushButton.clicked.connect(
        partial(next_screen, screen1 = thank_you_screen, screen2 = welcome_screen))


    welcome_screen.showFullScreen()

    sys.exit(app.exec_())