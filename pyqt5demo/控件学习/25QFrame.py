import sys
from PyQt5.Qt import *

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = QMainWindow()
    window.setWindowTitle('QFrame')
    window.resize(500, 500)

    frame = QFrame(window)
    frame.resize(100, 100)
    frame.move(10, 10)
    frame.setStyleSheet('background-color:cyan;')
    # 形状 阴影 等各种效果进行组合
    # 形状 枚举值
    print('frameShape:', frame.frameShape())
    frame.setFrameShape(QFrame.NoFrame)
    frame.setFrameShape(QFrame.Box)
    # frame.setFrameShape(QFrame.Panel)
    # frame.setFrameShape(QFrame.HLine)
    # frame.setFrameShape(QFrame.VLine)
    # frame.setFrameShape(QFrame.StyledPanel)
    # frame.setFrameShape(QFrame.WinPanel)

    # 阴影值
    print('frameShadow:', frame.frameShadow())
    # frame.setFrameShadow(QFrame.Plain)
    frame.setFrameShadow(QFrame.Raised)

    # frame.setFrameShadow(QFrame.Sunken)
    # 线条 宽度 
    frame.setLineWidth(5)
    print('lineWidth:', frame.lineWidth())
    frame.setMidLineWidth(10)
    print('midLineWidth', frame.midLineWidth())
    print('frameWidth', frame.frameWidth())

    # 样式 组合
    frame.setFrameStyle(QFrame.Box | QFrame.Raised)
    #
    frame.setFrameRect(QRect(10, 10, 10, 10))

    window.show()
    sys.exit(app.exec_())
