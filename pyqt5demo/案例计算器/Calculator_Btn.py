from PyQt5.Qt import *


class CalculatorBtn(QPushButton):
    key_pressed = pyqtSignal(str, str)

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent=parent, *args, **kwargs)

        self.mySetStyle()
        # 设置互斥性 但是无效 因为被覆盖了
        # self.setAutoExclusive(True)

    def mySetStyle(self):
        """
        设置样式
        :return:
        """
        import os
        import sys
        filename = os.path.join(os.path.dirname(sys.executable), 'Calculator_Btn.qss')
        print(filename)
        with open(filename, 'r') as f:
            # with open('Calculator_Btn.qss', 'r') as f:
            qss = f.read()
            qss += """
                    QPushButton[bg] {
                        border-radius:  %dpx;
                    }
                    """ % (min(self.width(), self.height()) / 2)
            self.setStyleSheet(qss)

    def resizeEvent(self, *args, **kwargs):
        super().resizeEvent(*args, **kwargs)
        self.mySetStyle()

    def mousePressEvent(self, *args, **kwargs):
        super().mousePressEvent(*args, **kwargs)
        self.key_pressed.emit(self.text(), self.property('role'))
