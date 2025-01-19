from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox, QLineEdit, QRadioButton, QComboBox
from sqlFunction import sqlFillTableView, findMandatory, findCustomer, findOrder, findSponser, findSource, fillInputPrice
import cb_lists
from DataEntry import Ui_Data_Entry
from cb_lists import *


class DataEntryWindow(QMainWindow, Ui_Data_Entry):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.initialize_elements()
       
        # self.inputPrice.setDisabled(False)

        self.form2 = None

    def goBack(self):

        self.hide()
        self.form2.show()
        self.clearAllFields()

    # function to control shipping status in Qcb
    def mov_control(self):
        selected_value = self.cbMovement.currentText()
        if selected_value == "شحن":
            self.inputTransporter.setDisabled(True)
            self.inputComment.setDisabled(False)
            self.inputShipmentCost.setDisabled(False)
            self.cbSpedition.setDisabled(False)
        elif selected_value == "توصيل":
            self.inputTransporter.setDisabled(False)
            self.inputComment.setDisabled(True)
            self.inputShipmentCost.setDisabled(True)
            self.cbSpedition.setDisabled(True)

        else:
            self.inputTransporter.setDisabled(True)
            self.inputComment.setDisabled(True)
            self.inputShipmentCost.setDisabled(True)
            self.cbSpedition.setDisabled(True)


    def set_reference(self, form2):
        self.form2 = form2
    def fillTAbelView(self):

        sqlResult = sqlFillTableView()
        ResutlData = sqlResult.fetchall()
        self.TableDataEntry.setRowCount(len(ResutlData))
        for row_num, row in enumerate(ResutlData):
            for col_num, data in enumerate(row):
                item = QTableWidgetItem(str(data))
                self.TableDataEntry.setItem(row_num, col_num, item)
          # print(row)
          #  print(str(row[1]))
       # print("herre")
       # print(sqlResult)
    def findAndFill(self, num):
        OrderNum = int(num)
        Result = findMandatory(OrderNum).fetchall()
        self.inputRate.setText(str(Result[0][0]))
        self.inputDiscountComm.setText(str(Result[0][1]))
        self.inputShippingRefund.setText(str(Result[0][2]))
        self.inputDeliveryDate.setText(str(Result[0][3]))

        ResultCustomer = findCustomer(OrderNum).fetchall()
        self.inputPhone.setText(str(ResultCustomer[0][0]))
        self.inputAdress.setText(str(ResultCustomer[0][1]))

        ResultOrder = findOrder(OrderNum).fetchall()
        self.inputOrderDate.setText(str(ResultOrder[0][0]))
        index = self.cbMovement.findText(str(ResultOrder[0][1]))
        self.cbMovement.setCurrentIndex(index)
        self.inputMovDate.setText(str(ResultOrder[0][2]))
        self.inputOffService.setText(str(ResultOrder[0][3]))

        ResultSponser = findSponser(OrderNum).fetchall()
        index = self.cbSponser.findText(str(ResultSponser[0][0]))
        self.cbSponser.setCurrentIndex(index)

        ResultSource = findSource(OrderNum).fetchall()
        index = self.cbSource.findText(str(ResultSource[0][0]))
        self.cbSource.setCurrentIndex(index)

        ResultPrice = fillInputPrice(OrderNum).fetchall()
        self.inputPrice.setText(str(ResultPrice[0][0]))

        print(Result)



    def selcetRow(self, item):
        row = item.row()
        col = item.column()
        OrderNum = self.TableDataEntry.item(row, 0).text()

        self.inputOrderNum.setText(OrderNum)
        self.inputOrderStatus.setText(self.TableDataEntry.item(row, 1).text())
        self.inputCustomerName.setText(self.TableDataEntry.item(row, 2).text())
        self.inputAdress.setText(self.TableDataEntry.item(row, 3).text())
        self.inputToPay.setText(self.TableDataEntry.item(row, 4).text())
        self.inputProduct.setText(self.TableDataEntry.item(row, 5).text())
        index = self.cbMarketingAgents.findText(self.TableDataEntry.item(row, 6).text())
        self.cbMarketingAgents.setCurrentIndex(index)
        self.inputDiscount.setText(self.TableDataEntry.item(row, 7).text())
       # self.cbMovement.setCurrentText(self.TableDataEntry.item(row, 8).text())
       # self.inputMovDate.setText(self.TableDataEntry.item(row, 9).text())
        self.findAndFill(OrderNum)
        orderStatus = str(self.inputOrderStatus.text())
        self.switch_rdb_statu(orderStatus)

    def switch_rdbNew(self):

        self.rdbnew.setDisabled(False)
        self.rdbnew.setChecked(True)
        self.rdbDelivery.setDisabled(False)
        self.rdbDelivered.setDisabled(False)
        self.rdbBooked.setDisabled(False)
        self.rdbSpecial.setDisabled(False)
        self.rdbDone.setDisabled(True)
        self.rdbPayed.setDisabled(True)
        self.rdbNoAsnwer.setDisabled(False)
        self.rdbNoLine.setDisabled(False)
        self.rdbPostponed.setDisabled(False)
        self.rdbnotAvailble.setDisabled(False)
        self.rdbRefund.setDisabled(True)
        self.rdbCanceld.setDisabled(False)
        self.rdbPending.setDisabled(True)

    def switch_rdbPostponed(self):

        self.rdbnew.setDisabled(True)
        self.rdbDelivery.setDisabled(False)
        self.rdbDelivered.setDisabled(False)
        self.rdbBooked.setDisabled(True)
        self.rdbSpecial.setDisabled(True)
        self.rdbDone.setDisabled(True)
        self.rdbPayed.setDisabled(True)
        self.rdbNoAsnwer.setDisabled(True)
        self.rdbNoLine.setDisabled(True)
        self.rdbPostponed.setDisabled(False)
        self.rdbPostponed.setChecked(True)
        self.rdbnotAvailble.setDisabled(True)
        self.rdbRefund.setDisabled(True)
        self.rdbCanceld.setDisabled(False)
        self.rdbPending.setDisabled(True)

    def switch_rdbnotAvailble(self):
        self.rdbnew.setDisabled(True)
        self.rdbDelivery.setDisabled(False)
        self.rdbDelivered.setDisabled(False)
        self.rdbBooked.setDisabled(True)
        self.rdbSpecial.setDisabled(True)
        self.rdbDone.setDisabled(True)
        self.rdbPayed.setDisabled(True)
        self.rdbNoAsnwer.setDisabled(True)
        self.rdbNoLine.setDisabled(True)
        self.rdbPostponed.setDisabled(True)
        self.rdbnotAvailble.setDisabled(False)
        self.rdbnotAvailble.setChecked(True)
        self.rdbRefund.setDisabled(True)
        self.rdbCanceld.setDisabled(False)
        self.rdbPending.setDisabled(True)

    def switch_rdbRefund(self):
        self.rdbnew.setDisabled(True)
        self.rdbDelivery.setDisabled(True)
        self.rdbDelivered.setDisabled(True)
        self.rdbBooked.setDisabled(True)
        self.rdbSpecial.setDisabled(True)
        self.rdbDone.setDisabled(True)
        self.rdbPayed.setDisabled(True)
        self.rdbNoAsnwer.setDisabled(True)
        self.rdbNoLine.setDisabled(True)
        self.rdbPostponed.setDisabled(True)
        self.rdbnotAvailble.setDisabled(True)
        self.rdbRefund.setDisabled(False)
        self.rdbRefund.setChecked(True)
        self.rdbCanceld.setDisabled(True)
        self.rdbPending.setDisabled(True)

    def switch_rdbCanceld(self):
        self.rdbnew.setDisabled(True)
        self.rdbDelivery.setDisabled(True)
        self.rdbDelivered.setDisabled(True)
        self.rdbBooked.setDisabled(True)
        self.rdbSpecial.setDisabled(True)
        self.rdbDone.setDisabled(True)
        self.rdbPayed.setDisabled(True)
        self.rdbNoAsnwer.setDisabled(True)
        self.rdbNoLine.setDisabled(True)
        self.rdbPostponed.setDisabled(True)
        self.rdbnotAvailble.setDisabled(True)
        self.rdbRefund.setDisabled(True)
        self.rdbCanceld.setDisabled(False)
        self.rdbCanceld.setChecked(True)
        self.rdbPending.setDisabled(True)

    def switch_rdbPending(self):
        self.rdbnew.setDisabled(True)
        self.rdbDelivery.setDisabled(True)
        self.rdbDelivered.setDisabled(True)
        self.rdbBooked.setDisabled(True)
        self.rdbSpecial.setDisabled(True)
        self.rdbDone.setDisabled(True)
        self.rdbPayed.setDisabled(False)
        self.rdbNoAsnwer.setDisabled(True)
        self.rdbNoLine.setDisabled(True)
        self.rdbPostponed.setDisabled(True)
        self.rdbnotAvailble.setDisabled(True)
        self.rdbRefund.setDisabled(True)
        self.rdbCanceld.setDisabled(False)
        self.rdbPending.setDisabled(False)
        self.rdbPending.setChecked(True)

    def switch_rdbDelivery(self):
        self.rdbnew.setDisabled(True)
        self.rdbDelivery.setDisabled(False)
        self.rdbDelivery.setChecked(True)
        self.rdbDelivered.setDisabled(True)
        self.rdbBooked.setDisabled(True)
        self.rdbSpecial.setDisabled(True)
        self.rdbDone.setDisabled(False)
        self.rdbPayed.setDisabled(True)
        self.rdbNoAsnwer.setDisabled(True)
        self.rdbNoLine.setDisabled(True)
        self.rdbPostponed.setDisabled(True)
        self.rdbnotAvailble.setDisabled(True)
        self.rdbRefund.setDisabled(True)
        self.rdbCanceld.setDisabled(False)
        self.rdbPending.setDisabled(False)

    def switch_rdbDelivered(self):
        self.rdbnew.setDisabled(True)
        self.rdbDelivery.setDisabled(True)
        self.rdbDelivered.setDisabled(False)
        self.rdbBooked.setDisabled(True)
        self.rdbSpecial.setDisabled(True)
        self.rdbDone.setDisabled(False)
        self.rdbPayed.setDisabled(True)
        self.rdbNoAsnwer.setDisabled(True)
        self.rdbNoLine.setDisabled(True)
        self.rdbPostponed.setDisabled(True)
        self.rdbnotAvailble.setDisabled(True)
        self.rdbRefund.setDisabled(False)
        self.rdbCanceld.setDisabled(True)
        self.rdbPending.setDisabled(True)

        self.rdbDelivered.setChecked(True)

    def switch_rdbBooked(self):
        self.rdbnew.setDisabled(True)
        self.rdbDelivery.setDisabled(False)
        self.rdbDelivered.setDisabled(False)
        self.rdbBooked.setDisabled(False)
        self.rdbSpecial.setDisabled(True)
        self.rdbDone.setDisabled(False)
        self.rdbPayed.setDisabled(True)
        self.rdbNoAsnwer.setDisabled(True)
        self.rdbNoLine.setDisabled(True)
        self.rdbPostponed.setDisabled(True)
        self.rdbnotAvailble.setDisabled(True)
        self.rdbRefund.setDisabled(True)
        self.rdbCanceld.setDisabled(False)
        self.rdbPending.setDisabled(True)

        self.rdbBooked.setChecked(True)

    def switch_rdbSpecial(self):
        self.rdbnew.setDisabled(True)
        self.rdbDelivery.setDisabled(False)
        self.rdbDelivered.setDisabled(False)
        self.rdbBooked.setDisabled(True)
        self.rdbSpecial.setDisabled(False)
        self.rdbDone.setDisabled(False)
        self.rdbPayed.setDisabled(True)
        self.rdbNoAsnwer.setDisabled(True)
        self.rdbNoLine.setDisabled(True)
        self.rdbPostponed.setDisabled(True)
        self.rdbnotAvailble.setDisabled(True)
        self.rdbRefund.setDisabled(True)
        self.rdbCanceld.setDisabled(False)
        self.rdbPending.setDisabled(True)

        self.rdbSpecial.setChecked(True)

    def switch_rdbDone(self):
        self.rdbnew.setDisabled(True)
        self.rdbDelivery.setDisabled(True)
        self.rdbDelivered.setDisabled(True)
        self.rdbBooked.setDisabled(True)
        self.rdbSpecial.setDisabled(True)
        self.rdbDone.setDisabled(False)
        self.rdbPayed.setDisabled(False)
        self.rdbNoAsnwer.setDisabled(True)
        self.rdbNoLine.setDisabled(True)
        self.rdbPostponed.setDisabled(True)
        self.rdbnotAvailble.setDisabled(True)
        self.rdbRefund.setDisabled(True)
        self.rdbCanceld.setDisabled(True)
        self.rdbPending.setDisabled(True)

        self.rdbDone.setChecked(True)

    def switch_rdbPayed(self):
        self.rdbnew.setDisabled(True)
        self.rdbDelivery.setDisabled(True)
        self.rdbDelivered.setDisabled(True)
        self.rdbBooked.setDisabled(True)
        self.rdbSpecial.setDisabled(True)
        self.rdbDone.setDisabled(True)
        self.rdbPayed.setDisabled(False)
        self.rdbNoAsnwer.setDisabled(True)
        self.rdbNoLine.setDisabled(True)
        self.rdbPostponed.setDisabled(True)
        self.rdbnotAvailble.setDisabled(True)
        self.rdbRefund.setDisabled(True)
        self.rdbCanceld.setDisabled(True)
        self.rdbPending.setDisabled(True)

        self.rdbPayed.setChecked(True)

    def switch_rdbNoAnswer(self):
        self.rdbnew.setDisabled(True)
        self.rdbDelivery.setDisabled(False)
        self.rdbDelivered.setDisabled(False)
        self.rdbBooked.setDisabled(True)
        self.rdbSpecial.setDisabled(True)
        self.rdbDone.setDisabled(True)
        self.rdbPayed.setDisabled(True)
        self.rdbNoAsnwer.setDisabled(False)
        self.rdbNoLine.setDisabled(True)
        self.rdbPostponed.setDisabled(True)
        self.rdbnotAvailble.setDisabled(True)
        self.rdbRefund.setDisabled(True)
        self.rdbCanceld.setDisabled(False)
        self.rdbPending.setDisabled(True)

        self.rdbNoAsnwer.setChecked(True)

    def switch_rdbNoLine(self):
        self.rdbnew.setDisabled(True)
        self.rdbDelivery.setDisabled(False)
        self.rdbDelivered.setDisabled(False)
        self.rdbBooked.setDisabled(True)
        self.rdbSpecial.setDisabled(True)
        self.rdbDone.setDisabled(True)
        self.rdbPayed.setDisabled(True)
        self.rdbNoAsnwer.setDisabled(True)
        self.rdbNoLine.setDisabled(False)
        self.rdbPostponed.setDisabled(True)
        self.rdbnotAvailble.setDisabled(True)
        self.rdbRefund.setDisabled(True)
        self.rdbCanceld.setDisabled(False)
        self.rdbPending.setDisabled(True)

        self.rdbNoAsnwer.setChecked(True)

    def switch_rdb_statu(self, status):
        if status == "جديد":
            self.switch_rdbNew()
        elif status == "مؤجل":
            self.switch_rdbPostponed()
        elif status == "غير متوفر":
            self.switch_rdbnotAvailble()
        elif status == "مرتجع":
            self.switch_rdbRefund()
        elif status == "ملغي":
            self.switch_rdbCanceld()
        elif status == "معلق":
            self.switch_rdbPending()
        elif status == "توصيل":
            self.switch_rdbDelivery()
        elif status == "مشحون":
            self.switch_rdbDelivered()
        elif status == "محجوز":
            self.switch_rdbBooked()
        elif status == "خاص":
            self.switch_rdbSpecial()
        elif status == "تم":
            self.switch_rdbDone()
        elif status == "مسدد":
            self.switch_rdbPayed()
        elif status == "لم يجب":
            self.switch_rdbNoAnswer()
        elif status == "الخط مغلق":
            self.switch_rdbNoLine()




    def delete_order(self):
        # check the order then sql DELETE request
        pass
    
    def modify_order(self):
        statu = str(self.inputOrderStatus.text())
        orderNum = str(self.inputOrderNum.text())
        self.check_Done_Refund_Canceld()
        self.check_movement()
        sum_boolean = self.check_sum_amount()
        boolean = self.checkInputIfEmpty()

        if boolean and sum_boolean:
            confirmation = self.show_message_box()
            if confirmation:
                # sql UPDATE request
                QMessageBox.information(self, "Information", f'تمت تعديل بيانات الطلب {orderNum} في قاعدة البيانات بنجاح! حالة الطلب الحالية : {statu}')
                self.SetToWhite()
                self.clearAllFields()

    def addToDataBase(self):

        self.check_Done_Refund_Canceld()
        self.check_movement()
        sum_boolean = self.check_sum_amount()
        boolean = self.checkInputIfEmpty()

        if boolean and sum_boolean:
            confirmation = self.show_message_box()
            if confirmation:
                # sql INSERT request
                QMessageBox.information(self, "Information", 'تمت اضافة البيانات الى قاعدة البيانات بنجاح!')
                self.SetToWhite()
                self.clearAllFields()




    # Function to check the conditions of the Sum and the Number of products
    def check_sum_amount(self):
        iseven = True
        total = float(self.inputPrice.text()) + float(self.inputOffService.text()) + float(self.inputRate.text())
        print(total)
        total_sum = float(self.inputToPay.text())
        print(total_sum)
        num_product = int(self.inputNumProd.text())
        if self.inputNumBack.text() == "":
            num_back = 0
        else:
            num_back = int(self.inputNumBack.text())

        if total != total_sum or num_back > num_product:
            if total != total_sum:
                QMessageBox.warning(self, "Warning", 'يرجى التأكد من سعر البضاعة و خدمات المكتب و نسبة المسوقة و المبلغ المطلوب!')
                iseven = False
            if num_back > num_product:
                if self.rdbDone.isChecked():
                    pass
                else:
                    QMessageBox.warning(self, "Warning", 'ان عدد الفطع المرتجعة غير صحيح!')
                    iseven = False
        return iseven

    def deactivate_movement(self):
        if self.rdbnew.isChecked() or self.rdbNoAsnwer.isChecked() or self.rdbPostponed.isChecked() or self.rdbNoLine.isChecked() or self.rdbBooked.isChecked() or self.rdbSpecial.isChecked():
            self.gpMovementInfo.setDisabled(True)
        else:
            self.gpMovementInfo.setDisabled(False)


    def check_movement(self):
        if not self.rdbnew.isChecked():
            if self.cbMovement.currentText() == "شحن" or self.cbMovement.currentText() == "توصيل":
                if self.inputMovDate.text() == "":
                    QMessageBox.warning(self, "Warning", 'يرجى تعبئة تاريخ الحركة!')
            if self.cbMovement.currentText() == "شحن":
                if self.cbSpedition.currentText() == "":
                    QMessageBox.warning(self, "Warning", 'يرجى تعبئة شركة الشجن!')
                if self.inputComment.text() == "":
                    QMessageBox.warning(self, "Warning", 'يرجى تعبئة رفم الاشعار!')
                if self.inputShipmentCost.text() == "":
                    QMessageBox.warning(self, "Warning", 'يرجى تعبئة اجور الشحن!')
            if self.cbMovement.currentText() == "توصيل":
                if self.inputTransporter.text() == "":
                    QMessageBox.warning(self, "Warning", 'يرجى تعبئة الناقل!')



    def set_Movement_disabled(self, boolean):

        self.cbMovement.setDisabled(boolean)
        self.inputMovDate.setDisabled(boolean)
        self.cbSpedition.setDisabled(boolean)
        self.inputComment.setDisabled(boolean)
        self.inputShipmentCost.setDisabled(boolean)
        self.inputShipmentCost.setDisabled(boolean)
    def Done_Refund_Canceld_control(self):
        if self.rdbDone.isChecked() or self.rdbRefund.isChecked() or self.rdbCanceld.isChecked():
            self.inputDiscount.setDisabled(False)
            self.inputDiscountComm.setDisabled(False)
            if self.rdbDone.isChecked() or self.rdbCanceld.isChecked():
                self.inputShippingRefund.setDisabled(True)
            if self.rdbRefund.isChecked():
                self.inputShippingRefund.setDisabled(False)
        else:
            self.inputDiscount.setDisabled(True)
            self.inputDiscountComm.setDisabled(True)
            self.inputShippingRefund.setDisabled(True)



    def check_Done_Refund_Canceld(self):
        if self.rdbDone.isChecked() or self.rdbRefund.isChecked() or self.rdbCanceld.isChecked():

            if self.inputDiscountComm.text() == "" or self.inputDiscount.text() == "" or self.inputDeliveryDate.text() == "":
                if self.inputDiscountComm.text() == "":
                    QMessageBox.warning(self, "Warning", 'الرجاء تعبئة بيان الخصم!')
                if self.inputDiscount.text() == "":
                    QMessageBox.warning(self, "Warning", 'الرجاء تعبئة الخصم!')
                if self.inputDeliveryDate.text() == "":
                    QMessageBox.warning(self, "Warning", 'الرجاء تعبئة تاريخ الاستلام!')
            if self.rdbRefund.isChecked():
                if self.inputShippingRefund.text() == "":
                    QMessageBox.warning(self, "Warning", 'الرجاء تعبئة تعويض الشحن!!')
            if self.rdbDone.isChecked():
                if self.inputPayedBack.text() == "" and self.cbMovement.currentText() == "توصيل":
                    QMessageBox.warning(self, "Warning", 'الرجاء تعبئة المرتجع!!')
                if self.inputNumBack.text() == "":
                    QMessageBox.warning(self, "Warning", 'الرجاء تعبئة عدد القطع المرتجعة!!')
                if int(self.inputNumBack.text()) > 0:
                    QMessageBox.warning(self, "Warning", 'يرجى التأكد من سعر البضاعة و خدمات المكتب و نسبة المسوقة و المبلغ المطلوب بما يتناسب مع البضاعة المستلمة!')



    # function to check if any of the QLine/Qcb if empty
    def checkInputIfEmpty(self):

        isNotempty = True

        for widget in self.findChildren(QLineEdit):
            if widget.isEnabled():
                if not widget.text() == "":
                    widget.setStyleSheet("background-color: white")

                if widget.text() == "":
                    widget.setStyleSheet("background-color: yellow")
                    isNotempty = False

        for widget in self.findChildren(QComboBox):
            if widget.isEnabled():
                if not widget.currentText() == "":
                    widget.setStyleSheet("background-color: white")

                if widget.currentText() == "":
                    widget.setStyleSheet("background-color: yellow")
                    isNotempty = False

        if isNotempty:
            return True
        else:
            QMessageBox.warning(self, "Warning", 'الرجاء التحقق من البيانات الناقصة!')
            return False
    # function to set the statu of the order in the statu QLine
    def setStatus(self):

        selected_rdb = None

        if self.rdbnew.isChecked():
            selected_rdb = self.rdbnew
        elif self.rdbDone.isChecked():
            selected_rdb = self.rdbDone
        elif self.rdbnotAvailble.isChecked():
            selected_rdb = self.rdbnotAvailble
        elif self.rdbDelivery.isChecked():
            selected_rdb = self.rdbDelivery
        elif self.rdbPayed.isChecked():
            selected_rdb = self.rdbPayed
        elif self.rdbRefund.isChecked():
            selected_rdb = self.rdbRefund
        elif self.rdbDelivered.isChecked():
            selected_rdb = self.rdbDelivered
        elif self.rdbNoAsnwer.isChecked():
            selected_rdb = self.rdbNoAsnwer
        elif self.rdbCanceld.isChecked():
            selected_rdb = self.rdbCanceld
        elif self.rdbBooked.isChecked():
            selected_rdb = self.rdbBooked
        elif self.rdbNoLine.isChecked():
            selected_rdb = self.rdbNoLine
        elif self.rdbPending.isChecked():
            selected_rdb = self.rdbPending
        elif self.rdbSpecial.isChecked():
            selected_rdb = self.rdbSpecial
        elif self.rdbPostponed.isChecked():
            selected_rdb = self.rdbPostponed
        elif self.btnRefresh.isChecked():
            selected_rdb = self.btnRefresh

        if selected_rdb:

            self.inputOrderStatus.setText(selected_rdb.text())


    def MandatoryChange(self):
        selected_opt = str(self.cbMarketingAgents.currentText())
        if selected_opt == "زبون مباشر":
            self.inputRate.setText('0')
            self.inputRate.setReadOnly(True)
        else:
            self.inputRate.setReadOnly(False)



    # function to clear all fields after goBack or INSERT
    def clearAllFields(self):

        self.clearAllRdb()

        for widget in self.findChildren(QLineEdit):
            widget.clear()
            widget.setDisabled(False)

        for widget in self.findChildren(QComboBox):
            widget.setCurrentIndex(-1)
            widget.setDisabled(False)

    def show_message_box(self):

        result = QMessageBox.question(self, "تـأكـيد",'هل أنت متأكد من كل معلومات الطلب؟')
        if result == 16384:
            return True
        else:
            return False




    # not working
    def clearAllRdb(self):
        self.rdbnew.setChecked(False)
        self.rdbDone.setChecked(False)
        self.rdbnotAvailble.setChecked(False)
        self.rdbDelivery.setChecked(False)
        self.rdbPayed.setChecked(False)
        self.rdbRefund.setChecked(False)
        self.rdbDelivered.setChecked(False)
        self.rdbNoAsnwer.setChecked(False)
        self.rdbCanceld.setChecked(False)
        self.rdbBooked.setChecked(False)
        self.rdbNoLine.setChecked(False)
        self.rdbPending.setChecked(False)
        self.rdbSpecial.setChecked(False)
        self.rdbPostponed.setChecked(False)
        self.btnRefresh.setChecked(False)

       # orderNum = int(self.inputOrderNum.text())
       # orderStatu = str(self.inputOrderStatus.text())
       # #orderSource = pass
       # orderDate = str(self.inputOrderDate.text())
       # orderPrice = str(self.inputPrice.text())
       # #orderSponser = pass
       # orderOffService = str(self.inputOffService.text())
       # orderTaxDiff = str(self.inputTaxDiff.text())
       # orderEarndDiff = str(self.inputEarnedDiff.text())

    def SetToWhite(self):
        for widget in self.findChildren(QLineEdit):
            widget.setStyleSheet("background-color: white")
    # function to initialize the Mainwindow elemnts afet SetUp
    def initialize_elements(self):
        
        self.cbSource.addItems(cb_lists.source)
        self.cbSponser.addItems(cb_lists.sponsor)
        self.cbMovement.addItems(cb_lists.shipping_statu)
        self.cbSpedition.addItems(cb_lists.shipping_agent)
        self.cbMarketingAgents.addItems(cb_lists.marketer)
        self.cbMarketingAgents.currentIndexChanged.connect(self.MandatoryChange)
        self.cbMovement.currentIndexChanged.connect(self.mov_control)
        self.rdbnew.toggled.connect(self.setStatus)
        self.rdbnew.toggled.connect(self.deactivate_movement)
        self.rdbDone.toggled.connect(self.setStatus)
        self.rdbDone.toggled.connect(self.Done_Refund_Canceld_control)
       # self.rdbnew.toggled.connect(self.set_Movement_disabled)
        self.rdbnotAvailble.toggled.connect(self.setStatus)
        self.rdbDelivery.toggled.connect(self.setStatus)
        self.rdbPayed.toggled.connect(self.setStatus)
        self.rdbRefund.toggled.connect(self.setStatus)
        self.rdbRefund.toggled.connect(self.Done_Refund_Canceld_control)
        self.rdbDelivered.toggled.connect(self.setStatus)
        self.rdbNoAsnwer.toggled.connect(self.setStatus)
        self.rdbNoAsnwer.toggled.connect(self.deactivate_movement)
        self.rdbCanceld.toggled.connect(self.setStatus)
        self.rdbCanceld.toggled.connect(self.Done_Refund_Canceld_control)
        self.rdbBooked.toggled.connect(self.setStatus)
        self.rdbBooked.toggled.connect(self.deactivate_movement())
        self.rdbNoLine.toggled.connect(self.setStatus)
        self.rdbNoLine.toggled.connect(self.deactivate_movement)
        self.rdbPending.toggled.connect(self.setStatus)
        self.rdbSpecial.toggled.connect(self.setStatus)
        self.rdbSpecial.toggled.connect(self.deactivate_movement)
        self.rdbPostponed.toggled.connect(self.setStatus)
        self.rdbPostponed.toggled.connect(self.deactivate_movement)
        self.btnRefresh.toggled.connect(self.setStatus)
        self.btnBack.clicked.connect(self.goBack)
        self.btnAdd.clicked.connect(self.addToDataBase)
        self.btnEdit.clicked.connect(self.modify_order)
        self.btnDelete.clicked.connect(self.delete_order)
        self.fillTAbelView()
        self.TableDataEntry.itemDoubleClicked.connect(self.selcetRow)


        


