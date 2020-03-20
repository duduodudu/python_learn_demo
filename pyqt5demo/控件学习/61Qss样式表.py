import sys
from PyQt5.Qt import *


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setWindowTitle('样式表')
        self.setup_ui()

    def setup_ui(self):
        box1 = QWidget()
        box2 = QWidget()

        layout = QVBoxLayout()
        self.setLayout(layout)

        layout.addWidget(box1)
        layout.addWidget(box2)
        #  控件本身 子控件 间接子控件
        # box1.setStyleSheet('background-color:orange;')
        # 选择器
        box1.setStyleSheet('QPushButton {background-color:orange;}')
        box2.setStyleSheet('background-color:cyan;')

        label1 = QLabel('标签1', box1)
        label1.move(50, 50)
        btn1 = QPushButton('按钮1', box1)
        btn1.move(150, 50)
        label1.setObjectName('label1')

        label2 = QLabel('标签1', box2)
        label2.move(50, 50)
        btn2 = QPushButton('按钮2', box2)
        btn2.move(150, 50)
        # 局部设置
        # 全局设置 QApplication

        # Qss 选择器 ######
        # 通配符选择器 类型选择器 类选择器 ID选择器 属性选择器 后代选择器 子选择器 子控件选择器
        # 通配符选择器 *

        # 类型选择器 QLabel QPushButton QWidget 及其子类
        # 类选择器 .QLabel 不包含子类

        # id选择器 #name 对应 setObjectName
        label2.setObjectName('idName')
        # 属性选择器 [key] [key='val']setProperty(key,val)
        label2.setProperty('notice_level', 'error')
        label1.setProperty('notice_level', 'warming')

        # 后代选择器 QDialog QPushButton 表示 QDialog中的QPushButton子孙控件
        # 子选择器 >  QDialog>QPushButton 子控件
        # 子控件选择器 :: 符合控件的子控件 
        cb = QCheckBox('python', self)
        cb.resize(100, 100)
        cb.move(300, 100)
        cb.setTristate(True)
        # , 不同的选择器 设置相同的css

        # Qss 伪状态 :状态 :!状态 !取反
        # :状态1:状态2  并且
        # :状态1，:状态2

        # 盒子模型:margin border padding content

        # border 边框：样色 宽度 颜色
        # margin 外边距

        pass


from Tools import QssTool

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    with open('61demo.qss', 'r') as f:
        content = f.read()
        app.setStyleSheet(content)
    QssTool.setQssToObj('61demo.qss', app)
    sys.exit(app.exec_())
    # 347
    pass
