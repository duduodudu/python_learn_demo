from PyQt5.Qt import *
import sys


# 1.所有可视化控件的积累
# 2.是一个最简单的空白控件
# 3.控件是用户界面上最小的元素，接受事件，绘制在桌面上
# 4.每个控件都是矩形的，他们按照Z轴顺序排序
# 5.控件由其父控件和前面的控件剪切
# 6.没有父控件的控件，称为窗口 ,具有一些特性

def get_ui(window: QWidget):
    print('x:', window.x())
    print('y:', window.y())
    print('pos:', window.pos())

    print('width:', window.width())
    print('height:', window.height())
    print('size:', window.size())

    # 相对于父控件的位置和尺寸的组合
    print('geometry:', window.geometry())
    # 0,0,width,height
    print('rect:', window.rect())
    # 框架
    print('frameSize:', window.frameSize())
    print('frameGeometry:', window.frameGeometry())


def set_ui(widget: QWidget):
    # move(x,y) 包括窗口框架
    widget.move(100, 100)

    # resize(width,height) 不包括窗口框架
    # 存在最小值的限定 用户区域的宽和高
    widget.resize(300, 400)

    # x,y,width,height
    # 在展示之前调用会有不一样的效果
    widget.setGeometry(0, 110, 400, 500)
    # 自适应
    widget.adjustSize()
    # 设置固定大小
    widget.setFixedSize(500, 500)




if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = QWidget()
    window.setWindowTitle("QWidget")

    get_ui(window)

    window.show()

    # 获取geometry: 最好在渲染完成之后使用
    print('-' * 20)

    get_ui(window)

    set_ui(window)

    sys.exit(app.exec_())
