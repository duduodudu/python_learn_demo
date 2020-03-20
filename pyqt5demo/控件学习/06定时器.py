from PyQt5.Qt import *
import sys


class MyObject(QObject):
    def timerEvent(self, evt) -> None:
        print("timerEvent", evt)


def set_ui(window):
    obj = MyObject(window)
    # 开启定时器 返回唯一的timer_id
    timer = obj.startTimer(1000);
    print('timer_id:', timer)

    # 关闭定时器
    # obj.killTimer(timer)


class MyTimerLabel(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resize(100, 100)
        self.move(100, 100)

    def timerEvent(self, a0: 'QTimerEvent') -> None:
        self.setText(str(int(self.text()) - 1))
        print("time count down", self.text())
        if (int(self.text()) == 0):
            # self.killTimer(a0.timerId())
            self.killTimer(self.timer_id)


def countDown(window: QWidget, num: int) -> None:
    lbl = MyTimerLabel(window)
    lbl.setText(str(num))
    lbl.timer_id = lbl.startTimer(1000)
    print('开始倒计时')


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = QWidget()
    window.setWindowTitle('定时器')

    set_ui(window)
    countDown(window, 10)

    window.show()
    sys.exit(app.exec_())
