# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DebtForm.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QListView,
    QMainWindow, QMenuBar, QPushButton, QRadioButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_DebtForm(object):
    def setupUi(self, DebtForm):
        if not DebtForm.objectName():
            DebtForm.setObjectName(u"DebtForm")
        DebtForm.resize(804, 1010)
        DebtForm.setLayoutDirection(Qt.RightToLeft)
        DebtForm.setStyleSheet(u"background-color: #e4e4e4;\n"
"	color: #000;\n"
"	selection-background-color: #46a2da;\n"
"	selection-color: #fff;")
        self.centralwidget = QWidget(DebtForm)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 80, 781, 341))
        self.frame_2.setFrameShape(QFrame.Box)
        self.frame_2.setFrameShadow(QFrame.Sunken)
        self.gridLayoutWidget = QWidget(self.frame_2)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 60, 761, 80))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(12)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.lblAgentSource = QLabel(self.gridLayoutWidget)
        self.lblAgentSource.setObjectName(u"lblAgentSource")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(12)
        self.lblAgentSource.setFont(font1)
        self.lblAgentSource.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lblAgentSource, 0, 1, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 0, 3, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)

        self.inputAmount = QLineEdit(self.gridLayoutWidget)
        self.inputAmount.setObjectName(u"inputAmount")
        font2 = QFont()
        font2.setPointSize(14)
        self.inputAmount.setFont(font2)
        self.inputAmount.setStyleSheet(u"QLineEdit\n"
"{\n"
"	background-color: #f6f6f6;\n"
"	color : #000;\n"
"	border: 1px solid #343434;\n"
"	padding: 3px;\n"
"	padding-left: 5px;\n"
"\n"
"}")

        self.gridLayout.addWidget(self.inputAmount, 1, 0, 1, 1)

        self.inputComment = QLineEdit(self.gridLayoutWidget)
        self.inputComment.setObjectName(u"inputComment")
        self.inputComment.setFont(font2)
        self.inputComment.setStyleSheet(u"QLineEdit\n"
"{\n"
"	background-color: #f6f6f6;\n"
"	color : #000;\n"
"	border: 1px solid #343434;\n"
"	padding: 3px;\n"
"	padding-left: 5px;\n"
"\n"
"}")

        self.gridLayout.addWidget(self.inputComment, 1, 2, 1, 1)

        self.inputSumDebt = QLineEdit(self.gridLayoutWidget)
        self.inputSumDebt.setObjectName(u"inputSumDebt")
        self.inputSumDebt.setFont(font2)
        self.inputSumDebt.setStyleSheet(u"QLineEdit\n"
"{\n"
"	background-color: #f6f6f6;\n"
"	color : #000;\n"
"	border: 1px solid #343434;\n"
"	padding: 3px;\n"
"	padding-left: 5px;\n"
"\n"
"}")

        self.gridLayout.addWidget(self.inputSumDebt, 1, 3, 1, 1)

        self.cbSource = QComboBox(self.gridLayoutWidget)
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

        self.gridLayout.addWidget(self.cbSource, 1, 1, 1, 1)

        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnStretch(2, 2)
        self.gridLayout.setColumnStretch(3, 1)
        self.gridLayoutWidget_2 = QWidget(self.frame_2)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(10, 200, 761, 80))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.gridLayoutWidget_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_9, 0, 0, 1, 1)

        self.lblAgentSource2 = QLabel(self.gridLayoutWidget_2)
        self.lblAgentSource2.setObjectName(u"lblAgentSource2")
        self.lblAgentSource2.setFont(font1)
        self.lblAgentSource2.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.lblAgentSource2, 0, 1, 1, 1)

        self.label_11 = QLabel(self.gridLayoutWidget_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font1)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_11, 0, 3, 1, 1)

        self.label_12 = QLabel(self.gridLayoutWidget_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font1)
        self.label_12.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_12, 0, 2, 1, 1)

        self.inputAmount2 = QLineEdit(self.gridLayoutWidget_2)
        self.inputAmount2.setObjectName(u"inputAmount2")
        self.inputAmount2.setFont(font2)
        self.inputAmount2.setStyleSheet(u"QLineEdit\n"
"{\n"
"	background-color: #f6f6f6;\n"
"	color : #000;\n"
"	border: 1px solid #343434;\n"
"	padding: 3px;\n"
"	padding-left: 5px;\n"
"\n"
"}")

        self.gridLayout_3.addWidget(self.inputAmount2, 1, 0, 1, 1)

        self.inputComment2 = QLineEdit(self.gridLayoutWidget_2)
        self.inputComment2.setObjectName(u"inputComment2")
        self.inputComment2.setFont(font2)
        self.inputComment2.setStyleSheet(u"QLineEdit\n"
"{\n"
"	background-color: #f6f6f6;\n"
"	color : #000;\n"
"	border: 1px solid #343434;\n"
"	padding: 3px;\n"
"	padding-left: 5px;\n"
"\n"
"}")

        self.gridLayout_3.addWidget(self.inputComment2, 1, 2, 1, 1)

        self.inputSumRest = QLineEdit(self.gridLayoutWidget_2)
        self.inputSumRest.setObjectName(u"inputSumRest")
        self.inputSumRest.setFont(font2)
        self.inputSumRest.setStyleSheet(u"QLineEdit\n"
"{\n"
"	background-color: #f6f6f6;\n"
"	color : #000;\n"
"	border: 1px solid #343434;\n"
"	padding: 3px;\n"
"	padding-left: 5px;\n"
"\n"
"}")

        self.gridLayout_3.addWidget(self.inputSumRest, 1, 3, 1, 1)

        self.cbAgent = QComboBox(self.gridLayoutWidget_2)
        self.cbAgent.setObjectName(u"cbAgent")
        self.cbAgent.setCursor(QCursor(Qt.PointingHandCursor))
        self.cbAgent.setLayoutDirection(Qt.LeftToRight)
        self.cbAgent.setStyleSheet(u"QComboBox::drop-down\n"
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

        self.gridLayout_3.addWidget(self.cbAgent, 1, 1, 1, 1)

        self.gridLayout_3.setColumnStretch(0, 1)
        self.gridLayout_3.setColumnStretch(1, 1)
        self.gridLayout_3.setColumnStretch(2, 2)
        self.gridLayout_3.setColumnStretch(3, 1)
        self.btnAdd = QPushButton(self.frame_2)
        self.btnAdd.setObjectName(u"btnAdd")
        self.btnAdd.setGeometry(QRect(10, 160, 129, 28))
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
        self.btnReturn = QPushButton(self.frame_2)
        self.btnReturn.setObjectName(u"btnReturn")
        self.btnReturn.setGeometry(QRect(10, 300, 129, 28))
        self.btnReturn.setStyleSheet(u"QPushButton {\n"
"  background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(184, 184,      184, 255),stop:1 rgba(159, 159, 159, 255));\n"
"	color: #000;\n"
"	min-width: 80px;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: #051a39;\n"
"	padding: 5px;\n"
"}\n"
"QPushButton#btnReturn:hover\n"
"{\n"
"	background-color: rgba(70,162,218,50%);\n"
"	border: 1px solid #46a2da;\n"
"\n"
"}\n"
"\n"
"QPushButton#btnReturn:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        self.btnPay = QPushButton(self.frame_2)
        self.btnPay.setObjectName(u"btnPay")
        self.btnPay.setGeometry(QRect(150, 300, 129, 28))
        self.btnPay.setStyleSheet(u"QPushButton {\n"
"  background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(184, 184,      184, 255),stop:1 rgba(159, 159, 159, 255));\n"
"	color: #000;\n"
"	min-width: 80px;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: #051a39;\n"
"	padding: 5px;\n"
"}\n"
"QPushButton#btnPay:hover\n"
"{\n"
"	background-color: rgba(70,162,218,50%);\n"
"	border: 1px solid #46a2da;\n"
"\n"
"}\n"
"\n"
"QPushButton#btnPay:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        self.horizontalLayoutWidget = QWidget(self.frame_2)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(610, 10, 160, 41))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.rdbAgent = QRadioButton(self.horizontalLayoutWidget)
        self.rdbAgent.setObjectName(u"rdbAgent")
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(12)
        font3.setBold(True)
        self.rdbAgent.setFont(font3)
        self.rdbAgent.setStyleSheet(u"QRadioButton \n"
"{\n"
"	color: #000;\n"
"	background-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QRadioButton#rdbAgent::indicator::unchecked:hover \n"
"{\n"
"	background-color: darkgray;\n"
"	border: 2px solid #46a2da;\n"
"	border-radius: 6px;\n"
"}\n"
"\n"
"\n"
"QRadioButton#rdbAgent::indicator::checked \n"
"{\n"
"	border: 2px solid #52beff;\n"
"	border-radius: 6px;\n"
"	background-color: #0088da;  \n"
"	width: 9px; \n"
"	height: 9px; \n"
"\n"
"}")

        self.horizontalLayout.addWidget(self.rdbAgent)

        self.rdbSource = QRadioButton(self.horizontalLayoutWidget)
        self.rdbSource.setObjectName(u"rdbSource")
        self.rdbSource.setFont(font3)
        self.rdbSource.setStyleSheet(u"QRadioButton \n"
"{\n"
"	color: #000;\n"
"	background-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QRadioButton#rdbSource::indicator::unchecked:hover \n"
"{\n"
"	background-color: darkgray;\n"
"	border: 2px solid #46a2da;\n"
"	border-radius: 6px;\n"
"}\n"
"\n"
"\n"
"QRadioButton#rdbSource::indicator::checked \n"
"{\n"
"	border: 2px solid #52beff;\n"
"	border-radius: 6px;\n"
"	background-color: #0088da;  \n"
"	width: 9px; \n"
"	height: 9px; \n"
"\n"
"}")

        self.horizontalLayout.addWidget(self.rdbSource)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(580, 10, 201, 51))
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Sunken)
        self.frame.setLineWidth(4)
        self.label_13 = QLabel(self.frame)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(30, 10, 141, 31))
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setPointSize(14)
        font4.setBold(True)
        self.label_13.setFont(font4)
        self.label_13.setAlignment(Qt.AlignCenter)
        self.btnBack = QPushButton(self.centralwidget)
        self.btnBack.setObjectName(u"btnBack")
        self.btnBack.setGeometry(QRect(10, 930, 153, 28))
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
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(730, 440, 49, 21))
        self.label_2.setFont(font3)
        self.label_2.setLayoutDirection(Qt.RightToLeft)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(320, 440, 49, 21))
        self.label_5.setFont(font3)
        self.label_5.setLayoutDirection(Qt.RightToLeft)
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(640, 440, 49, 21))
        self.label_6.setFont(font3)
        self.label_6.setLayoutDirection(Qt.RightToLeft)
        self.label_6.setAlignment(Qt.AlignCenter)
        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(10, 470, 781, 251))
        self.frame_4.setFrameShape(QFrame.Box)
        self.frame_4.setFrameShadow(QFrame.Sunken)
        self.listViewDebtList = QListView(self.frame_4)
        self.listViewDebtList.setObjectName(u"listViewDebtList")
        self.listViewDebtList.setGeometry(QRect(10, 10, 761, 221))
        self.listViewDebtList.setLayoutDirection(Qt.RightToLeft)
        self.listViewDebtList.setStyleSheet(u"QListView \n"
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
"QListView#listViewAgentsDebts::disabled \n"
"{\n"
"	background-color: #656565;\n"
"	color: #1b1b1b;\n"
"    border: 1px solid #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView#listViewAgentsDebts::item \n"
"{\n"
"	background-color: #f6f6f6;\n"
"    padding: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView#listViewAgentsDebts::item:alternate \n"
"{\n"
"    background-color: #c6c6c6;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView#listViewAgentsDebts::item:alternate:selected\n"
"{\n"
"    background-color: red;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView#listViewAgentsDebts::item:selected \n"
"{\n"
"	background-color: #b78620;\n"
"	border: 1px solid #b78620;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView#listViewAgentsDebts::item:selected:!active \n"
"{\n"
"	background-color: #46a2da;\n"
"	border: 1px solid #46a2da;\n"
"	color: #fff;\n"
"\n"
""
                        "}\n"
"\n"
"\n"
"QListView#listViewAgentsDebts::item:selected:active \n"
"{\n"
"	background-color: #46a2da;\n"
"	border: 1px solid #46a2da;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView#listViewAgentsDebts::item:hover {\n"
"    background-color: #5e5e5e;\n"
"    border: none;\n"
"    color: #000;\n"
"\n"
"}")
        self.frame_5 = QFrame(self.centralwidget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(10, 730, 781, 181))
        self.frame_5.setFrameShape(QFrame.Box)
        self.frame_5.setFrameShadow(QFrame.Sunken)
        self.gridLayoutWidget_3 = QWidget(self.frame_5)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(10, 10, 761, 80))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.gridLayoutWidget_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font3)
        self.label_10.setLayoutDirection(Qt.RightToLeft)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_10, 0, 6, 1, 1)

        self.btnEdit = QPushButton(self.gridLayoutWidget_3)
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

        self.gridLayout_2.addWidget(self.btnEdit, 1, 7, 1, 1)

        self.inputNum = QLineEdit(self.gridLayoutWidget_3)
        self.inputNum.setObjectName(u"inputNum")
        self.inputNum.setFont(font2)
        self.inputNum.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.inputNum, 1, 2, 1, 1)

        self.inputComment_2 = QLineEdit(self.gridLayoutWidget_3)
        self.inputComment_2.setObjectName(u"inputComment_2")
        self.inputComment_2.setFont(font2)
        self.inputComment_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.inputComment_2, 1, 6, 1, 1)

        self.label_14 = QLabel(self.gridLayoutWidget_3)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font3)
        self.label_14.setLayoutDirection(Qt.RightToLeft)
        self.label_14.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_14, 0, 5, 1, 1)

        self.label_7 = QLabel(self.gridLayoutWidget_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font3)
        self.label_7.setLayoutDirection(Qt.RightToLeft)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_7, 0, 2, 1, 1)

        self.inputSum = QLineEdit(self.gridLayoutWidget_3)
        self.inputSum.setObjectName(u"inputSum")
        self.inputSum.setFont(font2)
        self.inputSum.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.inputSum, 1, 4, 1, 1)

        self.label_8 = QLabel(self.gridLayoutWidget_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font3)
        self.label_8.setLayoutDirection(Qt.RightToLeft)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_8, 0, 4, 1, 1)

        self.inputAgent = QLineEdit(self.gridLayoutWidget_3)
        self.inputAgent.setObjectName(u"inputAgent")
        self.inputAgent.setFont(font2)
        self.inputAgent.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.inputAgent, 1, 5, 1, 1)

        self.btnDelete = QPushButton(self.gridLayoutWidget_3)
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

        self.gridLayout_2.addWidget(self.btnDelete, 1, 8, 1, 1)

        self.horizontalLayoutWidget_2 = QWidget(self.frame_5)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(10, 100, 761, 61))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_17 = QLabel(self.horizontalLayoutWidget_2)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font3)
        self.label_17.setLayoutDirection(Qt.RightToLeft)
        self.label_17.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_17)

        self.cbAgents = QComboBox(self.horizontalLayoutWidget_2)
        self.cbAgents.setObjectName(u"cbAgents")
        self.cbAgents.setCursor(QCursor(Qt.PointingHandCursor))
        self.cbAgents.setLayoutDirection(Qt.LeftToRight)
        self.cbAgents.setStyleSheet(u"QComboBox::drop-down\n"
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

        self.horizontalLayout_2.addWidget(self.cbAgents)

        self.label_16 = QLabel(self.horizontalLayoutWidget_2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font3)
        self.label_16.setLayoutDirection(Qt.RightToLeft)
        self.label_16.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_16)

        self.inpuToPay = QLineEdit(self.horizontalLayoutWidget_2)
        self.inpuToPay.setObjectName(u"inpuToPay")
        self.inpuToPay.setFont(font2)
        self.inpuToPay.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.inpuToPay)

        self.label_15 = QLabel(self.horizontalLayoutWidget_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font3)
        self.label_15.setLayoutDirection(Qt.RightToLeft)
        self.label_15.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_15)

        self.inputSumDebts = QLineEdit(self.horizontalLayoutWidget_2)
        self.inputSumDebts.setObjectName(u"inputSumDebts")
        self.inputSumDebts.setFont(font2)
        self.inputSumDebts.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.inputSumDebts)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 2)
        self.horizontalLayout_2.setStretch(3, 2)
        self.label_18 = QLabel(self.centralwidget)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(520, 440, 49, 21))
        self.label_18.setFont(font3)
        self.label_18.setLayoutDirection(Qt.RightToLeft)
        self.label_18.setAlignment(Qt.AlignCenter)
        self.label_19 = QLabel(self.centralwidget)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(70, 440, 49, 21))
        self.label_19.setFont(font3)
        self.label_19.setLayoutDirection(Qt.RightToLeft)
        self.label_19.setAlignment(Qt.AlignCenter)
        DebtForm.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(DebtForm)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 804, 24))
        self.menubar.setStyleSheet(u"QMenuBar \n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(227, 227, 227, 255),stop:1 rgba(187, 187, 187, 255));\n"
"	border: 1px solid #f1f1f1;\n"
"	color: #000;\n"
"\n"
"}\n"
"")
        DebtForm.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(DebtForm)
        self.statusbar.setObjectName(u"statusbar")
        DebtForm.setStatusBar(self.statusbar)

        self.retranslateUi(DebtForm)

        QMetaObject.connectSlotsByName(DebtForm)
    # setupUi

    def retranslateUi(self, DebtForm):
        DebtForm.setWindowTitle(QCoreApplication.translate("DebtForm", u"Debt From", None))
        self.label.setText(QCoreApplication.translate("DebtForm", u"\u0627\u0644\u0645\u0628\u0644\u063a", None))
        self.lblAgentSource.setText(QCoreApplication.translate("DebtForm", u"\u0627\u0644\u0645\u0635\u062f\u0631/\u0627\u0644\u0639\u0645\u064a\u0644", None))
        self.label_4.setText(QCoreApplication.translate("DebtForm", u"\u0645\u062c\u0645\u0648\u0639 \u0627\u0644\u0630\u0645\u0645", None))
        self.label_3.setText(QCoreApplication.translate("DebtForm", u"\u0627\u0644\u0628\u064a\u0627\u0646", None))
        self.label_9.setText(QCoreApplication.translate("DebtForm", u"\u0627\u0644\u0645\u0628\u0644\u063a", None))
        self.lblAgentSource2.setText(QCoreApplication.translate("DebtForm", u"\u0627\u0644\u0645\u0635\u062f\u0631/\u0627\u0644\u0639\u0645\u064a\u0644", None))
        self.label_11.setText(QCoreApplication.translate("DebtForm", u"\u0627\u0644\u062d\u0633\u0627\u0628 \u0627\u0644\u0645\u062a\u0628\u0642\u064a", None))
        self.label_12.setText(QCoreApplication.translate("DebtForm", u"\u0627\u0644\u0628\u064a\u0627\u0646", None))
        self.btnAdd.setText(QCoreApplication.translate("DebtForm", u"\u062a\u0633\u062c\u064a\u0644 \u0630\u0645\u0645", None))
        self.btnReturn.setText(QCoreApplication.translate("DebtForm", u"\u0645\u0631\u062a\u062c\u0639 \u0642\u0637\u0639", None))
        self.btnPay.setText(QCoreApplication.translate("DebtForm", u"\u062a\u0633\u062f\u064a\u062f \u0630\u0645\u0645", None))
        self.rdbAgent.setText(QCoreApplication.translate("DebtForm", u"\u0639\u0645\u064a\u0644", None))
        self.rdbSource.setText(QCoreApplication.translate("DebtForm", u"\u0645\u0635\u062f\u0631", None))
        self.label_13.setText(QCoreApplication.translate("DebtForm", u"\u0627\u0644\u0630\u0645\u0645", None))
        self.btnBack.setText(QCoreApplication.translate("DebtForm", u"\u0631\u062c\u0648\u0639", None))
        self.label_2.setText(QCoreApplication.translate("DebtForm", u"\u0627\u0644\u0631\u0642\u0645", None))
        self.label_5.setText(QCoreApplication.translate("DebtForm", u"\u0627\u0644\u0628\u064a\u0627\u0646", None))
        self.label_6.setText(QCoreApplication.translate("DebtForm", u"\u0627\u0644\u0645\u0628\u0644\u063a", None))
        self.label_10.setText(QCoreApplication.translate("DebtForm", u"\u0627\u0644\u0628\u064a\u0627\u0646", None))
        self.btnEdit.setText(QCoreApplication.translate("DebtForm", u"\u062a\u0639\u062f\u064a\u0644", None))
        self.label_14.setText(QCoreApplication.translate("DebtForm", u"\u0627\u0644\u0639\u0645\u064a\u0644", None))
        self.label_7.setText(QCoreApplication.translate("DebtForm", u"\u0627\u0644\u0631\u0642\u0645", None))
        self.label_8.setText(QCoreApplication.translate("DebtForm", u"\u0627\u0644\u0645\u0628\u0644\u063a", None))
        self.btnDelete.setText(QCoreApplication.translate("DebtForm", u"\u062d\u0630\u0641", None))
        self.label_17.setText(QCoreApplication.translate("DebtForm", u"\u0627\u062e\u062a\u0631 \u0627\u0644\u0645\u0635\u062f\u0631", None))
        self.label_16.setText(QCoreApplication.translate("DebtForm", u"\u0627\u0644\u0645\u062a\u0628\u0642\u064a \u0639\u0644\u064a\u0647", None))
        self.label_15.setText(QCoreApplication.translate("DebtForm", u"\u0645\u062c\u0645\u0648\u0639 \u0627\u0644\u0630\u0645\u0645", None))
        self.label_18.setText(QCoreApplication.translate("DebtForm", u"\u0627\u0644\u0645\u0635\u062f\u0631", None))
        self.label_19.setText(QCoreApplication.translate("DebtForm", u"\u0627\u0644\u062a\u0627\u0631\u064a\u062e", None))
    # retranslateUi

