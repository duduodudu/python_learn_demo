import sys
from PyQt5.Qt import *


def mouse(window: QWidget):
    # 更改鼠标形状
    window.setCursor(Qt.CursorShape.PointingHandCursor)
    # 可以自定义鼠标对象 QCursor

    lbl = QLabel(window)
    lbl.setText("测试")
    lbl.setStyleSheet('background:cyan;')
    lbl.resize(200, 200)

    lbl.setCursor(Qt.ForbiddenCursor)
    lbl.show()

    pixmap = QPixmap('./images/ic_mouse.png')
    pixmap = pixmap.scaled(20, 20)
    cursor = QCursor(pixmap, 0, 0)
    lbl.setCursor(cursor)

    # 重置鼠标对象
    window.unsetCursor()
    lbl.unsetCursor()

    print('cursor:', window.cursor())
    cursor2 = window.cursor()
    print('cursor.pos():', cursor2.pos())
    cursor2.setPos(0, 0)
    print('cursor.pos():', cursor2.pos())


class MyWidget(QLabel):
    def mouseMoveEvent(self, ev: QMouseEvent) -> None:
        print('鼠标移动了:mouseMoveEvent:', ev.localPos())


#     鼠标跟踪
def mouse_track(window: QWidget):
    print('hasMouseTracking:', window.hasMouseTracking())

    lbl1 = MyWidget(window)
    lbl1.setStyleSheet('background:yellow;')
    lbl1.resize(200, 200)
    lbl1.move(210, 0)
    lbl1.show()

    lbl1.setMouseTracking(True)

    lbl2 = MyWidget(window)
    lbl2.setStyleSheet('background:red;')
    lbl2.resize(200, 200)
    lbl2.move(420, 0)
    lbl2.show()


def demo(window: QWidget):
    lbl = QLabel(window)
    lbl.setText("跟随鼠标移动")
    lbl.move(300, 300)
    lbl.show()
    window.demoLbl = lbl;

    window.setMouseTracking(True)


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        print('__init__')

    def mouseMoveEvent(self, ev: QMouseEvent) -> None:
        print('鼠标:', ev.localPos())

        self.demoLbl.move(ev.localPos().x(), ev.localPos().y())


if __name__ == '__main__':
    app = QApplication(sys.argv)

    with open('03Qss.qss', 'r') as f:
        app.setStyleSheet(f.read())

    window = MyWindow()
    window.setWindowTitle("鼠标相关")
    window.show()
    mouse(window)
    mouse_track(window)
    demo(window)

    sys.exit(app.exec_())
