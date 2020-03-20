import sys
from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_ui()

    def set_ui(self):
        self.resize(300, 300)
        # 无边框无标题
        self.setWindowFlags(Qt.FramelessWindowHint)
        # 半透明
        self.setWindowOpacity(0.9)

        # 添加三个子控件-窗口右上角
        self.btn_y = 10
        self.btn_width = 80
        self.btn_height = 40

        # 关闭按钮
        close_btn = QPushButton(self)
        self.close_btn = close_btn
        close_btn.setText('关闭')
        close_btn.move(self.width() - self.btn_width, self.btn_y)
        close_btn.resize(self.btn_width, self.btn_height)

        # 最大化
        self.max_btn = QPushButton(self)
        self.max_btn.setText("最大化")
        self.max_btn.move(self.close_btn.x() - self.btn_width, self.btn_y)
        self.max_btn.resize(self.btn_width, self.btn_height)

        # 最小化
        self.min_btn = QPushButton(self)
        self.min_btn.setText("最小值")
        self.min_btn.move(self.max_btn.x() - self.btn_width, self.btn_y)
        self.min_btn.resize(self.btn_width, self.btn_height)

        # 事件处理
        def max_normal():
            # 判断状态并进行操作
            if self.isMaximized():
                self.showNormal()
                self.max_btn.setText('最大化')
            else:
                self.showMaximized()
                self.max_btn.setText('还原')

        self.max_btn.pressed.connect(max_normal)

        self.close_btn.pressed.connect(self.close)
        self.min_btn.pressed.connect(self.showMinimized)

    def resizeEvent(self, evt: QResizeEvent) -> None:
        print('resizeEvent:', evt.oldSize(), '->', evt.size())
        self.close_btn.move(self.width() - self.btn_width, self.btn_y)
        self.max_btn.move(self.close_btn.x() - self.btn_width, self.btn_y)
        self.min_btn.move(self.max_btn.x() - self.btn_width, self.btn_y)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
