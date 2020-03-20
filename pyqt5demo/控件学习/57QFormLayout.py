import sys
from PyQt5.Qt import *


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setWindowTitle('QFormLayout')
        self.setup_ui()

    def setup_ui(self):
        name_label = QLabel('姓名(&n):')
        age_label = QLabel('年龄:')

        name_le = QLineEdit()
        age_sb = QSpinBox()
        name_label.setBuddy(name_le)

        sex_label = QLabel('性别(&S)')
        male_rb = QRadioButton('男')
        female_rb = QRadioButton('女')

        h_layout = QHBoxLayout()
        h_layout.addWidget(male_rb)
        h_layout.addWidget(female_rb)

        # 创建管理器
        layout = QFormLayout()
        # 布局管理赋值给需要布局的父控件
        self.setLayout(layout)
        # 布局管理器赋值给子控件
        # 上下结构
        # layout.addWidget(name_label)
        # layout.addWidget(name_le)
        # 添加行
        layout.addRow(name_label, name_le)
        layout.addRow(age_label, age_sb)
        # layout.addRow('年龄(&A)', age_sb)
        # layout.addRow(sex_label, h_layout)
        layout.addRow(QPushButton('提交'))
        # 插入行 int 插入索引
        # layout.insertRow(0, '插入的:', QLabel('插入的标签'))
        # layout.insertRow(100, '索引越界了咋办', QLabel('插入的标签'))
        # 获取行的信息
        print('rowCount:', layout.rowCount())
        # 位置 角色
        # QFormLayout.LabelRole
        # QFormLayout.FieldRole
        # QFormLayout.SpanningRole
        # print(layout.getWidgetPosition(age_sb))
        # print(layout.getWidgetPosition(female_rb))
        #
        # layout.setWidget(0, QFormLayout.LabelRole, name_label)
        # layout.setWidget(0, QFormLayout.FieldRole, name_le)
        # 重复设置会警告
        # QFormLayoutPrivate::setItem: Cell (0, 0) already occupied
        # layout.setWidget(0, QFormLayout.LabelRole, age_label)

        # layout.setWidget(1, QFormLayout.LabelRole, age_label)
        # layout.setWidget(1, QFormLayout.FieldRole, age_sb)
        # 移除行 删除子控件
        name_le.destroyed.connect(lambda: print('name:被释放了'))
        age_label.destroyed.connect(lambda: print('age 被释放了'))
        # layout.removeRow(0)
        # 移除行 不删除子控件 返回 TakeRowResult #布局可能会乱套
        # type: QFormLayout.TakeRowResult
        # print(layout.takeRow(0).labelItem.widget().hide())
        # print(layout.takeRow(0).fieldItem.widget().hide())

        # 标签对象
        print(layout.labelForField(name_le))
        layout.labelForField(name_le).setText('测试' * 4)
        # 默认
        # layout.setRowWrapPolicy(QFormLayout.DontWrapRows)
        # 适应最长 不够换行
        # layout.setRowWrapPolicy(QFormLayout.WrapLongRows)
        # 全部换行
        # layout.setRowWrapPolicy(QFormLayout.WrapAllRows)

        # 对齐方式
        print((layout.formAlignment() == Qt.AlignLeft | Qt.AlignTop))
        layout.setAlignment(Qt.AlignBottom)
        # 标签对齐
        layout.setLabelAlignment(Qt.AlignCenter)
        # 间距
        layout.setHorizontalSpacing(30)  # 水平间距
        layout.setVerticalSpacing(60)  # 垂直间距

        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
