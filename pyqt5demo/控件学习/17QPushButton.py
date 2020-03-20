import sys
from PyQt5.Qt import *


class MyWindows(QWidget):
    def contextMenuEvent(self, event: QContextMenuEvent) -> None:
        print("contextMenuEvent 执行")
        menu = QMenu(self)
        menu.addAction(QAction(QIcon('images/ic_mouse.png'), "one", menu))
        menu.addAction(QAction(QIcon('images/ic_mouse.png'), "two", menu))
        # 显示右键菜单
        # menu.exec_(QPoint(100,100))
        # menu.exec_(QPoint(event.globalX(),event.globalY()))
        menu.exec_(event.globalPos())

        # 自定义菜单策略
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        # 坐标点转换
        dest_point = self.mapToGlobal(event.pos())
        print(dest_point, event.globalPos())


if __name__ == '__main__':
    #  创建QApplication()
    app = QApplication(sys.argv)
    # 创建Window
    window = MyWindows()
    window.setWindowTitle("QPushButton")
    window.resize(500, 500)

    btn = QPushButton()
    btn.setParent(window)
    btn.setText("Push Button")
    btn.setIcon(QIcon("images/ic_mouse.png"))
    btn.setMaximumSize(200, 100)
    # 扁平化样式
    print('扁平化', btn.isFlat())
    # btn.setFlat(True)
    # 默认事件处理
    print("isDefault", btn.isDefault())
    print("isDefault", btn.autoDefault())
    btn.setAutoDefault(True)
    btn.setDefault(True)

    # 菜单
    menu = QMenu()
    # 行为动作 分割线

    new_action = QAction()
    new_action.setText("新建")
    new_action.setIcon(QIcon('images/ic_mouse.png'))
    new_action.triggered.connect(lambda: print("点击新建文件"))
    menu.addAction(new_action)

    # 利用构造函数
    action = QAction(QIcon('images/ic_mouse.png'), "打开", menu)
    action.triggered.connect(lambda: print("点击打开"))
    menu.addAction(action)

    # 添加分割线
    menu.addSeparator()

    # 子菜单选项
    submenu = QMenu()
    submenu.setTitle("最近打开")
    menu.addMenu(submenu)
    file_action = QAction("python_demo.py")
    submenu.addAction(file_action)

    # 添加菜单
    btn.setMenu(menu)

    # 显示菜单，继承QWidget可以单独的显示
    # btn.showMenu()
    print('获取菜单', btn.menu())

    #

    # 运行
    window.show()
    sys.exit(app.exec_())
