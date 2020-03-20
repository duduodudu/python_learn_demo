import sys
from PyQt5.Qt import *

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = QMainWindow()
    window.setWindowTitle('QToolButton')
    window.resize(500, 500)
    # QToolButton
    # 提供快速访问按钮
    # 通常在工具栏内部使用
    # 工具栏按钮不显示文本标题，显示文本图标
    tb = QToolButton(window)
    tb.setIcon(QIcon('images/demo.png'))
    tb.setText('title')
    # tb.setIconSize(QSize(60, 60))

    # 样式风格,文字以及图标关系
    tb.setToolButtonStyle(Qt.ToolButtonIconOnly)
    tb.setToolButtonStyle(Qt.ToolButtonTextOnly)
    tb.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
    tb.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
    tb.setToolButtonStyle(Qt.ToolButtonFollowStyle)

    # 显示箭头图标
    tb.setArrowType(Qt.LeftArrow)
    print('箭头样式', tb.arrowType())
    # 扁平化
    tb.setAutoRaise(True)
    # 菜单设置 不会显示title
    menu = QMenu(tb)
    menu.setTitle('菜单')
    submenu = QMenu(menu)
    submenu.setTitle('子菜单')
    menu.addMenu(submenu)
    menu.addSeparator()

    action = QAction(QIcon('images/demo.png'), '行为', menu)
    menu.addAction(action)
    tb.setMenu(menu)


    #  需要设置菜单弹出模式 默认长按停一小会才会显示
    # tb.setPopupMode(QToolButton.DelayedPopup)
    # tb.setPopupMode(QToolButton.InstantPopup)

    # 信号
    def do_action(action: QAction):
        # action.data()  获取数据
        print('点击了', action, action.data())


    tb.triggered.connect(do_action)
    window.show()
    sys.exit(app.exec_())
