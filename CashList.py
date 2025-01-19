# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CashList.ui'
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

class Ui_CashList(object):
    def setupUi(self, CashList):
        if not CashList.objectName():
            CashList.setObjectName(u"CashList")
        CashList.resize(800, 600)
        CashList.setLayoutDirection(Qt.RightToLeft)
        CashList.setStyleSheet(u"background-color: #e4e4e4;\n"
"	color: #000;\n"
"	selection-background-color: #46a2da;\n"
"	selection-color: #fff;")
        self.centralwidget = QWidget(CashList)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabCashList = QTabWidget(self.centralwidget)
        self.tabCashList.setObjectName(u"tabCashList")
        self.tabCashList.setGeometry(QRect(20, 0, 761, 541))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(12)
        font.setBold(True)
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
        self.label = QLabel(self.tabEarned)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(700, 10, 49, 21))
        self.label.setFont(font)
        self.label.setLayoutDirection(Qt.RightToLeft)
        self.label.setAlignment(Qt.AlignCenter)
        self.label_4 = QLabel(self.tabEarned)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(220, 10, 49, 21))
        self.label_4.setFont(font)
        self.label_4.setLayoutDirection(Qt.RightToLeft)
        self.label_4.setAlignment(Qt.AlignCenter)
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
        self.gridLayoutWidget = QWidget(self.frame)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 731, 51))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.inputNum = QLineEdit(self.gridLayoutWidget)
        self.inputNum.setObjectName(u"inputNum")
        font1 = QFont()
        font1.setPointSize(14)
        self.inputNum.setFont(font1)
        self.inputNum.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.inputNum, 0, 0, 1, 1)

        self.inputComment = QLineEdit(self.gridLayoutWidget)
        self.inputComment.setObjectName(u"inputComment")
        self.inputComment.setFont(font1)
        self.inputComment.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.inputComment, 0, 3, 1, 1)

        self.btnEdit = QPushButton(self.gridLayoutWidget)
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

        self.gridLayout.addWidget(self.btnEdit, 0, 4, 1, 1)

        self.inputSum = QLineEdit(self.gridLayoutWidget)
        self.inputSum.setObjectName(u"inputSum")
        self.inputSum.setFont(font1)
        self.inputSum.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.inputSum, 0, 1, 1, 1)

        self.inputAgent = QLineEdit(self.gridLayoutWidget)
        self.inputAgent.setObjectName(u"inputAgent")
        self.inputAgent.setFont(font1)
        self.inputAgent.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.inputAgent, 0, 2, 1, 1)

        self.btnDelete = QPushButton(self.gridLayoutWidget)
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

        self.gridLayout.addWidget(self.btnDelete, 0, 5, 1, 1)

        self.horizontalLayoutWidget_2 = QWidget(self.tabEarned)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(340, 460, 401, 41))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.horizontalLayoutWidget_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_14)

        self.lblSumEarned = QLabel(self.horizontalLayoutWidget_2)
        self.lblSumEarned.setObjectName(u"lblSumEarned")
        self.lblSumEarned.setFont(font)
        self.lblSumEarned.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.lblSumEarned)

        self.horizontalLayout_2.setStretch(1, 1)
        self.tabCashList.addTab(self.tabEarned, "")
        self.tabExpenses = QWidget()
        self.tabExpenses.setObjectName(u"tabExpenses")
        self.label_7 = QLabel(self.tabExpenses)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(220, 10, 49, 21))
        self.label_7.setFont(font)
        self.label_7.setLayoutDirection(Qt.RightToLeft)
        self.label_7.setAlignment(Qt.AlignCenter)
        self.frame_2 = QFrame(self.tabExpenses)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 380, 741, 71))
        self.frame_2.setFrameShape(QFrame.Box)
        self.frame_2.setFrameShadow(QFrame.Sunken)
        self.gridLayoutWidget_2 = QWidget(self.frame_2)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(10, 10, 731, 51))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.inputNum_2 = QLineEdit(self.gridLayoutWidget_2)
        self.inputNum_2.setObjectName(u"inputNum_2")
        self.inputNum_2.setFont(font1)
        self.inputNum_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.inputNum_2, 0, 0, 1, 1)

        self.inputComment_2 = QLineEdit(self.gridLayoutWidget_2)
        self.inputComment_2.setObjectName(u"inputComment_2")
        self.inputComment_2.setFont(font1)
        self.inputComment_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.inputComment_2, 0, 3, 1, 1)

        self.btnEdit_2 = QPushButton(self.gridLayoutWidget_2)
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

        self.gridLayout_2.addWidget(self.btnEdit_2, 0, 4, 1, 1)

        self.inputSum_2 = QLineEdit(self.gridLayoutWidget_2)
        self.inputSum_2.setObjectName(u"inputSum_2")
        self.inputSum_2.setFont(font1)
        self.inputSum_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.inputSum_2, 0, 1, 1, 1)

        self.inputAgent_4 = QLineEdit(self.gridLayoutWidget_2)
        self.inputAgent_4.setObjectName(u"inputAgent_4")
        self.inputAgent_4.setFont(font1)
        self.inputAgent_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.inputAgent_4, 0, 2, 1, 1)

        self.btnDelete_2 = QPushButton(self.gridLayoutWidget_2)
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

        self.gridLayout_2.addWidget(self.btnDelete_2, 0, 5, 1, 1)

        self.label_9 = QLabel(self.tabExpenses)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(450, 10, 49, 21))
        self.label_9.setFont(font)
        self.label_9.setLayoutDirection(Qt.RightToLeft)
        self.label_9.setAlignment(Qt.AlignCenter)
        self.label_10 = QLabel(self.tabExpenses)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(40, 10, 49, 21))
        self.label_10.setFont(font)
        self.label_10.setLayoutDirection(Qt.RightToLeft)
        self.label_10.setAlignment(Qt.AlignCenter)
        self.label_11 = QLabel(self.tabExpenses)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(598, 10, 61, 21))
        self.label_11.setFont(font)
        self.label_11.setLayoutDirection(Qt.RightToLeft)
        self.label_11.setAlignment(Qt.AlignCenter)
        self.listViewCashList_2 = QListView(self.tabExpenses)
        self.listViewCashList_2.setObjectName(u"listViewCashList_2")
        self.listViewCashList_2.setGeometry(QRect(10, 40, 731, 331))
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
        self.label_12 = QLabel(self.tabExpenses)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(700, 10, 49, 21))
        self.label_12.setFont(font)
        self.label_12.setLayoutDirection(Qt.RightToLeft)
        self.label_12.setAlignment(Qt.AlignCenter)
        self.horizontalLayoutWidget = QWidget(self.tabExpenses)
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
        self.tabCashList.addTab(self.tabExpenses, "")
        CashList.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(CashList)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        CashList.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(CashList)
        self.statusbar.setObjectName(u"statusbar")
        CashList.setStatusBar(self.statusbar)

        self.retranslateUi(CashList)

        self.tabCashList.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(CashList)
    # setupUi

    def retranslateUi(self, CashList):
        CashList.setWindowTitle(QCoreApplication.translate("CashList", u"CashList", None))
        self.label_3.setText(QCoreApplication.translate("CashList", u"\u0627\u0644\u0645\u0635\u062f\u0631", None))
        self.label_5.setText(QCoreApplication.translate("CashList", u"\u0627\u0644\u062a\u0627\u0631\u064a\u062e", None))
        self.label_2.setText(QCoreApplication.translate("CashList", u"\u0627\u0644\u0645\u0642\u0628\u0648\u0636\u0627\u062a", None))
        self.label.setText(QCoreApplication.translate("CashList", u"\u0627\u0644\u0631\u0642\u0645", None))
        self.label_4.setText(QCoreApplication.translate("CashList", u"\u0627\u0644\u0628\u064a\u0627\u0646", None))
        self.btnEdit.setText(QCoreApplication.translate("CashList", u"\u062a\u0639\u062f\u064a\u0644", None))
        self.btnDelete.setText(QCoreApplication.translate("CashList", u"\u062d\u0630\u0641", None))
        self.label_14.setText(QCoreApplication.translate("CashList", u"\u0645\u062c\u0645\u0648\u0639 \u0627\u0644\u0645\u0642\u0628\u0648\u0636\u0627\u062a", None))
        self.lblSumEarned.setText("")
        self.tabCashList.setTabText(self.tabCashList.indexOf(self.tabEarned), QCoreApplication.translate("CashList", u"\u0627\u0644\u0645\u0642\u0628\u0648\u0636\u0627\u062a", None))
        self.label_7.setText(QCoreApplication.translate("CashList", u"\u0627\u0644\u0628\u064a\u0627\u0646", None))
        self.btnEdit_2.setText(QCoreApplication.translate("CashList", u"\u062a\u0639\u062f\u064a\u0644", None))
        self.btnDelete_2.setText(QCoreApplication.translate("CashList", u"\u062d\u0630\u0641", None))
        self.label_9.setText(QCoreApplication.translate("CashList", u"\u0627\u0644\u0645\u0635\u062f\u0631", None))
        self.label_10.setText(QCoreApplication.translate("CashList", u"\u0627\u0644\u062a\u0627\u0631\u064a\u062e", None))
        self.label_11.setText(QCoreApplication.translate("CashList", u"\u0627\u0644\u0645\u062f\u0641\u0648\u0639\u0627\u062a", None))
        self.label_12.setText(QCoreApplication.translate("CashList", u"\u0627\u0644\u0631\u0642\u0645", None))
        self.lblSumExpenses.setText(QCoreApplication.translate("CashList", u"\u0645\u062c\u0645\u0648\u0639 \u0627\u0644\u0645\u0635\u0627\u0631\u064a\u0641", None))
        self.lblSumExpenses_2.setText("")
        self.tabCashList.setTabText(self.tabCashList.indexOf(self.tabExpenses), QCoreApplication.translate("CashList", u"\u0627\u0644\u0645\u0635\u0627\u0631\u064a\u0641", None))
    # retranslateUi

