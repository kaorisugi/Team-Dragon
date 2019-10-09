import sys
import time
from PyQt5.QtWidgets import *
from PyQt5 import*
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class WelcomeScreen(QtWidgets.QMainWindow):
    def __init__(self,parent=None):
        super(StartWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
    def keyPressEvent(self, e):
        if e.key() == 16777220:
            pre_scan_screen.show()
            self.hide()
        elif e.key() == Qt.Key_Escape:
            product_registration.add_main()


class View1(QtWidgets.QWidget):
    def __init__(self,parent=None):
        super(View1, self).__init__(parent)
        self.ui = view1()
        self.ui.setupUi(self)
    def keyPressEvent(self, e):
        # エスケープキーを押すと画面が閉じる
        if e.key() == 16777220:
            self.register_main()
        elif e.key() == Qt.Key_Escape:
            self.close()


class ReadResult(QtWidgets.QMainWindow):
    def __init__(self,parent=None):
        super(ReadResult, self).__init__(parent)
        self.ui = Ui_read_result()
        self.ui.setupUi(self)




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
    
    welcome_screen.showFullScreen()
    if welcome_screen.return == "Enter":
        pre_scan_screen.show()
    elif welcome_screen.return == "Cancell":
        read_result_screen.show()

    sys.exit(app.exec_())