import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
import sqlite3


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
        sqlstr = 'SELECT * FROM dict'

        tablerow = 0
        results = cur.execute(sqlstr)
        self.tableWidget.setRowCount(6500)
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

    def gotomainfunc(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)


# main
app = QApplication(sys.argv)
mainwindow = MainWindow()
secwindow = SecondWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.addWidget(secwindow)
widget.setFixedHeight(850)
widget.setFixedWidth(1120)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")
