import sys
from PyQt5.Qt import *


class MyWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resize(500, 500)
        self.setWindowTitle('动画')
        self.setup_ui()

    def setup_ui(self):
        self.简单动画()
        # QMetaObject.connectSlotsByName(self)
        pass

    def 简单动画(self):
        btn = QPushButton('测试按钮', self)
        btn.resize(100, 100)
        btn.setStyleSheet('background-color:cyan;')
        btn.setObjectName('btn')

        # 动画对象
        animation = QPropertyAnimation(self)
        animation.setTargetObject(btn)
        animation.setPropertyName(b'pos')

        # 始末状态
        animation.setStartValue(QPoint(0, 0))
        animation.setEndValue(QPoint(400, 400))
        # 动画时长
        animation.setDuration(3000)
        # 重复
        animation.setLoopCount(3)
        # 开始动画
        animation.start()

    @pyqtSlot()
    def on_btn_clicked(self):
        print('按钮点击了')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    QMetaObject.connectSlotsByName(window)

    window.show()
    sys.exit(app.exec_())
