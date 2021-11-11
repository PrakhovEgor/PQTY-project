from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1220, 830)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1241, 841))
        self.widget.setStyleSheet("QWidget#widget{\n"
                                  "background-color: qlineargradient(spread:pad, x1:0.0547264, y1:0.063, x2:1, y2:1, stop:0 rgba(80, 242, 196, 255), stop:1 rgba(117, 122, 255, 255));}")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(320, 110, 641, 101))
        self.label.setStyleSheet("font: 36pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.loginline = QtWidgets.QLineEdit(self.widget)
        self.loginline.setGeometry(QtCore.QRect(500, 300, 251, 51))
        self.loginline.setObjectName("loginline")
        self.passwordline = QtWidgets.QLineEdit(self.widget)
        self.passwordline.setGeometry(QtCore.QRect(500, 410, 251, 51))
        self.passwordline.setObjectName("passwordline")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(500, 280, 55, 16))
        self.label_2.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(500, 380, 71, 31))
        self.label_3.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.login_b_2 = QtWidgets.QPushButton(self.widget)
        self.login_b_2.setGeometry(QtCore.QRect(540, 530, 181, 51))
        self.login_b_2.setStyleSheet("\n"
                                     "font: 14pt \"Calibri\";\n"
                                     "background-color: rgb(93, 255, 255);")
        self.login_b_2.setObjectName("login_b_2")
        self.errortext = QtWidgets.QLabel(self.widget)
        self.errortext.setGeometry(QtCore.QRect(500, 470, 251, 16))
        self.errortext.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                     "color: rgb(189, 0, 0)")
        self.errortext.setText("")
        self.errortext.setObjectName("errortext")
        self.back = QtWidgets.QPushButton(self.widget)
        self.back.setGeometry(QtCore.QRect(10, 10, 141, 31))
        self.back.setStyleSheet("\n"
                                "font: 11pt \"Calibri\";\n"
                                "background-color: rgb(93, 255, 255);")
        self.back.setObjectName("back")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Вход в учетную запись"))
        self.label_2.setText(_translate("Dialog", "Логин:"))
        self.label_3.setText(_translate("Dialog", "Пароль:"))
        self.login_b_2.setText(_translate("Dialog", "Войти"))
        self.back.setText(_translate("Dialog", "Назад"))
