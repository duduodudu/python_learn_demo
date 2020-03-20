import sys
from PyQt5.Qt import *
from du_resource.register_ui import Ui_Form


class RegisterPane(QWidget, Ui_Form):
    # 自定义信号
    exit_single = pyqtSignal()
    register_account_pws_single = pyqtSignal(str, str)

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent=parent, *args, **kwargs)
        # 修复顶层窗口没有背景的bug
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)

        self.animation_targets = [self.exit_menue_btn, self.reset_menue_btn, self.about_menue_btn]
        self.animation_targets_pos = [target.pos() for target in self.animation_targets]
        for _, target in enumerate(self.animation_targets):
            target.move(self.main_menue_btn.pos())

    def show_hide_menue(self, checked):
        print('菜单', checked)
        # 动画组

        animation_group = QSequentialAnimationGroup(self)
        for idx, target in enumerate(self.animation_targets):
            animation = QPropertyAnimation()
            animation.setTargetObject(target)
            animation.setPropertyName(b'pos')

            # 方式 1
            # if checked:
            #     animation.setStartValue(self.main_menue_btn.pos())
            #     animation.setEndValue(self.animation_targets_pos[idx])
            # else:
            #     animation.setStartValue(self.animation_targets_pos[idx])
            #     animation.setEndValue(self.main_menue_btn.pos())

            animation.setStartValue(self.main_menue_btn.pos())
            animation.setEndValue(self.animation_targets_pos[idx])

            animation.setDuration(200)
            animation.setEasingCurve(QEasingCurve.InOutBounce)
            animation_group.addAnimation(animation)

        # 方式二
        if not checked:
            animation_group.setDirection(QAbstractAnimation.Backward)

        animation_group.start(QAbstractAnimation.DeleteWhenStopped)

    def about_lk(self):
        print('关于')
        QMessageBox.about(self, '关于我', 'http://www.baidu.com')

    def reset(self):
        print('重置')
        self.account_le.clear()
        self.password_le.clear()
        self.confirm_le.clear()

    def enable_register_btn(self):
        """ 监听文本框输入以激活注册按钮 """
        print('输入改变')
        account_txt = self.account_le.text()
        password_txt = self.password_le.text()
        cp_txt = self.confirm_le.text()
        if len(account_txt) > 0 and len(password_txt) > 0 and len(cp_txt) > 0 and password_txt == cp_txt:
            self.register_btn.setEnabled(True)
        else:
            self.register_btn.setEnabled(False)

        pass

    def exit_pane(self):
        print('退出')
        self.exit_single.emit()

    def check_register(self):
        print('注册')
        self.register_account_pws_single.emit(self.account_le.text(), self.password_le.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RegisterPane()
    window.exit_single.connect(lambda: print('接受退出信号'))
    window.register_account_pws_single.connect(lambda name, pwd: print('接受信号：注册', name, pwd))
    window.show()
    sys.exit(app.exec_())
