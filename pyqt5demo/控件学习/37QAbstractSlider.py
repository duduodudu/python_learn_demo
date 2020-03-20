import sys
from PyQt5.Qt import *


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setWindowTitle('QAbstractSlider')
        self.setup_ui()

    def setup_ui(self):
        # 提供范围内的整数值 通过子类来实现
        slider = QSlider(self)
        slider.move(100, 100)
        lbl = QLabel(self)
        lbl.setText('展示标签')
        lbl.move(10, 10)
        lbl.resize(100, 30)

        # 数值范围
        print('范围：', slider.minimum(), '-', slider.maximum())
        slider.setMaximum(88)
        slider.setMinimum(22)
        # 当前值
        print('当前值:', slider.value())
        slider.setValue(55)
        # 步长
        print('pageStep:', slider.pageStep())  # page up down
        print('singleStep', slider.singleStep())  # 键盘上下
        slider.setPageStep(10)
        slider.setSingleStep(2)

        # 是否追踪 value是够跟随着滑块的位置变化而变化 默认为True
        print('滑块追踪:', slider.hasTracking())
        print('滑块追踪:', slider.hasMouseTracking())

        # 滑块位置
        print('sliderPosition:', slider.sliderPosition())

        # 信号
        slider.valueChanged.connect(lambda val: lbl.setText('当前值:' + str(val)))

        # 倒立外观
        print('invertedAppearance:', slider.invertedAppearance())
        slider.setInvertedAppearance(True)

        # 操作翻转
        print('invertedControls', slider.invertedControls())
        slider.setInvertedControls(True)

        # 滑块方向
        print('orientation:', slider.orientation())
        slider.setOrientation(Qt.Horizontal)
        slider.setOrientation(Qt.Vertical)  # 默认

        # 信号
        #
        # slider.valueChanged

        # 滑块
        # slider.sliderPressed
        # slider.sliderMoved
        # slider.sliderReleased
        # 

        # slider.actionTriggered 枚举值 
        # QAbstractSlider.SliderNoAction
        # QAbstractSlider.SliderSingleStepAdd
        # QAbstractSlider.SliderSingleStepSub
        # QAbstractSlider.SliderPageStepAdd
        # QAbstractSlider.SliderPageStepSub
        # QAbstractSlider.SliderToMaximum
        # QAbstractSlider.SliderToMinimum
        # QAbstractSlider.SliderMove

        # slider.rangeChanged
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
