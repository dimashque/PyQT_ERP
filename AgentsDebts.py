# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AgentsDebts.ui'
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
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_Agents_Debts(object):
    def setupUi(self, Agents_Debts):
        if not Agents_Debts.objectName():
            Agents_Debts.setObjectName(u"Agents_Debts")
        Agents_Debts.resize(800, 604)
        Agents_Debts.setLayoutDirection(Qt.RightToLeft)
        Agents_Debts.setStyleSheet(u"background-color: #e4e4e4;\n"
"	color: #000;\n"
"	selection-background-color: #46a2da;\n"
"	selection-color: #fff;")
        self.centralwidget = QWidget(Agents_Debts)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 40, 781, 341))
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Sunken)
        self.listViewAgentsDebts = QListView(self.frame)
        self.listViewAgentsDebts.setObjectName(u"listViewAgentsDebts")
        self.listViewAgentsDebts.setGeometry(QRect(10, 10, 761, 321))
        self.listViewAgentsDebts.setStyleSheet(u"QListView \n"
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
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(730, 10, 49, 21))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setLayoutDirection(Qt.RightToLeft)
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(640, 10, 49, 21))
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(Qt.RightToLeft)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(520, 10, 49, 21))
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(Qt.RightToLeft)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(320, 10, 49, 21))
        self.label_4.setFont(font)
        self.label_4.setLayoutDirection(Qt.RightToLeft)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(70, 10, 49, 21))
        self.label_5.setFont(font)
        self.label_5.setLayoutDirection(Qt.RightToLeft)
        self.label_5.setAlignment(Qt.AlignCenter)
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 390, 781, 171))
        self.frame_2.setFrameShape(QFrame.Box)
        self.frame_2.setFrameShadow(QFrame.Sunken)
        self.gridLayoutWidget = QWidget(self.frame_2)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 761, 80))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)
        self.label_6.setLayoutDirection(Qt.RightToLeft)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)

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

        self.gridLayout.addWidget(self.btnEdit, 1, 4, 1, 1)

        self.inputSum = QLineEdit(self.gridLayoutWidget)
        self.inputSum.setObjectName(u"inputSum")
        font1 = QFont()
        font1.setPointSize(14)
        self.inputSum.setFont(font1)
        self.inputSum.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.inputSum, 1, 1, 1, 1)

        self.inputComment = QLineEdit(self.gridLayoutWidget)
        self.inputComment.setObjectName(u"inputComment")
        self.inputComment.setFont(font1)
        self.inputComment.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.inputComment, 1, 3, 1, 1)

        self.inputNum = QLineEdit(self.gridLayoutWidget)
        self.inputNum.setObjectName(u"inputNum")
        self.inputNum.setFont(font1)
        self.inputNum.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.inputNum, 1, 0, 1, 1)

        self.inputAgent = QLineEdit(self.gridLayoutWidget)
        self.inputAgent.setObjectName(u"inputAgent")
        self.inputAgent.setFont(font1)
        self.inputAgent.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.inputAgent, 1, 2, 1, 1)

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

        self.gridLayout.addWidget(self.btnDelete, 1, 5, 1, 1)

        self.label_7 = QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)
        self.label_7.setLayoutDirection(Qt.RightToLeft)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_7, 0, 1, 1, 1)

        self.label_8 = QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)
        self.label_8.setLayoutDirection(Qt.RightToLeft)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_8, 0, 2, 1, 1)

        self.label_9 = QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)
        self.label_9.setLayoutDirection(Qt.RightToLeft)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_9, 0, 3, 1, 1)

        self.horizontalLayoutWidget = QWidget(self.frame_2)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 100, 761, 61))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.horizontalLayoutWidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)
        self.label_10.setLayoutDirection(Qt.RightToLeft)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_10)

        self.cbAgents = QComboBox(self.horizontalLayoutWidget)
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

        self.horizontalLayout.addWidget(self.cbAgents)

        self.label_11 = QLabel(self.horizontalLayoutWidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font)
        self.label_11.setLayoutDirection(Qt.RightToLeft)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_11)

        self.inpuToPay = QLineEdit(self.horizontalLayoutWidget)
        self.inpuToPay.setObjectName(u"inpuToPay")
        self.inpuToPay.setFont(font1)
        self.inpuToPay.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.inpuToPay)

        self.label_12 = QLabel(self.horizontalLayoutWidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font)
        self.label_12.setLayoutDirection(Qt.RightToLeft)
        self.label_12.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_12)

        self.inputSumDebts = QLineEdit(self.horizontalLayoutWidget)
        self.inputSumDebts.setObjectName(u"inputSumDebts")
        self.inputSumDebts.setFont(font1)
        self.inputSumDebts.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.inputSumDebts)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)
        self.horizontalLayout.setStretch(2, 1)
        self.horizontalLayout.setStretch(3, 2)
        self.horizontalLayout.setStretch(4, 1)
        self.horizontalLayout.setStretch(5, 2)
        Agents_Debts.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Agents_Debts)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        Agents_Debts.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Agents_Debts)
        self.statusbar.setObjectName(u"statusbar")
        Agents_Debts.setStatusBar(self.statusbar)

        self.retranslateUi(Agents_Debts)

        QMetaObject.connectSlotsByName(Agents_Debts)
    # setupUi

    def retranslateUi(self, Agents_Debts):
        Agents_Debts.setWindowTitle(QCoreApplication.translate("Agents_Debts", u"Agents_Debts", None))
        self.label.setText(QCoreApplication.translate("Agents_Debts", u"\u0627\u0644\u0631\u0642\u0645", None))
        self.label_2.setText(QCoreApplication.translate("Agents_Debts", u"\u0627\u0644\u0645\u0628\u0644\u063a", None))
        self.label_3.setText(QCoreApplication.translate("Agents_Debts", u"\u0627\u0644\u0639\u0645\u064a\u0644", None))
        self.label_4.setText(QCoreApplication.translate("Agents_Debts", u"\u0627\u0644\u0628\u064a\u0627\u0646", None))
        self.label_5.setText(QCoreApplication.translate("Agents_Debts", u"\u0627\u0644\u062a\u0627\u0631\u064a\u062e", None))
        self.label_6.setText(QCoreApplication.translate("Agents_Debts", u"\u0627\u0644\u0631\u0642\u0645", None))
        self.btnEdit.setText(QCoreApplication.translate("Agents_Debts", u"\u062a\u0639\u062f\u064a\u0644", None))
        self.btnDelete.setText(QCoreApplication.translate("Agents_Debts", u"\u062d\u0630\u0641", None))
        self.label_7.setText(QCoreApplication.translate("Agents_Debts", u"\u0627\u0644\u0645\u0628\u0644\u063a", None))
        self.label_8.setText(QCoreApplication.translate("Agents_Debts", u"\u0627\u0644\u0639\u0645\u064a\u0644", None))
        self.label_9.setText(QCoreApplication.translate("Agents_Debts", u"\u0627\u0644\u0628\u064a\u0627\u0646", None))
        self.label_10.setText(QCoreApplication.translate("Agents_Debts", u"\u0627\u062e\u062a\u0631 \u0627\u0644\u0639\u0645\u064a\u0644", None))
        self.label_11.setText(QCoreApplication.translate("Agents_Debts", u"\u0627\u0644\u0645\u062a\u0628\u0642\u064a \u0639\u0644\u064a\u0647", None))
        self.label_12.setText(QCoreApplication.translate("Agents_Debts", u"\u0645\u062c\u0645\u0648\u0639 \u0627\u0644\u0630\u0645\u0645", None))
    # retranslateUi

