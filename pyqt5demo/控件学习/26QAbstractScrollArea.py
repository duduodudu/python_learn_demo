import sys
from PyQt5.Qt import *

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = QMainWindow()
    window.resize(500, 500)
    window.setWindowTitle('QAbstractScrollArea功能测试')
    # QAbstractScrollArea
    # 继承 QFrame 
    # 是滚动区域的低级抽象 

    # 水平，垂直滚动条
    # 滚动策略
    # 角落控件

    te = QTextEdit(window)
    # 滚动条策略 
    te.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    te.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
    te.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
    #

    window.show()
    sys.exit(app.exec_())
