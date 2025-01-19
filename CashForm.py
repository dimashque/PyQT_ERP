# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CashForm.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QListView, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTabWidget, QWidget)

class Ui_CashForm(object):
    def setupUi(self, CashForm):
        if not CashForm.objectName():
            CashForm.setObjectName(u"CashForm")
        CashForm.resize(792, 871)
        CashForm.setLayoutDirection(Qt.RightToLeft)
        CashForm.setStyleSheet(u"background-color: #e4e4e4;\n"
"	color: #000;\n"
"	selection-background-color: #46a2da;\n"
"	selection-color: #fff;")
        self.centralwidget = QWidget(CashForm)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabCashForm = QTabWidget(self.centralwidget)
        self.tabCashForm.setObjectName(u"tabCashForm")
        self.tabCashForm.setGeometry(QRect(10, 20, 771, 191))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(12)
        font.setBold(True)
        self.tabCashForm.setFont(font)
        self.tabCashForm.setTabShape(QTabWidget.Triangular)
        self.tabExpenses = QWidget()
        self.tabExpenses.setObjectName(u"tabExpenses")
        self.gridLayoutWidget = QWidget(self.tabExpenses)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 20, 741, 80))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)
        self.label_7.setLayoutDirection(Qt.RightToLeft)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_7, 0, 1, 1, 1)

        self.inputComment1 = QLineEdit(self.gridLayoutWidget)
        self.inputComment1.setObjectName(u"inputComment1")
        font1 = QFont()
        font1.setPointSize(14)
        self.inputComment1.setFont(font1)
        self.inputComment1.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.inputComment1, 1, 2, 1, 1)

        self.inputSource1 = QLineEdit(self.gridLayoutWidget)
        self.inputSource1.setObjectName(u"inputSource1")
        self.inputSource1.setFont(font1)
        self.inputSource1.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.inputSource1, 1, 1, 1, 1)

        self.inputAmount1 = QLineEdit(self.gridLayoutWidget)
        self.inputAmount1.setObjectName(u"inputAmount1")
        self.inputAmount1.setFont(font1)
        self.inputAmount1.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.inputAmount1, 1, 0, 1, 1)

        self.label_9 = QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)
        self.label_9.setLayoutDirection(Qt.RightToLeft)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_9, 0, 3, 1, 1)

        self.label_8 = QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)
        self.label_8.setLayoutDirection(Qt.RightToLeft)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_8, 0, 2, 1, 1)

        self.label_6 = QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)
        self.label_6.setLayoutDirection(Qt.RightToLeft)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)

        self.inputSum1 = QLineEdit(self.gridLayoutWidget)
        self.inputSum1.setObjectName(u"inputSum1")
        self.inputSum1.setFont(font1)
        self.inputSum1.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.inputSum1, 1, 3, 1, 1)

        self.btnPaymentEntry = QPushButton(self.tabExpenses)
        self.btnPaymentEntry.setObjectName(u"btnPaymentEntry")
        self.btnPaymentEntry.setGeometry(QRect(10, 120, 121, 28))
        self.btnPaymentEntry.setStyleSheet(u"QPushButton {\n"
"  background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(184, 184,      184, 255),stop:1 rgba(159, 159, 159, 255));\n"
"	color: #000;\n"
"	min-width: 80px;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: #051a39;\n"
"	padding: 5px;\n"
"}\n"
"QPushButton#btnPaymentEntry:hover\n"
"{\n"
"	background-color: rgba(70,162,218,50%);\n"
"	border: 1px solid #46a2da;\n"
"\n"
"}\n"
"\n"
"QPushButton#btnPaymentEntry:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        self.tabCashForm.addTab(self.tabExpenses, "")
        self.tabEarnedEntry = QWidget()
        self.tabEarnedEntry.setObjectName(u"tabEarnedEntry")
        self.gridLayoutWidget_2 = QWidget(self.tabEarnedEntry)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(10, 20, 741, 80))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.gridLayoutWidget_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)
        self.label_10.setLayoutDirection(Qt.RightToLeft)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_10, 0, 1, 1, 1)

        self.label_12 = QLabel(self.gridLayoutWidget_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font)
        self.label_12.setLayoutDirection(Qt.RightToLeft)
        self.label_12.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_12, 0, 2, 1, 1)

        self.inputSum_2 = QLineEdit(self.gridLayoutWidget_2)
        self.inputSum_2.setObjectName(u"inputSum_2")
        self.inputSum_2.setFont(font1)
        self.inputSum_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.inputSum_2, 1, 3, 1, 1)

        self.inputAmount_2 = QLineEdit(self.gridLayoutWidget_2)
        self.inputAmount_2.setObjectName(u"inputAmount_2")
        self.inputAmount_2.setFont(font1)
        self.inputAmount_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.inputAmount_2, 1, 0, 1, 1)

        self.inputSource_2 = QLineEdit(self.gridLayoutWidget_2)
        self.inputSource_2.setObjectName(u"inputSource_2")
        self.inputSource_2.setFont(font1)
        self.inputSource_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.inputSource_2, 1, 1, 1, 1)

        self.inputComment_2 = QLineEdit(self.gridLayoutWidget_2)
        self.inputComment_2.setObjectName(u"inputComment_2")
        self.inputComment_2.setFont(font1)
        self.inputComment_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.inputComment_2, 1, 2, 1, 1)

        self.label_13 = QLabel(self.gridLayoutWidget_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font)
        self.label_13.setLayoutDirection(Qt.RightToLeft)
        self.label_13.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_13, 0, 0, 1, 1)

        self.label_11 = QLabel(self.gridLayoutWidget_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font)
        self.label_11.setLayoutDirection(Qt.RightToLeft)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_11, 0, 3, 1, 1)

        self.btnEarnedEntry = QPushButton(self.tabEarnedEntry)
        self.btnEarnedEntry.setObjectName(u"btnEarnedEntry")
        self.btnEarnedEntry.setGeometry(QRect(10, 120, 121, 28))
        self.btnEarnedEntry.setStyleSheet(u"QPushButton {\n"
"  background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(184, 184,      184, 255),stop:1 rgba(159, 159, 159, 255));\n"
"	color: #000;\n"
"	min-width: 80px;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: #051a39;\n"
"	padding: 5px;\n"
"}\n"
"QPushButton#btnEarnedEntry:hover\n"
"{\n"
"	background-color: rgba(70,162,218,50%);\n"
"	border: 1px solid #46a2da;\n"
"\n"
"}\n"
"\n"
"QPushButton#btnEarnedEntry:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        self.tabCashForm.addTab(self.tabEarnedEntry, "")
        self.tabWithdrwanEntry = QWidget()
        self.tabWithdrwanEntry.setObjectName(u"tabWithdrwanEntry")
        self.gridLayoutWidget_3 = QWidget(self.tabWithdrwanEntry)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(10, 20, 741, 80))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.gridLayoutWidget_3)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font)
        self.label_14.setLayoutDirection(Qt.RightToLeft)
        self.label_14.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_14, 0, 1, 1, 1)

        self.label_15 = QLabel(self.gridLayoutWidget_3)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font)
        self.label_15.setLayoutDirection(Qt.RightToLeft)
        self.label_15.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_15, 0, 2, 1, 1)

        self.inputSum_3 = QLineEdit(self.gridLayoutWidget_3)
        self.inputSum_3.setObjectName(u"inputSum_3")
        self.inputSum_3.setFont(font1)
        self.inputSum_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_3.addWidget(self.inputSum_3, 1, 3, 1, 1)

        self.inputAmount_3 = QLineEdit(self.gridLayoutWidget_3)
        self.inputAmount_3.setObjectName(u"inputAmount_3")
        self.inputAmount_3.setFont(font1)
        self.inputAmount_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_3.addWidget(self.inputAmount_3, 1, 0, 1, 1)

        self.inputSource_3 = QLineEdit(self.gridLayoutWidget_3)
        self.inputSource_3.setObjectName(u"inputSource_3")
        self.inputSource_3.setFont(font1)
        self.inputSource_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_3.addWidget(self.inputSource_3, 1, 1, 1, 1)

        self.inputComment_3 = QLineEdit(self.gridLayoutWidget_3)
        self.inputComment_3.setObjectName(u"inputComment_3")
        self.inputComment_3.setFont(font1)
        self.inputComment_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_3.addWidget(self.inputComment_3, 1, 2, 1, 1)

        self.label_16 = QLabel(self.gridLayoutWidget_3)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font)
        self.label_16.setLayoutDirection(Qt.RightToLeft)
        self.label_16.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_16, 0, 0, 1, 1)

        self.label_17 = QLabel(self.gridLayoutWidget_3)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font)
        self.label_17.setLayoutDirection(Qt.RightToLeft)
        self.label_17.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_17, 0, 3, 1, 1)

        self.btnWithdrawnEntry = QPushButton(self.tabWithdrwanEntry)
        self.btnWithdrawnEntry.setObjectName(u"btnWithdrawnEntry")
        self.btnWithdrawnEntry.setGeometry(QRect(10, 120, 121, 28))
        self.btnWithdrawnEntry.setStyleSheet(u"QPushButton {\n"
"  background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(184, 184,      184, 255),stop:1 rgba(159, 159, 159, 255));\n"
"	color: #000;\n"
"	min-width: 80px;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: #051a39;\n"
"	padding: 5px;\n"
"}\n"
"QPushButton#btnWithdrawnEntry:hover\n"
"{\n"
"	background-color: rgba(70,162,218,50%);\n"
"	border: 1px solid #46a2da;\n"
"\n"
"}\n"
"\n"
"QPushButton#btnWithdrawnEntry:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        self.tabCashForm.addTab(self.tabWithdrwanEntry, "")
        self.tabPayWithdrawn = QWidget()
        self.tabPayWithdrawn.setObjectName(u"tabPayWithdrawn")
        self.gridLayoutWidget_4 = QWidget(self.tabPayWithdrawn)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(10, 20, 741, 80))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_18 = QLabel(self.gridLayoutWidget_4)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font)
        self.label_18.setLayoutDirection(Qt.RightToLeft)
        self.label_18.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_18, 0, 1, 1, 1)

        self.label_19 = QLabel(self.gridLayoutWidget_4)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font)
        self.label_19.setLayoutDirection(Qt.RightToLeft)
        self.label_19.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_19, 0, 2, 1, 1)

        self.inputSum_4 = QLineEdit(self.gridLayoutWidget_4)
        self.inputSum_4.setObjectName(u"inputSum_4")
        self.inputSum_4.setFont(font1)
        self.inputSum_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_4.addWidget(self.inputSum_4, 1, 3, 1, 1)

        self.inputAmount_4 = QLineEdit(self.gridLayoutWidget_4)
        self.inputAmount_4.setObjectName(u"inputAmount_4")
        self.inputAmount_4.setFont(font1)
        self.inputAmount_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_4.addWidget(self.inputAmount_4, 1, 0, 1, 1)

        self.inputSource_4 = QLineEdit(self.gridLayoutWidget_4)
        self.inputSource_4.setObjectName(u"inputSource_4")
        self.inputSource_4.setFont(font1)
        self.inputSource_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_4.addWidget(self.inputSource_4, 1, 1, 1, 1)

        self.inputComment_4 = QLineEdit(self.gridLayoutWidget_4)
        self.inputComment_4.setObjectName(u"inputComment_4")
        self.inputComment_4.setFont(font1)
        self.inputComment_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_4.addWidget(self.inputComment_4, 1, 2, 1, 1)

        self.label_20 = QLabel(self.gridLayoutWidget_4)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font)
        self.label_20.setLayoutDirection(Qt.RightToLeft)
        self.label_20.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_20, 0, 0, 1, 1)

        self.label_21 = QLabel(self.gridLayoutWidget_4)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font)
        self.label_21.setLayoutDirection(Qt.RightToLeft)
        self.label_21.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_21, 0, 3, 1, 1)

        self.btnWithdrawnPaymentEntry = QPushButton(self.tabPayWithdrawn)
        self.btnWithdrawnPaymentEntry.setObjectName(u"btnWithdrawnPaymentEntry")
        self.btnWithdrawnPaymentEntry.setGeometry(QRect(10, 120, 121, 28))
        self.btnWithdrawnPaymentEntry.setStyleSheet(u"QPushButton {\n"
"  background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(184, 184,      184, 255),stop:1 rgba(159, 159, 159, 255));\n"
"	color: #000;\n"
"	min-width: 80px;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: #051a39;\n"
"	padding: 5px;\n"
"}\n"
"QPushButton#btnWithdrawnPaymentEntry:hover\n"
"{\n"
"	background-color: rgba(70,162,218,50%);\n"
"	border: 1px solid #46a2da;\n"
"\n"
"}\n"
"\n"
"QPushButton#btnWithdrawnPaymentEntry:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        self.tabCashForm.addTab(self.tabPayWithdrawn, "")
        self.btnBack = QPushButton(self.centralwidget)
        self.btnBack.setObjectName(u"btnBack")
        self.btnBack.setGeometry(QRect(10, 790, 191, 28))
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
        self.lblDate = QLabel(self.centralwidget)
        self.lblDate.setObjectName(u"lblDate")
        self.lblDate.setGeometry(QRect(20, -10, 241, 31))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(9)
        font2.setItalic(True)
        self.lblDate.setFont(font2)
        self.lblDate.setStyleSheet(u"")
        self.tabCashList = QTabWidget(self.centralwidget)
        self.tabCashList.setObjectName(u"tabCashList")
        self.tabCashList.setGeometry(QRect(10, 230, 771, 541))
        self.tabCashList.setFont(font)
        self.tabEarned = QWidget()
        self.tabEarned.setObjectName(u"tabEarned")
        self.label_3 = QLabel(self.tabEarned)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(450, 10, 49, 21))
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(Qt.RightToLeft)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_5 = QLabel(self.tabEarned)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(40, 10, 49, 21))
        self.label_5.setFont(font)
        self.label_5.setLayoutDirection(Qt.RightToLeft)
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.tabEarned)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(598, 10, 61, 21))
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(Qt.RightToLeft)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_4 = QLabel(self.tabEarned)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(700, 10, 49, 21))
        self.label_4.setFont(font)
        self.label_4.setLayoutDirection(Qt.RightToLeft)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_22 = QLabel(self.tabEarned)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(220, 10, 49, 21))
        self.label_22.setFont(font)
        self.label_22.setLayoutDirection(Qt.RightToLeft)
        self.label_22.setAlignment(Qt.AlignCenter)
        self.listViewCashList = QListView(self.tabEarned)
        self.listViewCashList.setObjectName(u"listViewCashList")
        self.listViewCashList.setGeometry(QRect(10, 40, 731, 331))
        self.listViewCashList.setStyleSheet(u"QListView \n"
"{\n"
"	background-color: #f6f6f6;\n"
"    border : none;\n"
"    color: #000;\n"
"    show-decoration-selected: 1; \n"
"    outline: 0;\n"
"	border: 1px solid gray;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView#listViewCashList::disabled \n"
"{\n"
"	background-color: #656565;\n"
"	color: #1b1b1b;\n"
"    border: 1px solid #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView#listViewCashList::item \n"
"{\n"
"	background-color: #f6f6f6;\n"
"    padding: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView#listViewCashList::item:alternate \n"
"{\n"
"    background-color: #c6c6c6;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView#listViewCashList::item:alternate:selected\n"
"{\n"
"    background-color: red;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView#listViewCashList::item:selected \n"
"{\n"
"	background-color: #b78620;\n"
"	border: 1px solid #b78620;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView#listViewCashList::item:selected:!active \n"
"{\n"
"	background-color: #46a2da;\n"
"	border: 1px solid #46a2da;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
""
                        "QListView#listViewCashList::item:selected:active \n"
"{\n"
"	background-color: #46a2da;\n"
"	border: 1px solid #46a2da;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView#listViewCashList::item:hover {\n"
"    background-color: #5e5e5e;\n"
"    border: none;\n"
"    color: #000;\n"
"\n"
"}")
        self.frame = QFrame(self.tabEarned)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 380, 741, 71))
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Sunken)
        self.gridLayoutWidget_5 = QWidget(self.frame)
        self.gridLayoutWidget_5.setObjectName(u"gridLayoutWidget_5")
        self.gridLayoutWidget_5.setGeometry(QRect(10, 10, 731, 51))
        self.gridLayout_5 = QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.inputNum = QLineEdit(self.gridLayoutWidget_5)
        self.inputNum.setObjectName(u"inputNum")
        self.inputNum.setFont(font1)
        self.inputNum.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_5.addWidget(self.inputNum, 0, 0, 1, 1)

        self.inputComment = QLineEdit(self.gridLayoutWidget_5)
        self.inputComment.setObjectName(u"inputComment")
        self.inputComment.setFont(font1)
        self.inputComment.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_5.addWidget(self.inputComment, 0, 3, 1, 1)

        self.btnEdit = QPushButton(self.gridLayoutWidget_5)
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

        self.gridLayout_5.addWidget(self.btnEdit, 0, 4, 1, 1)

        self.inputSum = QLineEdit(self.gridLayoutWidget_5)
        self.inputSum.setObjectName(u"inputSum")
        self.inputSum.setFont(font1)
        self.inputSum.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_5.addWidget(self.inputSum, 0, 1, 1, 1)

        self.inputAgent = QLineEdit(self.gridLayoutWidget_5)
        self.inputAgent.setObjectName(u"inputAgent")
        self.inputAgent.setFont(font1)
        self.inputAgent.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_5.addWidget(self.inputAgent, 0, 2, 1, 1)

        self.btnDelete = QPushButton(self.gridLayoutWidget_5)
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

        self.gridLayout_5.addWidget(self.btnDelete, 0, 5, 1, 1)

        self.horizontalLayoutWidget_2 = QWidget(self.tabEarned)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(340, 460, 401, 41))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_23 = QLabel(self.horizontalLayoutWidget_2)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_23)

        self.lblSumEarned = QLabel(self.horizontalLayoutWidget_2)
        self.lblSumEarned.setObjectName(u"lblSumEarned")
        self.lblSumEarned.setFont(font)
        self.lblSumEarned.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.lblSumEarned)

        self.horizontalLayout_2.setStretch(1, 1)
        self.tabCashList.addTab(self.tabEarned, "")
        self.tabExpenses_2 = QWidget()
        self.tabExpenses_2.setObjectName(u"tabExpenses_2")
        self.label_24 = QLabel(self.tabExpenses_2)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(220, 10, 49, 21))
        self.label_24.setFont(font)
        self.label_24.setLayoutDirection(Qt.RightToLeft)
        self.label_24.setAlignment(Qt.AlignCenter)
        self.frame_2 = QFrame(self.tabExpenses_2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 380, 741, 71))
        self.frame_2.setFrameShape(QFrame.Box)
        self.frame_2.setFrameShadow(QFrame.Sunken)
        self.gridLayoutWidget_6 = QWidget(self.frame_2)
        self.gridLayoutWidget_6.setObjectName(u"gridLayoutWidget_6")
        self.gridLayoutWidget_6.setGeometry(QRect(10, 10, 731, 51))
        self.gridLayout_6 = QGridLayout(self.gridLayoutWidget_6)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.inputNum_2 = QLineEdit(self.gridLayoutWidget_6)
        self.inputNum_2.setObjectName(u"inputNum_2")
        self.inputNum_2.setFont(font1)
        self.inputNum_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_6.addWidget(self.inputNum_2, 0, 0, 1, 1)

        self.inputComment_5 = QLineEdit(self.gridLayoutWidget_6)
        self.inputComment_5.setObjectName(u"inputComment_5")
        self.inputComment_5.setFont(font1)
        self.inputComment_5.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_6.addWidget(self.inputComment_5, 0, 3, 1, 1)

        self.btnEdit_2 = QPushButton(self.gridLayoutWidget_6)
        self.btnEdit_2.setObjectName(u"btnEdit_2")
        self.btnEdit_2.setStyleSheet(u"QPushButton {\n"
"  background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(184, 184,      184, 255),stop:1 rgba(159, 159, 159, 255));\n"
"	color: #000;\n"
"	min-width: 80px;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: #051a39;\n"
"	padding: 5px;\n"
"}\n"
"QPushButton#btnEdit_2:hover\n"
"{\n"
"	background-color: rgba(70,162,218,50%);\n"
"	border: 1px solid #46a2da;\n"
"\n"
"}\n"
"\n"
"QPushButton#btnEdit_2:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}")

        self.gridLayout_6.addWidget(self.btnEdit_2, 0, 4, 1, 1)

        self.inputSum_5 = QLineEdit(self.gridLayoutWidget_6)
        self.inputSum_5.setObjectName(u"inputSum_5")
        self.inputSum_5.setFont(font1)
        self.inputSum_5.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_6.addWidget(self.inputSum_5, 0, 1, 1, 1)

        self.inputAgent_4 = QLineEdit(self.gridLayoutWidget_6)
        self.inputAgent_4.setObjectName(u"inputAgent_4")
        self.inputAgent_4.setFont(font1)
        self.inputAgent_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_6.addWidget(self.inputAgent_4, 0, 2, 1, 1)

        self.btnDelete_2 = QPushButton(self.gridLayoutWidget_6)
        self.btnDelete_2.setObjectName(u"btnDelete_2")
        self.btnDelete_2.setStyleSheet(u"QPushButton {\n"
"  background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(184, 184,      184, 255),stop:1 rgba(159, 159, 159, 255));\n"
"	color: #000;\n"
"	min-width: 80px;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: #051a39;\n"
"	padding: 5px;\n"
"}\n"
"QPushButton#btnDelete_2:hover\n"
"{\n"
"	background-color: rgba(70,162,218,50%);\n"
"	border: 1px solid #46a2da;\n"
"\n"
"}\n"
"\n"
"QPushButton#btnDelete_2:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}")

        self.gridLayout_6.addWidget(self.btnDelete_2, 0, 5, 1, 1)

        self.label_25 = QLabel(self.tabExpenses_2)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(450, 10, 49, 21))
        self.label_25.setFont(font)
        self.label_25.setLayoutDirection(Qt.RightToLeft)
        self.label_25.setAlignment(Qt.AlignCenter)
        self.label_26 = QLabel(self.tabExpenses_2)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(40, 10, 49, 21))
        self.label_26.setFont(font)
        self.label_26.setLayoutDirection(Qt.RightToLeft)
        self.label_26.setAlignment(Qt.AlignCenter)
        self.label_27 = QLabel(self.tabExpenses_2)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(598, 10, 61, 21))
        self.label_27.setFont(font)
        self.label_27.setLayoutDirection(Qt.RightToLeft)
        self.label_27.setAlignment(Qt.AlignCenter)
        self.listViewCashList_2 = QListView(self.tabExpenses_2)
        self.listViewCashList_2.setObjectName(u"listViewCashList_2")
        self.listViewCashList_2.setGeometry(QRect(10, 40, 741, 331))
        self.listViewCashList_2.setStyleSheet(u"QListView \n"
"{\n"
"	background-color: #f6f6f6;\n"
"    border : none;\n"
"    color: #000;\n"
"    show-decoration-selected: 1; \n"
"    outline: 0;\n"
"	border: 1px solid gray;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView#listViewCashList::disabled \n"
"{\n"
"	background-color: #656565;\n"
"	color: #1b1b1b;\n"
"    border: 1px solid #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView#listViewCashList::item \n"
"{\n"
"	background-color: #f6f6f6;\n"
"    padding: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView#listViewCashList::item:alternate \n"
"{\n"
"    background-color: #c6c6c6;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView#listViewCashList::item:alternate:selected\n"
"{\n"
"    background-color: red;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView#listViewCashList::item:selected \n"
"{\n"
"	background-color: #b78620;\n"
"	border: 1px solid #b78620;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView#listViewCashList::item:selected:!active \n"
"{\n"
"	background-color: #46a2da;\n"
"	border: 1px solid #46a2da;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
""
                        "QListView#listViewCashList::item:selected:active \n"
"{\n"
"	background-color: #46a2da;\n"
"	border: 1px solid #46a2da;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView#listViewCashList::item:hover {\n"
"    background-color: #5e5e5e;\n"
"    border: none;\n"
"    color: #000;\n"
"\n"
"}")
        self.label_28 = QLabel(self.tabExpenses_2)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(700, 10, 49, 21))
        self.label_28.setFont(font)
        self.label_28.setLayoutDirection(Qt.RightToLeft)
        self.label_28.setAlignment(Qt.AlignCenter)
        self.horizontalLayoutWidget = QWidget(self.tabExpenses_2)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(339, 460, 401, 41))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.lblSumExpenses = QLabel(self.horizontalLayoutWidget)
        self.lblSumExpenses.setObjectName(u"lblSumExpenses")
        self.lblSumExpenses.setFont(font)

        self.horizontalLayout.addWidget(self.lblSumExpenses)

        self.lblSumExpenses_2 = QLabel(self.horizontalLayoutWidget)
        self.lblSumExpenses_2.setObjectName(u"lblSumExpenses_2")
        self.lblSumExpenses_2.setFont(font)
        self.lblSumExpenses_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.lblSumExpenses_2)

        self.horizontalLayout.setStretch(1, 1)
        self.tabCashList.addTab(self.tabExpenses_2, "")
        self.lblCasher = QLabel(self.centralwidget)
        self.lblCasher.setObjectName(u"lblCasher")
        self.lblCasher.setGeometry(QRect(460, 790, 181, 31))
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(12)
        font3.setItalic(True)
        self.lblCasher.setFont(font3)
        self.lblCasher.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(650, 790, 101, 31))
        self.label.setFont(font3)
        CashForm.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(CashForm)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 792, 22))
        CashForm.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(CashForm)
        self.statusbar.setObjectName(u"statusbar")
        CashForm.setStatusBar(self.statusbar)

        self.retranslateUi(CashForm)

        self.tabCashForm.setCurrentIndex(3)
        self.tabCashList.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(CashForm)
    # setupUi

    def retranslateUi(self, CashForm):
        CashForm.setWindowTitle(QCoreApplication.translate("CashForm", u"CashForm", None))
        self.label_7.setText(QCoreApplication.translate("CashForm", u"\u0627\u0644\u0645\u0635\u062f\u0631", None))
        self.label_9.setText(QCoreApplication.translate("CashForm", u"\u0627\u0644\u0645\u062c\u0645\u0648\u063a", None))
        self.label_8.setText(QCoreApplication.translate("CashForm", u"\u0627\u0644\u0628\u064a\u0627\u0646", None))
        self.label_6.setText(QCoreApplication.translate("CashForm", u"\u0627\u0644\u0645\u0628\u0644\u063a", None))
        self.btnPaymentEntry.setText(QCoreApplication.translate("CashForm", u"\u0627\u062f\u062e\u0627\u0644 \u0627\u0644\u0645\u062f\u0641\u0648\u0639\u0627\u062a", None))
        self.tabCashForm.setTabText(self.tabCashForm.indexOf(self.tabExpenses), QCoreApplication.translate("CashForm", u"\u0627\u062f\u062e\u0627\u0644 \u0627\u0644\u0645\u062f\u0641\u0648\u0639\u0627\u062a", None))
        self.label_10.setText(QCoreApplication.translate("CashForm", u"\u0627\u0644\u0645\u0635\u062f\u0631", None))
        self.label_12.setText(QCoreApplication.translate("CashForm", u"\u0627\u0644\u0628\u064a\u0627\u0646", None))
        self.label_13.setText(QCoreApplication.translate("CashForm", u"\u0627\u0644\u0645\u0628\u0644\u063a", None))
        self.label_11.setText(QCoreApplication.translate("CashForm", u"\u0627\u0644\u0645\u062c\u0645\u0648\u063a", None))
        self.btnEarnedEntry.setText(QCoreApplication.translate("CashForm", u"\u0627\u062f\u062e\u0627\u0644 \u0627\u0644\u0645\u0642\u0628\u0648\u0636\u0627\u062a", None))
        self.tabCashForm.setTabText(self.tabCashForm.indexOf(self.tabEarnedEntry), QCoreApplication.translate("CashForm", u"\u0627\u062f\u062e\u0627\u0644 \u0627\u0644\u0645\u0642\u0628\u0648\u0636\u0627\u062a", None))
        self.label_14.setText(QCoreApplication.translate("CashForm", u"\u0627\u0644\u0645\u0635\u062f\u0631", None))
        self.label_15.setText(QCoreApplication.translate("CashForm", u"\u0627\u0644\u0628\u064a\u0627\u0646", None))
        self.label_16.setText(QCoreApplication.translate("CashForm", u"\u0627\u0644\u0645\u0628\u0644\u063a", None))
        self.label_17.setText(QCoreApplication.translate("CashForm", u"\u0627\u0644\u0645\u062c\u0645\u0648\u063a", None))
        self.btnWithdrawnEntry.setText(QCoreApplication.translate("CashForm", u"\u0627\u062f\u062e\u0627\u0644 \u0627\u0644\u0645\u0633\u062d\u0648\u0628\u0627\u062a", None))
        self.tabCashForm.setTabText(self.tabCashForm.indexOf(self.tabWithdrwanEntry), QCoreApplication.translate("CashForm", u"\u0627\u062f\u062e\u0627\u0644 \u0627\u0644\u0645\u0633\u062d\u0648\u0628\u0627\u062a", None))
        self.label_18.setText(QCoreApplication.translate("CashForm", u"\u0627\u0644\u0645\u0635\u062f\u0631", None))
        self.label_19.setText(QCoreApplication.translate("CashForm", u"\u0627\u0644\u0628\u064a\u0627\u0646", None))
        self.label_20.setText(QCoreApplication.translate("CashForm", u"\u0627\u0644\u0645\u0628\u0644\u063a", None))
        self.label_21.setText(QCoreApplication.translate("CashForm", u"\u0627\u0644\u0645\u062c\u0645\u0648\u063a", None))
        self.btnWithdrawnPaymentEntry.setText(QCoreApplication.translate("CashForm", u"\u062a\u0633\u062f\u064a\u062f \u0627\u0644\u0645\u0633\u062d\u0648\u0628\u0627\u062a", None))
        self.tabCashForm.setTabText(self.tabCashForm.indexOf(self.tabPayWithdrawn), QCoreApplication.translate("CashForm", u"\u062a\u0633\u062f\u064a\u062f \u0627\u0644\u0645\u0633\u062d\u0648\u0628\u0627\u062a", None))
        self.btnBack.setText(QCoreApplication.translate("CashForm", u"\u0631\u062c\u0648\u0639", None))
        self.lblDate.setText("")
        self.label_3.setText(QCoreApplication.translate("CashForm", u"\u0627\u0644\u0645\u0635\u062f\u0631", None))
        self.label_5.setText(QCoreApplication.translate("CashForm", u"\u0627\u0644\u062a\u0627\u0631\u064a\u062e", None))
        self.label_2.setText(QCoreApplication.translate("CashForm", u"\u0627\u0644\u0645\u0642\u0628\u0648\u0636\u0627\u062a", None))
        self.label_4.setText(QCoreApplication.translate("CashForm", u"\u0627\u0644\u0631\u0642\u0645", None))
        self.label_22.setText(QCoreApplication.translate("CashForm", u"\u0627\u0644\u0628\u064a\u0627\u0646", None))
        self.btnEdit.setText(QCoreApplication.translate("CashForm", u"\u062a\u0639\u062f\u064a\u0644", None))
        self.btnDelete.setText(QCoreApplication.translate("CashForm", u"\u062d\u0630\u0641", None))
        self.label_23.setText(QCoreApplication.translate("CashForm", u"\u0645\u062c\u0645\u0648\u0639 \u0627\u0644\u0645\u0642\u0628\u0648\u0636\u0627\u062a", None))
        self.lblSumEarned.setText("")
        self.tabCashList.setTabText(self.tabCashList.indexOf(self.tabEarned), QCoreApplication.translate("CashForm", u"\u0627\u0644\u0645\u0642\u0628\u0648\u0636\u0627\u062a", None))
        self.label_24.setText(QCoreApplication.translate("CashForm", u"\u0627\u0644\u0628\u064a\u0627\u0646", None))
        self.btnEdit_2.setText(QCoreApplication.translate("CashForm", u"\u062a\u0639\u062f\u064a\u0644", None))
        self.btnDelete_2.setText(QCoreApplication.translate("CashForm", u"\u062d\u0630\u0641", None))
        self.label_25.setText(QCoreApplication.translate("CashForm", u"\u0627\u0644\u0645\u0635\u062f\u0631", None))
        self.label_26.setText(QCoreApplication.translate("CashForm", u"\u0627\u0644\u062a\u0627\u0631\u064a\u062e", None))
        self.label_27.setText(QCoreApplication.translate("CashForm", u"\u0627\u0644\u0645\u062f\u0641\u0648\u0639\u0627\u062a", None))
        self.label_28.setText(QCoreApplication.translate("CashForm", u"\u0627\u0644\u0631\u0642\u0645", None))
        self.lblSumExpenses.setText(QCoreApplication.translate("CashForm", u"\u0645\u062c\u0645\u0648\u0639 \u0627\u0644\u0645\u0635\u0627\u0631\u064a\u0641", None))
        self.lblSumExpenses_2.setText("")
        self.tabCashList.setTabText(self.tabCashList.indexOf(self.tabExpenses_2), QCoreApplication.translate("CashForm", u"\u0627\u0644\u0645\u0635\u0627\u0631\u064a\u0641", None))
        self.lblCasher.setText("")
        self.label.setText(QCoreApplication.translate("CashForm", u"\u0645\u062f\u0648\u0631 \u0627\u0644\u0635\u0646\u062f\u0648\u0642:", None))
    # retranslateUi

