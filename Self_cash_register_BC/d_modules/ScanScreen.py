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
    repeatTime = 100 # ms
    search_time = 10 # s
    '''

    '''
    def __init__(self, parent = None):
        '''

        :param parent:
        '''
        super().__init__(parent)
        self.ui = Ui_SuperScanScreen()
        self.ui.setupUi(self)
        self.table_items, self.dict_names, self.dict_prices = [], [], []
        self.read_result_screen = None

    def showEvent(self, _):
        '''
        :param _: 使わない
        :return:
        '''
        self.capture_display()

    def capture_display(self):
        self.CAMERA_MODE = 0
        self.v_width, self.v_height= 350, 280

        #camera setup
        self.capture = cv2.VideoCapture(self.CAMERA_MODE)

        if self.capture.isOpened() is False:
            raise Exception("IO Error")

        size = (self.v_width, self.v_height)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH ,self.v_width)
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT,self.v_height)

        self.start_time = time.time()
        self._set()
        #update timer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self._set)
        self.timer.start(self.repeatTime)

    def _set(self):
        #camera capture
        ret, cv_img = self.capture.read()
        # バーコードの読取り
        data = decode(cv_img)
        self._check_BC(data)
        if ret == False:
            return
        cv_img = cv2.cvtColor(cv_img,cv2.COLOR_BGR2RGB)
        height, width, dim = cv_img.shape
        bytesPerLine = dim * width
        self.image = QImage(cv_img.data, width, height, bytesPerLine, QImage.Format_RGB888)
        self.ui.label_2.setPixmap(QPixmap.fromImage(self.image))
        self._check_time()
    
    def _check_BC(self, data):
        if len(data) != 0:
            self.capture.release()
            self.timer.stop()
            #読み取れたらwhileから抜ける
            bc_num = data[0][0].decode('utf-8', 'ignore') if data[0][0].decode('utf-8', 'ignore') in self.dict_names.keys() else "somethingelse"
            if bc_num != "somethingelse":
                self.table_items.append(bc_num)
                self.hide()
                self.read_result_screen.showFullScreen()
            else:
                self.hide()
                self.else_item_screen.showFullScreen()

    def _check_time(self):
        current_time = time.time()
        if current_time - self.start_time > self.search_time:
            self.capture.release()
            self.timer.stop()
            self.hide()
            self.no_items_screen.showFullScreen()

    def cancel_scanning(self, welcome_screen, read_result_screen):
        self.capture.release()
        self.timer.stop()
        if self.table_items == []:
            self.hide()
            welcome_screen.showFullScreen()
        else:
            self.hide()
            read_result_screen.showFullScreen()