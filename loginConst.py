"""try:
    user = str(self.inputUserName.text())
    pass_w = str(self.inputPassword.text())

    if self.rdbAdmin.isChecked():
                cursor.execute(f"SELECT password FROM TeAmoDB.dbo.adminUsers WHERE username LIKE '{user}' ")

                for row in cursor:
                    print(row)
                    print(row[0])
                    passSQL = row[0]

                if pass_w == passSQL:
                    self.loggedUser = user
                    # print(user)
                    self.form2.show()
                    self.hide()

                    self.inputPassword.clear()
                    self.inputUserName.clear()

    elif self.rdbManager.isChecked():

                cursor.execute(f"SELECT password FROM TeAmoDB.dbo.managerUsers WHERE username LIKE '{user}' ")

                for row in cursor:
                    print(row)
                    print(row[0])
                    passSQL = row[0]

                if pass_w == passSQL:
                    self.loggedUser = user
                    # print(user)
                    self.form2.show()
                    self.hide()

                    self.inputPassword.clear()
                    self.inputUserName.clear()

    else:
                cursor.execute(f"SELECT password FROM TeAmoDB.dbo.users WHERE username LIKE '{user}' ")

                for row in cursor:
                    print(row)
                    print(row[0])
                    passSQL = row[0]

                if pass_w == passSQL:
                    self.loggedUser = user
                    # print(user)
                    self.form2.show()
                    self.hide()

                    self.inputPassword.clear()
                    self.inputUserName.clear()

except ValueError:
    QMessageBox.warning(self, "Warning", "Invalid Username or Password. Please try again!.")
except Exception as e:
    QMessageBox.warning(self, "Warning", "خطأ في اسم المستخدم أو كلمة مرور. حاول مرة اخرى!")







import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox, QLineEdit
from logIn import Ui_logIn
from mainWindow import Ui_MainWindow2
from mainWindowClass import Frm_main2
from sqlFunction import cursor


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
        self.loggedUser = ""

    def set_reference(self, form2):
        self.form2 = form2

    def openMainWindow(self):

        user = str(self.inputUserName.text())
        pass_w = str(self.inputPassword.text())

        if self.rdbAdmin.isChecked():

            try:


                cursor.execute(f"SELECT password FROM TeAmoDB.dbo.adminUsers WHERE username LIKE '{user}' ")

                for row in cursor:
                    print(row)
                    print(row[0])
                    passSQL = row[0]

                if pass_w == passSQL:
                    self.loggedUser = user
                    # print(user)
                    self.form2.show()
                    self.hide()

                    self.inputPassword.clear()
                    self.inputUserName.clear()
                else:
                    QMessageBox.warning(self, "Warning", "كلمة المرور خاطئة، يرجى المحاولة مرة أخرى!")
            except ValueError:
                QMessageBox.warning(self, "Warning", "Invalid Username or Password. Please try again!.")
            except Exception as e:
                QMessageBox.warning(self, "Warning", "خطأ في اسم المستخدم أو كلمة مرور. حاول مرة اخرى!")

        elif self.rdbManager.isChecked():

            try:


                cursor.execute(f"SELECT password FROM TeAmoDB.dbo.managerUsers WHERE username LIKE '{user}' ")

                for row in cursor:
                    print(row)
                    print(row[0])
                    passSQL = row[0]

                if pass_w == passSQL:
                    self.loggedUser = user
                    # print(user)
                    self.form2.show()
                    self.hide()

                    self.inputPassword.clear()
                    self.inputUserName.clear()
                else:
                    QMessageBox.warning(self, "Warning", "كلمة المرور خاطئة، يرجى المحاولة مرة أخرى!")
            except ValueError:
                QMessageBox.warning(self, "Warning", "Invalid Username or Password. Please try again!.")
            except Exception as e:
                QMessageBox.warning(self, "Warning", "خطأ في اسم المستخدم أو كلمة مرور. حاول مرة اخرى!")


        else:
            try:


                cursor.execute(f"SELECT password FROM TeAmoDB.dbo.users WHERE username LIKE '{user}' ")

                for row in cursor:
                    print(row)
                    print(row[0])
                    passSQL = row[0]

                if pass_w == passSQL:
                    self.loggedUser = user
                    # print(user)
                    self.form2.show()
                    self.hide()

                    self.inputPassword.clear()
                    self.inputUserName.clear()
                else:
                    QMessageBox.warning(self, "Warning", "كلمة المرور خاطئة، يرجى المحاولة مرة أخرى!")
            except ValueError:
                QMessageBox.warning(self, "Warning", "Invalid Username or Password. Please try again!.")
            except Exception as e:
                QMessageBox.warning(self, "Warning", "خطأ في اسم المستخدم أو كلمة مرور. حاول مرة اخرى!")



    def exitprog(self):
        sys.exit() """
