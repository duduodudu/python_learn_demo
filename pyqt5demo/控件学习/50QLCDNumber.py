import sys
from PyQt5.Qt import *


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setWindowTitle('QLCDNumber')

        # lcd = QLCDNumber(self)
        lcd = QLCDNumber(30, self)
        lcd.move(100, 100)
        lcd.resize(300, 50)
        # 显示内容
        lcd.display('12345')
        lcd.display('ABCDEDGHIJKLMNOBQRT')
        lcd.display(':')
        lcd.display(99.876)
        #
        print(type(lcd.value()), lcd.value(), lcd.intValue())
        # 位数限制
        lcd.setDigitCount(7)
        # 模式设置
        lcd.setMode(QLCDNumber.Bin)  # 二进制
        lcd.setMode(QLCDNumber.Oct)  # 八进制
        lcd.setMode(QLCDNumber.Dec)  # 十进制
        lcd.setMode(QLCDNumber.Hex)  # 十六进制
        lcd.setHexMode()
        lcd.setBinMode()
        lcd.setDecMode()
        lcd.setOctMode()
        # 信号
        # 溢出信号
        print(lcd.checkOverflow(99))  # 检查溢出
        lcd.overflow.connect(lambda: print('溢出信号'))
        # 样式
        lcd.setSegmentStyle(QLCDNumber.Outline)  # 突出
        lcd.setSegmentStyle(QLCDNumber.Flat)  #
        lcd.setSegmentStyle(QLCDNumber.Filled)  # 填充
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
    pass
