import sys
from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resize(300, 300)
        self.setWindowTitle('控件交互案例')
        self.setup_ui()

    def setup_ui(self):
        label = QLabel(self)
        label.setText("标签")
        label.move(100, 50)
        label.setHidden(True)

        le = QLineEdit(self)
        le.setText('文本框')
        le.move(100, 100)

        btn = QPushButton(self)
        btn.setText('登录')
        btn.move(100, 150)
        btn.setEnabled(len(le.text()) > 0)

        def text_cao(txt: str):
            print('文本内容发生改变:', txt)
            # if len(txt) > 0:
            #     btn.setEnabled(True)
            # else:
            #     btn.setEnabled(False)
            btn.setEnabled(len(txt) > 0)

        le.textChanged.connect(text_cao)

        def btn_pressed():
            print('按钮被点击了', le.text())
            txt = le.text()
            if txt == 'admin':
                label.setText('登录成功')
            else:
                label.setText('输入错误')

            label.adjustSize()
            label.show()

        btn.pressed.connect(btn_pressed)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Window()

    window.show()

    sys.exit(app.exec_())
