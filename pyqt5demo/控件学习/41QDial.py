import sys
from PyQt5.Qt import *


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setWindowTitle('QDial')
        self.setup_ui()

    def setup_ui(self):
        # 圆形 进度条
        d = QDial(self)
        # 刻度
        d.setNotchesVisible(True)
        # 包裹 没有缺口
        d.setWrapping(True)
        # 刻度密度
        d.setNotchTarget(20)
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
