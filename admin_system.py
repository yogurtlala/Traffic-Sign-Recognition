import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow



class Ui_AdminSystem(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_AdminSystem, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(517, 392)
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 521, 51))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(Form)
        self.textEdit_2.setGeometry(QtCore.QRect(0, 50, 191, 351))
        self.textEdit_2.setObjectName("textEdit_2")
        self.commandLinkButton_user = QtWidgets.QCommandLinkButton(Form)
        self.commandLinkButton_user.setGeometry(QtCore.QRect(0, 100, 186, 41))
        self.commandLinkButton_user.setObjectName("commandLinkButton_user")
        self.commandLinkButton_journal = QtWidgets.QCommandLinkButton(Form)
        self.commandLinkButton_journal.setGeometry(QtCore.QRect(0, 140, 186, 41))
        self.commandLinkButton_journal.setObjectName("commandLinkButton_journal")
        self.commandLinkButton_system = QtWidgets.QCommandLinkButton(Form)
        self.commandLinkButton_system.setGeometry(QtCore.QRect(0, 190, 186, 41))
        self.commandLinkButton_system.setObjectName("commandLinkButton_system")
        self.commandLinkButton_my = QtWidgets.QCommandLinkButton(Form)
        self.commandLinkButton_my.setGeometry(QtCore.QRect(0, 240, 186, 41))
        self.commandLinkButton_my.setObjectName("commandLinkButton_my")
        self.textEdit_3 = QtWidgets.QTextEdit(Form)
        self.textEdit_3.setGeometry(QtCore.QRect(190, 50, 381, 391))
        self.textEdit_3.setObjectName("textEdit_3")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(210, 70, 81, 41))
        self.label.setStyleSheet("font: 10pt \"Adobe 黑体 Std R\";")
        self.label.setObjectName("label")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(Form)
        self.dateTimeEdit.setGeometry(QtCore.QRect(250, 340, 194, 22))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.pushButton_photo = QtWidgets.QPushButton(Form)
        self.pushButton_photo.setGeometry(QtCore.QRect(310, 10, 81, 31))
        self.pushButton_photo.setObjectName("pushButton_photo")
        self.pushButton_exit = QtWidgets.QPushButton(Form)
        self.pushButton_exit.setGeometry(QtCore.QRect(400, 10, 81, 31))
        self.pushButton_exit.setObjectName("pushButton_exit")



        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)



    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">交通路标识别系统</span></p></body></html>"))
        self.commandLinkButton_user.setText(_translate("Form", "用户管理"))
        self.commandLinkButton_journal.setText(_translate("Form", "日志管理"))
        self.commandLinkButton_system.setText(_translate("Form", "系统管理"))
        self.commandLinkButton_my.setText(_translate("Form", "个人中心"))
        self.label.setText(_translate("Form", "系统管理"))
        self.pushButton_photo.setText(_translate("Form", "查询"))
        self.pushButton_exit.setText(_translate("Form", "退出"))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_AdminSystem()

    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())