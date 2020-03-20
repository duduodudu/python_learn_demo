import sys
from PyQt5.Qt import *


class MyWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resize(200, 200)
        self.mouse_move_flag = False
        self.setup_ui()

    def setup_ui(self):
        pass

    def mousePressEvent(self, ev: QMouseEvent) -> None:
        print('鼠标按下:')

        # 鼠标左键
        if ev.button() == Qt.LeftButton:
            self.mouse_move_flag = True

            self.mouse_x = ev.globalX()
            self.mouse_y = ev.globalY()

            self.origin_x = self.x()
            self.origin_y = self.y()

        subwidget = self.childAt(ev.x(),ev.y())
        if subwidget is not None:
            subwidget.setStyleSheet('background-color:red;')

    def mouseMoveEvent(self, ev: QMouseEvent) -> None:
        print('鼠标移动:', ev.x(), ev.y())
        # 确定向量（起点到终点）
        # 确定移动的距离
        # 原始起点+向量

        if self.mouse_move_flag:
            move_x = ev.globalX() - self.mouse_x
            move_y = ev.globalY() - self.mouse_y

            dest_x = self.origin_x + move_x
            dest_y = self.origin_y + move_y

            self.move(dest_x, dest_y)

    def mouseReleaseEvent(self, ev: QMouseEvent) -> None:
        print('鼠标释放:')
        self.mouse_move_flag = False


if __name__ == '__main__':
    app = QApplication(sys.argv)

    with open('03Qss.qss', 'r') as f:
        app.setStyleSheet(f.read())

    window = MyWindow()
    window.setWindowTitle('鼠标移动案例')
    window.show()
    window.setMouseTracking(True)

    lbl = QLabel(window)
    lbl.setText('测试Qss')
    lbl.setStyleSheet('background:green;')
    lbl.show()

    # 父子关系
    print('childAt:',window.childAt(5,5))
    print('childrenRect:',window.childrenRect())
    print('parentWidget:',lbl.parentWidget())

    # 父子关系案例
    for i in range(1,11):
        label = QLabel(window)
        label.setText(str(i))
        label.show()
        label.move(30*i,40*i)

    # 层级关系 z
    lbl2 = QLabel(window)
    lbl2.setText('测试Qss')
    lbl2.setStyleSheet("background:red;")
    lbl2.show()
    lbl2.move(10,20)

    # 默认：后添加的在上面
    # 升到最高
    # lbl.raise_()

    # 降到最低
    # lbl2.lower()

    # a放在b的下面
    lbl2.stackUnder(lbl)



    sys.exit(app.exec_())
