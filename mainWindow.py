# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
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
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow2(object):
    def setupUi(self, MainWindow2):
        if not MainWindow2.objectName():
            MainWindow2.setObjectName(u"MainWindow2")
        MainWindow2.resize(800, 337)
        MainWindow2.setStyleSheet(u"background-color: #e4e4e4;\n"
"	color: #000;\n"
"	selection-background-color: #46a2da;\n"
"	selection-color: #fff;")
        self.centralwidget = QWidget(MainWindow2)
        self.centralwidget.setObjectName(u"centralwidget")
        self.back = QPushButton(self.centralwidget)
        self.back.setObjectName(u"back")
        self.back.setGeometry(QRect(150, 250, 92, 31))
        self.back.setStyleSheet(u"QPushButton {\n"
"  background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(184, 184,      184, 255),stop:1 rgba(159, 159, 159, 255));\n"
"	color: #000;\n"
"	min-width: 80px;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: #051a39;\n"
"	padding: 5px;\n"
"}\n"
"QPushButton#back:hover\n"
"{\n"
"	background-color: rgba(70,162,218,50%);\n"
"	border: 1px solid #46a2da;\n"
"\n"
"}\n"
"\n"
"QPushButton#back:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        self.exit = QPushButton(self.centralwidget)
        self.exit.setObjectName(u"exit")
        self.exit.setGeometry(QRect(40, 250, 92, 31))
        self.exit.setStyleSheet(u"QPushButton {\n"
"  background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(184, 184,      184, 255),stop:1 rgba(159, 159, 159, 255));\n"
"	color: #000;\n"
"	min-width: 80px;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: #051a39;\n"
"	padding: 5px;\n"
"}\n"
"QPushButton#exit:hover\n"
"{\n"
"	background-color: rgba(70,162,218,50%);\n"
"	border: 1px solid #46a2da;\n"
"\n"
"}\n"
"\n"
"QPushButton#exit:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        self.framelogo2 = QFrame(self.centralwidget)
        self.framelogo2.setObjectName(u"framelogo2")
        self.framelogo2.setGeometry(QRect(30, 10, 241, 221))
        self.framelogo2.setStyleSheet(u"")
        self.framelogo2.setFrameShape(QFrame.WinPanel)
        self.framelogo2.setFrameShadow(QFrame.Raised)
        self.framelogo2.setLineWidth(7)
        self.label = QLabel(self.framelogo2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 221, 201))
        self.label.setFrameShape(QFrame.Panel)
        self.label.setPixmap(QPixmap(u"media/logo_and_new_collection_gold.pdf"))
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignCenter)
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(290, 40, 481, 81))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnDebts = QPushButton(self.verticalLayoutWidget)
        self.btnDebts.setObjectName(u"btnDebts")
        self.btnDebts.setStyleSheet(u"QPushButton\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(184, 184, 184, 255),stop:1 rgba(159, 159, 159, 255));\n"
"	color: #000;\n"
"	min-width: 80px;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: #051a39;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton#btnDebts::flat\n"
"{\n"
"	background-color: transparent;\n"
"	border: none;\n"
"	color: #000;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton#btnDebts::disabled\n"
"{\n"
"	background-color: #606060;\n"
"	color: #959595;\n"
"	border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton#btnDebts::hover\n"
"{\n"
"	background-color: rgba(70,162,218,50%);\n"
"	border: 1px solid #46a2da;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton#btnDebts::pressed\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(174, 174, 174, 255),stop:1 rgba(149, 149, 149, 255));\n"
"	border: 1px solid #46a2da;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton#btnDebts::checked\n"
"{\n"
"	background-co"
                        "lor: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(174, 174, 174, 255),stop:1 rgba(149, 149, 149, 255));\n"
"	border: 1px solid #222;\n"
"\n"
"}")

        self.horizontalLayout.addWidget(self.btnDebts)

        self.btnOfficeData = QPushButton(self.verticalLayoutWidget)
        self.btnOfficeData.setObjectName(u"btnOfficeData")
        self.btnOfficeData.setStyleSheet(u"QPushButton\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(184, 184, 184, 255),stop:1 rgba(159, 159, 159, 255));\n"
"	color: #000;\n"
"	min-width: 80px;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: #051a39;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton#btnOfficeData::flat\n"
"{\n"
"	background-color: transparent;\n"
"	border: none;\n"
"	color: #000;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton#btnOfficeData::disabled\n"
"{\n"
"	background-color: #606060;\n"
"	color: #959595;\n"
"	border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton#btnOfficeData::hover\n"
"{\n"
"	background-color: rgba(70,162,218,50%);\n"
"	border: 1px solid #46a2da;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton#btnOfficeData::pressed\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(174, 174, 174, 255),stop:1 rgba(149, 149, 149, 255));\n"
"	border: 1px solid #46a2da;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton#btnOfficeData::checked"
                        "\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(174, 174, 174, 255),stop:1 rgba(149, 149, 149, 255));\n"
"	border: 1px solid #222;\n"
"\n"
"}")

        self.horizontalLayout.addWidget(self.btnOfficeData)

        self.btnMarketing = QPushButton(self.verticalLayoutWidget)
        self.btnMarketing.setObjectName(u"btnMarketing")
        self.btnMarketing.setStyleSheet(u"QPushButton\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(184, 184, 184, 255),stop:1 rgba(159, 159, 159, 255));\n"
"	color: #000;\n"
"	min-width: 80px;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: #051a39;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton#btnMarketing::flat\n"
"{\n"
"	background-color: transparent;\n"
"	border: none;\n"
"	color: #000;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton#btnMarketing::disabled\n"
"{\n"
"	background-color: #606060;\n"
"	color: #959595;\n"
"	border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton#btnMarketing::hover\n"
"{\n"
"	background-color: rgba(70,162,218,50%);\n"
"	border: 1px solid #46a2da;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton#btnMarketing::pressed\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(174, 174, 174, 255),stop:1 rgba(149, 149, 149, 255));\n"
"	border: 1px solid #46a2da;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton#btnMarketing::checked\n"
""
                        "{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(174, 174, 174, 255),stop:1 rgba(149, 149, 149, 255));\n"
"	border: 1px solid #222;\n"
"\n"
"}")

        self.horizontalLayout.addWidget(self.btnMarketing)

        self.btnAdjust = QPushButton(self.verticalLayoutWidget)
        self.btnAdjust.setObjectName(u"btnAdjust")
        self.btnAdjust.setStyleSheet(u"QPushButton\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(184, 184, 184, 255),stop:1 rgba(159, 159, 159, 255));\n"
"	color: #000;\n"
"	min-width: 80px;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: #051a39;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton#btnAdjust::flat\n"
"{\n"
"	background-color: transparent;\n"
"	border: none;\n"
"	color: #000;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton#btnAdjust::disabled\n"
"{\n"
"	background-color: #606060;\n"
"	color: #959595;\n"
"	border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton#btnAdjust::hover\n"
"{\n"
"	background-color: rgba(70,162,218,50%);\n"
"	border: 1px solid #46a2da;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton#btnAdjust::pressed\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(174, 174, 174, 255),stop:1 rgba(149, 149, 149, 255));\n"
"	border: 1px solid #46a2da;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton#btnAdjust::checked\n"
"{\n"
"	backgrou"
                        "nd-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(174, 174, 174, 255),stop:1 rgba(149, 149, 149, 255));\n"
"	border: 1px solid #222;\n"
"\n"
"}")

        self.horizontalLayout.addWidget(self.btnAdjust)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btnChangePassword = QPushButton(self.verticalLayoutWidget)
        self.btnChangePassword.setObjectName(u"btnChangePassword")
        self.btnChangePassword.setStyleSheet(u"QPushButton\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(184, 184, 184, 255),stop:1 rgba(159, 159, 159, 255));\n"
"	color: #000;\n"
"	min-width: 80px;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: #051a39;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton#btnChangePassword::flat\n"
"{\n"
"	background-color: transparent;\n"
"	border: none;\n"
"	color: #000;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton#btnChangePassword::disabled\n"
"{\n"
"	background-color: #606060;\n"
"	color: #959595;\n"
"	border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton#btnChangePassword::hover\n"
"{\n"
"	background-color: rgba(70,162,218,50%);\n"
"	border: 1px solid #46a2da;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton#btnChangePassword::pressed\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(174, 174, 174, 255),stop:1 rgba(149, 149, 149, 255));\n"
"	border: 1px solid #46a2da;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton#btnCha"
                        "ngePassword::checked\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(174, 174, 174, 255),stop:1 rgba(149, 149, 149, 255));\n"
"	border: 1px solid #222;\n"
"\n"
"}")

        self.horizontalLayout_2.addWidget(self.btnChangePassword)

        self.btnData = QPushButton(self.verticalLayoutWidget)
        self.btnData.setObjectName(u"btnData")
        self.btnData.setStyleSheet(u"QPushButton\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(184, 184, 184, 255),stop:1 rgba(159, 159, 159, 255));\n"
"	color: #000;\n"
"	min-width: 80px;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: #051a39;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton#btnData::flat\n"
"{\n"
"	background-color: transparent;\n"
"	border: none;\n"
"	color: #000;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton#btnData::disabled\n"
"{\n"
"	background-color: #606060;\n"
"	color: #959595;\n"
"	border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton#btnData::hover\n"
"{\n"
"	background-color: rgba(70,162,218,50%);\n"
"	border: 1px solid #46a2da;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton#btnData::pressed\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(174, 174, 174, 255),stop:1 rgba(149, 149, 149, 255));\n"
"	border: 1px solid #46a2da;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton#btnData::checked\n"
"{\n"
"	background-color: "
                        "qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(174, 174, 174, 255),stop:1 rgba(149, 149, 149, 255));\n"
"	border: 1px solid #222;\n"
"\n"
"}")

        self.horizontalLayout_2.addWidget(self.btnData)

        self.btnEntry = QPushButton(self.verticalLayoutWidget)
        self.btnEntry.setObjectName(u"btnEntry")
        self.btnEntry.setStyleSheet(u"QPushButton\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(184, 184, 184, 255),stop:1 rgba(159, 159, 159, 255));\n"
"	color: #000;\n"
"	min-width: 80px;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: #051a39;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton#btnEntry::flat\n"
"{\n"
"	background-color: transparent;\n"
"	border: none;\n"
"	color: #000;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton#btnEntry::disabled\n"
"{\n"
"	background-color: #606060;\n"
"	color: #959595;\n"
"	border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton#btnEntry::hover\n"
"{\n"
"	background-color: rgba(70,162,218,50%);\n"
"	border: 1px solid #46a2da;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton#btnEntry::pressed\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(174, 174, 174, 255),stop:1 rgba(149, 149, 149, 255));\n"
"	border: 1px solid #46a2da;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton#btnEntry::checked\n"
"{\n"
"	background-co"
                        "lor: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(174, 174, 174, 255),stop:1 rgba(149, 149, 149, 255));\n"
"	border: 1px solid #222;\n"
"\n"
"}")

        self.horizontalLayout_2.addWidget(self.btnEntry)

        self.btnKasse = QPushButton(self.verticalLayoutWidget)
        self.btnKasse.setObjectName(u"btnKasse")
        self.btnKasse.setStyleSheet(u"QPushButton\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(184, 184, 184, 255),stop:1 rgba(159, 159, 159, 255));\n"
"	color: #000;\n"
"	min-width: 80px;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: #051a39;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton#btnKasse::flat\n"
"{\n"
"	background-color: transparent;\n"
"	border: none;\n"
"	color: #000;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton#btnKasse::disabled\n"
"{\n"
"	background-color: #606060;\n"
"	color: #959595;\n"
"	border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton#btnKasse::hover\n"
"{\n"
"	background-color: rgba(70,162,218,50%);\n"
"	border: 1px solid #46a2da;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton#btnKasse::pressed\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(174, 174, 174, 255),stop:1 rgba(149, 149, 149, 255));\n"
"	border: 1px solid #46a2da;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton#btnKasse::checked\n"
"{\n"
"	background-co"
                        "lor: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(174, 174, 174, 255),stop:1 rgba(149, 149, 149, 255));\n"
"	border: 1px solid #222;\n"
"\n"
"}")

        self.horizontalLayout_2.addWidget(self.btnKasse)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.framenewPass = QFrame(self.centralwidget)
        self.framenewPass.setObjectName(u"framenewPass")
        self.framenewPass.setGeometry(QRect(290, 140, 481, 111))
        self.framenewPass.setFrameShape(QFrame.Box)
        self.framenewPass.setFrameShadow(QFrame.Sunken)
        self.formLayoutWidget = QWidget(self.framenewPass)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(210, 10, 261, 92))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setLayoutDirection(Qt.RightToLeft)
        self.label_2.setStyleSheet(u"")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.label_2)

        self.inputUsername = QLineEdit(self.formLayoutWidget)
        self.inputUsername.setObjectName(u"inputUsername")
        self.inputUsername.setStyleSheet(u"QLineEdit\n"
"{\n"
"	background-color: #f6f6f6;\n"
"	color : #000;\n"
"	border: 1px solid #343434;\n"
"	padding: 3px;\n"
"	padding-left: 5px;\n"
"\n"
"}")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.inputUsername)

        self.label_4 = QLabel(self.formLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setLayoutDirection(Qt.RightToLeft)
        self.label_4.setStyleSheet(u"")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.label_4)

        self.label_3 = QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setLayoutDirection(Qt.RightToLeft)
        self.label_3.setStyleSheet(u"")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.label_3)

        self.inputPass = QLineEdit(self.formLayoutWidget)
        self.inputPass.setObjectName(u"inputPass")
        self.inputPass.setStyleSheet(u"QLineEdit\n"
"{\n"
"	background-color: #f6f6f6;\n"
"	color : #000;\n"
"	border: 1px solid #343434;\n"
"	padding: 3px;\n"
"	padding-left: 5px;\n"
"\n"
"}")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.inputPass)

        self.inputNewPass = QLineEdit(self.formLayoutWidget)
        self.inputNewPass.setObjectName(u"inputNewPass")
        self.inputNewPass.setStyleSheet(u"QLineEdit\n"
"{\n"
"	background-color: #f6f6f6;\n"
"	color : #000;\n"
"	border: 1px solid #343434;\n"
"	padding: 3px;\n"
"	padding-left: 5px;\n"
"\n"
"}")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.inputNewPass)

        self.btnPassConfirm = QPushButton(self.framenewPass)
        self.btnPassConfirm.setObjectName(u"btnPassConfirm")
        self.btnPassConfirm.setGeometry(QRect(10, 40, 111, 31))
        self.btnPassConfirm.setStyleSheet(u"QPushButton {\n"
"  background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(184, 184,      184, 255),stop:1 rgba(159, 159, 159, 255));\n"
"	color: #000;\n"
"	min-width: 80px;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: #051a39;\n"
"	padding: 5px;\n"
"}\n"
"QPushButton#btnPassConfirm:hover\n"
"{\n"
"	background-color: rgba(70,162,218,50%);\n"
"	border: 1px solid #46a2da;\n"
"\n"
"}\n"
"\n"
"QPushButton#btnPassConfirm:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        self.lbldate = QLabel(self.centralwidget)
        self.lbldate.setObjectName(u"lbldate")
        self.lbldate.setGeometry(QRect(570, 10, 201, 20))
        self.lbldate.setAlignment(Qt.AlignCenter)
        self.lblcurrentUser = QLabel(self.centralwidget)
        self.lblcurrentUser.setObjectName(u"lblcurrentUser")
        self.lblcurrentUser.setGeometry(QRect(450, 270, 201, 20))
        self.lblcurrentUser.setAlignment(Qt.AlignCenter)
        self.lbldate_3 = QLabel(self.centralwidget)
        self.lbldate_3.setObjectName(u"lbldate_3")
        self.lbldate_3.setGeometry(QRect(660, 270, 111, 20))
        self.lbldate_3.setAlignment(Qt.AlignCenter)
        MainWindow2.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow2)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow2.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow2)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow2.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow2)

        QMetaObject.connectSlotsByName(MainWindow2)
    # setupUi

    def retranslateUi(self, MainWindow2):
        MainWindow2.setWindowTitle(QCoreApplication.translate("MainWindow2", u"MainWindow", None))
        self.back.setText(QCoreApplication.translate("MainWindow2", u"\u0639\u0648\u062f\u0629", None))
        self.exit.setText(QCoreApplication.translate("MainWindow2", u"\u062e\u0631\u0648\u062c", None))
        self.label.setText("")
        self.btnDebts.setText(QCoreApplication.translate("MainWindow2", u"\u0627\u0644\u0630\u0645\u0645", None))
        self.btnOfficeData.setText(QCoreApplication.translate("MainWindow2", u"\u0628\u064a\u0627\u0646\u0627\u062a \u0627\u0644\u0645\u0643\u062a\u0628", None))
        self.btnMarketing.setText(QCoreApplication.translate("MainWindow2", u"\u062d\u0633\u0627\u0628 \u0627\u0644\u0645\u0633\u0648\u0642\u0627\u062a", None))
        self.btnAdjust.setText(QCoreApplication.translate("MainWindow2", u"\u062a\u0639\u062f\u064a\u0644 \u0627\u0644\u0642\u0648\u0627\u0626\u0645", None))
        self.btnChangePassword.setText(QCoreApplication.translate("MainWindow2", u"\u062a\u063a\u064a\u064a\u0631 \u0643\u0644\u0645\u0629 \u0627\u0644\u0645\u0631\u0648\u0631", None))
        self.btnData.setText(QCoreApplication.translate("MainWindow2", u"\u0627\u0644\u0628\u064a\u0627\u0646\u0627\u062a", None))
        self.btnEntry.setText(QCoreApplication.translate("MainWindow2", u"\u0627\u062f\u062e\u0627\u0644 \u0627\u0644\u0628\u064a\u0627\u0646\u0627\u062a", None))
        self.btnKasse.setText(QCoreApplication.translate("MainWindow2", u"\u064a\u0648\u0645\u064a\u0629 \u0627\u0644\u0635\u0646\u062f\u0648\u0642", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow2", u"\u0627\u0633\u0645 \u0627\u0644\u0645\u0633\u062a\u062e\u062f\u0645", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow2", u"\u0643\u0644\u0645\u0629 \u0627\u0644\u0645\u0631\u0648\u0631", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow2", u"\u0643\u0644\u0645\u0629 \u0627\u0644\u0645\u0631\u0648\u0631 \u0627\u0644\u062c\u062f\u064a\u062f\u0629", None))
        self.btnPassConfirm.setText(QCoreApplication.translate("MainWindow2", u"\u062a\u063a\u064a\u064a\u0631", None))
        self.lbldate.setText("")
        self.lblcurrentUser.setText("")
        self.lbldate_3.setText(QCoreApplication.translate("MainWindow2", u"\u0627\u0644\u0645\u0633\u062a\u062e\u062f\u0645 \u0627\u0644\u062d\u0627\u0644\u064a", None))
    # retranslateUi

