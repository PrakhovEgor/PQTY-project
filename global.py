import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
import sqlite3
import random
from ui_login import Ui_Dialog
from ui_lock import Ui_Dialog2
from ui_reg import Ui_Dialog3
from ui_main import Ui_Dialog4
from ui_sec import Ui_Dialog5
from ui_test import Ui_Dialog6
from ui_about import Ui_Dialog7
from ui_know import Ui_Dialog8

ids = []
login = ''


class LockWindow(QDialog, Ui_Dialog2):
    def __init__(self):
        super(LockWindow, self).__init__()
        self.setupUi(self)
        self.widget.setWindowTitle('Engkish')
        self.login_b.clicked.connect(self.gotologin)
        self.logup_b.clicked.connect(self.gotoreg)
        self.about_b.clicked.connect(self.aboutf)

    def gotologin(self):
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def aboutf(self):
        widget.setCurrentIndex(widget.currentIndex() + 6)

    def gotoreg(self):
        widget.setCurrentIndex(widget.currentIndex() + 2)


class LoginWindow(QDialog, Ui_Dialog):
    def __init__(self):
        global login
        super(LoginWindow, self).__init__()
        self.setupUi(self)
        self.passwordline.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login_b_2.clicked.connect(self.loginfunc)

        self.back.clicked.connect(self.backf)

    def backf(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)

    def loginfunc(self):
        global login
        login = self.loginline.text()
        password = self.passwordline.text()

        if not (login) or not (password):
            self.errortext.setText('Заполните все поля')
        else:
            con = sqlite3.connect("engdata.db")
            cur = con.cursor()
            queryforlogin = 'SELECT login from user_base'
            cur.execute(queryforlogin)
            resultl = cur.fetchall()
            flaglogin = 0
            for i in resultl:
                if login.strip() == i[0]:
                    flaglogin = 1

            if flaglogin == 1:
                query = 'SELECT password FROM user_base WHERE login =\'' + login.strip() + "\'"
                cur.execute(query)
                result = cur.fetchone()[0]
                if result == password.strip():
                    self.errortext.setText('')
                    widget.setCurrentIndex(widget.currentIndex() + 2)
                else:
                    self.errortext.setText('Неверный пароль')
            else:
                self.errortext.setText('Неверный логин')


class RegWindow(QDialog, Ui_Dialog3):
    def __init__(self):
        super(RegWindow, self).__init__()
        self.setupUi(self)
        self.passwordline.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordlinecon.setEchoMode(QtWidgets.QLineEdit.Password)
        self.logup_b.clicked.connect(self.regfunc)
        self.back.clicked.connect(self.backf)

    def backf(self):
        widget.setCurrentIndex(widget.currentIndex() - 2)

    def regfunc(self):
        login = str(self.loginline.text())
        password = str(self.passwordline.text())
        passwordcon = str(self.passwordlinecon.text())

        alfl = 'zxcvbnmlkjhgfdsaqwertyuiopйцукенгшщзхъэждлорпавыфячсмитьбю._-@1234567890ЯЧСМИТЬБЮЭЖДЛОРПАВЫФЙЦУКЕНГШЩ' \
               'ЗХЪZXCVBNMLKJHGFDSAQWERTYUIOP'
        alfp = 'zxcvbnmlkjhgfdsaqwertyuiopячсмитьбюэждлорпавыфйцукенгшщзхъЯЧСМИТЬБЮЭЖДЛОРПАВЫФЙЦУКЕНГШЩ' \
               'ЗХЪZXCVBNMLKJHGFDSAQWERTYUIOP1234567890'

        if not (login) or not (password) or not (passwordcon):
            self.errortext.setText('Заполните все поля')

        else:
            if password == passwordcon:
                if len(password) >= 4:
                    flagl = 1
                    flagp = 1
                    for i in login:
                        if i not in alfl:
                            flagl = 0
                            break

                    for i in password:
                        if i not in alfp:
                            flagp = 0
                            break
                    if flagl == 0 and flagp == 0:
                        self.errortext.setText('Недопустимиый формат логина и пароля')
                    elif flagp == 0:

                        self.errortext.setText('Недопустимиый формат пароля')


                    elif flagl == 0:
                        self.errortext.setText('Недопустимиый формат логина')
                    else:
                        if password.isdigit():
                            self.errortext.setText('Пароль не может содержать только цифры')
                        else:
                            flaglog = 1
                            con = sqlite3.connect("engdata.db")
                            cur = con.cursor()
                            query = 'SELECT login FROM user_base'
                            cur.execute(query)
                            result = cur.fetchall()
                            for i in result:
                                print(i, str(login))
                                if i[0] == str(login):
                                    flaglog = 0
                            if flaglog == 1:
                                cur.execute(
                                    'INSERT INTO user_base VALUES(\"%s\", \"%s\")' % (
                                        login.strip(), password.strip()))
                                con.commit()
                                widget.setCurrentIndex(widget.currentIndex() - 1)
                            else:
                                self.errortext.setText('Пользователь с данным логином уже зарегестрирован')




                else:
                    print('Пароли меньше 8 символов')
                    self.errortext.setText('Пароли меньше 8 символов')


            else:
                print('Пароли не совпадают')
                self.errortext.setText('Пароли не совпадают')


