from Login_Pane import LoginPane
from Register_Pane import RegisterPane
from Calculator_Pane import CalculatorPane

if __name__ == '__main__':
    import sys
    from PyQt5.Qt import *

    app = QApplication(sys.argv)
    login_pane = LoginPane()

    register_pane = RegisterPane(login_pane)
    register_pane.move(0, login_pane.height())
    register_pane.show()


    def exit_register_pane():
        print('应该退出')
        animation = QPropertyAnimation(register_pane)
        animation.setTargetObject(register_pane)
        animation.setPropertyName(b'pos')
        animation.setStartValue(QPoint(0, 0))
        animation.setEndValue(QPoint(0, login_pane.height()))
        animation.setDuration(1000)
        animation.setEasingCurve(QEasingCurve.InBounce)
        animation.start(QAbstractAnimation.DeleteWhenStopped)


    register_pane.exit_single.connect(exit_register_pane)
    register_pane.register_account_pws_single.connect(lambda name, pwd: print("注册：", name, pwd))


    def show_register_pane():
        """"""
        print('展示注册界面')

        animation = QPropertyAnimation(register_pane)
        animation.setTargetObject(register_pane)
        animation.setPropertyName(b'pos')
        animation.setStartValue(QPoint(0, login_pane.height()))
        animation.setEndValue(QPoint(0, 0))
        animation.setDuration(1000)
        animation.setEasingCurve(QEasingCurve.OutBounce)
        animation.start(QAbstractAnimation.DeleteWhenStopped)


    calculator_pane = CalculatorPane()


    def check_login(account, pwd):
        if account == '123456' and pwd == 'admin':
            print('登录成功')
            calculator_pane.show()
            login_pane.hide()
        else:
            print('登录失败')
            login_pane.show_error()


    # 加入QQ群：https://qun.qq.com/join.html 

    login_pane.show_register_pane_single.connect(show_register_pane)
    login_pane.check_login_single.connect(check_login)

    login_pane.show()
    sys.exit(app.exec_())
