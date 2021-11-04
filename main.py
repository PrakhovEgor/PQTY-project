import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QLabel, QLineEdit
import sqlite3
import random


class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("mainwindow.ui", self)
        self.tableWidget.setColumnWidth(0, 250)
        self.tableWidget.setColumnWidth(1, 100)
        self.tableWidget.setColumnWidth(2, 350)
        self.tableWidget.setHorizontalHeaderLabels(["Английские слова", "Транскрипция", "Перевод"])
        self.loaddata()
        self.gotolearn.clicked.connect(self.gotolearfunc)

    def gotolearfunc(self):
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def loaddata(self):
        connection = sqlite3.connect('engdata.db')
        cur = connection.cursor()
        query = 'SELECT * FROM dict'

        tablerow = 0
        results = cur.execute(query)
        self.tableWidget.setRowCount(6527)
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
        self.tableWidget2.setColumnWidth(1, 100)
        self.tableWidget2.setColumnWidth(2, 350)
        self.tableWidget2.setHorizontalHeaderLabels(["Английские слова", "Транскрипция", "Перевод"])

    def gotomainfunc(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)

    def gototestf(self):

        testwindow = TestWindow(secwindow.ids)
        widget.addWidget(testwindow)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        # if b:
        #  # global b
        # self.label_3.setText('')
        # else:
        #  self.label_3.setText('Упс... Кажется вы забыли сгенерировать и выучить слова')

    def loadwords(self):
        self.ids = []

        count = self.spinBox.text()

        for i in range(int(count)):
            a = random.randint(1, 6527)
            if not (a in self.ids):
                self.ids.append(a)
            else:
                b = random.randint(1, 6527)
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
        self.ids = a
        self.ids_back = self.ids
        super(TestWindow, self).__init__()
        loadUi('testwindow.ui', self)
        self.gotolearn2.clicked.connect(self.gotolearn2func)
        self.toans.clicked.connect(self.clc)
        self.starttest.clicked.connect(self.starttestfunc)

    def starttestfunc(self):
        self.starttest.setEnabled(False)
        self.toans.setEnabled(True)
        self.ques = []
        for j in range(len(self.ids)):
            a = random.randint(1, 2)
            self.ques.append(a)

        connection = sqlite3.connect('engdata.db')
        cur = connection.cursor()
        query = 'SELECT * FROM dict'
        results = cur.execute(query)
        k = 0
        self.flag = 1

        for row in results:
            if k in self.ids:
                self.que.setText(row[0])
                self.firstresult = row[2]
                self.firstid = 0
                for i in self.ids:
                    if k == i:
                        self.firstid = i
                break
            k += 1

    def gotolearn2func(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)
        self.flag = 0
        self.ids.clear()
        self.ans.setText('')
        self.que.setText('')
        self.ids = self.ids_back
        self.starttest.setEnabled(True)

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
                    self.ids.remove(self.firstid)
                else:
                    self.label_2.setText('Неправильно :(.\n Попробуй ещё!')





        else:
            k = 0
            if self.toans.text() == 'Следующее слово':
                for row in results:
                    if k in self.ids:
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
                    if k in self.ids:
                        if switch == 0:
                            self.answer = self.ans.text()
                            self.answer.replace(' ', '')
                            if self.answer:
                                if str(self.answer).strip().lower() in str(row[2]).split(', '):
                                    self.label_2.setText('Правильно!')
                                    self.toans.setText('Следующее слово')
                                    self.ids.remove(k)
                                    break

                                else:
                                    self.label_2.setText('Неправильно :(\n Попробуй ещё!')

                        k += 1
                    else:
                        k += 1


# main
app = QApplication(sys.argv)
mainwindow = MainWindow()
secwindow = SecondWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.addWidget(secwindow)

widget.setFixedHeight(830)
widget.setFixedWidth(1220)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")
