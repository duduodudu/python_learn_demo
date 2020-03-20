import sys
from PyQt5.Qt import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.setWindowTitle('QButtonGroup按钮组的使用')
    window.resize(500, 500)

    # 单选按钮 男女
    r_male = QRadioButton('男', window)
    r_female = QRadioButton('女', window)
    r_male.move(100, 100)
    r_female.move(100, 150)

    # 创建按钮组 并添加按钮
    sex_group = QButtonGroup(window)
    # 后面的id,用于标识，默认的-1开始，自动分配，-2，-3
    sex_group.addButton(r_male, id=1)
    sex_group.addButton(r_female, 2)
    print('buttons:', sex_group.buttons())
    print('指定ID的Button:', sex_group.button(2))
    r_male.setChecked(True)
    print('选中的按钮', sex_group.checkedButton())

    # 按钮移除 
    sex_group.removeButton(r_male)

    # 是否
    r_yes = QRadioButton('是', window)
    r_no = QRadioButton('否', window)
    r_yes.move(200, 100)
    r_no.move(200, 150)

    answer_group = QButtonGroup(window)
    answer_group.addButton(r_yes, 1)
    answer_group.addButton(r_no)

    # 绑定和获取ID
    answer_group.setId(r_yes, 1)
    answer_group.setId(r_no, 2)
    # checkedId默认是 -1，选中的时候就为选中的按钮的Id
    print('选中的ID', answer_group.checkedId())
    r_yes.setChecked(True)
    print('选中的ID', answer_group.checkedId())


    # 设置独占性 互斥
    # answer_group.setExclusive(False)
    # 信号
    def test(val):
        print('信号', val)


    # 默认传id
    # answer_group.buttonToggled.connect(test)
    # 相同的信号可以选择类型
    answer_group.buttonClicked[int].connect(test)
    answer_group.buttonClicked[QAbstractButton].connect(test)

    window.show()
    sys.exit(app.exec_())
