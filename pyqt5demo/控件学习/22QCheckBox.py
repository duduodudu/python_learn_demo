import sys
from PyQt5.Qt import *

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = QMainWindow()
    window.setWindowTitle('QCheckBox')
    window.resize(500, 500)

    # QCheckBox
    # __bases__ 基类
    print(QCheckBox.__bases__)
    cb = QCheckBox('&Python', window)
    cb.setIcon(QIcon('images/demo.png'))
    cb.setIconSize(QSize(16, 16))
    # 三态:选中，不选中，实心
    cb.setTristate(True)
    cb.setCheckState(Qt.Checked)
    cb.setCheckState(Qt.Unchecked)
    cb.setCheckState(Qt.PartiallyChecked)
    # 信号 [int] 0,1,2
    cb.stateChanged.connect(lambda val: print('三态信号', val))
    cb.toggled.connect(lambda isChecked: print('toggled:', isChecked))

    window.show()
    sys.exit(app.exec_())
