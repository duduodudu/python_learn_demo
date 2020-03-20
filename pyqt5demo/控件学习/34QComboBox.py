import sys
from PyQt5.Qt import *


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QComboBox')
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        # 组合框 QComboBox 组合控价
        # 默认显示最小的控件给用户操作
        # 可通过下拉选择界面 选取更多的预置选项
        # 继承QWidget
        cb = QComboBox(self)
        cb.move(100, 100)
        cb.resize(100, 25)
        # 数据操作 增删改查 条目项
        cb.addItem('选项1')
        cb.addItem('选项2', '用户数据')
        cb.addItems(['AAA-数组', 'BBB-数组'])
        cb.addItems(('CCC-元组', 'DDD-元组'))
        # 插入 下标
        cb.insertItem(0, '0')
        cb.insertItem(0, QIcon('images/demo.png'), '0')
        cb.insertItems(0, ['1', '2', '3'])
        cb.insertItems(0, ('11', '22', '33'))
        # 修改
        cb.setItemText(3, '修改了内容')
        cb.setItemIcon(4, QIcon('images/demo.png'))
        # 移除 
        cb.removeItem(7)
        # 插入分割线
        cb.insertSeparator(2)
        # 
        cb.setCurrentIndex(1)
        cb.setCurrentText('指定匹配的文本')
        # 编辑 可以进行输入
        # cb.setEditable(True)
        cb.setEditText('编辑的文本')
        #
        print(QAbstractItemModel.__subclasses__())
        model = QStandardItemModel()
        item1 = QStandardItem('1')
        item2 = QStandardItem('2')
        item21 = QStandardItem('21')
        item22 = QStandardItem('22')
        item2.appendRows([item21, item22])
        model.appendRow(item1)
        model.appendRow(item2)
        cb.setModel(model)
        cb.setView(QTreeView(cb))
        cb.resize(300, 30)
        # 获取数据
        print('count:', cb.count())
        print('currentIndex:', cb.currentIndex())
        print('currentData:', cb.currentData())
        print('currentText:', cb.currentText())

        print('itemData:', cb.itemData(cb.currentIndex()))
        print('itemIcon:', cb.itemIcon(cb.currentIndex()))
        print('itemText:', cb.itemText(cb.currentIndex()))
        # 数据限制 #### 条目个数限制
        print('maxCount:', cb.maxCount())
        cb.setMaxCount(100)
        print(cb.maxVisibleItems())  # 可以展示的
        # cb.setMaxVisibleItems()
        # 常规操作
        cb.setDuplicatesEnabled(True)  # 重复选项
        print(cb.hasFrame())
        cb.setFrame(True)
        # 尺寸调整策略
        cb.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        cb.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)
        # 清空
        # cb.clear()  # 清空所有的
        # cb.clearEditText()  # 清空编辑的文本
        # 弹出
        cb.showPopup()
        # 完成器
        cb.setEditable(True)
        cb.setCompleter(QCompleter(('123', '124')))
        # 验证器 同 LineEdit
        # 信号 #####
        # 被选中时
        cb.activated.connect(lambda val: print('信号', type(val), val))
        # cb.activated[int]
        # cb.activated[str]
        # 当前选中的索引发生改变时
        cb.currentIndexChanged.connect(lambda val: print('currentIndexChanged:信号', type(val)))
        # cb.currentIndexChanged[int]
        # cb.currentIndexChanged[str]
        # 当前的文本内容发生改变的时候
        # cb.currentTextChanged
        # 编辑的文本发生改变的时候
        # cb.editTextChanged
        # 高亮
        # cb.highlighted
        # cb.highlighted[int]
        # cb.highlighted[str]
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
