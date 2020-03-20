import sys
from PyQt5.Qt import *


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setWindowTitle('综合案例')
        self.setup_ui()

    def setup_ui(self):
        pro = QComboBox(self)
        pro.move(100, 100)
        pro.resize(100, 30)
        self.pro = pro
        city = QComboBox(self)
        city.move(200, 100)
        city.resize(100, 30)
        self.city = city
        self.city_dic = {
            '北京': {
                '东城': '001',
                '西城': '002',
                '朝阳': '003',
                '丰台': '004'
            }, '上海': {
                '黄埔': '005',
                '长宁': '006',
                '松江': '007'
            }, '广东': {
                '广州': '008',
                '深圳': '009',
                '佛山': '010'
            }
        }
        # 显示数据
        pro.currentIndexChanged[str].connect(self.pro_changed)
        pro.addItems(self.city_dic.keys())

        # self.pro_changed(pro.currentText())

        # 监听城市
        city.currentIndexChanged[int].connect(self.city_changed)
        pass

    def pro_changed(self, pro_name):
        print('省份', pro_name)
        # 根据省 获取城市
        citys = self.city_dic[pro_name]
        self.city.blockSignals(True)  # 阻断信号
        self.city.clear()  # 先清除条目
        self.city.blockSignals(False)  # 恢复信号
        # self.city.addItems(citys.keys())
        for k, v in citys.items():
            self.city.addItem(k, v)
        pass

    def city_changed(self, index):
        print('城市:', index, self.city.currentText(), self.city.currentData())
        if index == -1:
            print('城市信息:', self.city.itemText(index), self.city.itemData(index))
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.resize(500, 500)
    window.show()
    sys.exit(app.exec_())
