import sys
from PyQt5.Qt import *


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setWindowTitle('QProgressBar')
        self.setup_ui()

    def setup_ui(self):
        pb = QProgressBar(self)
        # 设置范围 当前值
        print('默认范围:', pb.minimum(), pb.maximum())
        pb.setMinimum(0)
        pb.setMaximum(100)
        pb.setRange(0, 120)
        pb.setValue(50)
        # 重置当前值
        pb.reset()
        # 设置文本  %p百分比 %v当前值 %总值
        print(pb.format())
        pb.setFormat('%p  %v  %m')
        pb.resize(300, 300)
        # 文本是否可见
        print(pb.isTextVisible())
        pb.setTextVisible(True)
        # 文本方式
        pb.setTextDirection(QProgressBar.TopToBottom)
        pb.setTextDirection(QProgressBar.BottomToTop)
        # 方向
        pb.setOrientation(Qt.Vertical)
        # 外观翻转
        pb.setInvertedAppearance(True)
        # 信号
        pb.valueChanged.connect(lambda val: print(type(val), val))
        timer = QTimer(self)

        def change_progress():
            print('定时任务 >>> ')
            if pb.value() >= pb.maximum():
                timer.stop()
            pb.setValue(pb.value() + 1)

            pass

        timer.timeout.connect(change_progress)
        timer.start(100)  # 毫秒
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
