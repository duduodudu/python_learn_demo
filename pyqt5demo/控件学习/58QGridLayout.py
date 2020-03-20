import sys
from PyQt5.Qt import *


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setWindowTitle('QGridLayout')
        self.setup_ui()

    def setup_ui(self):
        gl = QGridLayout()

        self.setLayout(gl)

        # 添加控件
        label1 = QLabel('标签1')
        label2 = QLabel('标签2')
        label3 = QLabel('标签3')
        label1.setStyleSheet('background-color:cyan;')
        label2.setStyleSheet('background-color:yellow;')
        label3.setStyleSheet('background-color:red;')
        # 行 列  跨行 跨列
        gl.addWidget(label1, 0, 0)
        gl.addWidget(label2, 1, 1, 1, 2)
        gl.addWidget(label3, 2, 2)

        label5 = QLabel('标签5')
        label6 = QLabel('标签6')
        label7 = QLabel('标签7')
        label5.setStyleSheet('background-color:pink;')
        label6.setStyleSheet('background-color:blue;')
        label7.setStyleSheet('background-color:cyan;')

        h_layout = QVBoxLayout()
        h_layout.addWidget(label5)
        h_layout.addWidget(label6)
        h_layout.addWidget(label7)
        gl.addLayout(h_layout, 4, 0)
        # 设置最小行高 列宽
        gl.setColumnMinimumWidth(2, 50)
        gl.setRowMinimumHeight(2, 50)
        # 拉伸系数
        gl.setColumnStretch(0, 1)
        gl.setRowStretch(0, 1)
        # 间距 垂直间距 水平间距
        print(gl.spacing())
        print(gl.verticalSpacing())
        print(gl.horizontalSpacing())
        #
        print(gl.rowCount())
        print(gl.columnCount())
        print(gl.cellRect(1, 0))
        #
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
