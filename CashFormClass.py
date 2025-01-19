from CashForm import Ui_CashForm
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox, QLineEdit

class CashFormWindow(QMainWindow, Ui_CashForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btnBack.clicked.connect(self.goBack)
        self.form2 = None

    def goBack(self):
        self.hide()
        self.form2.show()

    def set_reference(self, form2):
        self.form2 = form2
