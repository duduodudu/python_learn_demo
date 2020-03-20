import sys
from PyQt5.Qt import *


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setWindowTitle('QScrollBar')
        self.setup_ui()

    def setup_ui(self):
        # 使用户能够访问比用于显示它的窗口小部件更大的文档部分
        # 一般结合QAbstractScrollArea使用
        # 包括四个单独的控件：滑块，箭头，页面
        # 继承 QAbstractSlider
        bar = QScrollBar(self)
        bar.resize(30, 300)
        bar2 = QScrollBar(Qt.Horizontal, self)
        bar2.resize(300, 30)
        bar2.move(30, 0)
        # 滑块跨度
        bar.setPageStep(50)
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
