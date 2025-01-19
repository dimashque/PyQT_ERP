from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox, QLineEdit
from DebtList import Ui_DebtList


class DebtListWindow(QMainWindow, Ui_DebtList):

    def __init__(self):
        super().__init__()
        self.setupUi(self)