import sys
from PyQt5.Qt import *


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setWindowTitle('QRubberBand')
        self.setup_ui()

    def setup_ui(self):
        # 提供一个矩形或者线来只是选择或者边界
        rb = QRubberBand(QRubberBand.Rectangle, self)
        rb.setGeometry(10, 10, 60, 60)
        print('isVisible:', rb.isVisible())
        rb.setVisible(True)
        pass


class DemoWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setWindowTitle('QRubberBand案例')
        self.setup_ui()

    def setup_ui(self):
        for i in range(0, 30):
            cb = QCheckBox(self)
            cb.setText('{}'.format((i)))
            cb.move(i % 4 * 50, i // 4 * 60)
        self.rb = QRubberBand(QRubberBand.Rectangle, self)

    def mousePressEvent(self, evt: QMouseEvent) -> None:
        # 创建 起点 显示
        self.rb.setGeometry(QRect(evt.pos(), evt.pos()))
        self.rb.show()
        self.origin_pos = evt.pos()
        pass

    def mouseMoveEvent(self, evt: QMouseEvent) -> None:
        # 获取范围
        rect = QRect(self.origin_pos, evt.pos()).normalized()
        self.rb.setGeometry(rect)
        # 遍历子控件
        pass

    def mouseReleaseEvent(self, evt: QMouseEvent) -> None:
        rect = self.rb.geometry()
        for child in self.children():
            if rect.contains(child.geometry()) and child.inherits('QCheckBox'):
                print(child)
                child.toggle()

        self.rb.hide()
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DemoWindow()
    window.show()
    sys.exit(app.exec_())
