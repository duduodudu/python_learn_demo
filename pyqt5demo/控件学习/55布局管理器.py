import sys
from PyQt5.Qt import *


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setWindowTitle('布局管理器')
        # self.setup_ui()
        self.详解()

    def setup_ui(self):
        label1 = QLabel('标签1')
        label2 = QLabel('标签2')
        label3 = QLabel('标签3')
        label1.setStyleSheet('background-color:cyan;')
        label2.setStyleSheet('background-color:yellow;')
        label3.setStyleSheet('background-color:red;')

        layout = QHBoxLayout()
        # layout = QVBoxLayout()
        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(label3)
        # 边距 左上右下
        layout.setContentsMargins(10, 20, 30, 40)
        # 元素之间的空间 间距
        layout.setSpacing(40)
        # 对齐方式
        self.setLayoutDirection(Qt.LeftToRight)
        self.setLayoutDirection(Qt.RightToLeft)
        self.setLayoutDirection(Qt.LayoutDirectionAuto)

        # 会自动设置父子关系，包括子控件
        self.setLayout(layout)

    def 详解(self):
        label1 = QLabel('标签1')
        label2 = QLabel('标签2')
        label3 = QLabel('标签3')
        label1.setStyleSheet('background-color:cyan;')
        label2.setStyleSheet('background-color:yellow;')
        label3.setStyleSheet('background-color:red;')

        layout = QBoxLayout(QBoxLayout.TopToBottom)
        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(label3)
        # 间距
        print('spacing', layout.spacing())
        layout.setSpacing(60)
        # 边距
        print('margins:', layout.contentsMargins())
        # 替换子控件 #####
        # label4 = QLabel('标签 4 ')
        # label4.setStyleSheet('background-color:orange;')
        # layout.replaceWidget(label2, label4)
        # label2.hide()  # 有坑 需要隐藏？
        # label2.destroyed.connect(lambda: print('destroyed:', label2.parent()))
        # label2.setParent(None)

        # 添加子布局 布局嵌套 #####
        label5 = QLabel('标签5')
        label6 = QLabel('标签6')
        label7 = QLabel('标签7')
        label5.setStyleSheet('background-color:pink;')
        label6.setStyleSheet('background-color:blue;')
        label7.setStyleSheet('background-color:cyan;')

        h_layout = QBoxLayout(QBoxLayout.LeftToRight)
        h_layout.addWidget(label5)
        h_layout.addWidget(label6)
        h_layout.addWidget(label7)
        layout.addLayout(h_layout)
        # 生效
        layout.setEnabled(False)
        layout.setEnabled(True)

        self.setLayout(layout)
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
