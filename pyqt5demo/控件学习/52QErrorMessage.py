import sys
from PyQt5.Qt import *


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setWindowTitle('QErrorMessage')
        self.setup_ui()

    def setup_ui(self):
        # 继承对话框
        # 由文本标签和复选框组成
        # 该复选框允许用户控制将是否再次显示相同的错误信息
        btn = QPushButton('测试按钮', self)
        btn.move(10, 10)
        btn.clicked.connect(self.btn_clicked)

        pass

    def btn_clicked(self):
        # em = QErrorMessage(self)
        # em.setWindowTitle('错误提示')
        # em.showMessage('提示内容')
        # em.showMessage('提示内容')  # 相同的信息标识相同
        # em.show()
        # em.open()
        # em.exec_()
        #

        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()

    QErrorMessage.qtHandler()
    qDebug('debug info !!!!')
    # qWarning('warming!!!')

    sys.exit(app.exec_())
