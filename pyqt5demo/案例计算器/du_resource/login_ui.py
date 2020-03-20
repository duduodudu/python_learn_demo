# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 450)
        Form.setMinimumSize(QtCore.QSize(500, 450))
        Form.setMaximumSize(QtCore.QSize(500, 450))
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setStyleSheet("\n"
"")
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.login_top_bg_label = QtWidgets.QLabel(self.widget)
        self.login_top_bg_label.setText("")
        self.login_top_bg_label.setObjectName("login_top_bg_label")
        self.horizontalLayout_2.addWidget(self.login_top_bg_label)
        self.verticalLayout.addWidget(self.widget)
        self.login_bottom = QtWidgets.QWidget(Form)
        self.login_bottom.setStyleSheet("")
        self.login_bottom.setObjectName("login_bottom")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.login_bottom)
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.register_btn = QtWidgets.QPushButton(self.login_bottom)
        self.register_btn.setFlat(True)
        self.register_btn.setObjectName("register_btn")
        self.horizontalLayout.addWidget(self.register_btn, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignBottom)
        self.widget_3 = QtWidgets.QWidget(self.login_bottom)
        self.widget_3.setStyleSheet("\n"
"")
        self.widget_3.setObjectName("widget_3")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout.setObjectName("gridLayout")
        self.account_cb = QtWidgets.QComboBox(self.widget_3)
        self.account_cb.setMinimumSize(QtCore.QSize(0, 45))
        self.account_cb.setStyleSheet("QComboBox {\n"
"    font-size:20px;\n"
"    border:none ;\n"
"    border-bottom:1px solid lightgray;\n"
"    background-color:transparent;\n"
"}\n"
"QComboBox:hover{\n"
"    border-bottom:1px solid gray;\n"
"}\n"
"QComboBox:focus {\n"
"    border-bottom:1px solid rgb(254, 167, 111);\n"
"}\n"
"QComboBox::drop-down{\n"
"    background-color:transparent;\n"
"    width:60px;\n"
"    height:40px;\n"
"}\n"
"QComboBox::down-arrow {\n"
"    \n"
"    image: url(:/login/images/login_combobox_icon.png);\n"
"    width:40px;\n"
"    height:40px;\n"
"}\n"
"QComboBox QAbstractItemView{\n"
"    min-height:60px;    \n"
"}\n"
"QComboBox QAbstractItemView:item {\n"
"    color:lightblue;    \n"
"}")
        self.account_cb.setEditable(True)
        self.account_cb.setIconSize(QtCore.QSize(30, 30))
        self.account_cb.setObjectName("account_cb")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/login/images/login_item_icon1.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.account_cb.addItem(icon, "")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/login/images/login_item_icon2.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.account_cb.addItem(icon1, "")
        self.gridLayout.addWidget(self.account_cb, 0, 0, 1, 2)
        self.pwd_le = QtWidgets.QLineEdit(self.widget_3)
        self.pwd_le.setMinimumSize(QtCore.QSize(0, 45))
        self.pwd_le.setStyleSheet("QLineEdit {\n"
"    font-size:20px;\n"
"    border:none;\n"
"    border-bottom:1px solid lightgray;\n"
"    background-color:transparent;\n"
"}\n"
"QLineEdit:hover {\n"
"    border-bottom:1px solid lightgray;\n"
"}\n"
"QLineEdit:focus {\n"
"    border-bottom:1px solid rgb(18,183,245);\n"
"}")
        self.pwd_le.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.pwd_le.setClearButtonEnabled(True)
        self.pwd_le.setObjectName("pwd_le")
        self.gridLayout.addWidget(self.pwd_le, 1, 0, 1, 2)
        self.auto_login_cb = QtWidgets.QCheckBox(self.widget_3)
        self.auto_login_cb.setObjectName("auto_login_cb")
        self.gridLayout.addWidget(self.auto_login_cb, 2, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.remember_pwd_cb = QtWidgets.QCheckBox(self.widget_3)
        self.remember_pwd_cb.setObjectName("remember_pwd_cb")
        self.gridLayout.addWidget(self.remember_pwd_cb, 2, 1, 1, 1, QtCore.Qt.AlignRight)
        self.login_btn = QtWidgets.QPushButton(self.widget_3)
        self.login_btn.setEnabled(False)
        self.login_btn.setMinimumSize(QtCore.QSize(0, 50))
        self.login_btn.setStyleSheet("QPushButton {\n"
"    \n"
"    background-color: rgb(33, 174, 250);\n"
"    border-radius: 8px;\n"
"    color:white;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:rgb(72,203,250);\n"
"}    \n"
"QPushButton:pressed {\n"
"    background-color:rgb(85,85,255);\n"
"}    \n"
"QPushButton:disabled {\n"
"    background-color:rgb(108, 110, 110);\n"
"}    ")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/login/images/login_btn_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.login_btn.setIcon(icon2)
        self.login_btn.setIconSize(QtCore.QSize(20, 20))
        self.login_btn.setObjectName("login_btn")
        self.gridLayout.addWidget(self.login_btn, 3, 0, 1, 2)
        self.horizontalLayout.addWidget(self.widget_3)
        self.qrcode_btn = QtWidgets.QPushButton(self.login_bottom)
        self.qrcode_btn.setMinimumSize(QtCore.QSize(80, 80))
        self.qrcode_btn.setMaximumSize(QtCore.QSize(80, 80))
        self.qrcode_btn.setStyleSheet("border-image: url(:/login/images/login_qrcode.png);")
        self.qrcode_btn.setText("")
        self.qrcode_btn.setObjectName("qrcode_btn")
        self.horizontalLayout.addWidget(self.qrcode_btn, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignBottom)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 6)
        self.horizontalLayout.setStretch(2, 2)
        self.verticalLayout.addWidget(self.login_bottom)
        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 3)

        self.retranslateUi(Form)
        self.register_btn.clicked.connect(Form.show_register_pane)
        self.qrcode_btn.clicked.connect(Form.open_qq_link)
        self.account_cb.editTextChanged['QString'].connect(Form.enable_login_btn)
        self.pwd_le.textChanged['QString'].connect(Form.enable_login_btn)
        self.login_btn.clicked.connect(Form.check_login)
        self.auto_login_cb.clicked['bool'].connect(Form.auto_login)
        self.remember_pwd_cb.clicked['bool'].connect(Form.remember_pwd)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.register_btn.setText(_translate("Form", "注册账号"))
        self.account_cb.setItemText(0, _translate("Form", "123456"))
        self.account_cb.setItemText(1, _translate("Form", "234567"))
        self.auto_login_cb.setText(_translate("Form", "自动登录"))
        self.remember_pwd_cb.setText(_translate("Form", "记住密码"))
        self.login_btn.setText(_translate("Form", "安全登录"))
import images_rc