class MainWindow(QDialog, Ui_Dialog4):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.tableWidget.setColumnWidth(0, 250)
        self.tableWidget.setColumnWidth(1, 150)
        self.tableWidget.setColumnWidth(2, 350)
        self.tableWidget.setHorizontalHeaderLabels(["Английские слова", "Транскрипция", "Перевод"])
        self.loaddata()
        self.gotolearn.clicked.connect(self.gotolearfunc)
        self.changeprofile.clicked.connect(self.change)
        self.gotorem.clicked.connect(self.gotoremf)

    def gotoremf(self):
        widget.setCurrentIndex(widget.currentIndex() + 4)

    def gotolearfunc(self):
        global login
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def change(self):
        widget.setCurrentIndex(widget.currentIndex() - 3)

    def loaddata(self):
        connection = sqlite3.connect('engdata.db')
        cur = connection.cursor()
        query = 'SELECT * FROM dict'
        tablerow = 0
        results = cur.execute(query)
        self.tableWidget.setRowCount(7594)
        for row in results:
            self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            tablerow += 1


class SecondWindow(QDialog, Ui_Dialog5):
    def __init__(self):
        super(SecondWindow, self).__init__()
        self.setupUi(self)
        self.gotomain.clicked.connect(self.gotomainfunc)
        self.loadwordsbutton.clicked.connect(self.loadwords)
        self.gototest.clicked.connect(self.gototestf)
        self.tableWidget2.setColumnWidth(0, 250)
        self.tableWidget2.setColumnWidth(1, 150)
        self.tableWidget2.setColumnWidth(2, 350)
        self.tableWidget2.setHorizontalHeaderLabels(["Английские слова", "Транскрипция", "Перевод"])

    def gotomainfunc(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)

    def gototestf(self):
        global ids
        if ids:
            self.label_3.setText('')
            widget.setCurrentIndex(widget.currentIndex() + 1)
        else:
            self.label_3.setText('Упс... Кажется вы забыли сгенерировать и выучить слова')

    def loadwords(self):
        global ids
        ids = []
        count = self.spinBox.text()

        for i in range(int(count)):
            a = random.randint(1, 7600)
            if not (a in ids):
                ids.append(a)
            else:
                b = random.randint(1, 7600)
                ids.append(b)

        connection = sqlite3.connect('engdata.db')
        cur = connection.cursor()
        query = 'SELECT * FROM dict'

        tablerow = 0
        results = cur.execute(query)
        self.tableWidget2.setRowCount(len(ids))
        k = 0
        for row in results:
            if int(tablerow) in ids:
                self.tableWidget2.setItem(k, 0, QtWidgets.QTableWidgetItem(row[0]))
                self.tableWidget2.setItem(k, 1, QtWidgets.QTableWidgetItem(row[1]))
                self.tableWidget2.setItem(k, 2, QtWidgets.QTableWidgetItem(row[2]))
                k += 1
                tablerow += 1
            else:
                tablerow += 1


