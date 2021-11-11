from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog2(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1241, 841)
        Dialog.setStyleSheet("")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1241, 841))
        self.widget.setStyleSheet("QWidget#widget{\n"
                                  "background-color: qlineargradient(spread:pad, x1:0.0547264, y1:0.063, x2:1, y2:1, stop:0 rgba(80, 242, 196, 255), stop:1 rgba(117, 122, 255, 255));}")
        self.widget.setObjectName("widget")
        self.login_b = QtWidgets.QPushButton(self.widget)
        self.login_b.setGeometry(QtCore.QRect(490, 390, 271, 81))
        self.login_b.setStyleSheet("\n"
                                   "font: 14pt \"Calibri\";\n"
                                   "background-color: rgb(93, 255, 255);")
        self.login_b.setObjectName("login_b")
        self.logup_b = QtWidgets.QPushButton(self.widget)
        self.logup_b.setGeometry(QtCore.QRect(490, 550, 271, 81))
        self.logup_b.setStyleSheet("\n"
                                   "font: 14pt \"Calibri\";\n"
                                   "background-color: rgb(93, 255, 255);")
        self.logup_b.setObjectName("logup_b")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(500, 150, 251, 101))
        self.label.setStyleSheet("font: 36pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.about_b = QtWidgets.QPushButton(self.widget)
        self.about_b.setGeometry(QtCore.QRect(1080, 790, 121, 28))
        self.about_b.setStyleSheet("background-color: rgb(93, 255, 255);\n"
                                   "font: 10pt \"Calibri\";\n"
                                   "")
        self.about_b.setObjectName("about_b")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.login_b.setText(_translate("Dialog", "Войти"))
        self.logup_b.setText(_translate("Dialog", "Зарегестрироваться"))
        self.label.setText(_translate("Dialog", "Welcome"))
        self.about_b.setText(_translate("Dialog", "О приложении"))



