from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox, QLineEdit


from Marketing import Ui_Marketing
import cb_lists

class MarketingWindow(QMainWindow, Ui_Marketing):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.cbMarketingAgent.addItems(cb_lists.marketer)
        self.btnBack.clicked.connect(self.goBack)
        self.form2 = None

    def goBack(self):

        self.hide()
        self.form2.show()

    def set_reference(self, form2):
        self.form2 = form2