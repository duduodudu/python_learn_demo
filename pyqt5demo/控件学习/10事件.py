import sys
from PyQt5.Qt import *


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        print('__init__')
        self.set_ui()

    def set_ui(self):
        pass

    # 控件显示事件
    def showEvent(self, ev: QShowEvent) -> None:
        print('控件被展示:showEvent', ev)

    # 控件关闭事件
    def closeEvent(self, ev: QCloseEvent) -> None:
        print('控件被关闭:closeEvent', ev)

    # 移动
    def moveEvent(self, ev: QMoveEvent) -> None:
        print("控件被移动", ev.oldPos(), '->', ev.pos())

    # 改变尺寸大小
    def resizeEvent(self, ev: QResizeEvent) -> None:
        print('控件尺寸大小改变:', ev.oldSize(), '->', ev.size())

    def enterEvent(self, ev: QEvent) -> None:
        self.setStyleSheet('background-color:cyan;')
        print("鼠标进入")

    def leaveEvent(self, ev: QEvent) -> None:
        print("鼠标离开")
        self.setStyleSheet("background-color:white;")

    # 鼠标相关
    def mousePressEvent(self, ev: QMouseEvent) -> None:
        print('鼠标按下')
        self.setStyleSheet("background-color:yellow;")

    def mouseMoveEvent(self, ev: QMouseEvent) -> None:
        print("鼠标按下后移动了")

    def mouseReleaseEvent(self, ev: QMouseEvent) -> None:
        print("鼠标按下后释放")
        self.setStyleSheet("background-color:green;")

    def mouseDoubleClickEvent(self, ev: QMouseEvent) -> None:
        print("鼠标双击")
        self.setStyleSheet("background-color:#652;")

    # 键盘相关
    def keyPressEvent(self, ev: QKeyEvent) -> None:
        print("键盘按下:", ev.text())

    def keyReleaseEvent(self, ev: QKeyEvent) -> None:
        print("键盘松开:", ev.key())

    def focusInEvent(self, ev: QFocusEvent) -> None:
        print("获得焦点", ev.reason())

    def focusOutEvent(self, ev: QFocusEvent) -> None:
        print("失去焦点:")


# 拖拽事件 dragEnterEvent,dragMoveEvent,dragLeaveEvent,dropEvent
# 绘制事件 paintEvent
# 改变事件 changeEvent
# 右键菜单 contextMenuEvent
# 输入法 inputMethodEvent


if __name__ == '__main__':
    app = QApplication(sys.argv)

    with open('03Qss.qss', 'r') as f:
        app.setStyleSheet(f.read())

    window = MyWindow()
    window.setWindowTitle("事件")
    window.show()

    sys.exit(app.exec_())

# 事件转发机制
#
