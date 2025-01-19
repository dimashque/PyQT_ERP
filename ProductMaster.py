# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ProductMaster.ui'
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
    QLayout, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_ProductMaster(object):
    def setupUi(self, ProductMaster):
        if not ProductMaster.objectName():
            ProductMaster.setObjectName(u"ProductMaster")
        ProductMaster.resize(717, 670)
        ProductMaster.setLayoutDirection(Qt.RightToLeft)
        ProductMaster.setStyleSheet(u"background-color: #e4e4e4;\n"
"	color: #000;\n"
"	selection-background-color: #46a2da;\n"
"	selection-color: #fff;")
        self.centralwidget = QWidget(ProductMaster)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(50, 20, 601, 61))
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.Panel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(250, 10, 121, 41))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"border: 1px solid gray;\n"
"border-radius: 10px;")
        self.label.setAlignment(Qt.AlignCenter)
        self.lblTotalSum = QLabel(self.frame)
        self.lblTotalSum.setObjectName(u"lblTotalSum")
        self.lblTotalSum.setGeometry(QRect(10, 10, 141, 41))
        font1 = QFont()
        font1.setPointSize(12)
        self.lblTotalSum.setFont(font1)
        self.lblTotalSum.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.lblTotalSum.setAlignment(Qt.AlignCenter)
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(110, 100, 481, 131))
        self.frame_2.setFrameShape(QFrame.Box)
        self.frame_2.setFrameShadow(QFrame.Sunken)
        self.formLayoutWidget = QWidget(self.frame_2)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(200, 10, 261, 110))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.formLayout.setFieldGrowthPolicy(QFormLayout.FieldsStayAtSizeHint)
        self.formLayout.setVerticalSpacing(6)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.inputSort = QLineEdit(self.formLayoutWidget)
        self.inputSort.setObjectName(u"inputSort")
        font2 = QFont()
        font2.setPointSize(14)
        self.inputSort.setFont(font2)
        self.inputSort.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.inputSort)

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

        self.inputBuyPrice = QLineEdit(self.formLayoutWidget)
        self.inputBuyPrice.setObjectName(u"inputBuyPrice")
        self.inputBuyPrice.setFont(font2)
        self.inputBuyPrice.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.inputBuyPrice)

        self.inputSellPrice = QLineEdit(self.formLayoutWidget)
        self.inputSellPrice.setObjectName(u"inputSellPrice")
        self.inputSellPrice.setFont(font2)
        self.inputSellPrice.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.inputSellPrice)

        self.lblUserName = QLabel(self.formLayoutWidget)
        self.lblUserName.setObjectName(u"lblUserName")
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(14)
        font3.setBold(True)
        font3.setItalic(False)
        self.lblUserName.setFont(font3)
        self.lblUserName.setStyleSheet(u"\n"
"	background-color: transparent;\n"
"	color: rgb(0, 0, 0);")
        self.lblUserName.setFrameShape(QFrame.Box)
        self.lblUserName.setFrameShadow(QFrame.Raised)
        self.lblUserName.setTextFormat(Qt.PlainText)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lblUserName)

        self.lblpassword_2 = QLabel(self.formLayoutWidget)
        self.lblpassword_2.setObjectName(u"lblpassword_2")
        self.lblpassword_2.setStyleSheet(u"font: 700 14pt \"Arial\";\n"
"\n"
"	background-color: transparent;\n"
"\n"
"	color: black;")
        self.lblpassword_2.setFrameShape(QFrame.Box)
        self.lblpassword_2.setFrameShadow(QFrame.Raised)
        self.lblpassword_2.setTextFormat(Qt.PlainText)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.lblpassword_2)

        self.verticalLayoutWidget = QWidget(self.frame_2)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(30, 10, 101, 111))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.btnAdd = QPushButton(self.verticalLayoutWidget)
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

        self.verticalLayout.addWidget(self.btnAdd)

        self.btnExport = QPushButton(self.verticalLayoutWidget)
        self.btnExport.setObjectName(u"btnExport")
        self.btnExport.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout.addWidget(self.btnExport)

        self.btnRefresh = QPushButton(self.verticalLayoutWidget)
        self.btnRefresh.setObjectName(u"btnRefresh")
        self.btnRefresh.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout.addWidget(self.btnRefresh)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(20, 240, 671, 381))
        self.frame_3.setFrameShape(QFrame.Box)
        self.frame_3.setFrameShadow(QFrame.Sunken)
        self.listProductMaster = QListWidget(self.frame_3)
        self.listProductMaster.setObjectName(u"listProductMaster")
        self.listProductMaster.setGeometry(QRect(10, 10, 651, 361))
        self.listProductMaster.setStyleSheet(u"QListView \n"
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
"QListView#listProductMaster::disabled \n"
"{\n"
"	background-color: #656565;\n"
"	color: #1b1b1b;\n"
"    border: 1px solid #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView#listProductMaster::item \n"
"{\n"
"	background-color: #f6f6f6;\n"
"    padding: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView#listProductMaster::item:alternate \n"
"{\n"
"    background-color: #c6c6c6;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView#listProductMaster::item:alternate:selected\n"
"{\n"
"    background-color: red;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView#listProductMaster::item:selected \n"
"{\n"
"	background-color: #b78620;\n"
"	border: 1px solid #b78620;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView#listProductMaster::item:selected:!active \n"
"{\n"
"	background-color: #46a2da;\n"
"	border: 1px solid #46a2da;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
""
                        "\n"
"QListView#listProductMaster::item:selected:active \n"
"{\n"
"	background-color: #46a2da;\n"
"	border: 1px solid #46a2da;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView#listProductMaster::item:hover {\n"
"    background-color: #5e5e5e;\n"
"    border: none;\n"
"    color: #000;\n"
"\n"
"}")
        ProductMaster.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(ProductMaster)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 717, 22))
        ProductMaster.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(ProductMaster)
        self.statusbar.setObjectName(u"statusbar")
        ProductMaster.setStatusBar(self.statusbar)

        self.retranslateUi(ProductMaster)

        QMetaObject.connectSlotsByName(ProductMaster)
    # setupUi

    def retranslateUi(self, ProductMaster):
        ProductMaster.setWindowTitle(QCoreApplication.translate("ProductMaster", u"Product Master", None))
        self.label.setText(QCoreApplication.translate("ProductMaster", u"\u062f\u0644\u064a\u0644 \u0627\u0644\u0645\u0648\u0627\u062f", None))
        self.lblTotalSum.setText("")
        self.lblpassword.setText(QCoreApplication.translate("ProductMaster", u" \u0633\u0639\u0631 \u0627\u0644\u0634\u0631\u0627\u0621", None))
        self.lblUserName.setText(QCoreApplication.translate("ProductMaster", u"\u0627\u0644\u0635\u0646\u0641", None))
        self.lblpassword_2.setText(QCoreApplication.translate("ProductMaster", u"\u0633\u0639\u0631 \u0627\u0644\u0645\u0628\u064a\u0639", None))
        self.btnAdd.setText(QCoreApplication.translate("ProductMaster", u"\u0627\u0636\u0627\u0641\u0629", None))
        self.btnExport.setText(QCoreApplication.translate("ProductMaster", u"\u062a\u0635\u062f\u064a\u0631 \u0627\u0644\u0628\u064a\u0627\u0646\u0627\u062a", None))
        self.btnRefresh.setText(QCoreApplication.translate("ProductMaster", u"\u062a\u062d\u062f\u064a\u062b", None))
    # retranslateUi

