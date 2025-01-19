# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'logIn.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QLabel,
    QLayout, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QRadioButton, QSizePolicy, QStatusBar,
    QTabWidget, QVBoxLayout, QWidget)

class Ui_logIn(object):
    def setupUi(self, logIn):
        if not logIn.objectName():
            logIn.setObjectName(u"logIn")
        logIn.resize(353, 705)
        logIn.setCursor(QCursor(Qt.ArrowCursor))
        logIn.setLayoutDirection(Qt.RightToLeft)
        logIn.setAutoFillBackground(False)
        logIn.setStyleSheet(u"background-color: #FBAB7E;\n"
"background-image: linear-gradient(62deg, #FBAB7E 0%, #F7CE68 100%);\n"
"")
        logIn.setLocale(QLocale(QLocale.Arabic, QLocale.Syria))
        logIn.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(logIn)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: #e4e4e4;\n"
"	color: #000;\n"
"	selection-background-color: #46a2da;\n"
"	selection-color: #fff;\n"
"\n"
"go::hover\n"
"{\n"
"	background-color: rgba(70,162,218,50%);\n"
"	border: 1px solid #46a2da;\n"
"\n"
"}")
        self.frmLogo = QFrame(self.centralwidget)
        self.frmLogo.setObjectName(u"frmLogo")
        self.frmLogo.setGeometry(QRect(9, 19, 331, 281))
        self.frmLogo.setCursor(QCursor(Qt.ArrowCursor))
        self.frmLogo.setStyleSheet(u"")
        self.frmLogo.setFrameShape(QFrame.Box)
        self.frmLogo.setFrameShadow(QFrame.Raised)
        self.frmLogo.setLineWidth(4)
        self.frmLogo.setMidLineWidth(0)
        self.labelLogo = QLabel(self.frmLogo)
        self.labelLogo.setObjectName(u"labelLogo")
        self.labelLogo.setGeometry(QRect(10, 10, 311, 261))
        self.labelLogo.setFrameShape(QFrame.NoFrame)
        self.labelLogo.setPixmap(QPixmap(u"media/logo_and_new_collection_gold.pdf"))
        self.labelLogo.setScaledContents(True)
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(30, 550, 309, 62))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 0, 10, 0)
        self.go = QPushButton(self.verticalLayoutWidget)
        self.go.setObjectName(u"go")
        self.go.setEnabled(True)
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        gradient = QLinearGradient(1, 0, 1, 1)
        gradient.setSpread(QGradient.RepeatSpread)
        gradient.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient.setColorAt(0, QColor(184, 184, 184, 255))
        gradient.setColorAt(1, QColor(159, 159, 159, 255))
        brush1 = QBrush(gradient)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(238, 238, 238, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(111, 111, 111, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(148, 148, 148, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        gradient1 = QLinearGradient(1, 0, 1, 1)
        gradient1.setSpread(QGradient.RepeatSpread)
        gradient1.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient1.setColorAt(0, QColor(184, 184, 184, 255))
        gradient1.setColorAt(1, QColor(159, 159, 159, 255))
        brush6 = QBrush(gradient1)
        palette.setBrush(QPalette.Active, QPalette.Base, brush6)
        gradient2 = QLinearGradient(1, 0, 1, 1)
        gradient2.setSpread(QGradient.RepeatSpread)
        gradient2.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient2.setColorAt(0, QColor(184, 184, 184, 255))
        gradient2.setColorAt(1, QColor(159, 159, 159, 255))
        brush7 = QBrush(gradient2)
        palette.setBrush(QPalette.Active, QPalette.Window, brush7)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush)
        brush8 = QBrush(QColor(70, 162, 218, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush8)
        palette.setBrush(QPalette.Active, QPalette.HighlightedText, brush2)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        brush9 = QBrush(QColor(255, 255, 220, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush9)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        brush10 = QBrush(QColor(0, 0, 0, 128))
        brush10.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush10)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        gradient3 = QLinearGradient(1, 0, 1, 1)
        gradient3.setSpread(QGradient.RepeatSpread)
        gradient3.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient3.setColorAt(0, QColor(184, 184, 184, 255))
        gradient3.setColorAt(1, QColor(159, 159, 159, 255))
        brush11 = QBrush(gradient3)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush11)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        gradient4 = QLinearGradient(1, 0, 1, 1)
        gradient4.setSpread(QGradient.RepeatSpread)
        gradient4.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient4.setColorAt(0, QColor(184, 184, 184, 255))
        gradient4.setColorAt(1, QColor(159, 159, 159, 255))
        brush12 = QBrush(gradient4)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush12)
        gradient5 = QLinearGradient(1, 0, 1, 1)
        gradient5.setSpread(QGradient.RepeatSpread)
        gradient5.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient5.setColorAt(0, QColor(184, 184, 184, 255))
        gradient5.setColorAt(1, QColor(159, 159, 159, 255))
        brush13 = QBrush(gradient5)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush13)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush9)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush10)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        gradient6 = QLinearGradient(1, 0, 1, 1)
        gradient6.setSpread(QGradient.RepeatSpread)
        gradient6.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient6.setColorAt(0, QColor(184, 184, 184, 255))
        gradient6.setColorAt(1, QColor(159, 159, 159, 255))
        brush14 = QBrush(gradient6)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush14)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        gradient7 = QLinearGradient(1, 0, 1, 1)
        gradient7.setSpread(QGradient.RepeatSpread)
        gradient7.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient7.setColorAt(0, QColor(184, 184, 184, 255))
        gradient7.setColorAt(1, QColor(159, 159, 159, 255))
        brush15 = QBrush(gradient7)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush15)
        gradient8 = QLinearGradient(1, 0, 1, 1)
        gradient8.setSpread(QGradient.RepeatSpread)
        gradient8.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient8.setColorAt(0, QColor(184, 184, 184, 255))
        gradient8.setColorAt(1, QColor(159, 159, 159, 255))
        brush16 = QBrush(gradient8)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush16)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush2)
        brush17 = QBrush(QColor(222, 222, 222, 255))
        brush17.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush17)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush9)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush10)
