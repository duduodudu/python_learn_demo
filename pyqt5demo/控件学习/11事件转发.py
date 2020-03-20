import sys
from PyQt5.Qt import *


class RedWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resize(300, 300)
        self.move(100, 100)
        # QWidget CSS 样式默认被取消，设置使其显示
        self.setAttribute(Qt.WA_StyledBackground, True)


class GreenWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resize(100, 100)
        self.move(100, 100)
        # QWidget CSS 样式默认被取消，设置使其显示
        self.setAttribute(Qt.WA_StyledBackground, True)

        # 捕获事件:keyboard
        self.grabKeyboard()

    def mouseMoveEvent(self, ev: QMouseEvent) -> None:
        ev.ignore()
        print('mouseMoveEvent:isAccepted', ev.isAccepted())

    def enterEvent(self, ev: QEvent) -> None:
        print("enterEvent")

    def leaveEvent(self, ev: QEvent) -> None:
        print("leaveEvent")

    def keyPressEvent(self, ev: QKeyEvent) -> None:
        print('keyPressEvent', ev.modifiers() == Qt.NoModifier)
        if ev.modifiers() == Qt.ControlModifier and ev.key() == Qt.Key_S:
            print("按下 Ctrl(cmd??) + S")

        # 或运算
        if ev.modifiers() == Qt.ControlModifier | Qt.ShiftModifier and ev.key() == Qt.Key_A:
            print("按下 Ctrl(cmd??) + shift + A")

    # def keyReleaseEvent(self, ev: QKeyEvent) -> None:
    #     print('keyReleaseEvent', ev.text())


class MyWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("事件转发")
        self.resize(500, 500)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    with open('03Qss.qss', 'r') as f:
        app.setStyleSheet(f.read())

    window = MyWindow()

    red = RedWidget(window)
    green = GreenWidget(red)

    window.show()

    sys.exit(app.exec_())
