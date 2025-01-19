import sys
import datetime

from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox, QLineEdit, QComboBox

from mainWindow import Ui_MainWindow2

from sqlFunction import sqlChangePss


class mainWindwoWindwo(QMainWindow, Ui_MainWindow2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.form = None
        self.form3 = None
        self.form5 = None
        self.form7 = None
        self.form9 = None
        self.form10 = None
        self.form12 = None
        self.framenewPass.setHidden(True)
        self.btnOfficeData.clicked.connect(self.toOfficeData)
        self.btnMarketing.clicked.connect(self.toMarketing)
        self.btnAdjust.clicked.connect(self.toManageList)
        self.btnChangePassword.clicked.connect(self.ChangePass)
        self.btnDebts.clicked.connect(self.toDebtForm)
        self.btnData.clicked.connect(self.toData)
        self.btnEntry.clicked.connect(self.toDataEntry)
        self.btnKasse.clicked.connect(self.toCashForm)
        self.btnPassConfirm.clicked.connect(self.confirmPass)
        self.back.clicked.connect(self.goBack)
        self.exit.clicked.connect(self.exitProg)
        self.framenewPass.setHidden(True)
       # self.lblcurrentUser.setText(self.form.loggedUser)
        self.lbldate.setText(str(datetime.datetime.today()))
        self.table_name = ""

    def set_reference(self, form, form3, form5, form7, form9, form10, form12):
        self.form = form
        self.form3 = form3
        self.form5 = form5
        self.form7 = form7
        self.form9 = form9
        self.form12 = form12
        self.form10 = form10


    def toDebtForm(self):
        self.hide()
        self.form12.show()

    def toOfficeData(self):
         self.hide()
         self.form3.show()

    def toMarketing(self):
            self.hide()
            self.form10.show()

    def toManageList(self):
            self.hide()
            self.form5.show()

    def ChangePass(self):
            self.framenewPass.setHidden(False)
            self.inputUsername.setDisabled(True)
            print(self.table_name)

            #complete with the logic

    def toData(self):
        """ show data in DataBase"""

    def toDataEntry(self):
        self.hide()
        for widget in self.form9.findChildren(QComboBox):
            widget.setCurrentIndex(-1)
            widget.setDisabled(False)
        self.form9.show()

    def toCashForm(self):
            self.hide()
            self.form7.show()

    def goBack(self):
        self.hide()
        self.form.show()
        self.setAllBtnActive()
        self.framenewPass.setHidden(True)

    def confirmPass(self):
        username = self.form.loggedUser
        password = self.inputPass.text()
        newPass = self.inputNewPass.text()
        table = self.table_name

        if table == 'adminUsers':
            pass_changed = sqlChangePss(username, password, newPass, table)
            if pass_changed:
                QMessageBox.warning(self, "Information", 'تم تغيير كلمة المرور بنجاح')
                self.framenewPass.setHidden(True)
            else:
                QMessageBox.warning(self, "Information", 'الرجاء التحقق من كلمة المرور')

        if table == 'managerUsers':
            pass_changed = sqlChangePss(username, password, newPass, table)
            if pass_changed:
                QMessageBox.warning(self, "Information", 'تم تغيير كلمة المرور بنجاح')
                self.framenewPass.setHidden(True)
            else:
                QMessageBox.warning(self, "Information", 'الرجاء التحقق من كلمة المرور')

        if table == 'users':
            pass_changed = sqlChangePss(username, password, newPass, table)
            if pass_changed:
                QMessageBox.warning(self, "Information", 'تم تغيير كلمة المرور بنجاح')
                self.framenewPass.setHidden(True)
            else:
                QMessageBox.warning(self, "Information", 'الرجاء التحقق من كلمة المرور')

    def exitProg(self):
        sys.exit()

    def setAllBtnActive(self):

        self.btnDebts.setDisabled(False)
        self.btnData.setDisabled(False)
        self.btnAdjust.setDisabled(False)
        self.btnMarketing.setDisabled(False)
        self.btnKasse.setDisabled(False)
        self.btnOfficeData.setDisabled(False)
        self.inputUsername.clear()
        self.inputPass.clear()
        self.inputNewPass.clear()
        self.framenewPass.setHidden(True)

    def setTabelName(self, tableName):
        self.table_name = tableName
