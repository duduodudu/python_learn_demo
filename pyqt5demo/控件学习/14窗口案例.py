import sys
from PyQt5.Qt import *

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = QWidget(flags=Qt.FramelessWindowHint)
    window.resize(300, 300)
    # 无边框无标题
    window.setWindowFlags(Qt.FramelessWindowHint)
    # 半透明
    window.setWindowOpacity(0.9)

    # 添加三个子控件-窗口右上角
    btn_y = 10
    btn_width = 80
    btn_height = 40

    close_btn = QPushButton(window)
    close_btn.setText('关闭')
    close_btn.move(window.width() - btn_width, btn_y)
    close_btn.resize(btn_width, btn_height)

    max_btn = QPushButton(window)
    max_btn.setText("最大化")
    max_btn.move(close_btn.x() - btn_width, btn_y)
    max_btn.resize(btn_width, btn_height)

    min_btn = QPushButton(window)
    min_btn.setText("最小值")
    min_btn.move(max_btn.x() - btn_width, btn_y)
    min_btn.resize(btn_width, btn_height)

    def max_normal():
        # 判断状态并进行操作
        if window.isMaximized():
            window.showNormal()
            max_btn.setText('最大化')
        else:
            window.showMaximized()
            max_btn.setText('还原')

    max_btn.pressed.connect(max_normal)

    close_btn.pressed.connect(window.close)
    min_btn.pressed.connect(window.showMinimized)

    window.show()
    sys.exit(app.exec_())
