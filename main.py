import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox, QLineEdit
from logIn import Ui_logIn
from mainWindow import Ui_MainWindow2
from logInClass import Frm_main
from mainWindwoClass import mainWindwoWindwo
from AgentsDebtsClass import AgentsDebtsWindow
from CashFormClass import CashFormWindow
from CashListClass import CashListWindow
from DataEntryClass import DataEntryWindow
from DebtFormClass import DebtFormWindow
from DebtListClass import DebtListWindow
from MarketingClass import MarketingWindow
from PriductMasterClass import ProductMasterWindow
from SummaryClass import SummrayWindow
from ManageListsClass import ManageListsWindow


form = None
form2 = None
form3 = None
form4 = None
form5 = None
form6 = None
form7 = None
form8 = None
form9 = None
form10 = None
form11 = None
form12 = None


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Frm_main()
    form2 = mainWindwoWindwo()
    form3 = SummrayWindow()
    form4 = ProductMasterWindow()
    form5 = ManageListsWindow()
    form6 = AgentsDebtsWindow()
    form7 = CashFormWindow()
    form8 = CashListWindow()
    form9 = DataEntryWindow()
    form10 = MarketingWindow()
    form11 = DebtListWindow()
    form12 = DebtFormWindow()
    form.set_reference(form2, form5, form10)
    form2.set_reference(form, form3, form5, form7, form9, form10, form12)
    form3.set_reference(form2)
    form5.set_reference(form2)
    form7.set_reference(form2)
    form9.set_reference(form2)
    form10.set_reference(form2)
    form12.set_reference(form2)

    sys.exit(app.exec())



