from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox, QLineEdit
from Summary import Ui_Summary


class SummrayWindow(QMainWindow, Ui_Summary):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btnBack.clicked.connect(self.toMainmenu)
        self.form2 = None

    def toMainmenu(self):
        self.hide()
        self.form2.show()

    def set_reference(self, form2):
        self.form2 = form2
