import sys
from PyQt5.Qt import *

if __name__ == '__main__':
    app = QApplication(sys.argv)

    win = QMainWindow()
    win.setWindowTitle('QRadioButton单选按钮')
    win.resize(300, 300)

    # 单选按钮 继承 QAbstractButton
    # 在一个父控件内，最后都会有一个选中的
    # 快捷键设置 -&单词首字母
    rb_man = QRadioButton('男-&Male', win)
    rb_man.move(30, 100)
    rb_man.setIcon(QIcon('images/demo.png'))
    rb_man.setIconSize(QSize(10, 10))
    rb_man.setShortcut('Alt+M')

    rb_woman = QRadioButton('女', win)
    rb_woman.move(30, 150)
    rb_woman.toggled.connect(lambda isChecked: print('选中女:', isChecked))
    rb_man.toggled.connect(lambda isChecked: print('选中男:', isChecked))
    # 排他性
    # rb_woman.setAutoExclusive(False)

    # 多组互斥问题
    red = QWidget(win)
    red.resize(100, 100)
    red.move(150, 0)
    red.setStyleSheet('background-color:red')

    rb1 = QRadioButton('')

    win.show()
    sys.exit(app.exec_())
