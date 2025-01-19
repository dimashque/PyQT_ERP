from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox, QLineEdit
from ManageLists import Ui_Managelists


class ManageListsWindow(QMainWindow, Ui_Managelists):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btnBack.clicked.connect(self.toMainMenu)
        self.form2 = None

    def toMainMenu(self):
        self.hide()
        self.form2.show()

    def set_reference(self, form2):
        self.form2 = form2
