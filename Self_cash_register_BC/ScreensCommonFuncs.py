# -*- coding: utf-8 -*-

import time
from PyQt5.QtWidgets import *
from PyQt5 import*
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import cv2
from pyzbar.pyzbar import decode

#参考・引用
#https://tech-k-labs.xyz/post/pyqt3/

def next_screen(screen1, screen2):
    '''
    簡易的な画面遷移
    :param screen1:遷移前の画面
    :param screen2: 遷移後の画面
    :return: なし
    '''
    '''
    position = screen1.pos()  # 遷移前のdlgの座標を取得
    size = screen1.size()  # 遷移前のサイズを取得
    screen2.move(position.x(), position.y())  # 同じ位置へ
    screen2.resize(size)  # 同じサイズへ
    # 画面の位置が完全に重なる
    '''
    screen1.hide()  # 遷移前のダイアログを非表示
    screen2.showFullScreen()  # 遷移後のダイアログを表示

def next_screen_scan(screen1, screen2):
    '''
    簡易的な画面遷移
    :param screen1:遷移前の画面
    :param screen2: 遷移後の画面
    :return: なし
    '''
    '''
    position = screen1.pos()  # 遷移前のdlgの座標を取得
    size = screen1.size()  # 遷移前のサイズを取得
    screen2.move(position.x(), position.y())  # 同じ位置へ
    screen2.resize(size)  # 同じサイズへ
    # 画面の位置が完全に重なる
    '''
    screen1.hide()  # 遷移前のダイアログを非表示
    screen2.showFullScreen()  # 遷移後のダイアログを表示
    screen2.register_main()


def read_BC(window=None, camera=0):
    # VideoCaptureのインスタンスを作成する。
    # 引数でカメラを選べれる。
    cap = cv2.VideoCapture(camera)
    #cap.set(cv2.CAP_PROP_FRAME_WIDTH, 50)  # カメラ画像の横幅を250に設定
    #cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 50)  # カメラ画像の縦幅を250に設定

    if cap.isOpened() is False:
        print("can not open camera")
        sys.exit()

    while True:
        # VideoCaptureから1フレーム読み込む
        ret, frame = cap.read()

        # バーコードの読取り
        data = decode(frame)

        #ウィンドウの中でカメラの映像を表示したい
        #img_res = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        #img_res = cv2.resize(img_res, (250, 250))
        #qt_img = create_QPixmap(img_res)
        #window.ui.label_setPix.setPixmap(qt_img)
        #cv2.imshow('frame', frame)
        if len(data) != 0:
            #読み取れたらwhileから抜ける
            break

        # キー入力を1ms待って、キーが'q'だったらBreakする
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    return data

#それぞれの画面に定義したい関数
def register_main(dict_names = None, table_items = None, scan_screen = None, read_result_screen = None):
        '''

        :return:
        '''
        data = read_BC()
        if len(data) == 0:
            print("バーコードが読み取れていない！！！！") # 例外処理について後で考える！
        bc_num = data[0][0].decode('utf-8', 'ignore') if data[0][0].decode('utf-8', 'ignore') in dict_names.keys() else "その他" #"その他"よりも任意の英数字の方が良い？
        table_items.append(bc_num)
        #read_result.draw_read_result_func(table_items)
        read_result_screen.showFullScreen()
        scan_screen.hide()

def check_table_items(table_items, self_screen = None, total_screen = None, welcome_screen = None):
    '''
    table_items（お買い物リスト）をチェックして、
    アイテムがあれば、精算画面へ遷移する。
    アイテムがなければ、開始画面へ遷移する。
    :return:
    '''
    if len(tabel_items) != 0:
        total_screen.showFullScreen()
        self_screen.hide()
    else:
        welcome_screen.showFullScreen()
        self_screen.hide()

def draw_read_result(read_result_screen = None, table_items = None, dict_names = None, dict_prices = None):
    '''
    買い物リストを受け取る。
    最後にリストに加えられたものを表示する。
    リスト内の商品名、個数、金額のテーブルを表示する。
    :param table_items: 買い物リスト
    :return:
    '''

    #テスト用

    ## 行数の設定
    read_result_screen.ui.tableWidget.setRowCount(len(table_items))

    for n, t_item in enumerate(table_items):
        # print(t_item[1])
        read_result_screen.ui.tableWidget.setItem(n, 0, QtWidgets.QTableWidgetItem(str(t_item)))
        read_result_screen.ui.tableWidget.setItem(n, 1, QtWidgets.QTableWidgetItem(str(t_item)))

