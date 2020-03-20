import sys
from PyQt5.Qt import *


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setWindowTitle('QSS学习')
        self.setup_ui()

    def setup_ui(self):
        label = QLabel(self)
        label.move(100, 100)
        label.resize(300, 300)
        self.qss边框(label)
        pass

    def qss边框(self, label):
        with open('62Qss.qss', 'r') as file:
            content = file.read()
            label.setStyleSheet(content)
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
