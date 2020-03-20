import sys
from PyQt5.Qt import *


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setWindowTitle('QLabel')

        label = QLabel('文字(&s):', self)
        label.setStyleSheet('background-color:red')
        #   文本对齐
        label.setAlignment(Qt.AlignRight)
        # 缩进
        label.setIndent(20)
        # 边距
        label.setMargin(30)
        # 文本格式 

        # 小伙伴
        le1 = QLineEdit(self)
        le1.move(300, 300)
        le2 = QLineEdit(self)
        le2.move(300, 350)
        label.setBuddy(le1)

        # 内容缩放  仅对图片有效
        label.setPixmap(QPixmap('images/demo.png'))
        label.setScaledContents(True)
        # 文本交互
        # label.setTextInteractionFlags(Qt.TextSelectableByMouse | Qt.TextSelectableByKeyboard | Qt.TextEditable)
        # 选中相关 前提是可以选中
        label.setText("<a href='http://www.baidu.com'>百度</a>")
        print(label.selectedText())
        # 打开连接
        label.setOpenExternalLinks(True)
        # 换行 但是保证单词的完整性
        label.setWordWrap(True)
        # 内容操作
        label.setText("<img src='./images/demo1.png' width=60 height=60>")
        label.setNum(999)
        # 设置图像
        # pic = QPicture()
        # painter = QPainter(pic)
        # painter.setBrush(QBrush(QColor(100, 200, 230)))
        # painter.drawEllipse(0, 0, 200, 200)
        # label.setPicture(pic)
        # 动图
        movie = QMovie('images/demo.gif')

        label.setMovie(movie)
        movie.start()
        # 100 标识一倍速
        movie.setSpeed(100)
        # 清空
        label.clear()

        # 信号
        label.setText("<a href='http://www.baidu.com'>百度</a>")
        label.linkActivated.connect(lambda link: print(link))
        label.linkHovered.connect(lambda a: print('hovered:', a))

        pass

    pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
