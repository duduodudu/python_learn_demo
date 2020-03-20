import sys
from PyQt5.Qt import *


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setWindowTitle('QCalendarWidget')
        self.setup_ui()

    def setup_ui(self):
        # 日期 每月的日历，允许用户选择一个日期
        cal = QCalendarWidget(self)
        # 设置最大值 最小值 当前值
        print('默认范围:', cal.minimumDate(), cal.maximumDate())
        print(cal.selectedDate())
        # cal.setMinimumDate(QDate(2012, 1, 1))
        # cal.setMaximumDate(QDate(2020, 12, 12))
        cal.setDateRange(QDate(2010, 10, 10), QDate(2100, 10, 10))

        # 编辑状态
        cal.setDateEditEnabled(True)
        cal.setDateEditAcceptDelay(300)  # 延迟效果

        # 获取值
        def show():
            print(cal.yearShown())
            print(cal.monthShown())
            print(cal.selectedDate())

        btn = QPushButton(self)
        btn.setText('测试按钮')
        btn.move(30, 400)
        btn.clicked.connect(show)
        # 外观设置
        # 导航条
        cal.setNavigationBarVisible(False)
        # 一周的第一天
        cal.setFirstDayOfWeek(Qt.Sunday)
        # 网格
        cal.setGridVisible(True)
        # 文本格式
        tcf = QTextCharFormat()
        tcf.setFontFamily('隶书')
        cal.setHeaderTextFormat(tcf)
        #
        cal.showToday()
        cal.showSelectedDate()
        cal.showNextMonth()
        cal.showNextYear()
        cal.showPreviousMonth()
        cal.showPreviousYear()
        cal.setCurrentPage(2019, 9)
        # 信号
        cal.activated.connect(lambda date: print(date))
        cal.clicked.connect(lambda date: print(date))
        cal.currentPageChanged.connect(lambda year, month: print(year, month))
        cal.selectionChanged.connect(lambda: print('changed'))

        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
