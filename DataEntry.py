# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DataEntry.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QFormLayout,
    QFrame, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QRadioButton, QSizePolicy, QStatusBar,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Data_Entry(object):
    def setupUi(self, Data_Entry):
        if not Data_Entry.objectName():
            Data_Entry.setObjectName(u"Data_Entry")
        Data_Entry.resize(1182, 783)
        Data_Entry.setLayoutDirection(Qt.RightToLeft)
        Data_Entry.setStyleSheet(u"background-color: #e4e4e4;\n"
"	color: #000;\n"
"	selection-background-color: #46a2da;\n"
"	selection-color: #fff;")
        self.centralwidget = QWidget(Data_Entry)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(281, 10, 581, 51))
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Sunken)
        self.frame.setLineWidth(4)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(140, 10, 321, 31))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.gpOfficeInfo = QGroupBox(self.centralwidget)
        self.gpOfficeInfo.setObjectName(u"gpOfficeInfo")
        self.gpOfficeInfo.setGeometry(QRect(861, 70, 301, 651))
        self.gpOfficeInfo.setLayoutDirection(Qt.RightToLeft)
        self.gpOfficeInfo.setStyleSheet(u"QGroupBox \n"
"{\n"
"    border: 1px solid;\n"
"    border-color: #666666;\n"
"    margin-top: 23px;\n"
"\n"
"}\n"
"\n"
"\n"
"QGroupBox#gpOfficeInfo::title  \n"
"{\n"
"    background-color: #a0a2a4;\n"
"    color: #000;\n"
"	subcontrol-position: top left;\n"
"    subcontrol-origin: margin;\n"
"    padding: 5px;\n"
"	border: 1px solid #000;\n"
"	border-bottom: none;\n"
"\n"
"}\n"
"")
        self.gpOfficeInfo.setFlat(False)
        self.gpOfficeInfo.setCheckable(False)
        self.formLayoutWidget = QWidget(self.gpOfficeInfo)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 30, 279, 72))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(11)
        font1.setBold(True)
        self.label_2.setFont(font1)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.inputOrderNum = QLineEdit(self.formLayoutWidget)
        self.inputOrderNum.setObjectName(u"inputOrderNum")
        font2 = QFont()
        font2.setPointSize(14)
        self.inputOrderNum.setFont(font2)
        self.inputOrderNum.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.inputOrderNum)

        self.label_3 = QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.inputOrderStatus = QLineEdit(self.formLayoutWidget)
        self.inputOrderStatus.setObjectName(u"inputOrderStatus")
        self.inputOrderStatus.setFont(font2)
        self.inputOrderStatus.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.inputOrderStatus)

        self.lblUnknown = QLabel(self.gpOfficeInfo)
        self.lblUnknown.setObjectName(u"lblUnknown")
        self.lblUnknown.setGeometry(QRect(10, 110, 279, 51))
        self.lblUnknown.setFont(font1)
        self.lblUnknown.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid black")
        self.layoutWidget = QWidget(self.gpOfficeInfo)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 170, 279, 201))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.rdbnew = QRadioButton(self.layoutWidget)
        self.rdbnew.setObjectName(u"rdbnew")
        self.rdbnew.setStyleSheet(u"QRadioButton \n"
"{\n"
"	color: #000;\n"
"	background-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QRadioButton#rdbnew::indicator::unchecked:hover \n"
"{\n"
"	background-color: darkgray;\n"
"	border: 2px solid #46a2da;\n"
"	border-radius: 6px;\n"
"}\n"
"\n"
"\n"
"QRadioButton#rdbnew::indicator::checked \n"
"{\n"
"	border: 2px solid #52beff;\n"
"	border-radius: 6px;\n"
"	background-color: #0088da;  \n"
"	width: 9px; \n"
"	height: 9px; \n"
"\n"
"}")

        self.horizontalLayout.addWidget(self.rdbnew)

        self.rdbDone = QRadioButton(self.layoutWidget)
        self.rdbDone.setObjectName(u"rdbDone")
        self.rdbDone.setStyleSheet(u"QRadioButton \n"
"{\n"
"	color: #000;\n"
"	background-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QRadioButton#rdbDone::indicator::unchecked:hover \n"
"{\n"
"	background-color: darkgray;\n"
"	border: 2px solid #46a2da;\n"
"	border-radius: 6px;\n"
"}\n"
"\n"
"\n"
"QRadioButton#rdbDone::indicator::checked \n"
"{\n"
"	border: 2px solid #52beff;\n"
"	border-radius: 6px;\n"
"	background-color: #0088da;  \n"
"	width: 9px; \n"
"	height: 9px; \n"
"\n"
"}")

        self.horizontalLayout.addWidget(self.rdbDone)

        self.rdbnotAvailble = QRadioButton(self.layoutWidget)
        self.rdbnotAvailble.setObjectName(u"rdbnotAvailble")
        self.rdbnotAvailble.setStyleSheet(u"QRadioButton \n"
"{\n"
"	color: #000;\n"
"	background-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QRadioButton#rdbnotAvailble::indicator::unchecked:hover \n"
"{\n"
"	background-color: darkgray;\n"
"	border: 2px solid #46a2da;\n"
"	border-radius: 6px;\n"
"}\n"
"\n"
"\n"
"QRadioButton#rdbnotAvailble::indicator::checked \n"
"{\n"
"	border: 2px solid #52beff;\n"
"	border-radius: 6px;\n"
"	background-color: #0088da;  \n"
"	width: 9px; \n"
"	height: 9px; \n"
"\n"
"}")

        self.horizontalLayout.addWidget(self.rdbnotAvailble)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.rdbDelivery = QRadioButton(self.layoutWidget)
        self.rdbDelivery.setObjectName(u"rdbDelivery")
        self.rdbDelivery.setStyleSheet(u"QRadioButton \n"
"{\n"
"	color: #000;\n"
"	background-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QRadioButton#rdbDelivery::indicator::unchecked:hover \n"
"{\n"
"	background-color: darkgray;\n"
"	border: 2px solid #46a2da;\n"
"	border-radius: 6px;\n"
"}\n"
"\n"
"\n"
"QRadioButton#rdbDelivery::indicator::checked \n"
"{\n"
"	border: 2px solid #52beff;\n"
"	border-radius: 6px;\n"
"	background-color: #0088da;  \n"
"	width: 9px; \n"
"	height: 9px; \n"
"\n"
"}")

        self.horizontalLayout_2.addWidget(self.rdbDelivery)

        self.rdbPayed = QRadioButton(self.layoutWidget)
        self.rdbPayed.setObjectName(u"rdbPayed")
        self.rdbPayed.setStyleSheet(u"QRadioButton \n"
"{\n"
"	color: #000;\n"
"	background-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QRadioButton#rdbPayed::indicator::unchecked:hover \n"
"{\n"
"	background-color: darkgray;\n"
"	border: 2px solid #46a2da;\n"
"	border-radius: 6px;\n"
"}\n"
"\n"
"\n"
"QRadioButton#rdbPayed::indicator::checked \n"
"{\n"
"	border: 2px solid #52beff;\n"
"	border-radius: 6px;\n"
"	background-color: #0088da;  \n"
"	width: 9px; \n"
"	height: 9px; \n"
"\n"
"}")

        self.horizontalLayout_2.addWidget(self.rdbPayed)

        self.rdbRefund = QRadioButton(self.layoutWidget)
        self.rdbRefund.setObjectName(u"rdbRefund")
        self.rdbRefund.setStyleSheet(u"QRadioButton \n"
"{\n"
"	color: #000;\n"
"	background-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QRadioButton#rdbRefund::indicator::unchecked:hover \n"
"{\n"
"	background-color: darkgray;\n"
"	border: 2px solid #46a2da;\n"
"	border-radius: 6px;\n"
"}\n"
"\n"
"\n"
"QRadioButton#rdbRefund::indicator::checked \n"
"{\n"
"	border: 2px solid #52beff;\n"
"	border-radius: 6px;\n"
"	background-color: #0088da;  \n"
"	width: 9px; \n"
"	height: 9px; \n"
"\n"
"}")

        self.horizontalLayout_2.addWidget(self.rdbRefund)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.rdbDelivered = QRadioButton(self.layoutWidget)
        self.rdbDelivered.setObjectName(u"rdbDelivered")
        self.rdbDelivered.setStyleSheet(u"QRadioButton \n"
"{\n"
"	color: #000;\n"
"	background-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QRadioButton#rdbDelivered::indicator::unchecked:hover \n"
"{\n"
"	background-color: darkgray;\n"
"	border: 2px solid #46a2da;\n"
"	border-radius: 6px;\n"
"}\n"
"\n"
"\n"
"QRadioButton#rdbDelivered::indicator::checked \n"
"{\n"
"	border: 2px solid #52beff;\n"
"	border-radius: 6px;\n"
"	background-color: #0088da;  \n"
"	width: 9px; \n"
"	height: 9px; \n"
"\n"
"}")

        self.horizontalLayout_3.addWidget(self.rdbDelivered)

        self.rdbNoAsnwer = QRadioButton(self.layoutWidget)
        self.rdbNoAsnwer.setObjectName(u"rdbNoAsnwer")
        self.rdbNoAsnwer.setStyleSheet(u"QRadioButton \n"
"{\n"
"	color: #000;\n"
"	background-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QRadioButton#rdbNoAsnwer::indicator::unchecked:hover \n"
"{\n"
"	background-color: darkgray;\n"
"	border: 2px solid #46a2da;\n"
"	border-radius: 6px;\n"
"}\n"
"\n"
"\n"
"QRadioButton#rdbNoAsnwer::indicator::checked \n"
"{\n"
"	border: 2px solid #52beff;\n"
"	border-radius: 6px;\n"
"	background-color: #0088da;  \n"
"	width: 9px; \n"
"	height: 9px; \n"
"\n"
"}")

        self.horizontalLayout_3.addWidget(self.rdbNoAsnwer)

        self.rdbCanceld = QRadioButton(self.layoutWidget)
        self.rdbCanceld.setObjectName(u"rdbCanceld")
        self.rdbCanceld.setStyleSheet(u"QRadioButton \n"
"{\n"
"	color: #000;\n"
"	background-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QRadioButton#rdbCanceld::indicator::unchecked:hover \n"
"{\n"
"	background-color: darkgray;\n"
"	border: 2px solid #46a2da;\n"
"	border-radius: 6px;\n"
"}\n"
"\n"
"\n"
"QRadioButton#rdbCanceld::indicator::checked \n"
"{\n"
"	border: 2px solid #52beff;\n"
"	border-radius: 6px;\n"
"	background-color: #0088da;  \n"
"	width: 9px; \n"
"	height: 9px; \n"
"\n"
"}")

        self.horizontalLayout_3.addWidget(self.rdbCanceld)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.rdbBooked = QRadioButton(self.layoutWidget)
        self.rdbBooked.setObjectName(u"rdbBooked")
        self.rdbBooked.setStyleSheet(u"QRadioButton \n"
"{\n"
"	color: #000;\n"
"	background-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QRadioButton#rdbBooked::indicator::unchecked:hover \n"
"{\n"
"	background-color: darkgray;\n"
"	border: 2px solid #46a2da;\n"
"	border-radius: 6px;\n"
"}\n"
"\n"
"\n"
"QRadioButton#rdbBooked::indicator::checked \n"
"{\n"
"	border: 2px solid #52beff;\n"
"	border-radius: 6px;\n"
"	background-color: #0088da;  \n"
"	width: 9px; \n"
"	height: 9px; \n"
"\n"
"}")

        self.horizontalLayout_4.addWidget(self.rdbBooked)

        self.rdbNoLine = QRadioButton(self.layoutWidget)
        self.rdbNoLine.setObjectName(u"rdbNoLine")
        self.rdbNoLine.setStyleSheet(u"QRadioButton \n"
"{\n"
"	color: #000;\n"
"	background-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QRadioButton#rdbNoLine::indicator::unchecked:hover \n"
"{\n"
"	background-color: darkgray;\n"
"	border: 2px solid #46a2da;\n"
"	border-radius: 6px;\n"
"}\n"
"\n"
"\n"
"QRadioButton#rdbNoLine::indicator::checked \n"
"{\n"
"	border: 2px solid #52beff;\n"
"	border-radius: 6px;\n"
"	background-color: #0088da;  \n"
"	width: 9px; \n"
"	height: 9px; \n"
"\n"
"}")

        self.horizontalLayout_4.addWidget(self.rdbNoLine)

        self.rdbPending = QRadioButton(self.layoutWidget)
        self.rdbPending.setObjectName(u"rdbPending")
        self.rdbPending.setStyleSheet(u"QRadioButton \n"
"{\n"
"	color: #000;\n"
"	background-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QRadioButton#rdbPending::indicator::unchecked:hover \n"
"{\n"
"	background-color: darkgray;\n"
"	border: 2px solid #46a2da;\n"
"	border-radius: 6px;\n"
"}\n"
"\n"
"\n"
"QRadioButton#rdbPending::indicator::checked \n"
"{\n"
"	border: 2px solid #52beff;\n"
"	border-radius: 6px;\n"
"	background-color: #0088da;  \n"
"	width: 9px; \n"
"	height: 9px; \n"
"\n"
"}")

        self.horizontalLayout_4.addWidget(self.rdbPending)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.rdbSpecial = QRadioButton(self.layoutWidget)
        self.rdbSpecial.setObjectName(u"rdbSpecial")
        self.rdbSpecial.setStyleSheet(u"QRadioButton \n"
"{\n"
"	color: #000;\n"
"	background-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QRadioButton#rdbSpecial::indicator::unchecked:hover \n"
"{\n"
"	background-color: darkgray;\n"
"	border: 2px solid #46a2da;\n"
"	border-radius: 6px;\n"
"}\n"
"\n"
"\n"
"QRadioButton#rdbSpecial::indicator::checked \n"
"{\n"
"	border: 2px solid #52beff;\n"
"	border-radius: 6px;\n"
"	background-color: #0088da;  \n"
"	width: 9px; \n"
"	height: 9px; \n"
"\n"
"}")

        self.horizontalLayout_5.addWidget(self.rdbSpecial)

        self.rdbPostponed = QRadioButton(self.layoutWidget)
        self.rdbPostponed.setObjectName(u"rdbPostponed")
        self.rdbPostponed.setStyleSheet(u"QRadioButton \n"
"{\n"
"	color: #000;\n"
"	background-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QRadioButton#rdbPostponed::indicator::unchecked:hover \n"
"{\n"
"	background-color: darkgray;\n"
"	border: 2px solid #46a2da;\n"
"	border-radius: 6px;\n"
"}\n"
"\n"
"\n"
"QRadioButton#rdbPostponed::indicator::checked \n"
"{\n"
"	border: 2px solid #52beff;\n"
"	border-radius: 6px;\n"
"	background-color: #0088da;  \n"
"	width: 9px; \n"
"	height: 9px; \n"
"\n"
"}")

        self.horizontalLayout_5.addWidget(self.rdbPostponed)

        self.btnRefresh = QRadioButton(self.layoutWidget)
        self.btnRefresh.setObjectName(u"btnRefresh")
        self.btnRefresh.setStyleSheet(u"QRadioButton \n"
"{\n"
"	color: #000;\n"
"	background-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QRadioButton#btnRefresh::indicator::unchecked:hover \n"
"{\n"
"	background-color: darkgray;\n"
"	border: 2px solid #46a2da;\n"
"	border-radius: 6px;\n"
"}\n"
"\n"
"\n"
"QRadioButton#btnRefresh::indicator::checked \n"
"{\n"
"	border: 2px solid #52beff;\n"
"	border-radius: 6px;\n"
"	background-color: #0088da;  \n"
"	width: 9px; \n"
"	height: 9px; \n"
"\n"
"}")
        icon = QIcon()
        icon.addFile(u"2546705.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnRefresh.setIcon(icon)

        self.horizontalLayout_5.addWidget(self.btnRefresh)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 1)
        self.verticalLayout_2.setStretch(3, 1)
        self.verticalLayout_2.setStretch(4, 1)
        self.layoutWidget1 = QWidget(self.gpOfficeInfo)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 380, 279, 251))
        self.formLayout_2 = QFormLayout(self.layoutWidget1)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.layoutWidget1)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_5)

        self.inputOrderDate = QLineEdit(self.layoutWidget1)
        self.inputOrderDate.setObjectName(u"inputOrderDate")
        self.inputOrderDate.setFont(font2)
        self.inputOrderDate.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.inputOrderDate)

        self.label_6 = QLabel(self.layoutWidget1)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_6)

        self.label_7 = QLabel(self.layoutWidget1)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_7)

        self.inputPrice = QLineEdit(self.layoutWidget1)
        self.inputPrice.setObjectName(u"inputPrice")
        self.inputPrice.setFont(font2)
        self.inputPrice.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.inputPrice)

        self.label_8 = QLabel(self.layoutWidget1)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_8)

        self.inputOffService = QLineEdit(self.layoutWidget1)
        self.inputOffService.setObjectName(u"inputOffService")
        self.inputOffService.setFont(font2)
        self.inputOffService.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.inputOffService)

        self.label_11 = QLabel(self.layoutWidget1)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font1)

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.label_11)

        self.inputTaxDiff = QLineEdit(self.layoutWidget1)
        self.inputTaxDiff.setObjectName(u"inputTaxDiff")
        self.inputTaxDiff.setFont(font2)
        self.inputTaxDiff.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.inputTaxDiff)

        self.label_10 = QLabel(self.layoutWidget1)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font1)

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.label_10)

        self.inputEarnedDiff = QLineEdit(self.layoutWidget1)
        self.inputEarnedDiff.setObjectName(u"inputEarnedDiff")
        self.inputEarnedDiff.setFont(font2)
        self.inputEarnedDiff.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout_2.setWidget(6, QFormLayout.FieldRole, self.inputEarnedDiff)

        self.label_9 = QLabel(self.layoutWidget1)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)

        self.formLayout_2.setWidget(6, QFormLayout.LabelRole, self.label_9)

        self.cbSource = QComboBox(self.layoutWidget1)
        self.cbSource.setObjectName(u"cbSource")
        self.cbSource.setCursor(QCursor(Qt.PointingHandCursor))
        self.cbSource.setLayoutDirection(Qt.LeftToRight)
        self.cbSource.setStyleSheet(u"QComboBox::drop-down\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(157, 157, 157, 255),stop:1 rgba(150, 150, 150, 255));\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"    border-left-width: 1px;\n"
"    border-left-color: black;\n"
"    border-left-style: solid; \n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.cbSource)

        self.cbSponser = QComboBox(self.layoutWidget1)
        self.cbSponser.setObjectName(u"cbSponser")
        self.cbSponser.setCursor(QCursor(Qt.PointingHandCursor))
        self.cbSponser.setLayoutDirection(Qt.LeftToRight)
        self.cbSponser.setStyleSheet(u"QComboBox::drop-down\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(157, 157, 157, 255),stop:1 rgba(150, 150, 150, 255));\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"    border-left-width: 1px;\n"
"    border-left-color: black;\n"
"    border-left-style: solid; \n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.cbSponser)

        self.gpcustomerInfo = QGroupBox(self.centralwidget)
        self.gpcustomerInfo.setObjectName(u"gpcustomerInfo")
        self.gpcustomerInfo.setGeometry(QRect(460, 70, 381, 261))
        self.gpcustomerInfo.setStyleSheet(u"QGroupBox \n"
"{\n"
"    border: 1px solid;\n"
"    border-color: #666666;\n"
"    margin-top: 23px;\n"
"\n"
"}\n"
"\n"
"\n"
"QGroupBox#gpcustomerInfo::title  \n"
"{\n"
"    background-color: #a0a2a4;\n"
"    color: #000;\n"
"	subcontrol-position: top left;\n"
"    subcontrol-origin: margin;\n"
"    padding: 5px;\n"
"	border: 1px solid #000;\n"
"	border-bottom: none;\n"
"\n"
"}\n"
"")
        self.formLayoutWidget_3 = QWidget(self.gpcustomerInfo)
        self.formLayoutWidget_3.setObjectName(u"formLayoutWidget_3")
        self.formLayoutWidget_3.setGeometry(QRect(8, 30, 361, 151))
        self.formLayout_3 = QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.formLayoutWidget_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font1)
        self.label_12.setAlignment(Qt.AlignCenter)

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_12)

        self.inputCustomerName = QLineEdit(self.formLayoutWidget_3)
        self.inputCustomerName.setObjectName(u"inputCustomerName")
        self.inputCustomerName.setFont(font2)
        self.inputCustomerName.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.inputCustomerName)

        self.label_13 = QLabel(self.formLayoutWidget_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font1)
        self.label_13.setAlignment(Qt.AlignCenter)

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_13)

        self.inputPhone = QLineEdit(self.formLayoutWidget_3)
        self.inputPhone.setObjectName(u"inputPhone")
        self.inputPhone.setFont(font2)
        self.inputPhone.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.inputPhone)

        self.label_15 = QLabel(self.formLayoutWidget_3)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font1)

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label_15)

        self.inputAdress = QLineEdit(self.formLayoutWidget_3)
        self.inputAdress.setObjectName(u"inputAdress")
        self.inputAdress.setFont(font2)
        self.inputAdress.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.inputAdress)

        self.label_14 = QLabel(self.formLayoutWidget_3)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font1)

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.label_14)

        self.inputToPay = QLineEdit(self.formLayoutWidget_3)
        self.inputToPay.setObjectName(u"inputToPay")
        self.inputToPay.setFont(font2)
        self.inputToPay.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.inputToPay)

        self.label_17 = QLabel(self.gpcustomerInfo)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(320, 220, 44, 29))
        self.label_17.setFont(font1)
        self.label_17.setAlignment(Qt.AlignCenter)
        self.inputPayedBack = QLineEdit(self.gpcustomerInfo)
        self.inputPayedBack.setObjectName(u"inputPayedBack")
        self.inputPayedBack.setGeometry(QRect(141, 220, 141, 32))
        self.inputPayedBack.setFont(font2)
        self.inputPayedBack.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_16 = QLabel(self.gpcustomerInfo)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(322, 182, 42, 29))
        self.label_16.setFont(font1)
        self.label_16.setAlignment(Qt.AlignCenter)
        self.inputProduct = QLineEdit(self.gpcustomerInfo)
        self.inputProduct.setObjectName(u"inputProduct")
        self.inputProduct.setGeometry(QRect(141, 182, 141, 32))
        self.inputProduct.setFont(font2)
        self.inputProduct.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.formLayoutWidget_5 = QWidget(self.gpcustomerInfo)
        self.formLayoutWidget_5.setObjectName(u"formLayoutWidget_5")
        self.formLayoutWidget_5.setGeometry(QRect(10, 180, 131, 72))
        self.formLayout_5 = QFormLayout(self.formLayoutWidget_5)
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.formLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_18 = QLabel(self.formLayoutWidget_5)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font1)

        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.label_18)

        self.label_19 = QLabel(self.formLayoutWidget_5)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font1)

        self.formLayout_5.setWidget(1, QFormLayout.LabelRole, self.label_19)

        self.inputNumBack = QLineEdit(self.formLayoutWidget_5)
        self.inputNumBack.setObjectName(u"inputNumBack")
        self.inputNumBack.setFont(font2)
        self.inputNumBack.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout_5.setWidget(1, QFormLayout.FieldRole, self.inputNumBack)

        self.inputNumProd = QLineEdit(self.formLayoutWidget_5)
        self.inputNumProd.setObjectName(u"inputNumProd")
        self.inputNumProd.setFont(font2)
        self.inputNumProd.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout_5.setWidget(0, QFormLayout.FieldRole, self.inputNumProd)

        self.gpMovementInfo = QGroupBox(self.centralwidget)
        self.gpMovementInfo.setObjectName(u"gpMovementInfo")
        self.gpMovementInfo.setGeometry(QRect(241, 70, 201, 261))
        self.gpMovementInfo.setStyleSheet(u"QGroupBox \n"
"{\n"
"    border: 1px solid;\n"
"    border-color: #666666;\n"
"    margin-top: 23px;\n"
"\n"
"}\n"
"\n"
"\n"
"QGroupBox#gpMovementInfo::title  \n"
"{\n"
"    background-color: #a0a2a4;\n"
"    color: #000;\n"
"	subcontrol-position: top left;\n"
"    subcontrol-origin: margin;\n"
"    padding: 5px;\n"
"	border: 1px solid #000;\n"
"	border-bottom: none;\n"
"\n"
"}\n"
"")
        self.formLayoutWidget_4 = QWidget(self.gpMovementInfo)
        self.formLayoutWidget_4.setObjectName(u"formLayoutWidget_4")
        self.formLayoutWidget_4.setGeometry(QRect(10, 30, 181, 224))
        self.formLayout_4 = QFormLayout(self.formLayoutWidget_4)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_20 = QLabel(self.formLayoutWidget_4)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font1)
        self.label_20.setAlignment(Qt.AlignCenter)

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_20)

        self.label_21 = QLabel(self.formLayoutWidget_4)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font1)
        self.label_21.setAlignment(Qt.AlignCenter)

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.label_21)

        self.inputMovDate = QLineEdit(self.formLayoutWidget_4)
        self.inputMovDate.setObjectName(u"inputMovDate")
        self.inputMovDate.setFont(font2)
        self.inputMovDate.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.inputMovDate)

        self.label_22 = QLabel(self.formLayoutWidget_4)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font1)

        self.formLayout_4.setWidget(2, QFormLayout.LabelRole, self.label_22)

        self.inputTransporter = QLineEdit(self.formLayoutWidget_4)
        self.inputTransporter.setObjectName(u"inputTransporter")
        self.inputTransporter.setFont(font2)
        self.inputTransporter.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout_4.setWidget(2, QFormLayout.FieldRole, self.inputTransporter)

        self.label_23 = QLabel(self.formLayoutWidget_4)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font1)

        self.formLayout_4.setWidget(3, QFormLayout.LabelRole, self.label_23)

        self.label_24 = QLabel(self.formLayoutWidget_4)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font1)

        self.formLayout_4.setWidget(4, QFormLayout.LabelRole, self.label_24)

        self.inputComment = QLineEdit(self.formLayoutWidget_4)
        self.inputComment.setObjectName(u"inputComment")
        self.inputComment.setFont(font2)
        self.inputComment.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout_4.setWidget(4, QFormLayout.FieldRole, self.inputComment)

        self.label_25 = QLabel(self.formLayoutWidget_4)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font1)

        self.formLayout_4.setWidget(5, QFormLayout.LabelRole, self.label_25)

        self.inputShipmentCost = QLineEdit(self.formLayoutWidget_4)
        self.inputShipmentCost.setObjectName(u"inputShipmentCost")
        self.inputShipmentCost.setFont(font2)
        self.inputShipmentCost.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout_4.setWidget(5, QFormLayout.FieldRole, self.inputShipmentCost)

        self.cbMovement = QComboBox(self.formLayoutWidget_4)
        self.cbMovement.setObjectName(u"cbMovement")
        self.cbMovement.setCursor(QCursor(Qt.PointingHandCursor))
        self.cbMovement.setLayoutDirection(Qt.LeftToRight)
        self.cbMovement.setStyleSheet(u"QComboBox::drop-down\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(157, 157, 157, 255),stop:1 rgba(150, 150, 150, 255));\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"    border-left-width: 1px;\n"
"    border-left-color: black;\n"
"    border-left-style: solid; \n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"")

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.cbMovement)

        self.cbSpedition = QComboBox(self.formLayoutWidget_4)
        self.cbSpedition.setObjectName(u"cbSpedition")
        self.cbSpedition.setCursor(QCursor(Qt.PointingHandCursor))
        self.cbSpedition.setLayoutDirection(Qt.LeftToRight)
        self.cbSpedition.setStyleSheet(u"QComboBox::drop-down\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(157, 157, 157, 255),stop:1 rgba(150, 150, 150, 255));\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"    border-left-width: 1px;\n"
"    border-left-color: black;\n"
"    border-left-style: solid; \n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"")

        self.formLayout_4.setWidget(3, QFormLayout.FieldRole, self.cbSpedition)

        self.gpSalerInfo = QGroupBox(self.centralwidget)
        self.gpSalerInfo.setObjectName(u"gpSalerInfo")
        self.gpSalerInfo.setGeometry(QRect(21, 70, 201, 261))
        self.gpSalerInfo.setStyleSheet(u"QGroupBox \n"
"{\n"
"    border: 1px solid;\n"
"    border-color: #666666;\n"
"    margin-top: 23px;\n"
"\n"
"}\n"
"\n"
"\n"
"QGroupBox#gpSalerInfo::title  \n"
"{\n"
"    background-color: #a0a2a4;\n"
"    color: #000;\n"
"	subcontrol-position: top left;\n"
"    subcontrol-origin: margin;\n"
"    padding: 5px;\n"
"	border: 1px solid #000;\n"
"	border-bottom: none;\n"
"\n"
"}\n"
"")
        self.formLayoutWidget_6 = QWidget(self.gpSalerInfo)
        self.formLayoutWidget_6.setObjectName(u"formLayoutWidget_6")
        self.formLayoutWidget_6.setGeometry(QRect(10, 30, 181, 224))
        self.formLayout_6 = QFormLayout(self.formLayoutWidget_6)
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.formLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_26 = QLabel(self.formLayoutWidget_6)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font1)
        self.label_26.setAlignment(Qt.AlignCenter)

        self.formLayout_6.setWidget(0, QFormLayout.LabelRole, self.label_26)

        self.label_27 = QLabel(self.formLayoutWidget_6)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font1)
        self.label_27.setAlignment(Qt.AlignCenter)

        self.formLayout_6.setWidget(1, QFormLayout.LabelRole, self.label_27)

        self.inputRate = QLineEdit(self.formLayoutWidget_6)
        self.inputRate.setObjectName(u"inputRate")
        self.inputRate.setFont(font2)
        self.inputRate.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout_6.setWidget(1, QFormLayout.FieldRole, self.inputRate)

        self.label_28 = QLabel(self.formLayoutWidget_6)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font1)

        self.formLayout_6.setWidget(2, QFormLayout.LabelRole, self.label_28)

        self.inputDiscount = QLineEdit(self.formLayoutWidget_6)
        self.inputDiscount.setObjectName(u"inputDiscount")
        self.inputDiscount.setFont(font2)
        self.inputDiscount.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout_6.setWidget(2, QFormLayout.FieldRole, self.inputDiscount)

        self.label_29 = QLabel(self.formLayoutWidget_6)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font1)

        self.formLayout_6.setWidget(3, QFormLayout.LabelRole, self.label_29)

        self.label_30 = QLabel(self.formLayoutWidget_6)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font1)

        self.formLayout_6.setWidget(4, QFormLayout.LabelRole, self.label_30)

        self.inputShippingRefund = QLineEdit(self.formLayoutWidget_6)
        self.inputShippingRefund.setObjectName(u"inputShippingRefund")
        self.inputShippingRefund.setFont(font2)
        self.inputShippingRefund.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout_6.setWidget(4, QFormLayout.FieldRole, self.inputShippingRefund)

        self.label_31 = QLabel(self.formLayoutWidget_6)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font1)

        self.formLayout_6.setWidget(5, QFormLayout.LabelRole, self.label_31)

        self.inputDeliveryDate = QLineEdit(self.formLayoutWidget_6)
        self.inputDeliveryDate.setObjectName(u"inputDeliveryDate")
        self.inputDeliveryDate.setFont(font2)
        self.inputDeliveryDate.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout_6.setWidget(5, QFormLayout.FieldRole, self.inputDeliveryDate)

        self.cbMarketingAgents = QComboBox(self.formLayoutWidget_6)
        self.cbMarketingAgents.setObjectName(u"cbMarketingAgents")
        self.cbMarketingAgents.setCursor(QCursor(Qt.PointingHandCursor))
        self.cbMarketingAgents.setLayoutDirection(Qt.LeftToRight)
        self.cbMarketingAgents.setStyleSheet(u"QComboBox::drop-down\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(157, 157, 157, 255),stop:1 rgba(150, 150, 150, 255));\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"    border-left-width: 1px;\n"
"    border-left-color: black;\n"
"    border-left-style: solid; \n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"")

        self.formLayout_6.setWidget(0, QFormLayout.FieldRole, self.cbMarketingAgents)

        self.inputDiscountComm = QLineEdit(self.formLayoutWidget_6)
        self.inputDiscountComm.setObjectName(u"inputDiscountComm")
        self.inputDiscountComm.setFont(font2)
        self.inputDiscountComm.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout_6.setWidget(3, QFormLayout.FieldRole, self.inputDiscountComm)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(21, 650, 821, 71))
        self.frame_2.setFrameShape(QFrame.Box)
        self.frame_2.setFrameShadow(QFrame.Sunken)
        self.horizontalLayoutWidget_6 = QWidget(self.frame_2)
        self.horizontalLayoutWidget_6.setObjectName(u"horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QRect(410, 20, 401, 31))
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.btnAdd = QPushButton(self.horizontalLayoutWidget_6)
        self.btnAdd.setObjectName(u"btnAdd")
        self.btnAdd.setStyleSheet(u"QPushButton {\n"
"  background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(184, 184,      184, 255),stop:1 rgba(159, 159, 159, 255));\n"
"	color: #000;\n"
"	min-width: 80px;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: #051a39;\n"
"	padding: 5px;\n"
"}\n"
"QPushButton#btnAdd:hover\n"
"{\n"
"	background-color: rgba(70,162,218,50%);\n"
"	border: 1px solid #46a2da;\n"
"\n"
"}\n"
"\n"
"QPushButton#btnAdd:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}")

        self.horizontalLayout_6.addWidget(self.btnAdd)

        self.btnEdit = QPushButton(self.horizontalLayoutWidget_6)
        self.btnEdit.setObjectName(u"btnEdit")
        self.btnEdit.setStyleSheet(u"QPushButton {\n"
"  background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(184, 184,      184, 255),stop:1 rgba(159, 159, 159, 255));\n"
"	color: #000;\n"
"	min-width: 80px;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: #051a39;\n"
"	padding: 5px;\n"
"}\n"
"QPushButton#btnEdit:hover\n"
"{\n"
"	background-color: rgba(70,162,218,50%);\n"
"	border: 1px solid #46a2da;\n"
"\n"
"}\n"
"\n"
"QPushButton#btnEdit:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}")

        self.horizontalLayout_6.addWidget(self.btnEdit)

        self.btnDelete = QPushButton(self.horizontalLayoutWidget_6)
        self.btnDelete.setObjectName(u"btnDelete")
        self.btnDelete.setStyleSheet(u"QPushButton {\n"
"  background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(184, 184,      184, 255),stop:1 rgba(159, 159, 159, 255));\n"
"	color: #000;\n"
"	min-width: 80px;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: #051a39;\n"
"	padding: 5px;\n"
"}\n"
"QPushButton#btnDelete:hover\n"
"{\n"
"	background-color: rgba(70,162,218,50%);\n"
"	border: 1px solid #46a2da;\n"
"\n"
"}\n"
"\n"
"QPushButton#btnDelete:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}")

        self.horizontalLayout_6.addWidget(self.btnDelete)

        self.btnBack = QPushButton(self.frame_2)
        self.btnBack.setObjectName(u"btnBack")
        self.btnBack.setGeometry(QRect(10, 20, 153, 28))
        self.btnBack.setStyleSheet(u"QPushButton {\n"
"  background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(184, 184,      184, 255),stop:1 rgba(159, 159, 159, 255));\n"
"	color: #000;\n"
"	min-width: 80px;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: #051a39;\n"
"	padding: 5px;\n"
"}\n"
"QPushButton#btnBack:hover\n"
"{\n"
"	background-color: rgba(70,162,218,50%);\n"
"	border: 1px solid #46a2da;\n"
"\n"
"}\n"
"\n"
"QPushButton#btnBack:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        self.TableDataEntry = QTableWidget(self.centralwidget)
        if (self.TableDataEntry.columnCount() < 10):
            self.TableDataEntry.setColumnCount(10)
        __qtablewidgetitem = QTableWidgetItem()
        self.TableDataEntry.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.TableDataEntry.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.TableDataEntry.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.TableDataEntry.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.TableDataEntry.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.TableDataEntry.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.TableDataEntry.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.TableDataEntry.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.TableDataEntry.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.TableDataEntry.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        self.TableDataEntry.setObjectName(u"TableDataEntry")
        self.TableDataEntry.setGeometry(QRect(20, 370, 821, 261))
        self.TableDataEntry.setStyleSheet(u"QHeaderView#TableDataEntry::section\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(227, 227, 227, 255),stop:1 rgba(187, 187, 187, 255));\n"
"	border: 1px solid #000;\n"
"    color: #000;\n"
"    text-align: left;\n"
"	padding: 4px;\n"
"	\n"
"}\n"
"\n"
"\n"
"QHeaderView#TableDataEntry::section:disabled\n"
"{\n"
"    background-color: #525251;\n"
"    color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView#TableDataEntry::section:checked\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(227, 227, 227, 255),stop:1 rgba(187, 187, 187, 255));\n"
"    color: #000;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView#TableDataEntry::section::vertical::first,\n"
"QHeaderView#TableDataEntry::section::vertical::only-one\n"
"{\n"
"    border-top: 1px solid #353635;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView#TableDataEntry::section::vertical\n"
"{\n"
"    border-top: 1px solid #353635;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView#TableDataEntry::section::"
                        "horizontal::first,\n"
"QHeaderView#TableDataEntry::section::horizontal::only-one\n"
"{\n"
"    border-left: 1px solid #353635;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView#TableDataEntry::section::horizontal\n"
"{\n"
"    border-left: 1px solid #353635;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableCornerButton#TableDataEntry::section\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(227, 227, 227, 255),stop:1 rgba(187, 187, 187, 255));\n"
"	border: 1px solid #000;\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"QScrollBar:horizontal\n"
"{\n"
"    border: 1px solid #222222;\n"
"    background-color: #9d9d9d;\n"
"    height: 13px;\n"
"    margin: 0px 16px 0 16px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(227, 227, 227, 255),stop:1 rgba(187, 187, 187, 255));\n"
"	border: 1px solid #2d2d2d;\n"
"    min-height: 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:horizontal\n"
"{\n"
"	back"
                        "ground-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(227, 227, 227, 255),stop:1 rgba(187, 187, 187, 255));\n"
"	border: 1px solid #2d2d2d;\n"
"    width: 15px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:horizontal\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(227, 227, 227, 255),stop:1 rgba(187, 187, 187, 255));\n"
"	border: 1px solid #2d2d2d;\n"
"    width: 15px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::right-arrow:horizontal\n"
"{\n"
"    image: url(://arrow-right.png);\n"
"    width: 6px;\n"
"    height: 6px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::left-arrow:horizontal\n"
"{\n"
"    image: url(://arrow-left.png);\n"
"    width: 6px;\n"
"    height: 6px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"    background: none;\n"
"\n"
"}\n"
"\n"
"\n"
""
                        "QScrollBar:vertical\n"
"{\n"
"    background-color: #9d9d9d;\n"
"    width: 13px;\n"
"	border: 1px solid #2d2d2d;\n"
"    margin: 16px 0px 16px 0px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(227, 227, 227, 255),stop:1 rgba(187, 187, 187, 255));\n"
"	border: 1px solid #2d2d2d;\n"
"    min-height: 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(227, 227, 227, 255),stop:1 rgba(187, 187, 187, 255));\n"
"	border: 1px solid #2d2d2d;\n"
"    height: 15px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(227, 227, 227, 255),stop:1 rgba(187, 187, 187, 255));\n"
"	border: 1px solid #2d2d2d;\n"
"    height: 15px;\n"
"    subcontrol-pos"
                        "ition: top;\n"
"    subcontrol-origin: margin;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::up-arrow:vertical\n"
"{\n"
"    image: url(://arrow-up.png);\n"
"    width: 6px;\n"
"    height: 6px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::down-arrow:vertical\n"
"{\n"
"    image: url(://arrow-down.png);\n"
"    width: 6px;\n"
"    height: 6px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"    background: none;\n"
"\n"
"}")
        self.TableDataEntry.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.TableDataEntry.setSelectionBehavior(QAbstractItemView.SelectRows)
        Data_Entry.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Data_Entry)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1182, 24))
        self.menubar.setStyleSheet(u"QMenuBar \n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(227, 227, 227, 255),stop:1 rgba(187, 187, 187, 255));\n"
"	border: 1px solid #f1f1f1;\n"
"	color: #000;\n"
"\n"
"}\n"
"")
        Data_Entry.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Data_Entry)
        self.statusbar.setObjectName(u"statusbar")
        Data_Entry.setStatusBar(self.statusbar)

        self.retranslateUi(Data_Entry)

        self.cbSource.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(Data_Entry)
    # setupUi

    def retranslateUi(self, Data_Entry):
        Data_Entry.setWindowTitle(QCoreApplication.translate("Data_Entry", u"Data_Entry", None))
        self.label.setText(QCoreApplication.translate("Data_Entry", u"\u0634\u0631\u0643\u0629 \u062a\u064a\u0627\u0645\u0648 \u062a\u064a\u0645\u0648 \u0644\u0644\u062a\u0633\u0648\u064a\u0642 \u0627\u0644\u0627\u0644\u0643\u062a\u0631\u0648\u0646\u064a", None))
        self.gpOfficeInfo.setTitle(QCoreApplication.translate("Data_Entry", u"\u0645\u0639\u0644\u0648\u0645\u0627\u062a \u0627\u0644\u0645\u0643\u062a\u0628", None))
        self.label_2.setText(QCoreApplication.translate("Data_Entry", u"\u0631\u0642\u0645 \u0627\u0644\u0637\u0644\u0628", None))
        self.label_3.setText(QCoreApplication.translate("Data_Entry", u"\u0627\u0644\u062d\u0627\u0644\u0629", None))
        self.lblUnknown.setText("")
        self.rdbnew.setText(QCoreApplication.translate("Data_Entry", u"\u062c\u062f\u064a\u062f", None))
        self.rdbDone.setText(QCoreApplication.translate("Data_Entry", u"\u062a\u0645", None))
        self.rdbnotAvailble.setText(QCoreApplication.translate("Data_Entry", u"\u063a\u064a\u0631 \u0645\u062a\u0648\u0641\u0631", None))
        self.rdbDelivery.setText(QCoreApplication.translate("Data_Entry", u"\u062a\u0648\u0635\u064a\u0644", None))
        self.rdbPayed.setText(QCoreApplication.translate("Data_Entry", u"\u0645\u0633\u062f\u062f", None))
        self.rdbRefund.setText(QCoreApplication.translate("Data_Entry", u"\u0645\u0631\u062a\u062c\u0639", None))
        self.rdbDelivered.setText(QCoreApplication.translate("Data_Entry", u"\u0645\u0634\u062d\u0648\u0646", None))
        self.rdbNoAsnwer.setText(QCoreApplication.translate("Data_Entry", u"\u0644\u0645 \u064a\u062c\u0628", None))
        self.rdbCanceld.setText(QCoreApplication.translate("Data_Entry", u"\u0645\u0644\u063a\u064a", None))
        self.rdbBooked.setText(QCoreApplication.translate("Data_Entry", u"\u0645\u062d\u062c\u0648\u0632", None))
        self.rdbNoLine.setText(QCoreApplication.translate("Data_Entry", u"\u0627\u0644\u062e\u0637 \u0645\u063a\u0644\u0642", None))
        self.rdbPending.setText(QCoreApplication.translate("Data_Entry", u"\u0645\u0639\u0644\u0642", None))
        self.rdbSpecial.setText(QCoreApplication.translate("Data_Entry", u"\u062e\u0627\u0635", None))
        self.rdbPostponed.setText(QCoreApplication.translate("Data_Entry", u"\u0645\u0624\u062c\u0644", None))
        self.btnRefresh.setText("")
        self.label_5.setText(QCoreApplication.translate("Data_Entry", u"\u062a\u0627\u0631\u064a\u062e \u0627\u0644\u0637\u0644\u0628", None))
        self.label_6.setText(QCoreApplication.translate("Data_Entry", u"\u0627\u0644\u0645\u0635\u062f\u0631", None))
        self.label_7.setText(QCoreApplication.translate("Data_Entry", u"\u0633\u0639\u0631 \u0627\u0644\u0628\u0636\u0627\u0639\u0629", None))
        self.label_8.setText(QCoreApplication.translate("Data_Entry", u"\u0627\u0644\u0645\u0645\u0648\u0644", None))
        self.label_11.setText(QCoreApplication.translate("Data_Entry", u"\u062e\u062f\u0645\u0627\u062a \u0627\u0644\u0645\u0643\u062a\u0628", None))
        self.label_10.setText(QCoreApplication.translate("Data_Entry", u"\u0641\u0631\u0642 \u0631\u0633\u0648\u0645", None))
        self.label_9.setText(QCoreApplication.translate("Data_Entry", u"\u0641\u0631\u0642 \u0645\u0643\u062a\u0633\u0628", None))
        self.cbSource.setCurrentText("")
        self.gpcustomerInfo.setTitle(QCoreApplication.translate("Data_Entry", u"\u0645\u0639\u0644\u0648\u0645\u0627\u062a \u0627\u0644\u0632\u0628\u0648\u0646", None))
        self.label_12.setText(QCoreApplication.translate("Data_Entry", u"\u0627\u0633\u0645 \u0627\u0644\u0632\u0628\u0648\u0646", None))
        self.label_13.setText(QCoreApplication.translate("Data_Entry", u"\u0627\u0644\u0647\u0627\u062a\u0641", None))
        self.label_15.setText(QCoreApplication.translate("Data_Entry", u"\u0627\u0644\u0639\u0646\u0648\u0627\u0646", None))
        self.label_14.setText(QCoreApplication.translate("Data_Entry", u"\u0627\u0644\u0645\u0628\u0644\u063a \u0627\u0644\u0645\u0637\u0644\u0648\u0628", None))
        self.label_17.setText(QCoreApplication.translate("Data_Entry", u"\u0627\u0644\u0645\u0631\u062a\u062c\u0639", None))
        self.label_16.setText(QCoreApplication.translate("Data_Entry", u"\u0627\u0644\u0628\u0636\u0627\u0639\u0629", None))
        self.label_18.setText(QCoreApplication.translate("Data_Entry", u"\u0627\u0644\u0639\u062f\u062f", None))
        self.label_19.setText(QCoreApplication.translate("Data_Entry", u"\u0627\u0644\u0639\u062f\u062f", None))
        self.gpMovementInfo.setTitle(QCoreApplication.translate("Data_Entry", u"\u0645\u0639\u0644\u0648\u0645\u0627\u062a \u0627\u0644\u062d\u0631\u0643\u0629", None))
        self.label_20.setText(QCoreApplication.translate("Data_Entry", u"\u0627\u0644\u062d\u0631\u0643\u0629", None))
        self.label_21.setText(QCoreApplication.translate("Data_Entry", u"\u062a\u0627\u0631\u064a\u062e \u0627\u0644\u062d\u0631\u0643\u0629", None))
        self.label_22.setText(QCoreApplication.translate("Data_Entry", u"\u0627\u0644\u0646\u0627\u0642\u0644", None))
        self.label_23.setText(QCoreApplication.translate("Data_Entry", u"\u0634\u0631\u0643\u0629 \u0627\u0644\u0634\u062d\u0646", None))
        self.label_24.setText(QCoreApplication.translate("Data_Entry", u"\u0631\u0642\u0645 \u0627\u0644\u0627\u0634\u0639\u0627\u0631", None))
        self.label_25.setText(QCoreApplication.translate("Data_Entry", u"\u0627\u062c\u0648\u0631 \u0627\u0644\u0634\u062d\u0646", None))
        self.cbMovement.setCurrentText("")
        self.gpSalerInfo.setTitle(QCoreApplication.translate("Data_Entry", u"\u0645\u0639\u0644\u0648\u0645\u0627\u062a \u0627\u0644\u0645\u0633\u0648\u0642\u0629", None))
        self.label_26.setText(QCoreApplication.translate("Data_Entry", u"\u0627\u0644\u0645\u0646\u062f\u0648\u0628\u0629/\u0627\u0644\u0645\u0633\u0648\u0642\u0629", None))
        self.label_27.setText(QCoreApplication.translate("Data_Entry", u"\u0627\u0644\u0646\u0633\u0628\u0629", None))
        self.label_28.setText(QCoreApplication.translate("Data_Entry", u"\u0627\u0644\u062e\u0635\u0645", None))
        self.label_29.setText(QCoreApplication.translate("Data_Entry", u"\u0628\u064a\u0627\u0646 \u0627\u0644\u062e\u0635\u0645", None))
        self.label_30.setText(QCoreApplication.translate("Data_Entry", u"\u062a\u0639\u0648\u064a\u0636 \u0627\u0644\u0634\u062d\u0646", None))
        self.label_31.setText(QCoreApplication.translate("Data_Entry", u"\u062a\u0627\u0631\u064a\u062e \u0627\u0644\u0627\u0633\u062a\u0644\u0627\u0645", None))
        self.btnAdd.setText(QCoreApplication.translate("Data_Entry", u"\u0627\u0636\u0627\u0641\u0629", None))
        self.btnEdit.setText(QCoreApplication.translate("Data_Entry", u"\u062a\u0639\u062f\u064a\u0644 \u0627\u0644\u0637\u0644\u0628", None))
        self.btnDelete.setText(QCoreApplication.translate("Data_Entry", u"\u0645\u0633\u062d", None))
        self.btnBack.setText(QCoreApplication.translate("Data_Entry", u"\u0631\u062c\u0648\u0639", None))
        ___qtablewidgetitem = self.TableDataEntry.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Data_Entry", u"\u0631\u0642\u0645 \u0627\u0644\u0637\u0644\u0628", None));
        ___qtablewidgetitem1 = self.TableDataEntry.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Data_Entry", u"\u0627\u0644\u062d\u0627\u0644\u0629", None));
        ___qtablewidgetitem2 = self.TableDataEntry.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Data_Entry", u"\u0627\u0633\u0645 \u0627\u0644\u0632\u0628\u0648\u0646", None));
        ___qtablewidgetitem3 = self.TableDataEntry.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Data_Entry", u"\u0627\u0644\u0639\u0646\u0648\u0627\u0646", None));
        ___qtablewidgetitem4 = self.TableDataEntry.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Data_Entry", u"\u0627\u0644\u0645\u0628\u0644\u063a \u0627\u0644\u0645\u0637\u0644\u0648\u0628", None));
        ___qtablewidgetitem5 = self.TableDataEntry.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Data_Entry", u"\u0627\u0644\u0628\u0636\u0627\u0639\u0629", None));
        ___qtablewidgetitem6 = self.TableDataEntry.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Data_Entry", u"\u0627\u0644\u0645\u0646\u062f\u0648\u0628\u0629", None));
        ___qtablewidgetitem7 = self.TableDataEntry.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Data_Entry", u"\u0627\u0644\u062e\u0635\u0645", None));
        ___qtablewidgetitem8 = self.TableDataEntry.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Data_Entry", u"\u0627\u0644\u062d\u0631\u0643\u0629", None));
        ___qtablewidgetitem9 = self.TableDataEntry.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Data_Entry", u"\u062a\u0627\u0631\u064a\u062e \u0627\u0644\u062d\u0631\u0643\u0629", None));
    # retranslateUi

