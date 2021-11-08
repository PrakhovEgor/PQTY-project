import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QLabel, QLineEdit
import sqlite3
import random


class LockWindow(QDialog):
    def __init__(self):
        super(LockWindow, self).__init__()
        loadUi('lockwindow.ui', self)
        self.login_b.clicked.connect(self.gotologin)
        self.logup_b.clicked.connect(self.gotoreg)

    def gotologin(self):
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotoreg(self):
        widget.setCurrentIndex(widget.currentIndex() + 2)


class LoginWindow(QDialog):
    def __init__(self):
        super(LoginWindow, self).__init__()
        loadUi('loginwindow.ui', self)
        self.passwordline.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login_b_2.clicked.connect(self.loginfunc)
        self.login = self.loginline.text()

    def loginfunc(self):
        self.login = self.loginline.text()
        password = self.passwordline.text()

        if not (self.login) or not (password):
            self.errortext.setText('Заполните все поля')
        else:
            con = sqlite3.connect("engdata.db")
            cur = con.cursor()
            queryforlogin = 'SELECT login from user_base'
            cur.execute(queryforlogin)
            resultl = cur.fetchall()
            flaglogin = 0
            for i in resultl:
                if self.login == i[0]:
                    flaglogin = 1

            if flaglogin == 1:
                query = 'SELECT password FROM user_base WHERE login =\'' + self.login + "\'"
                cur.execute(query)
                result = cur.fetchone()[0]
                if result == password:
                    self.errortext.setText('')
                    mainwindow = MainWindow(self.login)
                    widget.addWidget(mainwindow)
                    widget.setCurrentIndex(widget.currentIndex() + 3)
                else:
                    self.errortext.setText('Неверный пароль')
            else:
                self.errortext.setText('Неверный логин')


class RegWindow(QDialog):
    def __init__(self):
        super(RegWindow, self).__init__()
        loadUi('registerwindow.ui', self)
        self.passwordline.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordlinecon.setEchoMode(QtWidgets.QLineEdit.Password)
        self.logup_b.clicked.connect(self.regfunc)

    def regfunc(self):
        login = self.loginline.text()
        password = self.passwordline.text()
        passwordcon = self.passwordlinecon.text()

        alfl = 'zxcvbnmlkjhgfdsaqwertyuiopйцукенгшщзхъэждлорпавыфячсмитьбю._-@1234567890ЯЧСМИТЬБЮЭЖДЛОРПАВЫФЙЦУКЕНГШЩ' \
               'ЗХЪZXCVBNMLKJHGFDSAQWERTYUIOP'
        alfp = 'zxcvbnmlkjhgfdsaqwertyuiopячсмитьбюэждлорпавыфйцукенгшщзхъЯЧСМИТЬБЮЭЖДЛОРПАВЫФЙЦУКЕНГШЩ' \
               'ЗХЪZXCVBNMLKJHGFDSAQWERTYUIOP1234567890'

        if not (login) or not (password) or not (passwordcon):
            print('оля')
            self.errortext.setText('Заполните все поля')

        else:
            print(password, passwordcon)
            if password == passwordcon:
                print('==+')
                if len(password) >= 8:
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
                        con = sqlite3.connect("engdata.db")
                        cur = con.cursor()
                        cur.execute('INSERT INTO user_base VALUES(\'%s\', \'%s\')' % (login, password))
                        con.commit()
                        widget.setCurrentIndex(widget.currentIndex() - 1)


                else:
                    print('Пароли меньше 8 символов')
                    self.errortext.setText('Пароли меньше 8 символов')


            else:
                print('Пароли не совпадают')
                self.errortext.setText('Пароли не совпадают')


class MainWindow(QDialog):
    def __init__(self, login):
        self.login = login
        super(MainWindow, self).__init__()
        loadUi("mainwindow.ui", self)
        self.tableWidget.setColumnWidth(0, 250)
        self.tableWidget.setColumnWidth(1, 150)
        self.tableWidget.setColumnWidth(2, 350)
        self.tableWidget.setHorizontalHeaderLabels(["Английские слова", "Транскрипция", "Перевод"])
        self.loaddata()
        self.gotolearn.clicked.connect(self.gotolearfunc)
        self.changeprofile.clicked.connect(self.change)
        self.profilename.setText(self.login)


    def gotolearfunc(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)

    def change(self):
        widget.setCurrentIndex(widget.currentIndex() - 2)

    def loaddata(self):
        connection = sqlite3.connect('engdata.db')
        cur = connection.cursor()
        query = 'SELECT * FROM dict'

        tablerow = 0
        results = cur.execute(query)
        self.tableWidget.setRowCount(7600)
        for row in results:
            self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            tablerow += 1


