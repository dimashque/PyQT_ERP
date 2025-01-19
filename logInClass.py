import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox, QLineEdit
from logIn import Ui_logIn
from mainWindow import Ui_MainWindow2

from sqlFunction import sqlLogin


class Frm_main(QMainWindow, Ui_logIn):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.inputPassword.setEchoMode(QLineEdit.Password)

        self.btnExit.clicked.connect(self.exitprog)
        self.go.clicked.connect(self.openMainWindow)


        self.show()
        self.userName = 1234
        self.password = 1234
        self.form2 = None
        self.form10 = None
        self.form5 = None
        self.loggedUser = ""

    def set_reference(self, form2, form5, form10):
        self.form2 = form2
        self.form10 = form10
        self.form5 = form5





    def openMainWindow(self):

        try:
            user = str(self.inputUserName.text())
            pass_w = str(self.inputPassword.text())


            if self.rdbAdmin.isChecked():


                passSQL = sqlLogin(user, 'adminUsers')

                if pass_w == passSQL:
                    self.loggedUser = user
                    # print(user)
                    self.form2.show()
                    self.hide()
                    self.form2.setTabelName('adminUsers')

                    self.inputPassword.clear()
                    self.inputUserName.clear()
                else:
                    QMessageBox.warning(self, "Warning", "كلمة المرور خاطئة، يرجى المحاولة مرة أخرى!")

            elif self.rdbManager.isChecked():

                passSQL = sqlLogin(user, 'managerUsers')

                if pass_w == passSQL:
                    self.loggedUser = user
                    # print(user)
                    self.hide()
                    self.form2.show()
                    self.form2.setTabelName('managerUsers')
                    self.form10.btnPay.setDisabled(True)
                    self.form10.btnClose.setDisabled(True)
                    self.form2.btnKasse.setDisabled(True)
                    self.form2.btnDebts.setDisabled(True)
                    self.form5.rdbUsers.setDisabled(True)

                    self.inputPassword.clear()
                    self.inputUserName.clear()

                else:
                    QMessageBox.warning(self, "Warning", "كلمة المرور خاطئة، يرجى المحاولة مرة أخرى!")

            else:


                passSQL = sqlLogin(user, 'users')

                if pass_w == passSQL:
                    self.loggedUser = user
                    self.hide()
                    # print(user)

                    self.form2.show()
                    self.form2.btnKasse.setDisabled(True)
                    self.form2.btnDebts.setDisabled(True)
                    self.form2.btnOfficeData.setDisabled(True)
                    self.form2.btnAdjust.setDisabled(True)
                    self.form2.btnData.setDisabled(True)
                    self.form2.btnKasse.setDisabled(True)
                    self.form2.btnMarketing.setDisabled(True)
                    self.form2.setTabelName('users')



                    self.inputPassword.clear()
                    self.inputUserName.clear()

                else:
                    QMessageBox.warning(self, "Warning", "كلمة المرور خاطئة، يرجى المحاولة مرة أخرى!")

            self.form2.lblcurrentUser.setText(self.loggedUser)
            self.form2.inputUsername.setText(self.loggedUser)

        except ValueError:
            QMessageBox.warning(self, "Warning", "Invalid Username or Password. Please try again!.")
        except Exception as e:
            QMessageBox.warning(self, "Warning", "خطأ في اسم المستخدم أو كلمة مرور. حاول مرة اخرى!")

    def exitprog(self):
        sys.exit()
