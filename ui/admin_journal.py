import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

from administrator import *
from admin_my import *
from admin_system import *

class Ui_AdminJournal(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_AdminJournal, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(556, 400)
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 561, 51))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton_photo = QtWidgets.QPushButton(Form)
        self.pushButton_photo.setGeometry(QtCore.QRect(350, 10, 81, 31))
        self.pushButton_photo.setObjectName("pushButton_photo")
        self.pushButton_exit = QtWidgets.QPushButton(Form)
        self.pushButton_exit.setGeometry(QtCore.QRect(440, 10, 81, 31))
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(0, 50, 191, 351))
        self.textEdit.setObjectName("textEdit")
        self.commandLinkButton_user = QtWidgets.QCommandLinkButton(Form)
        self.commandLinkButton_user.setGeometry(QtCore.QRect(0, 120, 186, 41))
        self.commandLinkButton_user.setObjectName("commandLinkButton_user")
        self.commandLinkButton_journal = QtWidgets.QCommandLinkButton(Form)
        self.commandLinkButton_journal.setGeometry(QtCore.QRect(0, 170, 186, 41))
        self.commandLinkButton_journal.setObjectName("commandLinkButton_journal")
        self.commandLinkButton_system = QtWidgets.QCommandLinkButton(Form)
        self.commandLinkButton_system.setGeometry(QtCore.QRect(0, 230, 186, 41))
        self.commandLinkButton_system.setObjectName("commandLinkButton_system")
        self.commandLinkButton_my = QtWidgets.QCommandLinkButton(Form)
        self.commandLinkButton_my.setGeometry(QtCore.QRect(0, 290, 186, 41))
        self.commandLinkButton_my.setObjectName("commandLinkButton_my")
        self.label_journal = QtWidgets.QLabel(Form)
        self.label_journal.setGeometry(QtCore.QRect(220, 80, 91, 31))
        self.label_journal.setStyleSheet("font: 10pt \"Adobe 黑体 Std R\";")
        self.label_journal.setObjectName("label_journal")

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
        self.pushButton_photo.setText(_translate("Form", "查询"))
        self.pushButton_exit.setText(_translate("Form", "退出"))
        self.commandLinkButton_user.setText(_translate("Form", "用户管理"))
        self.commandLinkButton_journal.setText(_translate("Form", "日志管理"))
        self.commandLinkButton_system.setText(_translate("Form", "系统管理"))
        self.commandLinkButton_my.setText(_translate("Form", "个人信息"))
        self.label_journal.setText(_translate("Form", "日志管理"))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_AdminJournal()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())