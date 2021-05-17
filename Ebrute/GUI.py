import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter import *

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Ebrute(object):
    def setupUi(self, Ebrute):
        Ebrute.setObjectName("Ebrute")
        Ebrute.resize(610, 431)
        Ebrute.setWindowIcon(QtGui.QIcon('./assets/Etroll.png'))

        with open('./assets/GUI.css', 'r') as stsh:
            stylesheet = stsh.read()
            stsh.close()
        Ebrute.setStyleSheet(stylesheet)

        self.centralwidget = QtWidgets.QWidget(Ebrute)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 290, 250, 120))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 30, 220, 40))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 180, 90, 40))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton.setObjectName("pushButton")

        self.verticalLayout_2.addWidget(self.pushButton)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 57, 22))
        self.label_4.setObjectName("label_4")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(480, 380, 120, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(10, 110, 220, 40))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_4.addWidget(self.lineEdit_2)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 90, 62, 25))
        self.label_5.setObjectName("label_5")
        Ebrute.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Ebrute)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 610, 20))
        self.menubar.setObjectName("menubar")
        Ebrute.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Ebrute)
        self.statusbar.setObjectName("statusbar")
        Ebrute.setStatusBar(self.statusbar)

        self.retranslateUi(Ebrute)
        QtCore.QMetaObject.connectSlotsByName(Ebrute)

    def retranslateUi(self, Ebrute):
        _translate = QtCore.QCoreApplication.translate
        Ebrute.setWindowTitle(_translate("Ebrute", "Ebrute"))
        self.label.setText(_translate("Ebrute", "Current Password"))
        self.label_3.setText(_translate("Ebrute", "TimeElapsed"))
        self.label_2.setText(_translate("Ebrute", "Password number"))
        self.pushButton.setText(_translate("Ebrute", "Start"))
        self.label_4.setText(_translate("Ebrute", "URL"))
        self.pushButton_2.setText(_translate("Ebrute", "Password Generator"))
        self.label_5.setText(_translate("Ebrute", "Dictionary"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Ebrute = QtWidgets.QMainWindow()
    ui = Ui_Ebrute()
    ui.setupUi(Ebrute)
    Ebrute.show()
    sys.exit(app.exec_())



