import sys
from PyQt5.Qt import *


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setWindowTitle('QSlider')
        self.setup_ui()

    def setup_ui(self):
        slider = QSlider(self)
        slider.move(100, 100)
        slider.resize(20, 100)
        # 继承QAbstractSlider
        # 刻度控制
        slider.setTickPosition(QSlider.NoTicks)
        slider.setTickPosition(QSlider.TicksBothSides)
        # slider.setTickPosition(QSlider.TicksAbove)
        # slider.setTickPosition(QSlider.TicksBelow)
        # slider.setTickPosition(QSlider.TicksLeft)
        # slider.setTickPosition(QSlider.TicksRight)
        # 刻度间隔
        print('刻度间隔:', slider.tickInterval())
        # slider.setTickInterval(5)

        slider.valueChanged.connect(lambda val: print('value:', val))

        pass

    pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
