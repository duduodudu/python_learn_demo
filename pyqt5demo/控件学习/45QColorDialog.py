import sys
from PyQt5.Qt import *


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setWindowTitle('QColorDialog')

        cd = QColorDialog(self)

        # cd.colorSelected.connect(lambda val: print(val))
        # 设置背景颜色 
        def color_sel(col):
            palette = QPalette()
            palette.setColor(QPalette.Background, col)
            self.setPalette(palette)

        # cd.colorSelected.connect(color_sel)
        # cd.show()
        def color_open():
            palette = QPalette()
            palette.setColor(QPalette.Background, cd.selectedColor())
            self.setPalette(palette)

        # 2
        cd.setOptions(QColorDialog.NoButtons | QColorDialog.ShowAlphaChannel)
        # cd.setOption( QColorDialog.DontUseNativeDialog,True)

        # cd.open(color_open)
        # 3
        # if cd.exec():
        #     color_open()
        self.静态方法()
        pass

    def 静态方法(self):
        # 自定义颜色个数
        print('customCount:', QColorDialog.customCount())
        # 设置自定义颜色
        QColorDialog.setCustomColor(0, QColor(100, 120, 130))
        print(QColorDialog.customColor(0))
        #
        color = QColorDialog.getColor(QColor(10, 150, 190), self, '选择颜色')
        print(color)
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
