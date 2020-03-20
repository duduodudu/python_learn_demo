import sys
from PyQt5.Qt import *


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setWindowTitle('QDateTimeEdit')
        self.setup_ui()

    def setup_ui(self):
        # 编辑日期和事件的单行文本
        # 箭头 或者 键盘输入
        # 可以单独调节某个部分
        # -> QDateEdit QTimeEdit
        # dte = QDateTimeEdit(self)
        dte = QDateTimeEdit(QDateTime.currentDateTime(), self)

        dte.move(100, 100)
        dte.resize(300, 25)
        # 范围 最大值 最小值
        print('日期范围:', dte.minimumDate(), dte.maximumDate())
        print('时间范围:', dte.minimumDateTime(), dte.maximumDateTime())
        # 显示格式
        # 没有0,有0,简写的本地化，完成的本地化
        # d dd ddd dddd
        # M MM MMM MMMM
        # yy yyyy
        # 时间格式
        # h hh H HH
        # m mm
        # s ss
        # z zzz 毫秒
        # AP/A ap/a
        # t 时区
        dte.setDisplayFormat('yy年MM月dd日 dddd HH:mm:ss:zzz')

        # section ########
        print('sectionCount:', dte.sectionCount())
        print('currentSection:', dte.currentSection())
        print('currentSectionIndex:', dte.currentSectionIndex())
        dte.setCurrentSectionIndex(1)
        dte.setCurrentSection(QDateTimeEdit.DaySection)
        print('sectionText', dte.sectionText(QDateTimeEdit.DaySection))
        dte.setFocus()

        # 最大 最小 ####
        dte.setMaximumDateTime(QDateTime(2020, 12, 32, 24, 59))
        dte.clearMaximumDateTime()

        # 弹出日历选择控件 ####
        print('calendarPopup:', dte.calendarPopup())
        dte.setCalendarPopup(True)
        # 可以自定义弹出的日历控价  

        # 获取日期时间等信息 #########
        print(dte.dateTime())
        print(dte.date())
        print(dte.time())
        # 信号
        dte.dateTimeChanged.connect(lambda val: print('信号1', val))
        dte.dateChanged.connect(lambda val: print('信号2', val))
        dte.timeChanged.connect(lambda val: print('信号3', val))

        self.测试QDateEdit()
        self.测试QTimeEdit()
        pass

    def 测试QDateEdit(self):
        de = QDateEdit(self)
        de.move(100, 150)

    def 测试QTimeEdit(self):
        te = QTimeEdit(self)
        te.move(100, 200)


def 日期时间测试():
    # QDateTime QDate QTime
    dt = QDateTime(2018, 12, 12, 12, 30)
    dt = QDateTime.currentDateTime()
    dt = dt.addYears(1)
    dt = dt.addMonths(30)
    dt = dt.addDays(10)
    dt = dt.addSecs(60)
    dt = dt.addMSecs(60)
    print('offsetFromUtc:', dt.offsetFromUtc())
    print(dt)
    d = QDate.currentDate()
    d.day()
    d.month()
    print(d)
    t = QTime.currentTime()
    t.start()
    print(t)
    print(t.elapsed())
    pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    日期时间测试()
    sys.exit(app.exec_())
