import sys
from PyQt5.Qt import *


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setWindowTitle('')
        self.setup_ui()

    def setup_ui(self):
        label1 = QLabel('标签1')
        label2 = QLabel('标签2')
        label3 = QLabel('标签3')
        label4 = QLabel('标签4')
        label1.setStyleSheet('background-color:cyan;')
        label2.setStyleSheet('background-color:yellow;')
        label3.setStyleSheet('background-color:red;')
        label4.setStyleSheet('background-color:orange;')

        layout = QBoxLayout(QBoxLayout.LeftToRight)
        layout.addWidget(label1)
        # layout.addSpacing(100)  # 添加额外的间距
        layout.addWidget(label2)
        layout.addWidget(label3)
        # layout.addWidget(label4)
        layout.insertWidget(1, label4)

        # def test():
        #     layout.setDirection((layout.direction() + 1) % 4)
        #     pass
        #
        # timer = QTimer(self)
        # timer.timeout.connect(test)
        # timer.start(1000)

        # 添加子布局 布局嵌套 #####
        label5 = QLabel('标签5')
        label6 = QLabel('标签6')
        label7 = QLabel('标签7')
        label5.setStyleSheet('background-color:pink;')
        label6.setStyleSheet('background-color:blue;')
        label7.setStyleSheet('background-color:cyan;')

        h_layout = QBoxLayout(QBoxLayout.TopToBottom)
        # stretch 伸展 类似于 flex 按比例分配 剩下的距离
        h_layout.addWidget(label5)
        h_layout.addWidget(label6, 2)
        h_layout.addStretch(5)
        h_layout.addWidget(label7, 3)
        # layout.addLayout(h_layout)
        layout.insertLayout(2, h_layout)
        layout.setStretchFactor(label2, 1)
        # 插入控件
        # 移除控价
        # layout.removeWidget(label1)
        # label1.hide()  # hide() 会推出布局管理
        # label1.setParent(None)
        # label1.show()

        # 添加伸缩因子
        layout.addSpacing(30)
        # 第三个参数为伸缩因子
        # layout.insertSpacing(2, 60)  # 索引不包括 spacing

        self.setLayout(layout)
        pass
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
