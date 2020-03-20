import sys
from PyQt5.Qt import *


class MySpinBox(QSpinBox):
    def textFromValue(self, v: int) -> str:
        print(v)
        return '自定义格式' + str(v)


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setWindowTitle('QSpinBox')
        self.setup_ui()

    def setup_ui(self):
        sb = QSpinBox(self)
        sb.resize(100, 25)
        sb.move(100, 100)
        self.sb = sb

        # 默认限定 0 - 99 ，无法输入字母
        # 设置数值范围
        sb.setMaximum(999)  # 最大值
        sb.setMinimum(0)  # 最小值
        sb.setRange(18, 180)  # 范围
        print('范围', sb.minimum(), '-', sb.maximum())

        # 数值循环 #########
        print('数值循环', sb.wrapping())
        sb.setWrapping(True)

        # 设置步长
        print('步长：', sb.singleStep())
        sb.setSingleStep(2)
        # 设置前缀 和 后缀
        sb.setPrefix('前缀')
        print(sb.prefix())
        sb.setSuffix('后缀')
        print(sb.suffix())

        # 显示基数（进制）
        # print('进制数', self.sb.displayIntegerBase())
        # self.sb.setDisplayIntegerBase(2)  # 二进制
        # self.sb.setDisplayIntegerBase(8)  # 八进制

        # 获取值 设置值
        print(sb.value())  # 不包括前后缀
        print(sb.text())
        print(sb.lineEdit().text())
        sb.setValue(20)

        btn = QPushButton(self)
        btn.setText('测试按钮')
        btn.clicked.connect(lambda: self.btn_clicked())

        sb1 = MySpinBox(self)
        sb1.resize(100, 25)
        sb1.move(100, 200)
        # 信号
        sb.valueChanged.connect(lambda val: print('默认信号', type(val), val))
        sb.valueChanged[int].connect(lambda val: print('int', val))
        sb.valueChanged[str].connect(lambda val: print('str', val))
        pass

    def btn_clicked(self):
        print('点击按钮')
        self.月份()

    def 自定义展示格式(self):
        pass

    def 月份(self):
        self.sb.setRange(1, 12)
        self.sb.setSuffix('月')
        self.sb.setPrefix('')
        self.sb.setSpecialValueText('正月')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
