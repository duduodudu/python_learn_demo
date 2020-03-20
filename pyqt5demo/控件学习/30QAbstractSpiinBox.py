import sys
from PyQt5.Qt import *


class MySpinBox(QAbstractSpinBox):
    def __init__(self, parent=None, num=0, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.lineEdit().setText(str(num))

    def stepEnabled(self):
        current_num = int(self.text())
        if current_num == 0:
            return QAbstractSpinBox.StepUpEnabled
        elif current_num == 9:
            return QAbstractSpinBox.StepDownEnabled
        elif current_num < 0 or current_num > 9:
            return QAbstractSpinBox.StepNone
        else:
            return QAbstractSpinBox.StepUpEnabled | QAbstractSpinBox.StepDownEnabled

    def stepBy(self, steps: int) -> None:
        print('stepBy:', steps)
        # 设置回去
        current_num = int(self.text()) + steps
        self.lineEdit().setText(str(current_num))

    # 验证方法
    def validate(self, p_str: str, p_int: int):
        num = int(p_str)
        if num < 18:
            return (QValidator.Intermediate, p_str, p_int)
        elif num <= 180:
            return (QValidator.Acceptable, p_str, p_int)
        else:
            return (QValidator.Invalid, p_str, p_int)

    def fixup(self, input: str) -> str:
        return '18'


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QAbstractSpinBox')
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        # 步长调节器 ， 通过控件进行组合的
        # asb = QAbstractSpinBox(self)
        asb = MySpinBox(self, 1)
        asb.resize(100, 30)
        asb.move(100, 100)

        # 设置文本内容
        # asb.lineEdit().setText('1')

        # 加速 长按步长加速 #####
        print('isAccelerated', asb.isAccelerated())
        asb.setAccelerated(True)
        print('isAccelerated', asb.isAccelerated())

        # 只读 不允许用户键盘输入 ######
        print('readonly:', asb.isReadOnly())
        # asb.setReadOnly(True)
        print('readonly:', asb.isReadOnly())

        # 设置以及获取内容 #######
        print('获取内容', asb.text())
        # asb.lineEdit() # 设置
        asb.lineEdit().setText('5')
        # asb.lineEdit().setText('55')

        # 测试 QLineEdit 的其他方法
        asb.lineEdit().setAlignment(Qt.AlignCenter)

        # 对齐方式
        asb.setAlignment(Qt.AlignRight)

        # 周边框架
        print('hasFrame:', asb.hasFrame())

        # 清空 
        # asb.clear()

        # 按钮样式
        # asb.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        # asb.setButtonSymbols(QAbstractSpinBox.NoButtons)

        # 验证文本输入的内容

        # 信号
        asb.editingFinished.connect(lambda: print('结束编辑'))
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