#endif
        self.go.setPalette(palette)
        self.go.setCursor(QCursor(Qt.PointingHandCursor))
        self.go.setMouseTracking(True)
        self.go.setAutoFillBackground(False)
        self.go.setStyleSheet(u"QPushButton {\n"
"  background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(184, 184,      184, 255),stop:1 rgba(159, 159, 159, 255));\n"
"	color: #000;\n"
"	min-width: 80px;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: #051a39;\n"
"	padding: 5px;\n"
"}\n"
"QPushButton#go:hover\n"
"{\n"
"	background-color: rgba(70,162,218,50%);\n"
"	border: 1px solid #46a2da;\n"
"\n"
"}\n"
"\n"
"QPushButton#go:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}")

        self.verticalLayout.addWidget(self.go)

        self.btnExit = QPushButton(self.verticalLayoutWidget)
        self.btnExit.setObjectName(u"btnExit")
        self.btnExit.setEnabled(True)
        self.btnExit.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnExit.setAutoFillBackground(False)
        self.btnExit.setStyleSheet(u"QPushButton {\n"
"  background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(184, 184,      184, 255),stop:1 rgba(159, 159, 159, 255));\n"
"	color: #000;\n"
"	min-width: 80px;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: #051a39;\n"
"	padding: 5px;\n"
"}\n"
"QPushButton#btnExit:hover\n"
"{\n"
"	background-color: rgba(70,162,218,50%);\n"
"	border: 1px solid #46a2da;\n"
"\n"
"}\n"
"\n"
"QPushButton#btnExit:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        self.btnExit.setFlat(False)

        self.verticalLayout.addWidget(self.btnExit)

        self.formLayoutWidget = QWidget(self.centralwidget)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(40, 330, 299, 81))
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
        font.setPointSize(14)
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

        self.lblpassword = QLabel(self.formLayoutWidget)
        self.lblpassword.setObjectName(u"lblpassword")
        self.lblpassword.setStyleSheet(u"font: 700 14pt \"Arial\";\n"
"\n"
"	background-color: transparent;\n"
"\n"
"	color: black;")
        self.lblpassword.setFrameShape(QFrame.Box)
        self.lblpassword.setFrameShadow(QFrame.Raised)
        self.lblpassword.setTextFormat(Qt.PlainText)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lblpassword)

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

        self.verticalLayoutWidget_3 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(180, 450, 160, 80))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.rdbAdmin = QRadioButton(self.verticalLayoutWidget_3)
        self.rdbAdmin.setObjectName(u"rdbAdmin")

        self.verticalLayout_3.addWidget(self.rdbAdmin)

        self.rdbManager = QRadioButton(self.verticalLayoutWidget_3)
        self.rdbManager.setObjectName(u"rdbManager")

        self.verticalLayout_3.addWidget(self.rdbManager)

        self.rdbUser = QRadioButton(self.verticalLayoutWidget_3)
        self.rdbUser.setObjectName(u"rdbUser")

        self.verticalLayout_3.addWidget(self.rdbUser)

        logIn.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(logIn)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 353, 24))
        self.menubar.setStyleSheet(u"background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(227, 227, 227, 255),stop:1 rgba(187, 187, 187, 255));\n"
"	border: 1px solid #f1f1f1;\n"
"	color: #000;")
        logIn.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(logIn)
        self.statusbar.setObjectName(u"statusbar")
        logIn.setStatusBar(self.statusbar)

        self.retranslateUi(logIn)

        QMetaObject.connectSlotsByName(logIn)
    # setupUi

    def retranslateUi(self, logIn):
        logIn.setWindowTitle(QCoreApplication.translate("logIn", u"LogIn", None))
        self.labelLogo.setText("")
        self.go.setText(QCoreApplication.translate("logIn", u"\u062a\u0633\u062c\u064a\u0644 \u0627\u0644\u062f\u062e\u0648\u0644", None))
        self.btnExit.setText(QCoreApplication.translate("logIn", u"\u062e\u0631\u0648\u062c", None))
        self.lblUserName.setText(QCoreApplication.translate("logIn", u"\u0627\u0633\u0645 \u0627\u0644\u0645\u0633\u062a\u062e\u062f\u0645", None))
        self.lblpassword.setText(QCoreApplication.translate("logIn", u" \u0643\u0644\u0645\u0629 \u0627\u0644\u0645\u0631\u0648\u0631", None))
        self.rdbAdmin.setText(QCoreApplication.translate("logIn", u"\u0627\u0644\u062f\u062e\u0648\u0644 \u0643\u0623\u062f\u0645\u0646", None))
        self.rdbManager.setText(QCoreApplication.translate("logIn", u"\u0627\u0644\u062f\u062e\u0648\u0644 \u0643\u0645\u062f\u064a\u0631", None))
        self.rdbUser.setText(QCoreApplication.translate("logIn", u"\u0627\u0644\u062f\u062e\u0648\u0644 \u0643\u0645\u0633\u062a\u062e\u062f\u0645", None))
    # retranslateUi

