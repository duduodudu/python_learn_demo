# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
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
        Form.setStyleSheet("QWidget#Form{\n"
"    border-image: url(:/register/images/register_background.jpg);\n"
"}\n"
"QPushButton {\n"
"    color:white;\n"
"        \n"
"    background-color: rgb(144, 255, 231);\n"
"    border:2px solid rgb(21, 152, 249);\n"
"    border-radius:200px;\n"
"}\n"
"QPushButton:hover {\n"
"    border:4px double rgb(247, 252, 250);\n"
"}\n"
"QPushButton:checked {\n"
"    background-color: rgb(195, 255, 104);\n"
"}")
        self.main_menue_btn = QtWidgets.QPushButton(Form)
        self.main_menue_btn.setGeometry(QtCore.QRect(10, 10, 40, 40))
        self.main_menue_btn.setStyleSheet("border-radius:20px;\n"
"background-color: rgb(144, 180, 5);\n"
"font: 13pt \"Baoli SC\";")
        self.main_menue_btn.setCheckable(True)
        self.main_menue_btn.setObjectName("main_menue_btn")
        self.exit_menue_btn = QtWidgets.QPushButton(Form)
        self.exit_menue_btn.setGeometry(QtCore.QRect(10, 70, 40, 40))
        self.exit_menue_btn.setStyleSheet("border-radius:20px;\n"
"background-color: rgb(144, 180, 5);\n"
"font: 13pt \"Baoli SC\";")
        self.exit_menue_btn.setObjectName("exit_menue_btn")
        self.reset_menue_btn = QtWidgets.QPushButton(Form)
        self.reset_menue_btn.setGeometry(QtCore.QRect(60, 60, 40, 40))
        self.reset_menue_btn.setStyleSheet("border-radius:20px;\n"
"background-color: rgb(144, 180, 5);\n"
"font: 13pt \"Baoli SC\";")
        self.reset_menue_btn.setObjectName("reset_menue_btn")
        self.about_menue_btn = QtWidgets.QPushButton(Form)
        self.about_menue_btn.setGeometry(QtCore.QRect(80, 10, 40, 40))
        self.about_menue_btn.setStyleSheet("border-radius:20px;\n"
"background-color: rgb(144, 180, 5);\n"
"font: 13pt \"Baoli SC\";")
        self.about_menue_btn.setObjectName("about_menue_btn")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(170, 200, 191, 212))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setHorizontalSpacing(7)
        self.formLayout.setVerticalSpacing(20)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setStyleSheet("color: rgb(154, 255, 240);")
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.account_le = QtWidgets.QLineEdit(self.layoutWidget)
        self.account_le.setMinimumSize(QtCore.QSize(0, 35))
        self.account_le.setStyleSheet("background-color: transparent;\n"
"color: rgb(255, 255, 255);\n"
"border:none;\n"
"border-bottom:1px solid lightgray;")
        self.account_le.setText("")
        self.account_le.setClearButtonEnabled(True)
        self.account_le.setObjectName("account_le")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.account_le)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setStyleSheet("color: rgb(154, 255, 240);")
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.password_le = QtWidgets.QLineEdit(self.layoutWidget)
        self.password_le.setMinimumSize(QtCore.QSize(0, 35))
        self.password_le.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color: transparent;\n"
"border:none;\n"
"border-bottom:1px solid lightgray;")
        self.password_le.setText("")
        self.password_le.setClearButtonEnabled(True)
        self.password_le.setObjectName("password_le")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.password_le)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setStyleSheet("color: rgb(154, 255, 240);")
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.confirm_le = QtWidgets.QLineEdit(self.layoutWidget)
        self.confirm_le.setMinimumSize(QtCore.QSize(0, 35))
        self.confirm_le.setStyleSheet("background-color: transparent;\n"
"color: rgb(255, 255, 255);\n"
"border:none;\n"
"border-bottom:1px solid lightgray;")
        self.confirm_le.setText("")
        self.confirm_le.setClearButtonEnabled(True)
        self.confirm_le.setObjectName("confirm_le")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.confirm_le)
        self.register_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.register_btn.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.register_btn.sizePolicy().hasHeightForWidth())
        self.register_btn.setSizePolicy(sizePolicy)
        self.register_btn.setMinimumSize(QtCore.QSize(0, 45))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.register_btn.setFont(font)
        self.register_btn.setStyleSheet("QPushButton {\n"
"    background-color: transparent;\n"
"color:white;\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(111, 255, 72);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color:rgb(254, 172, 66);\n"
"}\n"
"QPushButton:disabled {\n"
"    background-color:rgb(178, 182, 182);\n"
"}")
        self.register_btn.setObjectName("register_btn")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.register_btn)
        self.exit_menue_btn.raise_()
        self.reset_menue_btn.raise_()
        self.about_menue_btn.raise_()
        self.layoutWidget.raise_()
        self.main_menue_btn.raise_()

        self.retranslateUi(Form)
        self.main_menue_btn.clicked['bool'].connect(Form.show_hide_menue)
        self.about_menue_btn.clicked.connect(Form.about_lk)
        self.reset_menue_btn.clicked.connect(Form.reset)
        self.exit_menue_btn.clicked.connect(Form.exit_pane)
        self.register_btn.clicked.connect(Form.check_register)
        self.account_le.textChanged['QString'].connect(Form.enable_register_btn)
        self.password_le.textChanged['QString'].connect(Form.enable_register_btn)
        self.confirm_le.textChanged['QString'].connect(Form.enable_register_btn)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.main_menue_btn.setText(_translate("Form", "菜单"))
        self.exit_menue_btn.setText(_translate("Form", "退出"))
        self.reset_menue_btn.setText(_translate("Form", "重置"))
        self.about_menue_btn.setText(_translate("Form", "关于"))
        self.label.setText(_translate("Form", "账    号:"))
        self.label_2.setText(_translate("Form", "密     码:"))
        self.label_3.setText(_translate("Form", "确认密码:"))
        self.register_btn.setText(_translate("Form", "注册"))
import images_rc
