from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox, QLineEdit
from CashList import Ui_CashList


class CashListWindow(QMainWindow, Ui_CashList):

    def __init__(self):
        super().__init__()
        self.setupUi(self)