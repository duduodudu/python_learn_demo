import sys
from PyQt5.Qt import *
from du_resource.calculator_ui import Ui_Form


class Calculator(QObject):
    # 自定义信号
    show_content = pyqtSignal(str)

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent=parent, *args, **kwargs)
        # 数字键位 num 运算符 operator
        self.key_models = []

    def calculate(self):
        # 删除最后一个运算符
        if len(self.key_models) > 0 and self.key_models[-1]['role'] == 'operator':
            self.key_models.pop(-1)
        # 计算
        expression = ''
        for i in self.key_models:
            expression += i['title']
        print(expression, '=', eval(expression))
        return eval(expression)

    def parse_key_model(self, key_model):
        # {'title': '3', 'role': 'num'}
        if key_model['role'] == 'clear':
            print('清空所有内容')
            self.key_models = []
            self.show_content.emit('0.0')
            return None
        # 计算
        if key_model['role'] == 'calculate':
            print('计算所有内容')
            result = self.calculate()
            self.show_content.emit(str(result))
            return None

        # 第一次按下
        if len(self.key_models) == 0:
            if key_model['role'] == 'num':
                if key_model['title'] == '.':
                    key_model['title'] = '0.'
                self.key_models.append(key_model)
                self.show_content.emit(self.key_models[-1]['title'])
            return None

        # 处理 % +/-
        if key_model['title'] in ['%', '+/-']:
            if self.key_models[-1]['role'] != 'num':
                return None
            else:
                if key_model['title'] == '%':
                    self.key_models[-1]['title'] = str(float(self.key_models[-1]['title']) / 100)
                elif key_model['title'] == '+/-':
                    self.key_models[-1]['title'] = str(float(self.key_models[-1]['title']) * -1)
            self.show_content.emit(self.key_models[-1]['title'])
            return None
        # 角色相等
        if key_model['role'] == self.key_models[-1]['role']:
            if key_model['role'] == 'num':
                # 已经包含小数点了
                if key_model['title'] == '.' and self.key_models[-1]['title'].__contains__('.'):
                    return None
                    # 首个数组为0
                if self.key_models[-1]['title'] != '0':
                    self.key_models[-1]['title'] += key_model['title']
                else:
                    self.key_models[-1]['title'] = key_model['title']
                self.show_content.emit(self.key_models[-1]['title'])
            # 运算符
            elif key_model['role'] == 'operator':
                self.key_models[-1]['title'] = key_model['title']
                self.show_content.emit(str(self.calculate()))
        else:
            if key_model['title'] in ['.', '%', '+/-']:
                return None
            if key_model['role'] == 'num':
                self.show_content.emit(key_model['title'])
            elif key_model['role'] == 'operator':
                self.show_content.emit(str(self.calculate()))
            self.key_models.append(key_model)


class CalculatorPane(QWidget, Ui_Form):
    # 自定义信号
    exit_single = pyqtSignal()
    register_account_pws_single = pyqtSignal(str, str)

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent=parent, *args, **kwargs)
        # 修复顶层窗口没有背景的bug
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)
        self.calculator = Calculator(self)
        self.calculator.show_content.connect(self.show_content)

    def get_key(self, title, role):
        """
        点击按钮
        :param title:
        :param role:
        :return:
        """
        print('点击按钮:', title, role)
        self.calculator.parse_key_model({'title': title, 'role': role})

    def show_content(self, txt):
        """
        展示文本内容
        :return:
        """
        self.lineEdit.setText(txt)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CalculatorPane()
    window.show()
    sys.exit(app.exec_())
