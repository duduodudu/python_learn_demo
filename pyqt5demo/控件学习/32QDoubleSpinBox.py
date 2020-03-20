import sys
from PyQt5.Qt import *


class MyDoubleSpinBox(QDoubleSpinBox):
    def textFromValue(self, v: float) -> str:
        return '自定义格式:' + str(v)

    pass


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setWindowTitle('QDoubleSpinBox')
        self.setup_ui()

    def setup_ui(self):
        dsb = MyDoubleSpinBox(self)
        dsb.resize(300, 25)
        dsb.move(100, 100)

        # 最大最小值 数值范围
        print('min:', dsb.minimum(), 'max', dsb.maximum())
        dsb.setMinimum(1.11)
        dsb.setMaximum(88.88)

        # 步长
        print('singleStep:', dsb.singleStep())

        # 循环
        dsb.setWrapping(True)
        # 前缀 后缀
        dsb.setPrefix('前缀')
        dsb.setSuffix('后缀')
        dsb.setSpecialValueText('正常')
        # 小数位数
        print('小数位数:', dsb.decimals())
        dsb.setDecimals(3)
        # 设置数值
        print('value:', dsb.value())
        print('cleanText:', dsb.cleanText())
        print('text:', dsb.text())
        dsb.setValue(0.05)
        #

        # 信号 valueChanged
        dsb.valueChanged.connect(lambda val: print(type(val), val))
        dsb.valueChanged[float].connect(lambda val: print(type(val), val))
        dsb.valueChanged[str].connect(lambda val: print(type(val), val))
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
