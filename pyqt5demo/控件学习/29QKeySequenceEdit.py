import sys
from PyQt5.Qt import *


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setWindowTitle('QKeySequenceEdit')
        self.setup_ui()

    def setup_ui(self):
        # 快捷键
        kse = QKeySequenceEdit(self)
        # ks = QKeySequence('Ctrl+C') #字符串
        # ks = QKeySequence(QKeySequence.Copy) # 枚举值
        ks = QKeySequence(Qt.CTRL + Qt.Key_C, Qt.CTRL + Qt.Key_A)
        kse.setKeySequence(ks)

        btn = QPushButton(self)
        btn.move(100, 100)
        btn.setText('按钮')
        btn.clicked.connect(lambda: print(kse.keySequence().toString()))
        kse.clear()  # 清除
        kse.editingFinished.connect(lambda: print('结束编辑'))
        kse.keySequenceChanged.connect(lambda val: print('键位改变', val.toString()))
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
