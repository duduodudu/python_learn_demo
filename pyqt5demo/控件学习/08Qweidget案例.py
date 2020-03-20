import sys
from PyQt5.Qt import *


def show_grid(window: QWidget, num: int):
    window.resize(600, 600);
    column = 3
    width = window.width() / column
    row = (num - 1) // column + 1
    height = window.height() / row

    # 父控件展示后添加的话，没有展示，子控件可以调用show主动展示
    for i in range(0, num):
        item = QLabel(window)
        item.setStyleSheet("background-color:red;margin:5px;")
        item.move((i % column) * width, (i // column) % row * height)
        item.resize(width, height)
        item.setText(str(i))
        item.setAlignment(Qt.AlignCenter)
        item.show()


# 最大最小尺寸，固定size 自适应
def set_max_min(window: QWidget):
    print('minimumSize:', window.minimumSize())
    print('maximumSize', window.maximumSize())
    window.setMinimumSize(300, 300)
    window.setMaximumSize(600, 600)

    # 限定最大最小之后，resize() 也在范围内
    window.resize(100, 10)


# 内容边距
def set_contents_margins(window: QWidget):
    label = QLabel(window)
    label.resize(300, 300)
    label.setText('社会我顺哥')
    label.setStyleSheet("background-color:cyan;")

    print('contentsRect',label.contentsRect())
    label.setContentsMargins(100,100,0,0)

    label.show()

    print('contentsRect',label.contentsRect())


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = QWidget()
    window.setWindowTitle("QWidget案例")

    window.show()

    # show_grid(window, 50)

    # set_max_min(window)
    set_contents_margins(window)

    sys.exit(app.exec_())
