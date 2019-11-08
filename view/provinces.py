# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\pycharm_workspase\sprider_baidumap\view\provinces.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(844, 562)
        self.comboBox_city = QtWidgets.QComboBox(Form)
        self.comboBox_city.setGeometry(QtCore.QRect(120, 410, 211, 31))
        self.comboBox_city.setEditable(True)
        self.comboBox_city.setCurrentText("")
        self.comboBox_city.setIconSize(QtCore.QSize(20, 20))
        self.comboBox_city.setObjectName("comboBox_city")
        self.result = QtWidgets.QTextEdit(Form)
        self.result.setEnabled(True)
        self.result.setGeometry(QtCore.QRect(360, 60, 451, 481))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.result.setFont(font)
        self.result.setObjectName("result")
        self.okButton = QtWidgets.QPushButton(Form)
        self.okButton.setGeometry(QtCore.QRect(220, 510, 111, 31))
        self.okButton.setObjectName("okButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(360, 20, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.keyWord = QtWidgets.QLineEdit(Form)
        self.keyWord.setGeometry(QtCore.QRect(120, 460, 211, 31))
        self.keyWord.setObjectName("keyWord")

        self.host = QtWidgets.QLineEdit(Form)
        self.host.setGeometry(QtCore.QRect(120, 20, 211, 31))
        self.host.setObjectName("host")

        self.label_host = QtWidgets.QLabel(Form)
        self.label_host.setGeometry(QtCore.QRect(30, 30, 72, 15))
        self.label_host.setObjectName("label_host")
        self.label_port = QtWidgets.QLabel(Form)
        self.label_port.setGeometry(QtCore.QRect(30, 90, 72, 16))
        self.label_port.setObjectName("label_port")
        self.label_user = QtWidgets.QLabel(Form)
        self.label_user.setGeometry(QtCore.QRect(30, 150, 72, 16))
        self.label_user.setObjectName("label_user")
        self.label_passwd = QtWidgets.QLabel(Form)
        self.label_passwd.setGeometry(QtCore.QRect(30, 210, 72, 16))
        self.label_passwd.setObjectName("label_passwd")
        self.label_db = QtWidgets.QLabel(Form)
        self.label_db.setGeometry(QtCore.QRect(30, 260, 72, 16))
        self.label_db.setObjectName("label_db")
        self.label_charset = QtWidgets.QLabel(Form)
        self.label_charset.setGeometry(QtCore.QRect(30, 310, 72, 16))
        self.label_charset.setObjectName("label_charset")

        self.port = QtWidgets.QLineEdit(Form)
        self.port.setGeometry(QtCore.QRect(120, 80, 211, 31))
        self.port.setObjectName("port")

        self.user = QtWidgets.QLineEdit(Form)
        self.user.setGeometry(QtCore.QRect(120, 140, 211, 31))
        self.user.setObjectName("user")

        self.passwd = QtWidgets.QLineEdit(Form)
        self.passwd.setGeometry(QtCore.QRect(120, 200, 211, 31))
        self.passwd.setObjectName("passwd")

        self.database = QtWidgets.QLineEdit(Form)
        self.database.setGeometry(QtCore.QRect(120, 250, 211, 31))
        self.database.setObjectName("database")

        self.charset = QtWidgets.QLineEdit(Form)
        self.charset.setGeometry(QtCore.QRect(120, 300, 211, 31))
        self.charset.setObjectName("charset")

        self.table = QtWidgets.QLineEdit(Form)
        self.table.setGeometry(QtCore.QRect(120, 360, 211, 31))
        self.table.setObjectName("table")

        self.label_table = QtWidgets.QLabel(Form)
        self.label_table.setGeometry(QtCore.QRect(30, 370, 72, 16))
        self.label_table.setObjectName("label_table")
        self.label_keyword = QtWidgets.QLabel(Form)
        self.label_keyword.setGeometry(QtCore.QRect(30, 470, 72, 16))
        self.label_keyword.setObjectName("label_keyword")
        self.label_city = QtWidgets.QLabel(Form)
        self.label_city.setGeometry(QtCore.QRect(30, 420, 72, 16))
        self.label_city.setObjectName("label_city")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.okButton.setText(_translate("Form", "确定"))
        self.label.setText(_translate("Form", "查询结果："))
        self.label_host.setText(_translate("Form", "host:"))
        self.label_port.setText(_translate("Form", "port:"))
        self.label_user.setText(_translate("Form", "user:"))
        self.label_passwd.setText(_translate("Form", "passwd:"))
        self.label_db.setText(_translate("Form", "db:"))
        self.label_charset.setText(_translate("Form", "charset:"))
        self.label_table.setText(_translate("Form", "table:"))
        self.label_keyword.setText(_translate("Form", "关键字:"))
        self.label_city.setText(_translate("Form", "城市:"))
