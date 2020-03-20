from PyQt5.Qt import *
import sys


def set_ui(window):
    btn = QPushButton(window)
    btn.setText('按钮')
    btn.move(100, 100)

    def btnClick():
        print('按钮被点击了')

    def btnPressed():
        print('按钮 Pressed')

    btn.clicked.connect(btnClick)
    btn.pressed.connect(btnPressed)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = QWidget()
    window.setWindowTitle('事件机制')
    set_ui(window)

    window.show()
    sys.exit(app.exec_())
