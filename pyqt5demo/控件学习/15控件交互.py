import sys
from PyQt5.Qt import *


class Window(QMainWindow):
    def paintEvent(self, evt: QPaintEvent) -> None:
        print('窗口绘制:paintEvent')
        return super().paintEvent(evt)




if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Window()
    window.resize(300, 300)
    window.setWindowTitle('控件交互')

    # enable 可用状态
    btn = QPushButton(window)
    btn.setText('是否可用')
    btn.pressed.connect(lambda: print('按钮被点击了'))

    print('isEnabled:', btn.isEnabled())
    btn.setEnabled(False)
    print('isEnabled:', btn.isEnabled())

    # window.showMaximized()
    window.show()

    # 显示/隐藏
    lbl = QLabel(window)
    lbl.setText('显示/隐藏')
    lbl.move(100, 0)
    print('isVisible: 1', lbl.isVisible())
    print('isHidden:  1', lbl.isHidden())
    lbl.show()
    print('isVisible: 2', lbl.isVisible())
    print('isHidden:  2', lbl.isHidden())
    lbl.hide()
    print('isVisible: 3', lbl.isVisible())
    print('isHidden:  3', lbl.isHidden())

    lbl.setHidden(True)
    print('isVisible: 4', lbl.isVisible())
    print('isHidden:  4', lbl.isHidden())

    lbl.setHidden(False)
    print('isVisible: 5', lbl.isVisible())
    print('isHidden:  5', lbl.isHidden())
    # 全部重新绘制
    # 先绘制父控件，再绘制子控件
    # 父控件不显示，子控件也不显示

    # isHidden() 隐藏
    # isVisible() 可见
    # isVisibleTo(widget) 随着一个控件隐藏显示变化而变化

    lbl.destroyed.connect(lambda: print("lbl destroyed"))
    # lbl.setHidden(True)
    # lbl.setVisible(False)
    # lbl.hide()
    # lbl.setAttribute(Qt.WA_DeleteOnClose, True)
    # lbl.close()
    # lbl.deleteLater()

    print('isVisibleTo:', lbl.isVisibleTo(window))

    window.setWindowModality(True)
    # 是否被编辑

    window.setWindowTitle('测试[*]')

    print('isWindowModified:', window.isWindowModified())

    w2 = QWidget()
    # w2.show()

    print('isActiveWindow:', window.isActiveWindow())

    # 状态提示
    lbl2 = QLabel(window)
    lbl2.setText('状态提示')
    lbl2.move(100, 50)
    lbl2.show()
    lbl2.setStatusTip('这是label的StatusTip')
    lbl2.setToolTip('这是label的ToolTip')
    # tooltip 停留时长 毫毛
    lbl2.setToolTipDuration(2000)

    # whatsThis
    window.setWindowFlags(Qt.WindowContextHelpButtonHint)
    lbl2.setWhatsThis('设置啥')

    # QMainWindow
    # 懒加载
    window.statusBar()
    window.setStatusTip('这是StatusTip')
    print('statusTip:', window.statusTip())
    window.setToolTip('这是window的ToolTip')

    # 焦点控制
    le1 = QLineEdit(window)
    le1.move(20, 150)

    le = QLineEdit(window)
    le.move(10, 100)

    le2 = QLineEdit(window)
    le2.move(30, 200)

    le2.setFocus(True)
    le2.setFocusPolicy(Qt.TabFocus)
    # le2.setFocusPolicy(Qt.ClickFocus)
    # le2.setFocusPolicy(Qt.StrongFocus)
    # le2.setFocusPolicy(Qt.NoFocus)

    # 父控件角度
    # 获取子控件中当前聚焦的控件
    print("focusWidget:",window.focusWidget())
    # 聚焦下一个子控件
    window.focusNextChild()
    # 聚焦上一个子控件
    window.focusPreviousChild()
    # True 上一个，False 下一个
    window.focusNextPrevChild(True)

    # 静态方法，设置Tab焦点获取的顺序
    QWidget.setTabOrder(le,le2)


    window.show()
    le2.clearFocus()
    sys.exit(app.exec_())

