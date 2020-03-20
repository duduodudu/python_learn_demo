import sys
from PyQt5.Qt import *


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setWindowTitle('QProgressDialog')
        self.setup_ui()

    def setup_ui(self):
        pass


import time


def show(window):
    # 创建之后会展示弹出，会有延迟
    pd = QProgressDialog(window)
    print('时长:', pd.minimumDuration())
    # pd.setMinimumDuration(0)
    for i in range(1, 101):
        # time.sleep(100)
        pd.setValue(i)
    # pd.show()
    # 自动关闭
    pd.setAutoClose(False)
    # 自动重置
    pd.setAutoReset(False)
    # 设置文本
    print(pd.wasCanceled())
    # 信号
    pd.canceled.connnect(lambda: print('取消了'))
    
    pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    show(window)
    sys.exit(app.exec_())
