import sys
from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('登录')
        self.resize(300, 300)
        self.setMinimumSize(300, 300)
        self.setup_ui()

    def setup_ui(self):
        self.account_le = QLineEdit(self)
        self.account_le.setPlaceholderText('账号')
        # 自动联想补全 
        completer = QCompleter(['admin'], self.account_le)
        self.account_le.setCompleter(completer)

        self.pwd_le = QLineEdit(self)
        self.pwd_le.setEchoMode(QLineEdit.Password)
        self.pwd_le.setPlaceholderText('密码')
        # 清除按钮
        self.pwd_le.setClearButtonEnabled(True)
        # 添加按钮
        action = QAction(self.pwd_le)
        action.setIcon(QIcon('images/demo.png'))

        def action_change():
            print('改变明文和密文')
            if self.pwd_le.echoMode() == QLineEdit.Normal:
                self.pwd_le.setEchoMode(QLineEdit.Password)
                action.setIcon(QIcon('images/demo.png'))
            else:
                self.pwd_le.setEchoMode(QLineEdit.Normal)
                action.setIcon(QIcon('images/demo1.png'))

        action.triggered.connect(action_change)
        self.pwd_le.addAction(action, QLineEdit.TrailingPosition)

        self.login_btn = QPushButton(self)
        self.login_btn.setText('登   录')
        # self.login_btn.clicked.connect(self.login_cao)
        self.login_btn.clicked.connect(self.login_clicked)

    def login_cao(self):
        print('点击登录按钮')
        account = self.account_le.text()
        pwd = self.pwd_le.text()
        print(account, pwd)
        if account == 'admin':
            if pwd == '123':
                print('登录成功')
            else:
                self.pwd_le.setText('')
                self.pwd_le.setFocus()
        else:
            print('账号错误')
            self.account_le.setText('')
            self.pwd_le.setText('')
            self.account_le.setFocus()

    def login_clicked(self):
        account = self.account_le.text()
        pwd = self.pwd_le.text()
        state = AccountTool.check_login(account, pwd)
        if state == AccountTool.ACCOUNT_ERROR:
            print('用户名错误')
            return None
        if state == AccountTool.PWD_ERROR:
            print('密码错误')
            return None
        if state == AccountTool.SUCCESS:
            print('登录成功')

    # 尺寸改变的时候重新设置
    def resizeEvent(self, evt: QResizeEvent) -> None:
        widget_w = 150
        widget_h = 40
        margin = 20
        self.account_le.resize(widget_w, widget_h)
        self.pwd_le.resize(widget_w, widget_h)
        self.login_btn.resize(widget_w, widget_h)

        x = (self.width() - widget_w) / 2

        self.account_le.move(x, self.height() / 5)
        self.pwd_le.move(x, self.account_le.y() + widget_h + margin)
        self.login_btn.move(x, self.pwd_le.y() + widget_h + margin)


class AccountTool:
    ACCOUNT_ERROR = 1
    PWD_ERROR = 2
    SUCCESS = 3

    # @staticmethod 标识成静态方法
    @staticmethod
    def check_login(account, pwd):
        if account != 'admin':
            return AccountTool.ACCOUNT_ERROR

        if pwd != '123':
            return AccountTool.PWD_ERROR

        return AccountTool.SUCCESS


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
