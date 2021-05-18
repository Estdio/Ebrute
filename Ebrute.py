from src.functions.brute import Brute
from src.GUI.GUI import Ui_Ebrute

from PyQt5 import QtWidgets

import sys
app = QtWidgets.QApplication(sys.argv)
Ebrute = QtWidgets.QMainWindow()
ui = Ui_Ebrute()
ui.setupUi(Ebrute)
Ebrute.show()
sys.exit(app.exec_())