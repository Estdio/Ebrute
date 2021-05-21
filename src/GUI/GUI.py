from src.functions.brute import Brute
from src.functions.passwordgenerator import PasswordGenerator

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRunnable, Qt, QThreadPool

class Ui_PasswordGen(object):
    def setupUi(self, PasGenG):
        PasGenG.setObjectName("PasGenG")
        PasGenG.resize(400, 600)
        PasGenG.setWindowIcon(QtGui.QIcon('./assets/Etroll.png'))

        with open('./assets/GUI.css', 'r') as stsh:
            stylesheet = stsh.read()
            stsh.close()
        PasGenG.setStyleSheet(stylesheet)

        self.centralwidget = QtWidgets.QWidget(PasGenG)


        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 50, 300, 500))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        self.pswentrybox = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.pswentrybox.setContentsMargins(0, 0, 0, 0)
        self.pswentrybox.setObjectName("pswentrybox")

        self.pswentry1 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.pswentry1.setObjectName("pswentry1")
        self.pswentrybox.addWidget(self.pswentry1)

        self.pswentry2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.pswentry2.setObjectName("pswentry2")
        self.pswentrybox.addWidget(self.pswentry2)

        self.pswentry3 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.pswentry3.setObjectName("pswentry3")
        self.pswentrybox.addWidget(self.pswentry3)

        self.pswentry4 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.pswentry4.setObjectName("pswentry4")
        self.pswentrybox.addWidget(self.pswentry4)

        self.pswentry5 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.pswentry5.setObjectName("pswentry5")
        self.pswentrybox.addWidget(self.pswentry5)

        self.pswentry6 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.pswentry6.setObjectName("pswentry6")
        self.pswentrybox.addWidget(self.pswentry6)

        self.pswentry7 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.pswentry7.setObjectName("pswentry7")
        self.pswentrybox.addWidget(self.pswentry7)

        self.pswentry8 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.pswentry8.setObjectName("pswentry8")
        self.pswentrybox.addWidget(self.pswentry8)

        self.pswentry9 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.pswentry9.setObjectName("pswentry9")
        self.pswentrybox.addWidget(self.pswentry9)

        self.pswentry10 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.pswentry10.setObjectName("pswentry10")
        self.pswentrybox.addWidget(self.pswentry10)

        self.pswentry11 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.pswentry11.setObjectName("pswentry11")
        self.pswentrybox.addWidget(self.pswentry11)

        self.pswpushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pswpushButton.setObjectName("pswpushButton")
        self.pswentrybox.addWidget(self.pswpushButton)

        PasGenG.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PasGenG)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 610, 20))
        self.menubar.setObjectName("menubar")
        PasGenG.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(PasGenG)
        self.statusbar.setObjectName("statusbar")
        PasGenG.setStatusBar(self.statusbar)

        self.retranslateUi(PasGenG)
        QtCore.QMetaObject.connectSlotsByName(PasGenG)

    def retranslateUi(self, PasGenG):
        _translate = QtCore.QCoreApplication.translate
        PasGenG.setWindowTitle(_translate("PasGenG", "Password Generator"))

        self.pswpushButton.setText(_translate("PasGenG", "Generate"))
        self.pswpushButton.clicked.connect(self.generate)

    def generate(self):
        pswcontent1 = self.pswentry1.text()
        pswcontent2 = self.pswentry2.text()
        pswcontent3 = self.pswentry3.text()
        pswcontent4 = self.pswentry4.text()
        pswcontent5 = self.pswentry5.text()
        pswcontent6 = self.pswentry6.text()
        pswcontent7 = self.pswentry7.text()
        pswcontent8 = self.pswentry8.text()
        pswcontent9 = self.pswentry9.text()
        pswcontent10 = self.pswentry10.text()
        pswcontent11 = self.pswentry11.text()

        concatpasscontent = (pswcontent1 + "|" +
                             pswcontent2 + "|" +
                             pswcontent3 + "|" +
                             pswcontent4 + "|" +
                             pswcontent5 + "|" +
                             pswcontent6 + "|" +
                             pswcontent7 + "|" +
                             pswcontent8 + "|" +
                             pswcontent9 + "|" +
                             pswcontent10 + "|" +
                             pswcontent11 + "|")

        passgen = PasswordGenerator(concatpasscontent)
        print(concatpasscontent)
        passgen.product('output')


class Ui_Ebrute(object):
    def __init__(self):
        self.brteclass = Brute()
        self.brteclass.currentpswd = ''
    def openPswGen(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_PasswordGen()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, Ebrute):
        Ebrute.setObjectName("Ebrute")
        Ebrute.resize(610, 431)
        Ebrute.setWindowIcon(QtGui.QIcon('./assets/Etroll.png'))

        self.currentpswd = ''

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

        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)

        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)

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
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 220, 90, 40))
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
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(10, 95, 220, 40))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_4.addWidget(self.lineEdit_2)

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 75, 62, 25))
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 135, 64, 22))
        self.label_6.setObjectName("label_6")

        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 163, 220, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")

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

        self.pushButton.setText(_translate("Ebrute", "Start"))
        self.pushButton.clicked.connect(self.initiateEbrute)

        self.label_4.setText(_translate("Ebrute", "URL"))

        self.pushButton_2.setText(_translate("Ebrute", "Password Generator"))
        self.pushButton_2.clicked.connect(self.openPswGen)

        self.label_3.setText(_translate("Ebrute", "TimeElapsed"))
        self.label.setText(_translate("Ebrute", "Current Password"))
        self.label_2.setText(_translate("Ebrute", "Password number"))
        self.label_5.setText(_translate("Ebrute", "Dictionary"))
        self.label_6.setText(_translate("Ebrute", "Username"))

    def initiateEbrute(self):
        _url = self.lineEdit.text()
        _dictionary = self.lineEdit_2.text()
        _username = self.lineEdit_3.text()
        self.brteclass.set_url(_url)
        self.brteclass.set_dictionary(_dictionary)
        self.brteclass.start_Ebrute(_username)




