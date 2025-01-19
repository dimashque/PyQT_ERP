from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox, QLineEdit
from ProductMaster import Ui_ProductMaster

class ProductMasterWindow(QMainWindow, Ui_ProductMaster):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
