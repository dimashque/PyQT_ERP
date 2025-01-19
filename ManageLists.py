# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ManageLists.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QListView,
    QMainWindow, QMenuBar, QPushButton, QRadioButton,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_Managelists(object):
    def setupUi(self, Managelists):
        if not Managelists.objectName():
            Managelists.setObjectName(u"Managelists")
        Managelists.resize(800, 614)
        Managelists.setLayoutDirection(Qt.RightToLeft)
        Managelists.setStyleSheet(u"background-color: #e4e4e4;\n"
"	color: #000;\n"
"	selection-background-color: #46a2da;\n"
"	selection-color: #fff;")
        self.centralwidget = QWidget(Managelists)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btnBack = QPushButton(self.centralwidget)
        self.btnBack.setObjectName(u"btnBack")
        self.btnBack.setGeometry(QRect(20, 530, 161, 28))
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
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(20, 70, 361, 151))
        self.frame_3.setFrameShape(QFrame.Box)
        self.frame_3.setFrameShadow(QFrame.Sunken)
        self.formLayoutWidget = QWidget(self.frame_3)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(100, 10, 251, 72))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.formLayout.setFieldGrowthPolicy(QFormLayout.FieldsStayAtSizeHint)
        self.formLayout.setVerticalSpacing(6)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.lblUserName = QLabel(self.formLayoutWidget)
        self.lblUserName.setObjectName(u"lblUserName")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        self.lblUserName.setFont(font)
        self.lblUserName.setStyleSheet(u"\n"
"	background-color: transparent;\n"
"	color: rgb(0, 0, 0);")
        self.lblUserName.setFrameShape(QFrame.Box)
        self.lblUserName.setFrameShadow(QFrame.Raised)
        self.lblUserName.setTextFormat(Qt.PlainText)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lblUserName)

        self.inputUserName = QLineEdit(self.formLayoutWidget)
        self.inputUserName.setObjectName(u"inputUserName")
        font1 = QFont()
        font1.setPointSize(14)
        self.inputUserName.setFont(font1)
        self.inputUserName.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.inputUserName)

        self.inputPassword = QLineEdit(self.formLayoutWidget)
        self.inputPassword.setObjectName(u"inputPassword")
        self.inputPassword.setFont(font1)
        self.inputPassword.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.inputPassword)

        self.lblUserName_2 = QLabel(self.formLayoutWidget)
        self.lblUserName_2.setObjectName(u"lblUserName_2")
        self.lblUserName_2.setFont(font)
        self.lblUserName_2.setStyleSheet(u"\n"
"	background-color: transparent;\n"
"	color: rgb(0, 0, 0);")
        self.lblUserName_2.setFrameShape(QFrame.Box)
        self.lblUserName_2.setFrameShadow(QFrame.Raised)
        self.lblUserName_2.setTextFormat(Qt.PlainText)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lblUserName_2)

        self.inputUnknown = QLineEdit(self.frame_3)
        self.inputUnknown.setObjectName(u"inputUnknown")
        self.inputUnknown.setGeometry(QRect(10, 10, 81, 32))
        self.inputUnknown.setFont(font1)
        self.inputUnknown.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.horizontalLayoutWidget = QWidget(self.frame_3)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 90, 341, 51))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btnAdd = QPushButton(self.horizontalLayoutWidget)
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

        self.horizontalLayout.addWidget(self.btnAdd)

        self.btnEdit = QPushButton(self.horizontalLayoutWidget)
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

        self.horizontalLayout.addWidget(self.btnEdit)

        self.btnDelete = QPushButton(self.horizontalLayoutWidget)
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

        self.horizontalLayout.addWidget(self.btnDelete)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(20, 240, 761, 271))
        self.frame_2.setFrameShape(QFrame.Box)
        self.frame_2.setFrameShadow(QFrame.Sunken)
        self.listViewManageLists = QListView(self.frame_2)
        self.listViewManageLists.setObjectName(u"listViewManageLists")
        self.listViewManageLists.setGeometry(QRect(10, 10, 741, 251))
        self.listViewManageLists.setStyleSheet(u"QListView \n"
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
"QListView#listViewManageLists::disabled \n"
"{\n"
"	background-color: #656565;\n"
"	color: #1b1b1b;\n"
"    border: 1px solid #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView#listViewManageLists::item \n"
"{\n"
"	background-color: #f6f6f6;\n"
"    padding: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView#listViewManageLists::item:alternate \n"
"{\n"
"    background-color: #c6c6c6;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView#listViewManageLists::item:alternate:selected\n"
"{\n"
"    background-color: red;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView#listViewManageLists::item:selected \n"
"{\n"
"	background-color: #b78620;\n"
"	border: 1px solid #b78620;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView#listViewManageLists::item:selected:!active \n"
"{\n"
"	background-color: #46a2da;\n"
"	border: 1px solid #46a2da;\n"
"	color: #fff;\n"
"\n"
""
                        "}\n"
"\n"
"\n"
"QListView#listViewManageLists::item:selected:active \n"
"{\n"
"	background-color: #46a2da;\n"
"	border: 1px solid #46a2da;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView#listViewManageLists::item:hover {\n"
"    background-color: #5e5e5e;\n"
"    border: none;\n"
"    color: #000;\n"
"\n"
"}")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(580, 10, 201, 51))
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Sunken)
        self.frame.setLineWidth(4)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 10, 141, 31))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(14)
        font2.setBold(True)
        self.label.setFont(font2)
        self.label.setAlignment(Qt.AlignCenter)
        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(400, 70, 381, 151))
        self.frame_4.setFrameShape(QFrame.Box)
        self.frame_4.setFrameShadow(QFrame.Sunken)
        self.verticalLayoutWidget = QWidget(self.frame_4)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(5, 10, 361, 131))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.rdbAgents = QRadioButton(self.verticalLayoutWidget)
        self.rdbAgents.setObjectName(u"rdbAgents")
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(12)
        font3.setBold(False)
        self.rdbAgents.setFont(font3)
        self.rdbAgents.setStyleSheet(u"QRadioButton \n"
"{\n"
"	color: #000;\n"
"	background-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QRadioButton#rdbAgents::indicator::unchecked:hover \n"
"{\n"
"	background-color: darkgray;\n"
"	border: 2px solid #46a2da;\n"
"	border-radius: 6px;\n"
"}\n"
"\n"
"\n"
"QRadioButton#rdbAgents::indicator::checked \n"
"{\n"
"	border: 2px solid #52beff;\n"
"	border-radius: 6px;\n"
"	background-color: #0088da;  \n"
"	width: 9px; \n"
"	height: 9px; \n"
"\n"
"}")

        self.horizontalLayout_3.addWidget(self.rdbAgents)

        self.rdbMovement = QRadioButton(self.verticalLayoutWidget)
        self.rdbMovement.setObjectName(u"rdbMovement")
        self.rdbMovement.setFont(font3)
        self.rdbMovement.setStyleSheet(u"QRadioButton \n"
"{\n"
"	color: #000;\n"
"	background-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QRadioButton#rdbMovement::indicator::unchecked:hover \n"
"{\n"
"	background-color: darkgray;\n"
"	border: 2px solid #46a2da;\n"
"	border-radius: 6px;\n"
"}\n"
"\n"
"\n"
"QRadioButton#rdbMovement::indicator::checked \n"
"{\n"
"	border: 2px solid #52beff;\n"
"	border-radius: 6px;\n"
"	background-color: #0088da;  \n"
"	width: 9px; \n"
"	height: 9px; \n"
"\n"
"}")

        self.horizontalLayout_3.addWidget(self.rdbMovement)

        self.rdbShipping = QRadioButton(self.verticalLayoutWidget)
        self.rdbShipping.setObjectName(u"rdbShipping")
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setPointSize(12)
        font4.setBold(False)
        font4.setItalic(False)
        self.rdbShipping.setFont(font4)
        self.rdbShipping.setStyleSheet(u"QRadioButton \n"
"{\n"
"	color: #000;\n"
"	background-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QRadioButton#rdbShipping::indicator::unchecked:hover \n"
"{\n"
"	background-color: darkgray;\n"
"	border: 2px solid #46a2da;\n"
"	border-radius: 6px;\n"
"}\n"
"\n"
"\n"
"QRadioButton#rdbShipping::indicator::checked \n"
"{\n"
"	border: 2px solid #52beff;\n"
"	border-radius: 6px;\n"
"	background-color: #0088da;  \n"
"	width: 9px; \n"
"	height: 9px; \n"
"\n"
"}")

        self.horizontalLayout_3.addWidget(self.rdbShipping)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.rdbSource = QRadioButton(self.verticalLayoutWidget)
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

        self.horizontalLayout_2.addWidget(self.rdbSource)

        self.rdbSalesAgent = QRadioButton(self.verticalLayoutWidget)
        self.rdbSalesAgent.setObjectName(u"rdbSalesAgent")
        self.rdbSalesAgent.setFont(font4)
        self.rdbSalesAgent.setStyleSheet(u"QRadioButton \n"
"{\n"
"	color: #000;\n"
"	background-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QRadioButton#rdbSalesAgent::indicator::unchecked:hover \n"
"{\n"
"	background-color: darkgray;\n"
"	border: 2px solid #46a2da;\n"
"	border-radius: 6px;\n"
"}\n"
"\n"
"\n"
"QRadioButton#rdbSalesAgen::indicator::checked \n"
"{\n"
"	border: 2px solid #52beff;\n"
"	border-radius: 6px;\n"
"	background-color: #0088da;  \n"
"	width: 9px; \n"
"	height: 9px; \n"
"\n"
"}")

        self.horizontalLayout_2.addWidget(self.rdbSalesAgent)

        self.rdbFund = QRadioButton(self.verticalLayoutWidget)
        self.rdbFund.setObjectName(u"rdbFund")
        self.rdbFund.setFont(font3)
        self.rdbFund.setStyleSheet(u"QRadioButton \n"
"{\n"
"	color: #000;\n"
"	background-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QRadioButton#rdbFund::indicator::unchecked:hover \n"
"{\n"
"	background-color: darkgray;\n"
"	border: 2px solid #46a2da;\n"
"	border-radius: 6px;\n"
"}\n"
"\n"
"\n"
"QRadioButton#rdbFund::indicator::checked \n"
"{\n"
"	border: 2px solid #52beff;\n"
"	border-radius: 6px;\n"
"	background-color: #0088da;  \n"
"	width: 9px; \n"
"	height: 9px; \n"
"\n"
"}")

        self.horizontalLayout_2.addWidget(self.rdbFund)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.rdbUsers = QRadioButton(self.verticalLayoutWidget)
        self.rdbUsers.setObjectName(u"rdbUsers")
        self.rdbUsers.setFont(font3)
        self.rdbUsers.setStyleSheet(u"QRadioButton \n"
"{\n"
"	color: #000;\n"
"	background-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QRadioButton#rdbUsers::indicator::unchecked:hover \n"
"{\n"
"	background-color: darkgray;\n"
"	border: 2px solid #46a2da;\n"
"	border-radius: 6px;\n"
"}\n"
"\n"
"\n"
"QRadioButton#rdbUsers::indicator::checked \n"
"{\n"
"	border: 2px solid #52beff;\n"
"	border-radius: 6px;\n"
"	background-color: #0088da;  \n"
"	width: 9px; \n"
"	height: 9px; \n"
"\n"
"}")

        self.verticalLayout.addWidget(self.rdbUsers)

        Managelists.setCentralWidget(self.centralwidget)
        self.menubarManageLists = QMenuBar(Managelists)
        self.menubarManageLists.setObjectName(u"menubarManageLists")
        self.menubarManageLists.setGeometry(QRect(0, 0, 800, 24))
        self.menubarManageLists.setStyleSheet(u"QMenuBar \n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(227, 227, 227, 255),stop:1 rgba(187, 187, 187, 255));\n"
"	border: 1px solid #f1f1f1;\n"
"	color: #000;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenuBar#menubarManageLists::item \n"
"{\n"
"	background-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenuBar#menubarManageLists::item:selected \n"
"{\n"
"	background-color: rgba(70,162,218,50%);\n"
"	border: 1px solid #46a2da;\n"
"	color: #000;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenuBar#menubarManageLists::item:pressed \n"
"{\n"
"	background-color: #46a2da;\n"
"	border: 1px solid #46a2da;\n"
"	color: #fff;\n"
"\n"
"}\n"
"")
        Managelists.setMenuBar(self.menubarManageLists)
        self.statusbar = QStatusBar(Managelists)
        self.statusbar.setObjectName(u"statusbar")
        Managelists.setStatusBar(self.statusbar)

        self.retranslateUi(Managelists)

        QMetaObject.connectSlotsByName(Managelists)
    # setupUi

    def retranslateUi(self, Managelists):
        Managelists.setWindowTitle(QCoreApplication.translate("Managelists", u"Manage Lists", None))
        self.btnBack.setText(QCoreApplication.translate("Managelists", u"\u0639\u0648\u062f\u0629", None))
        self.lblUserName.setText(QCoreApplication.translate("Managelists", u"\u0627\u0633\u0645 \u0627\u0644\u0645\u0633\u062a\u062e\u062f\u0645", None))
        self.lblUserName_2.setText(QCoreApplication.translate("Managelists", u"\u0643\u0644\u0645\u0629 \u0627\u0644\u0645\u0631\u0648\u0631", None))
        self.btnAdd.setText(QCoreApplication.translate("Managelists", u"\u0627\u0636\u0627\u0641\u0629", None))
        self.btnEdit.setText(QCoreApplication.translate("Managelists", u"\u062a\u0639\u062f\u064a\u0644", None))
        self.btnDelete.setText(QCoreApplication.translate("Managelists", u"\u062d\u0630\u0641", None))
        self.label.setText(QCoreApplication.translate("Managelists", u"\u062a\u0639\u062f\u064a\u0644 \u0627\u0644\u0642\u0648\u0627\u0626\u0645", None))
        self.rdbAgents.setText(QCoreApplication.translate("Managelists", u"\u0627\u0644\u0639\u0645\u0644\u0627\u0621", None))
        self.rdbMovement.setText(QCoreApplication.translate("Managelists", u"\u0627\u0644\u062d\u0631\u0643\u0629", None))
        self.rdbShipping.setText(QCoreApplication.translate("Managelists", u"\u0634\u0631\u0643\u0629 \u0627\u0644\u0634\u062d\u0646", None))
        self.rdbSource.setText(QCoreApplication.translate("Managelists", u"\u0627\u0644\u0645\u0635\u0627\u062f\u0631", None))
        self.rdbSalesAgent.setText(QCoreApplication.translate("Managelists", u"\u0627\u0644\u0645\u0633\u0648\u0642\u0627\u062a", None))
        self.rdbFund.setText(QCoreApplication.translate("Managelists", u"\u0627\u0644\u0645\u0645\u0648\u0644", None))
        self.rdbUsers.setText(QCoreApplication.translate("Managelists", u"\u0627\u0644\u0645\u0633\u062a\u062e\u062f\u0645\u0648\u0646", None))
    # retranslateUi

