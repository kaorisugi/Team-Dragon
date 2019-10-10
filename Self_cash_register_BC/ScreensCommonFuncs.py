# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5 import*
from PyQt5.QtGui import *
from PyQt5.QtCore import *

#参考・引用
#https://tech-k-labs.xyz/post/pyqt3/

def next_screen(screen1, screen2):
    '''
    簡易的な画面遷移
    :param screen1:遷移前の画面
    :param screen2: 遷移後の画面
    :return: なし
    '''
    position = screen1.pos()  # 遷移前のdlgの座標を取得
    size = screen1.size()  # 遷移前のサイズを取得
    screen2.move(position.x(), position.y())  # 同じ位置へ
    screen2.resize(size)  # 同じサイズへ
    # 画面の位置が完全に重なる
    screen2.show()  # 遷移後のダイアログを表示
    screen1.hide()  # 遷移前のダイアログを非表示


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