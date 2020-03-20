from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("信号与槽机制")

lbl = QLabel()
lbl.setText("状态改变")
lbl.setParent(window)
lbl2 = QLabel()
lbl2.setText("状态改变")
lbl2.setParent(window)
lbl2.move(200, 0)

btn = QPushButton(window)
btn.setText("点击1")
btn.move(200, 200)

btn2 = QPushButton(window)
btn2.setText("点击2")
btn2.move(300, 200)


# 信号：触犯的
# 槽：操作函数

# 信号具有内置的和自定义的
# 一个信号可以连接多个槽
# 一个信号可以连接另一个信号
# 一个槽可以监听多个信号

# destroyed 销毁
def des(self):
    print(self, "对象被释放了")


def test():
    lbl = QLabel()
    lbl.destroyed.connect(des)
    lbl2 = QLabel(window)
    lbl2.destroyed.connect(des)

    print('lbl1', lbl)
    print('lbl2', lbl2)

    def obj_name_changed(name):
        print("对象名称发生改变", name)

    lbl.objectNameChanged.connect(obj_name_changed)
    lbl.setObjectName('demo')
    # #断开连接
    # lbl.objectNameChanged.disconnect()
    # 临时阻断连接
    lbl.blockSignals(True)
    # 恢复连接
    lbl.blockSignals(False)
    lbl.setObjectName('again')

    # 接收器数量
    print('receivers:', lbl.receivers(lbl.objectNameChanged))


test()


def btnClicked():
    print('按钮被点击了:')


btn.clicked.connect(btnClicked)
btn2.clicked.connect(lambda: print('匿名函数执行'))


def titleChanged(title):
    print("窗口标题发生变化", title)

    # 先取消 再次连接
    # 或者临时中断，再次恢复连接
    window.blockSignals(True)
    window.setWindowTitle('添加前缀-' + title)
    window.blockSignals(False)


window.windowTitleChanged.connect(titleChanged)
window.setWindowTitle('title 1')
window.setWindowTitle('title 2')
window.setWindowTitle('title 3')
window.setWindowTitle('title 4')


# QObject类型判定
def QObject类型判定():
    objs = [QObject(), QWidget(), QPushButton(), QLabel()]
    for obj in objs:
        # 直接判定
        print('类型', obj, obj.isWidgetType())
        # 判定继承关系
        print('inherits:', obj.inherits('QWidget'))


QObject类型判定()

# 延迟删除：解除父子关系
# btn.deleteLater()
del btn

with open('03Qss.qss', 'r') as f:
    app.setStyleSheet(f.read())

window.show()
sys.exit(app.exec_())
