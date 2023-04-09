import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

from admin_journal import *
from administrator import *
from admin_system import *

class Ui_AdminMy(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_AdminMy, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(522, 443)
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 521, 61))
        self.textBrowser.setObjectName("textBrowser")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(0, 60, 191, 431))
        self.textEdit.setObjectName("textEdit")
        self.commandLinkButton_user = QtWidgets.QCommandLinkButton(Form)
        self.commandLinkButton_user.setGeometry(QtCore.QRect(0, 100, 186, 41))
        self.commandLinkButton_user.setObjectName("commandLinkButton_user")
        self.commandLinkButton_person = QtWidgets.QCommandLinkButton(Form)
        self.commandLinkButton_person.setGeometry(QtCore.QRect(0, 250, 186, 41))
        self.commandLinkButton_person.setObjectName("commandLinkButton_person")
        self.commandLinkButton_journal = QtWidgets.QCommandLinkButton(Form)
        self.commandLinkButton_journal.setGeometry(QtCore.QRect(0, 150, 186, 41))
        self.commandLinkButton_journal.setObjectName("commandLinkButton_journal")
        self.commandLinkButton_system = QtWidgets.QCommandLinkButton(Form)
        self.commandLinkButton_system.setGeometry(QtCore.QRect(0, 200, 186, 41))
        self.commandLinkButton_system.setObjectName("commandLinkButton_system")
        self.textEdit_2 = QtWidgets.QTextEdit(Form)
        self.textEdit_2.setGeometry(QtCore.QRect(190, 60, 351, 381))
        self.textEdit_2.setObjectName("textEdit_2")
        self.formLayoutWidget = QtWidgets.QWidget(Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(240, 120, 221, 251))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(420, 20, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(220, 80, 81, 21))
        self.label_5.setStyleSheet("font: 10pt \"Adobe 黑体 Std R\";")
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">交通路标识别系统</span></p></body></html>"))
        self.commandLinkButton_user.setText(_translate("Form", "用户管理"))
        self.commandLinkButton_person.setText(_translate("Form", "个人信息"))
        self.commandLinkButton_journal.setText(_translate("Form", "日志管理"))
        self.commandLinkButton_system.setText(_translate("Form", "系统管理"))
        self.label.setText(_translate("Form", "账号"))
        self.label_2.setText(_translate("Form", "用户名"))
        self.label_3.setText(_translate("Form", "邮箱"))
        self.label_4.setText(_translate("Form", "手机号码"))
        self.pushButton.setText(_translate("Form", "退出"))
        self.label_5.setText(_translate("Form", "个人信息"))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_AdminMy()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())