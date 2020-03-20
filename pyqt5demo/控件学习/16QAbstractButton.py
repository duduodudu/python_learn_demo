import sys
from PyQt5.Qt import *


class MyButton(QAbstractButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def paintEvent(self, e: QPaintEvent) -> None:
        print("抽象方法")


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = QMainWindow()
    window.setWindowTitle('QAbstractButton')

    # TypeError: PyQt5.QtWidgets.QAbstractButton represents a C++ abstract class and cannot be instantiated
    btn = MyButton(window)
    btn.setText("XXX")
    # NotImplementedError: QAbstractButton.paintEvent() is abstract and must be overridden

    window.show()
    sys.exit(app.exec_())

# 按钮组件:
# QPushButton # QCommandLinkButton
# QToolButton
# QRadioButton
# QCheckBox

# QAbstractButton
# 所有按钮的基类，
# 必须子类化：Abstract

# 自动重复
# 排他性
# 图标
# text
# 有效性
