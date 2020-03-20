import sys
from PyQt5.Qt import *


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setWindowTitle('QFontDialog')
        self.setup_ui()

    def setup_ui(self):
        # fd = QFontDialog(self)
        font = QFont()
        font.setFamily('华文黑体 ')
        font.setBold(True)
        font.setPixelSize(60)
        fd = QFontDialog(font, self)
        fd.setCurrentFont(font)
        label = QLabel(self)
        label.setText('测试文字')
        self.label = label

        btn = QPushButton(self)
        btn.setText('按钮')
        btn.move(200, 200)

        def font_sel(*args):
            print('字体已经被选择了', args)
            label.setFont(fd.selectedFont())
            label.adjustSize()

        # 信号
        def current_font(f):
            label.setFont(f)
            label.adjustSize()

        fd.currentFontChanged.connect(current_font)
        fd.fontSelected.connect(current_font)

        # btn.clicked.connect(lambda: fd.open(font_sel))
        btn.clicked.connect(self.btn_clicked)
        # fd.show()
        # fd.open()
        # fd.exec()
        # if fd.exec():
        # label.setFont(fd.selectedFont())

        # 可选项
        fd.setOption(QFontDialog.NoButtons, True)
        fd.setOptions(QFontDialog.NoButtons | QFontDialog.DontUseNativeDialog)
        # fd.show()
        pass

    def btn_clicked(self):
        print('点击按钮')
        # result = QFontDialog.getFont()
        result = QFontDialog.getFont(self.label.font(), self, '选择一个好看的标题')
        # font ，是否点击了OK
        if result[1]:
            self.label.setFont(result[0])
            self.label.adjustSize()
        print(result)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
    pass
