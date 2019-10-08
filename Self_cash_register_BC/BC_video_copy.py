import numpy as np
import sys
import cv2
from pyzbar.pyzbar import decode
from PIL import Image

# 商品コードと商品名、金額
def txt2dict(path, dict_type):
    dict0 = {}
    with open(path) as f:
        data = f.read()
    lines = data.strip().split("\n")
    for line in lines:
        try:
            key, value = line.split(",")
            if dict_type == "name":
                dict0[key] = value
            elif dict_type == "price":
                dict0[key] = int(value)
        except:
            pass
    return dict0

def read_BC(camera=0):
    # VideoCaptureのインスタンスを作成する。
    # 引数でカメラを選べれる。
    cap = cv2.VideoCapture(camera)

    if cap.isOpened() is False:
        print("can not open camera")
        sys.exit()

    while True:
        # VideoCaptureから1フレーム読み込む
        ret, frame = cap.read()

        # バーコードの読取り
        data = decode(frame)

        cv2.imshow('frame', frame)
        if len(data) != 0:

            #読み取れたらwhileから抜ける
            break

        # キー入力を1ms待って、キーが'q'だったらBreakする
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    return data

def register_main():

    #金額の初期化
    prices = 0
    while True:

        data = read_BC()
        if len(data)==0:
            break #例外処理について後で考える！

        # コード内容を出力
        print(dict_name[data[0][0].decode('utf-8', 'ignore')],
              ":", dict_prices[data[0][0].decode('utf-8', 'ignore')])
        #print(data[0][0].decode('utf-8', 'ignore'))

        # 料金を加算
        prices += dict_prices[data[0][0].decode('utf-8', 'ignore')]
        print("小計 =", prices)

        while True:
            inp=input("続けるなら'C'キー、終了するなら'Q'キーを押してください。：")
            if inp in ['c','C','q','Q']:break #正しいキーが入力されるまで繰り返す
            print('正しいキーを入力してください')

        # キー入力を無制限に待って、キーが'q'だったらBreakする
        if inp in ['c','C']:
            continue
        elif inp in ['q','Q']:
            break

        # キー入力を1ms待って、キーが'q'だったらBreakする
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    prices = int(np.ceil(prices*1.1))
    print("合計 =", prices)

if __name__ == "__main__":
    dict_name = txt2dict(path='names_prices/BC_names.txt', dict_type="name")
    dict_prices = txt2dict(path='names_prices/BC_prices.txt', dict_type="price")
    register_main()