class TestWindow(QDialog, Ui_Dialog6):
    def __init__(self):
        super(TestWindow, self).__init__()
        self.setupUi(self)
        self.gotolearn2.clicked.connect(self.gotolearn2func)
        self.toans.clicked.connect(self.clc)
        self.starttest.clicked.connect(self.starttestfunc)

    def starttestfunc(self):
        global ids

        self.remove_id = []
        self.starttest.setEnabled(False)
        self.toans.setEnabled(True)
        connection = sqlite3.connect('engdata.db')
        cur = connection.cursor()
        query = 'SELECT * FROM dict'
        results = cur.execute(query)
        k = 0
        self.flag = 1

        for row in results:
            if k in ids:
                self.que.setText(row[0])
                self.firstresult = row[2]
                self.firstid = 0
                for i in ids:
                    if k == i:
                        self.firstid = i
                break
            k += 1

    def gotolearn2func(self):
        global ids
        try:
            for i in self.remove_id:
                ids.append(i)
            if self.remove_id:
                self.remove_id.clear()
            self.flag = 0
            self.ans.setText('')
            self.que.setText('')
            self.starttest.setEnabled(True)
            self.toans.setEnabled(False)
            self.label_2.setText('')
            widget.setCurrentIndex(widget.currentIndex() - 1)
        except:
            self.flag = 0
            self.ans.setText('')
            self.que.setText('')
            self.starttest.setEnabled(True)
            self.toans.setEnabled(False)
            self.label_2.setText('')
            widget.setCurrentIndex(widget.currentIndex() - 1)

    def clc(self):
        global ids
        global login
        connection = sqlite3.connect('engdata.db')
        cur = connection.cursor()
        query = 'SELECT * FROM dict'
        results = cur.execute(query)
        switch = 0
        if self.flag == 1:
            self.answer = self.ans.text()
            self.answer.replace(' ', '')

            if self.answer:
                if str(self.answer).strip().lower() in str(self.firstresult).split(', '):
                    self.label_2.setText('Правильно!')
                    self.toans.setText('Следующее слово')
                    self.flag = 0
                    self.remove_id.append(self.firstid)
                    ids.remove(self.firstid)
                else:
                    self.label_2.setText('Неправильно :(.\n Попробуй ещё!')

        else:
            if ids:
                k = 0
                if self.toans.text() == 'Следующее слово':
                    for row in results:
                        if k in ids:
                            if switch == 0:
                                self.que.setText(row[0])
                                self.ans.setText('')
                                self.toans.setText('Ответить')
                                self.label_2.setText('')
                                break
                            k += 1
                        else:
                            k += 1


                else:
                    k = 0
                    for row in results:
                        if k in ids:
                            if switch == 0:
                                self.answer = self.ans.text()
                                self.answer.replace(' ', '')
                                if self.answer:
                                    if str(self.answer).strip().lower() in str(row[2]).split(', '):
                                        self.label_2.setText('Правильно!')
                                        self.toans.setText('Следующее слово')
                                        self.remove_id.append(k)
                                        ids.remove(k)
                                        break

                                    else:
                                        self.label_2.setText('Неправильно :(\n Попробуй ещё!')

                            k += 1
                        else:
                            k += 1
            else:
                k = 0
                self.label_2.setText('Поздравляю, Вы прошли тест!!!')
                connection = sqlite3.connect('engdata.db')
                cur = connection.cursor()
                query = 'SELECT * FROM dict'
                results = cur.execute(query)
                for row in results:
                    if k in ids or k in self.remove_id:
                        cur.execute("INSERT INTO learn VALUES(\"%s\", \"%s\", \"%s\", \"%s\")" % (
                            login, row[0], row[1], row[2]))
                        connection.commit()
                    k += 1
                connection.close()
                self.toans.setEnabled(False)


class About(QDialog, Ui_Dialog7):
    def __init__(self):
        super(About, self).__init__()
        self.setupUi(self)
        self.back.clicked.connect(self.backf)
        self.label_2.setStyleSheet("QLabel{{border-image: url({});}}".format('qw.jpg'))

    def backf(self):
        widget.setCurrentIndex(widget.currentIndex() - 6)


class Remember(QDialog, Ui_Dialog8):
    def __init__(self):
        super(Remember, self).__init__()
        self.setupUi(self)
        self.gotomain.clicked.connect(self.gotomainf)
        self.tableWidget.setColumnWidth(0, 250)
        self.tableWidget.setColumnWidth(1, 150)
        self.tableWidget.setColumnWidth(2, 350)
        self.tableWidget.setHorizontalHeaderLabels(["Английские слова", "Транскрипция", "Перевод"])
        self.updateb.clicked.connect(self.loaddata)

    def gotomainf(self):
        widget.setCurrentIndex(widget.currentIndex() - 4)

    def loaddata(self):
        global login
        self.tableWidget.setRowCount(0)
        connection = sqlite3.connect('engdata.db')
        cur = connection.cursor()
        query = 'SELECT * FROM learn'
        results = cur.execute(query)
        tablerow = 0
        a = ''
        for row in results:
            if row[0] == login:
                if not (a):
                    r = self.tableWidget.rowCount()
                    self.tableWidget.insertRow(r)
                    self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[1]))
                    self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[2]))
                    self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[3]))
                    tablerow += 1
                    a = row[1]
                else:
                    b = row[1]
                    if a == b:
                        continue
                    else:
                        r = self.tableWidget.rowCount()
                        self.tableWidget.insertRow(r)
                        self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[1]))
                        self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[2]))
                        self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[3]))
                        tablerow += 1
                        a = row[1]


# main
app = QApplication(sys.argv)
lockscreen = LockWindow()
redwindow = RegWindow()
loginwindow = LoginWindow()
mainwindow = MainWindow()
secwindow = SecondWindow()
testwindow = TestWindow()
about = About()
rem = Remember()
widget = QtWidgets.QStackedWidget()
widget.addWidget(lockscreen)
widget.addWidget(loginwindow)
widget.addWidget(redwindow)
widget.addWidget(mainwindow)
widget.addWidget(secwindow)
widget.addWidget(testwindow)
widget.addWidget(about)
widget.addWidget(rem)
widget.setFixedHeight(830)
widget.setFixedWidth(1220)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")