class SecondWindow(QDialog):
    def __init__(self):
        super(SecondWindow, self).__init__()
        loadUi('secwindow.ui', self)
        self.gotomain.clicked.connect(self.gotomainfunc)
        self.loadwordsbutton.clicked.connect(self.loadwords)
        self.gototest.clicked.connect(self.gototestf)
        self.tableWidget2.setColumnWidth(0, 250)
        self.tableWidget2.setColumnWidth(1, 150)
        self.tableWidget2.setColumnWidth(2, 350)
        self.tableWidget2.setHorizontalHeaderLabels(["Английские слова", "Транскрипция", "Перевод"])

    def gotomainfunc(self):
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gototestf(self):
        testwindow = TestWindow(secwindow.ids)
        widget.addWidget(testwindow)
        widget.setCurrentIndex(widget.currentIndex() + 2)
        print(self.ids)

        # if b:
        #  # global b
        # self.label_3.setText('')
        # else:
        #  self.label_3.setText('Упс... Кажется вы забыли сгенерировать и выучить слова')

    def loadwords(self):
        self.ids = []

        count = self.spinBox.text()

        for i in range(int(count)):
            a = random.randint(1, 7600)
            if not (a in self.ids):
                self.ids.append(a)
            else:
                b = random.randint(1, 7600)
                self.ids.append(b)

        connection = sqlite3.connect('engdata.db')
        cur = connection.cursor()
        query = 'SELECT * FROM dict'

        tablerow = 0
        results = cur.execute(query)
        self.tableWidget2.setRowCount(len(self.ids))
        k = 0
        for row in results:
            if int(tablerow) in self.ids:
                self.tableWidget2.setItem(k, 0, QtWidgets.QTableWidgetItem(row[0]))
                self.tableWidget2.setItem(k, 1, QtWidgets.QTableWidgetItem(row[1]))
                self.tableWidget2.setItem(k, 2, QtWidgets.QTableWidgetItem(row[2]))
                k += 1
                tablerow += 1
            else:
                tablerow += 1


class TestWindow(QDialog):
    def __init__(self, a):
        self.id = a
        super(TestWindow, self).__init__()
        loadUi('testwindow.ui', self)
        self.gotolearn2.clicked.connect(self.gotolearn2func)
        self.toans.clicked.connect(self.clc)
        self.starttest.clicked.connect(self.starttestfunc)

    def starttestfunc(self):
        self.remove_id = []
        self.starttest.setEnabled(False)
        self.toans.setEnabled(True)
        self.ques = []
        for j in range(len(self.id)):
            a = random.randint(1, 2)
            self.ques.append(a)

        connection = sqlite3.connect('engdata.db')
        cur = connection.cursor()
        query = 'SELECT * FROM dict'
        results = cur.execute(query)
        k = 0
        self.flag = 1

        for row in results:
            if k in self.id:
                self.que.setText(row[0])
                self.firstresult = row[2]
                self.firstid = 0
                for i in self.id:
                    if k == i:
                        self.firstid = i
                break
            k += 1

    def gotolearn2func(self):
        print('dfghfdh', self.remove_id)
        for i in self.remove_id:
            self.id.append(i)
            print('dfh')
            print(self.remove_id, self.id)
        if self.remove_id:
            self.remove_id.clear()

        self.flag = 0
        self.ans.setText('')
        self.que.setText('')
        self.starttest.setEnabled(True)
        self.toans.setEnabled(False)
        self.label_2.setText('')
        widget.setCurrentIndex(widget.currentIndex() - 2)

    def clc(self):
        connection = sqlite3.connect('engdata.db')
        cur = connection.cursor()
        query = 'SELECT * FROM dict'
        results = cur.execute(query)
        k = 0
        switch = 0

        if self.flag == 1:
            self.answer = self.ans.text()
            self.answer.replace(' ', '')

            if self.answer:
                if str(self.answer).strip().lower() in str(self.firstresult).split(', '):
                    self.label_2.setText('Правильность!')
                    self.toans.setText('Следующее слово')
                    self.flag = 0
                    self.remove_id.append(self.firstid)
                    print(self.firstid, self.remove_id)
                    self.id.remove(self.firstid)
                else:
                    self.label_2.setText('Неправильно :(.\n Попробуй ещё!')

        else:
            if self.id:
                k = 0
                if self.toans.text() == 'Следующее слово':
                    for row in results:
                        if k in self.id:
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
                        if k in self.id:
                            if switch == 0:
                                self.answer = self.ans.text()
                                self.answer.replace(' ', '')
                                if self.answer:
                                    if str(self.answer).strip().lower() in str(row[2]).split(', '):
                                        self.label_2.setText('Правильно!')
                                        self.toans.setText('Следующее слово')
                                        self.remove_id.append(k)
                                        print(k, self.remove_id)
                                        self.id.remove(k)
                                        break

                                    else:
                                        self.label_2.setText('Неправильно :(\n Попробуй ещё!')

                            k += 1
                        else:
                            k += 1
            else:
                self.label_2.setText('Поздравляю, Вы прошли тест!!!')
                connection = sqlite3.connect('engdata.db')
                cur = connection.cursor()
                query = 'SELECT * FROM dict'
                results = cur.execute(query)
                for row in results:
                    if k in self.id or k in self.remove_id:
                        cur.execute("INSERT INTO learn VALUES(\"%s\", \"%s\", \"%s\")" % (row[0], row[1], row[2]))
                        connection.commit()
                        print(row[0], row[1], row[2])
                    k += 1
                connection.close()


# main

app = QApplication(sys.argv)
lockscreen = LockWindow()
loginwindow = LoginWindow()
redwindow = RegWindow()

secwindow = SecondWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(lockscreen)
widget.addWidget(loginwindow)
widget.addWidget(redwindow)

widget.addWidget(secwindow)

widget.setFixedHeight(830)
widget.setFixedWidth(1220)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")
