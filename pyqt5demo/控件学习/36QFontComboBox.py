import sys
from PyQt5.Qt import *


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setWindowTitle('QFontComboBox学习')
        self.setup_ui()

    def setup_ui(self):
        fcb = QFontComboBox(self)
        fcb.move(100, 100)
        # 信号
        # 字体改变
        lbl = QLabel(self)
        lbl.setText('测试文字')
        fcb.setEditable(False)
        fcb.currentFontChanged.connect(lambda font: lbl.setFont(font))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
