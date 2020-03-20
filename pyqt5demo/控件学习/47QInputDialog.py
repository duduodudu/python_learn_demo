import sys
from PyQt5.Qt import *


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setWindowTitle('QInputDialog')
        self.setup_ui()

    def setup_ui(self):
        # self.静态方法()
        self.demo()
        pass

    def 静态方法(self):
        # result = QInputDialog.getInt(self, '标题', '提示标签', 999, step=5)
        # result = QInputDialog.getDouble(self, '标题', '提示标签', decimals=2)
        # result = QInputDialog.getText(self, '标题', '提示标签', echo=QLineEdit.Password)
        # result = QInputDialog.getMultiLineText(self, '标题', '提示标签')
        # 下拉列表
        result = QInputDialog.getItem(self, '标题', '提示标签', ('1', '2', '3'))
        print(result)
        pass

    def demo(self):
        input_d = QInputDialog(self, Qt.FramelessWindowHint)
        # 可选项
        # input_d.setOption(QInputDialog.UseListViewForComboBoxItems)
        # input_d.setOption(QInputDialog.NoButtons)

        # input_d.setComboBoxItems(['1', '2', '3'])
        #  输入类型限制  ###
        # input_d.setInputMode(QInputDialog.DoubleInput)
        # input_d.setInputMode(QInputDialog.IntInput)
        # input_d.setInputMode(QInputDialog.TextInput)
        # 界面文本设置 #####
        input_d.setLabelText('这是输入标签')
        input_d.setOkButtonText('好的')
        input_d.setCancelButtonText('点我取消哦')
        # 小分类设置 最大值 最小值 范围 步长 当前值 小数位数 字符串输入模式
        # input_d.setInputMode(QInputDialog.DoubleInput)
        # input_d.setDoubleMaximum(999.9)
        # input_d.setDoubleRange(19.9, 22.20)

        # 信号 ##
        input_d.intValueChanged.connect(lambda val: print('intValueChanged', val))
        input_d.intValueSelected.connect(lambda val: print('intValueSelected', val))
        input_d.doubleValueChanged.connect(lambda val: print('doubleValueChanged', val))
        input_d.doubleValueSelected.connect(lambda val: print('doubleValueSelected', val))
        input_d.textValueChanged.connect(lambda val: print('textValueChanged', val))
        input_d.textValueSelected.connect(lambda val: print('textValueSelected', val))
        # 下拉列表
        input_d.show()
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
