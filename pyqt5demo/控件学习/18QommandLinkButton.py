import sys
from PyQt5.Qt import *

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = QMainWindow()
    window.setWindowTitle('QCommandLinkButton命令连接')

    btn = QCommandLinkButton('标题', '描述', window)
    btn.setText('修改标题')
    btn.setDescription('修改描述')
    btn.setIcon(QIcon('images/ic_mouse.png'))

    window.show()
    sys.exit(app.exec_())
