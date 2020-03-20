import sys
from PyQt5.Qt import *


class MyWidget(QLabel):
    def minimumSizeHint(self) -> QSize:
        return QSize(100, 100)

    pass


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setWindowTitle('')
        self.setup_ui()

    def setup_ui(self):
        label1 = QLabel('标签1')
        label2 = QPushButton('标签2')
        label3 = MyWidget('标签3')
        label1.setStyleSheet('background-color:cyan;')
        label2.setStyleSheet('background-color:yellow;')
        label3.setStyleSheet('background-color:red;')

        layout = QVBoxLayout()
        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(label3)

        # QSizePolicy.Fixed
        # QSizePolicy.Minimum
        # QSizePolicy.Maximum
        # QSizePolicy.Preferred
        # QSizePolicy.Expanding
        # QSizePolicy.MinimumExpanding
        # QSizePolicy.Ignored
        a = QSizePolicy.Ignored
        label3.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.setLayout(layout)
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
