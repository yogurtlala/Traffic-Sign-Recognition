import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

from administrator import *
from photo import *



class Ui_hello(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_hello, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(240, 50, 271, 371))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setObjectName("textBrowser")
        self.label_welcome = QtWidgets.QLabel(self.centralwidget)
        self.label_welcome.setGeometry(QtCore.QRect(340, 80, 111, 41))
        self.label_welcome.setStyleSheet("font: 18pt \"微软雅黑\";")
        self.label_welcome.setObjectName("label_welcome")
        self.label_please = QtWidgets.QLabel(self.centralwidget)
        self.label_please.setGeometry(QtCore.QRect(350, 130, 131, 16))
        self.label_please.setStyleSheet("font: 8pt \"宋体\";")
        self.label_please.setObjectName("label_please")
        self.label_user = QtWidgets.QLabel(self.centralwidget)
        self.label_user.setGeometry(QtCore.QRect(270, 170, 71, 21))
        self.label_user.setStyleSheet("font: 25 10pt \"等线 Light\";")
        self.label_user.setObjectName("label_user")
        self.label_password = QtWidgets.QLabel(self.centralwidget)
        self.label_password.setGeometry(QtCore.QRect(270, 210, 71, 16))
        self.label_password.setStyleSheet("font: 25 10pt \"等线 Light\";")
        self.label_password.setObjectName("label_password")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(352, 170, 131, 21))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(352, 210, 131, 20))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.button_user = QtWidgets.QRadioButton(self.centralwidget)
        self.button_user.setGeometry(QtCore.QRect(330, 255, 151, 21))
        self.button_user.setStyleSheet("font: 25 10pt \"Adobe 宋体 Std L\";")
        self.button_user.setObjectName("button_user")
        self.button_admin = QtWidgets.QRadioButton(self.centralwidget)
        self.button_admin.setGeometry(QtCore.QRect(330, 290, 171, 21))
        self.button_admin.setStyleSheet("font: 25 10pt \"Adobe 宋体 Std L\";")
        self.button_admin.setObjectName("button_admin")
        self.pushButton_login = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_login.setGeometry(QtCore.QRect(340, 330, 75, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_login.sizePolicy().hasHeightForWidth())
        self.pushButton_login.setSizePolicy(sizePolicy)
        self.pushButton_login.setStyleSheet("QPushButton { background-color: rgb(54, 85, 211); border-radius: 3px; color: rgb(255, 255, 255); } QPushButton:hover { background-color: rgb(37, 73, 217); }")
        self.pushButton_login.setObjectName("pushButton_login")
        self.pushButton_new = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_new.setGeometry(QtCore.QRect(340, 370, 75, 23))
        self.pushButton_new.setStyleSheet("QPushButton { background-color: rgb(191, 196, 213); border-radius: 3px; color: rgb(0, 0, 0); }")
        self.pushButton_new.setObjectName("pushButton_new")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.pushButton_login.clicked.connect(self.administrator)
        self.pushButton_new.clicked.connect(self.photo)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def administrator(self):
        ui_administrator.show()
        MainWindow.close()

    def photo(self):
        ui_photo.show()
        MainWindow.close()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_welcome.setText(_translate("MainWindow", "欢迎"))
        self.label_please.setText(_translate("MainWindow", "登录你的账号"))
        self.label_user.setText(_translate("MainWindow", "用户名"))
        self.label_password.setText(_translate("MainWindow", "密码"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "请输入用户名"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "请输入密码"))
        self.button_user.setText(_translate("MainWindow", "我是用户"))
        self.button_admin.setText(_translate("MainWindow", "我是管理员"))
        self.pushButton_login.setText(_translate("MainWindow", "登录"))
        self.pushButton_new.setText(_translate("MainWindow", "注册"))

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_hello()
    ui_administrator = Ui_administrator()
    ui_photo = Ui_Photo()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())