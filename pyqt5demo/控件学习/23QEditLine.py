import sys
from typing import Tuple

from PyQt5.Qt import *


# 验证器的使用
class AgeValidator(QValidator):
    def validate(self, input_str: str, pos_int: int) -> Tuple['QValidator.State', str, int]:
        # def validate(self, input_str: str, pos_int: int):
        print('validate', input_str, pos_int)
        # 先判断纯数字
        try:
            if 18 <= int(input_str) <= 180:
                return (QValidator.Acceptable, input_str, pos_int)
            elif 1 < int(pos_int) < 17:
                return (QValidator.Intermediate, input_str, pos_int)
            else:
                return (QValidator.Invalid, input_str, pos_int)
        except:
            if len(input_str) == 0:
                return (QValidator.Intermediate, input_str, pos_int)
            return (QValidator.Invalid, input_str, pos_int)

    def fixup(self, p_str: str) -> str:
        print('fixup', p_str)
        try:
            if int(p_str) < 18:
                return '18'
            return '180'
        except:
            return '18'


class AgeIntValidator(QIntValidator):
    def fixup(self, input: str) -> str:
        print('fixup:', input)
        if len(input) == 0 or int(input) < 18:
            return '18'


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = QMainWindow()
    window.setWindowTitle('QEditLine')
    window.resize(500, 500)

    # QLineEdit 继承 QWidget
    # 单行输入框
    le = QLineEdit(window)
    le = QLineEdit('内容信息', window)

    # 设置文本，获取文本
    le.setText('这是设置的文本')
    le.insert('在光标处插入内容')
    print('获取文本框的内容', le.text())
    print('获取用户看到的内容', le.displayText())

    btn = QPushButton('按钮', window)
    btn.move(100, 100)
    btn.pressed.connect(lambda: le.insert('AAA'))
    btn.pressed.connect(lambda: print(le.text()))
    # 复制案例
    le2 = QLineEdit(window)
    le2.move(0, 100)
    btn.pressed.connect(lambda: le2.setText(le.text()))

    # 文本输出模式
    # le2.setEchoMode(QLineEdit.NoEcho)
    # le2.setEchoMode(QLineEdit.Normal)
    # le2.setEchoMode(QLineEdit.Password)
    # le2.setEchoMode(QLineEdit.PasswordEchoOnEdit)

    # 占位提示文本
    le2.setPlaceholderText('占位文本Placeholder')
    print('占位文本', le2.placeholderText())
    # 清空按钮
    le2.setClearButtonEnabled(True)
    print('清空按钮', le2.isClearButtonEnabled())
    # 自定义操作行为
    le3 = QLineEdit(window)
    le3.move(10, 300)
    action = QAction(QIcon('images/demo.png'), '', le3)
    le3.addAction(action, QLineEdit.TrailingPosition)
    action.triggered.connect(lambda: print('点击按按钮'))

    action1 = QAction(le3)
    action1.setIcon(QIcon('images/demo1.png'))
    # le3.addAction(action1, QLineEdit.LeadingPosition)
    le3.addAction(action1, QLineEdit.TrailingPosition)


    def change():
        print('改变明文和密文')


    action.triggered.connect(change)
    action1.triggered.connect(change)

    le3.setClearButtonEnabled(True)

    # 自动联想补全
    completer = QCompleter(['admin', '123456'], le3)
    le3.setCompleter(completer)
    # 内容限制 , 限制最大的长度
    le3.setMaxLength(10)
    # 只读限制
    # le3.setReadOnly(True)
    le3.setText('只读能通过代码设置吗？123456789')

    # 规则验证
    # validator = QValidator()
    # le3.setValidator()
    # 验证通过，暂不验证，验证不通过
    # validate() -> fixup()
    # 抽象类需要使用子类，或系统提供的子类，自定义的子类
    le4 = QLineEdit(window)
    le4.setPlaceholderText('数字验证器的使用')
    le4.move(10, 350)
    # 自定义子类 ?
    # validator = AgeValidator()
    # le4.setValidator(validator)
    # 系统的子类 ?
    validator = QIntValidator(18, 180)
    validator = AgeIntValidator()
    le4.setValidator(validator)

    # 掩码验证 固定位置的固定的数据类型，达到一个格式上的限制 ，例如座机号码，IP地址
    # le4.setInputMask()

    # 文本是否被修改状态，是否被编辑过状态
    print('是否被编辑过状态', le4.isModified())
    le4.setModified(True)
    print('是否被编辑过状态', le4.isModified())

    # 光标控制
    # 向后移动，是否选中，字符数量
    le4.cursorBackward(True, 3)
    # le4.cursorForward(False,4)
    # le4.cursorWordBackward(True)
    # le4.cursorWordForward(True)
    # le4.home(True) # 移至开头
    # le4.end(Flase) # 移至末尾
    # le4.setCursorPosition() # 设置光标位置
    # le4.cursorPosition() # 获取光标位置
    # 聚焦了才能看到光标
    le4.setFocus()

    # 内容边距
    # le4.setContentsMargins(20, 0, 0, 0) #整体的
    # le4.setTextMargins(20, 30, 20, 30) #文本的
    le4.setStyleSheet('background-color:cyan;')

    # 对齐方式
    le4.setAlignment(Qt.AlignRight | Qt.AlignBottom)
    print('对齐方式:', le4.alignment())
    # 常用编辑状态: 退格，删除，清空，复制，剪切，黏贴，撤销，重做，拖放，文本选中
    # 右键菜单有：undo,redo,cut, copy,paste,delete,select all;
    le4.backspace()  # 退格
    le4.clear()  # 清空
    le4.undo()  # 撤销
    print('undoAvailable', le4.isUndoAvailable())
    le4.redo()  # 重做
    print('redoAvailable', le4.isRedoAvailable())
    le4.cut()  # 剪切
    le4.copy()  # 复制
    le4.paste()  # 粘贴
    le4.del_()  # delete
    le4.setDragEnabled(True)  # 拖拽文本

    # 选中
    le4.selectAll()  # 全选
    le4.deselect()  # 取消选中
    le4.setSelection(0, len(le4.text()))  # 选择，开始，结束位置
    #
    print('hasSelectedText', le4.hasSelectedText())
    print('selectionLength', le4.selectionLength())
    print('selectedText', le4.selectedText())
    print('selectionStart', le4.selectionStart())
    print('selectionEnd', le4.selectionEnd())
    # 信号相关
    # 文本框编辑
    le4.textEdited.connect(lambda val: print('textEdited编辑', val))
    # 文本框内容发生改变
    le4.textChanged.connect(lambda val: print('textChanged改变', val))
    # 按下回车键
    le4.returnPressed.connect(lambda: print('returnPressed回车'))
    # 结束编辑
    le4.editingFinished.connect(lambda: print('editingFinished'))
    # 光标位置改变信号
    le4.cursorPositionChanged.connect(lambda pos0, pos1: print('cursorPositionChanged', pos0, pos1))
    # 选中的文本改变
    le4.selectionChanged.connect(lambda: print('selectionChanged'))

    #
    window.show()
    sys.exit(app.exec_())
