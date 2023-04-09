import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

from hello import *
from my import *
from TSR import *
import numpy as np

import matplotlib.pyplot as plt
import pylab
import imageio
import skimage.io
import numpy as np  
import cv2  

class Ui_Photo(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_Photo, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(498, 479)
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 511, 51))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(Form)
        self.textEdit_2.setGeometry(QtCore.QRect(0, 50, 191, 431))
        self.textEdit_2.setObjectName("textEdit_2")
        self.commandLinkButton_photo = QtWidgets.QCommandLinkButton(Form)
        self.commandLinkButton_photo.setGeometry(QtCore.QRect(0, 100, 186, 41))
        self.commandLinkButton_photo.setObjectName("commandLinkButton_photo")
        self.commandLinkButton_my = QtWidgets.QCommandLinkButton(Form)
        self.commandLinkButton_my.setGeometry(QtCore.QRect(0, 170, 186, 41))
        self.commandLinkButton_my.setObjectName("commandLinkButton_my")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(210, 80, 71, 21))
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton_collect = QtWidgets.QPushButton(Form)
        self.pushButton_collect.setGeometry(QtCore.QRect(240, 260, 81, 31))
        self.pushButton_collect.setStyleSheet("font: 10pt \"Adobe 黑体 Std R\";")
        self.pushButton_collect.setObjectName("pushButton_collect")
        self.pushButton_collect.clicked.connect(self.resultshow)

        self.pushButton_recognize = QtWidgets.QPushButton(Form)
        self.pushButton_recognize.setGeometry(QtCore.QRect(360, 260, 81, 31))
        self.pushButton_recognize.setStyleSheet("font: 10pt \"Adobe 黑体 Std R\";")
        self.pushButton_recognize.setObjectName("pushButton_recognize")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(190, 310, 311, 192))
        self.textBrowser.setObjectName("textBrowser")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(210, 340, 81, 21))
        self.label_2.setStyleSheet("font: 10pt \"Adobe 黑体 Std R\";")
        self.label_2.setObjectName("label_2")
        self.pushButton_yes = QtWidgets.QPushButton(Form)
        self.pushButton_yes.setGeometry(QtCore.QRect(240, 390, 71, 31))
        self.pushButton_yes.setStyleSheet("font: 10pt \"Adobe 黑体 Std R\";")
        self.pushButton_yes.setObjectName("pushButton_yes")
        self.pushButton_no = QtWidgets.QPushButton(Form)
        self.pushButton_no.setGeometry(QtCore.QRect(360, 390, 81, 31))
        self.pushButton_no.setStyleSheet("font: 10pt \"Adobe 黑体 Std R\";")
        self.pushButton_no.setObjectName("pushButton_no")
        self.pushButton_exit = QtWidgets.QPushButton(Form)
        self.pushButton_exit.setGeometry(QtCore.QRect(400, 10, 71, 31))
        self.pushButton_exit.setObjectName("pushButton_exit")

        self.pushButton_exit.clicked.connect(self.hello)
        self.commandLinkButton_my.clicked.connect(self.my)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    def resultshow(self):
        # get_result()
        cap = cv2.VideoCapture('output6.avi')  
        while(cap.isOpened()):  
            ret, frame = cap.read()  
            cv2.imshow('image', frame)  
            k = cv2.waitKey(20)  
            #q键退出
            if (k & 0xff == ord('q')):  
                break 
        cap.release()  
        cv2.destroyAllWindows()
    def hello(self):
        ui_hello.show()
        MainWindow.close()

    def my(self):
        ui_my.show()
        MainWindow.close()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">交通路标识别系统</span></p></body></html>"))
        self.commandLinkButton_photo.setText(_translate("Form", "开启摄像设备识别"))
        self.commandLinkButton_my.setText(_translate("Form", "个人主页"))
        self.pushButton_collect.setText(_translate("Form", "采集信息"))
        self.pushButton_recognize.setText(_translate("Form", "开始识别"))
        self.label_2.setText(_translate("Form", "识别结果"))
        self.pushButton_yes.setText(_translate("Form", "准确"))
        self.pushButton_no.setText(_translate("Form", "不准确"))
        self.pushButton_exit.setText(_translate("Form", "退出"))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_Photo()
    ui_hello = Ui_hello()
    ui_my = Ui_My()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())