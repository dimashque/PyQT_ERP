from AgentsDebts import Ui_Agents_Debts
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox, QLineEdit


class AgentsDebtsWindow(QMainWindow, Ui_Agents_Debts):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
