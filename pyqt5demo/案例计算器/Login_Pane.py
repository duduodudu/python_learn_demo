import sys
from PyQt5.Qt import *
from du_resource.login_ui import Ui_Form


class LoginPane(QWidget, Ui_Form):
    # 自定义信号
    show_register_pane_single = pyqtSignal()
    check_login_single = pyqtSignal(str, str)

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent=parent, *args, **kwargs)
        # 修复顶层窗口没有背景的bug
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)

        # 设置动画
        movie = QMovie(':/login/images/login_top_bg.gif')
        movie.setScaledSize(QSize(500, 235))
        self.login_top_bg_label.setMovie(movie)
        movie.start()

    def show_register_pane(self):
        print('点击注册按钮，应该弹出注册界面')
        self.show_register_pane_single.emit()

    def open_qq_link(self):
        print('点击二维码按钮')
        link = 'http://qun.qq.com/join.html'
        QDesktopServices.openUrl(QUrl(link))

    def enable_login_btn(self):
        account = self.account_cb.currentText()
        pwd = self.pwd_le.text()
        print('输入内容-> 判断登录按钮是否可用', account, pwd)
        if len(account) > 0 and len(pwd) > 0:
            self.login_btn.setEnabled(True)
        else:
            self.login_btn.setEnabled(False)

    def check_login(self):
        print('LoginPane:点击登录按钮')
        account = self.account_cb.currentText()
        pwd = self.pwd_le.text()
        self.check_login_single.emit(account, pwd)

    def auto_login(self, checked):
        print('点击自动登录', checked)
        if checked:
            self.remember_pwd_cb.setChecked(checked)

    def remember_pwd(self, checked):
        print('点击记住密码', checked)
        if not checked:
            self.auto_login_cb.setChecked(checked)

    def show_error(self):
        """错误动画处理"""
        animation = QPropertyAnimation(self)
        animation.setTargetObject(self.login_bottom)
        animation.setPropertyName(b'pos')
        animation.setKeyValueAt(0, self.login_bottom.pos())
        animation.setKeyValueAt(0.2, self.login_bottom.pos() + QPoint(15, 0))
        animation.setKeyValueAt(0.5, self.login_bottom.pos())
        animation.setKeyValueAt(0.7, self.login_bottom.pos() + QPoint(-15, 0))
        animation.setKeyValueAt(1, QPoint(0, self.login_bottom.y()))

        animation.setLoopCount(3)
        animation.setDuration(200)
        animation.start(QAbstractAnimation.DeleteWhenStopped)
        print(self.login_bottom.pos())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginPane()
    window.show()
    sys.exit(app.exec_())
