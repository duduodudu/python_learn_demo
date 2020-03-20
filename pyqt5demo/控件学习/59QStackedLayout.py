import sys
from PyQt5.Qt import *


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setWindowTitle('QStackedLayout')
        self.setup_ui()

    def setup_ui(self):
        sl = QStackedLayout()
        self.setLayout(sl)  # 必须先设置给父布局

        # sl = QStackedLayout(self)

        #
        # 添加控件
        label1 = QLabel('标签1')
        label2 = QLabel('标签2')
        label3 = QLabel('标签3')
        label1.setStyleSheet('background-color:cyan;')
        label2.setStyleSheet('background-color:yellow;')
        label3.setStyleSheet('background-color:red;')

        label4 = QLabel('标签4')
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

        print(sl.addWidget(label1))
        print(sl.addWidget(label2))
        print(sl.addWidget(label3))

        # 插入
        print(sl.insertWidget(1, label4))
        print('currentIndex', sl.currentIndex())
        #
        print(sl.widget(3).text())
        # 设置显示的页面
        # sl.setCurrentIndex(3)
        # sl.setCurrentWidget(label4)
        # 信号
        sl.currentChanged.connect(lambda val: print(val))

        # 切换
        # timer = QTimer(self)
        # timer.timeout.connect(lambda: sl.setCurrentIndex((sl.currentIndex() + 1) % sl.count()))
        # timer.start(1000)

        # 显示模式
        sl.setStackingMode(QStackedLayout.StackOne)  # 默认只显示一个
        label1.resize(100, 100)
        label2.resize(200, 200)
        label3.resize(300, 300)
        sl.setStackingMode(QStackedLayout.StackAll)  # 显示全部

        # 信号
        sl.widgetRemoved.connect(lambda val: print(val))
        sl.removeWidget(label1)

        # 尺寸策略 
        
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
