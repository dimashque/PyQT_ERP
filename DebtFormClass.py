from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox, QLineEdit
from DebtForm import Ui_DebtForm


class DebtFormWindow(QMainWindow, Ui_DebtForm):

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
