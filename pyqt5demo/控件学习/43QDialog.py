import sys
from PyQt5.Qt import *


# 对话框
# 是顶级窗口，主要用于短期任务和与用户的简短通讯
# - 模态级别：
#   - 应用程序级别：默认，关闭了才能访问其他窗口
#   - 窗口级别：阻塞与之关联的窗口
# - 非模态级别：不会阻塞与对话框关联的窗口以及与其他窗口进行交互


# - QFontDialog
# - QColorDialog
# - QFileDialog
# - QInputDialog

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setWindowTitle('QDialog')
        self.setup_ui()

    def setup_ui(self):
        btn = QPushButton(self)
        btn.setText('弹出Dialog')
        btn.clicked.connect(self.btn_clicked)

        pass

    def 基本使用(self):
        d = QDialog(self)
        d.setWindowTitle('弹出框')

        # 应用程序级别模态弹出 ########
        # d.exec_()
        # 等同于
        # d.setModal(True)  # 设置成model
        # d.setWindowModality(Qt.ApplicationModal)
        # d.show()

        # 应用程序级别 ######
        # d.open()
        # 等同于
        # d.setModal(True)  # 设置成model
        # d.setWindowModality(Qt.WindowModal)
        # d.show()

        # 非模态，不会阻塞 ######
        # d.setModal(True)  # 设置成model
        # d.setWindowModality(Qt.WindowModal)  # 窗口级别
        # d.setWindowModality(Qt.ApplicationModal) # 应用程序级别
        # d.show()

        # 尺寸调整控件，可以缩放大小
        print('isSizeGripEnabled:', d.isSizeGripEnabled())
        d.setSizeGripEnabled(True)

        # 添加子控件
        btn1 = QPushButton(d)
        btn1.setText('one')
        btn1.move(20, 20)
        btn1.clicked.connect(lambda: d.accept())

        btn2 = QPushButton(d)
        btn2.setText('two')
        btn2.move(170, 20)
        btn2.clicked.connect(lambda: d.reject())

        btn3 = QPushButton(d)
        btn3.setText('three')
        btn3.move(320, 20)
        btn3.clicked.connect(lambda: d.done(8))

        # d.show()
        # result = d.exec()
        # print('结果:', result)
        # 信号
        d.accepted.connect(lambda: print('点击accept'))
        d.rejected.connect(lambda: print('点击reject'))
        d.finished.connect(lambda val: print('点击finish', val))
        d.show()
        pass

    def btn_clicked(self):
        print('点击按钮')
        self.基本使用()
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
