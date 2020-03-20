import sys
from PyQt5.Qt import *


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setWindowTitle('QMessageBox')
        self.setup_ui()

    def setup_ui(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    mb = QMessageBox(window)
    # 图标 标题 提示信息 复选框 按钮组  详细信息
    # mb.setIcon(QMessageBox.NoIcon)
    # mb.setIcon(QMessageBox.Warning)
    # mb.setIcon(QMessageBox.Question) # 问号
    # mb.setIcon(QMessageBox.Information)  # 灰色 感叹号
    # mb.setIcon(QMessageBox.Critical) # 红色 感叹号
    # 图片

    mb.setIconPixmap(QPixmap('images/demo.png').scaled(50, 50))
    mb.setText('大标题')
    mb.setText('<h3>富文本的大白兔</h3>')
    mb.setInformativeText('Info Text')

    mb.setCheckBox(QCheckBox('下次不再提醒', mb))
    mb.setDetailedText('DetailText')
    mb.show()
    mb.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel | QMessageBox.Discard)

    sys.exit(app.exec_())
