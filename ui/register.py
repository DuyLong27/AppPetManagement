# Form implementation generated from reading ui file 'regeister.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


import os
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox

import json
import re

class Ui_R(object):
    def setupUi(self, R):
        R.setObjectName("R")
        R.resize(337, 478)
        R.setStyleSheet("QPushButton#btnLogin{\n"
"    background-color: rgba(127, 108, 213, 0.8);\n"
"    color: rgba(197, 188, 234, 0.8);\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton#btnLogin:pressed{\n"
"    padding-left: 5px;;\n"
"    padding-top: 5px;\n"
"    padding-right: 5px;\n"
"    padding-bottom: 5px;\n"
"}\n"
"QPushButton#btnLogin:hover{\n"
"    background-color: rgba(241, 240, 247, 0.15);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(parent=R)
        self.centralwidget.setObjectName("centralwidget")
        self.login = QtWidgets.QLabel(parent=self.centralwidget)
        self.login.setGeometry(QtCore.QRect(30, 30, 281, 421))
        self.login.setStyleSheet("background-color: rgba(38, 4, 54, 0.76);\n"
"border-radius: 15px;\n"
"color:white;")
        self.login.setText("")
        self.login.setObjectName("login")
        self.btnLogin = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnLogin.setGeometry(QtCore.QRect(40, 390, 261, 31))
        self.btnLogin.setObjectName("btnLogin")
        self.txtEmail = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.txtEmail.setGeometry(QtCore.QRect(130, 240, 171, 31))
        self.txtEmail.setStyleSheet("backgroud-color: white;\n"
"")
        self.txtEmail.setObjectName("txtEmail")
        self.txtPassword = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.txtPassword.setGeometry(QtCore.QRect(130, 280, 171, 31))
        self.txtPassword.setStyleSheet("backgroud-color: white;\n"
"")
        self.txtPassword.setObjectName("txtPassword")
        self.txtRePassword = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.txtRePassword.setGeometry(QtCore.QRect(130, 320, 171, 31))
        self.txtRePassword.setStyleSheet("backgroud-color: white;\n"
"")
        self.txtRePassword.setObjectName("txtRePassword")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 240, 81, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 280, 81, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 320, 91, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 30, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("")
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(60, 90, 221, 121))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("../lesson8/lesson8/img/derry.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        R.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=R)
        self.statusbar.setObjectName("statusbar")
        R.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(parent=R)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 337, 22))
        self.menubar.setObjectName("menubar")
        R.setMenuBar(self.menubar)

        #ket noi su kien
        self.btnLogin.clicked.connect(self.xu_ly_dang_ky)

        self.retranslateUi(R)
        QtCore.QMetaObject.connectSlotsByName(R)
    #ham hien thi thong bao loi
    def thong_bao_loi(self, set_title, set_text):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setText(set_text)
        msg.setWindowTitle(set_title)
        msg.exec()
    
    def retranslateUi(self, R):
        _translate = QtCore.QCoreApplication.translate
        R.setWindowTitle(_translate("R", "MainWindow"))
        self.btnLogin.setText(_translate("R", "Đăng kí"))
        self.label.setText(_translate("R", "<html><head/><body><p align=\"center\">Email</p><p align=\"center\"><br/></p></body></html>"))
        self.label_2.setText(_translate("R", "<html><head/><body><p align=\"center\">Mật khẩu</p></body></html>"))
        self.label_3.setText(_translate("R", "<html><head/><body><p align=\"center\">Nhập lại mật khẩu</p></body></html>"))
        self.label_4.setText(_translate("R", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Đăng kí tài khoản</span></p></body></html>"))
    def xu_ly_dang_ky(self):
        email = self.txtEmail.text().strip()
        password = self.txtPassword.text().strip()
        re_password = self.txtRePassword.text().strip()
        if email == "" or password == "" or re_password == "":
            self.thong_bao_loi("Lỗi", "Vui lòng nhập đầy đủ thông tin")    
            return
        if password != re_password:
            self.thong_bao_loi("Lỗi", "Mật khẩu không trùng khớp")    
            return
        #kiem tra tinh hop le cua email
        # if self.kiem_tra_email(email) == False:
        #     self.thong_bao_loi("Lỗi", "Email không hợp lệ")    
        #     return
        #kiem tra tinh hop le cua mat khau
        if self.kiem_tra_mat_khau(password) == False:
            self.thong_bao_loi("Lỗi", "Mật khẩu phải có ít nhất 6 ký tự")    
            return
        #mo file json de kiem tai khoan da ton tai chua
        file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'account.json')
        with open(file_path, "r") as f:
            dataAccount = json.load(f)
        for i in dataAccount["accounts"]:
            if i["email"] == email:
                self.thong_bao_loi("Lỗi", "Email đã tồn tại")    
                return
        #them tai khoan moi vao file json
        file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'account.json')
        with open(file_path, "w") as f:
            dataAccount["accounts"].append({
                "email": email,
                "password": password
            })
            json.dump(dataAccount, f)
    #ham kiem tra email hop le
    def kiem_tra_email(self, email):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.fullmatch(regex, email):
                return False
        else:
                return True
    #ham kiem tra mat khau lon hon 6 ky tu
    def kiem_tra_mat_khau(self, password):
        if len(password) < 6:
                return False
        else:
                return True

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    R = QtWidgets.QMainWindow()
    ui = Ui_R()
    ui.setupUi(R)
    R.show()
    sys.exit(app.exec())
