import sys
from PyQt5.Qt import  *


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = QWidget()
    # 没有父控件

    # 标题
    print('windowTitle:',window.windowTitle())
    window.setWindowTitle("顶层窗口相关")
    print('windowTitle:',window.windowTitle())

    # 图标
    icon = QIcon('images/ic_mouse.png')
    window.setWindowIcon(icon)
    window.setWindowIconText('测试')
    print('windowIcon:',window.windowIcon())
    print('windowIconText:',window.windowIconText())

    # 不透明度
    window.setWindowOpacity(0.9)
    print('windowOpacity:',window.windowOpacity())

    # 窗口状态：None(默认),active 最大化，最小,全屏等
    print('windowState:',window.windowState())
    window.setWindowState(Qt.WindowActive)
    # window.setWindowState(Qt.WindowFullScreen)
    # window.setWindowState(Qt.WindowMinimized)
    window.setWindowState(Qt.WindowMaximized)
    window.setWindowState(Qt.WindowNoState)



    # window.showFullScreen()
    # window.showMaximized()
    # window.showMinimized()
    # window.showNormal()

    print('isFullScreen:',window.isFullScreen())
    print('isMaximized:',window.isMaximized())
    print('isMinimized:',window.isMinimized())

    # 窗口标识
    window.setWindowFlags(Qt.FramelessWindowHint)



    window.show()
    sys.exit(app.exec_())