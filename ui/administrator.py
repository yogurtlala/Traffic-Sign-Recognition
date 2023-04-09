import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

from admin_journal import *
from admin_my import *
from admin_system import *

class Ui_administrator(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_administrator, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 537)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 811, 591))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(0, 0, 811, 51))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(0, 50, 191, 511))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.button_my = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.button_my.setGeometry(QtCore.QRect(0, 250, 186, 41))
        self.button_my.setObjectName("button_my")
        self.button_user = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.button_user.setGeometry(QtCore.QRect(0, 100, 186, 41))
        self.button_user.setObjectName("button_user")
        self.button_journal = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.button_journal.setGeometry(QtCore.QRect(0, 150, 186, 41))
        self.button_journal.setObjectName("button_journal")
        self.button_system = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.button_system.setGeometry(QtCore.QRect(0, 200, 186, 41))
        self.button_system.setObjectName("button_system")
        self.pushButton_photo = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_photo.setGeometry(QtCore.QRect(440, 10, 81, 31))
        self.pushButton_photo.setStyleSheet("font: 10pt \"Adobe 黑体 Std R\";")
        self.pushButton_photo.setObjectName("pushButton_photo")
        self.pushButton_exit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_exit.setGeometry(QtCore.QRect(530, 10, 81, 31))
        self.pushButton_exit.setStyleSheet("font: 10pt \"Adobe 黑体 Std R\";")
        self.pushButton_exit.setObjectName("pushButton_exit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.button_journal.clicked.connect(self.admin_journal)
        self.button_my.clicked.connect(self.admin_my)
        self.button_system.clicked.connect(self.admin_system)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def admin_journal(self):
        ui_adminJournal.show()
        MainWindow.close()

    def admin_my(self):
        ui_adminMy.show()
        MainWindow.close()

    def admin_system(self):
        ui_adminSystem.show()
        MainWindow.close()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "交通路标识别系统"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">交通路标识别系统</span></p></body></html>"))
        self.button_my.setText(_translate("MainWindow", "个人信息"))
        self.button_user.setText(_translate("MainWindow", "用户管理"))
        self.button_journal.setText(_translate("MainWindow", "日志管理"))
        self.button_system.setText(_translate("MainWindow", "系统管理"))
        self.pushButton_photo.setText(_translate("MainWindow", "查询"))
        self.pushButton_exit.setText(_translate("MainWindow", "退出"))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_administrator()
    ui_adminJournal = Ui_AdminJournal()
    ui_adminMy = Ui_AdminMy()
    ui_adminSystem = Ui_AdminSystem()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())