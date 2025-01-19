# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Marketing.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_Marketing(object):
    def setupUi(self, Marketing):
        if not Marketing.objectName():
            Marketing.setObjectName(u"Marketing")
        Marketing.resize(1058, 610)
        Marketing.setLayoutDirection(Qt.RightToLeft)
        Marketing.setStyleSheet(u"background-color: #e4e4e4;\n"
"	color: #000;\n"
"	selection-background-color: #46a2da;\n"
"	selection-color: #fff;")
        self.centralwidget = QWidget(Marketing)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(840, 10, 201, 51))
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Sunken)
        self.frame.setLineWidth(4)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 10, 141, 31))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.formLayoutWidget_2 = QWidget(self.centralwidget)
        self.formLayoutWidget_2.setObjectName(u"formLayoutWidget_2")
        self.formLayoutWidget_2.setGeometry(QRect(760, 70, 279, 31))
        self.formLayout_2 = QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.formLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(11)
        font1.setBold(True)
        self.label_2.setFont(font1)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.cbMarketingAgent = QComboBox(self.formLayoutWidget_2)
        self.cbMarketingAgent.setObjectName(u"cbMarketingAgent")
        self.cbMarketingAgent.setLayoutDirection(Qt.LeftToRight)
        self.cbMarketingAgent.setStyleSheet(u"QComboBox::drop-down\n"
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

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.cbMarketingAgent)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(700, 110, 341, 461))
        self.frame_2.setFrameShape(QFrame.Box)
        self.frame_2.setFrameShadow(QFrame.Sunken)
        self.gridLayoutWidget = QWidget(self.frame_2)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 321, 441))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_18 = QLabel(self.gridLayoutWidget)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font1)
        self.label_18.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_18, 9, 0, 1, 1)

        self.lineEditNumpayed = QLineEdit(self.gridLayoutWidget)
        self.lineEditNumpayed.setObjectName(u"lineEditNumpayed")
        self.lineEditNumpayed.setStyleSheet(u"QLineEdit\n"
"{\n"
"	background-color: #f6f6f6;\n"
"	color : #000;\n"
"	border: 1px solid #343434;\n"
"	padding: 3px;\n"
"	padding-left: 5px;\n"
"\n"
"}")

        self.gridLayout.addWidget(self.lineEditNumpayed, 1, 1, 1, 1)

        self.label_14 = QLabel(self.gridLayoutWidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font)
        self.label_14.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_14, 0, 2, 1, 1)

        self.label_25 = QLabel(self.gridLayoutWidget)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font1)
        self.label_25.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_25, 10, 0, 1, 1)

        self.label_12 = QLabel(self.gridLayoutWidget)
        self.label_12.setObjectName(u"label_12")
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setItalic(False)
        self.label_12.setFont(font2)
        self.label_12.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_12, 0, 0, 1, 1)

        self.label_16 = QLabel(self.gridLayoutWidget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font1)
        self.label_16.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_16, 2, 0, 1, 1)

        self.label_20 = QLabel(self.gridLayoutWidget)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font1)
        self.label_20.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_20, 12, 0, 1, 1)

        self.label_22 = QLabel(self.gridLayoutWidget)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font1)
        self.label_22.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_22, 5, 0, 1, 1)

        self.label_21 = QLabel(self.gridLayoutWidget)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font1)
        self.label_21.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_21, 7, 0, 1, 1)

        self.label_27 = QLabel(self.gridLayoutWidget)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font1)
        self.label_27.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_27, 11, 0, 1, 1)

        self.label_26 = QLabel(self.gridLayoutWidget)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font1)
        self.label_26.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_26, 4, 0, 1, 1)

        self.label_13 = QLabel(self.gridLayoutWidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font)
        self.label_13.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_13, 0, 1, 1, 1)

        self.label_15 = QLabel(self.gridLayoutWidget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font1)
        self.label_15.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_15, 1, 0, 1, 1)

        self.lineEditRatePayed = QLineEdit(self.gridLayoutWidget)
        self.lineEditRatePayed.setObjectName(u"lineEditRatePayed")
        self.lineEditRatePayed.setStyleSheet(u"QLineEdit\n"
"{\n"
"	background-color: #f6f6f6;\n"
"	color : #000;\n"
"	border: 1px solid #343434;\n"
"	padding: 3px;\n"
"	padding-left: 5px;\n"
"\n"
"}")

        self.gridLayout.addWidget(self.lineEditRatePayed, 1, 2, 1, 1)

        self.label_23 = QLabel(self.gridLayoutWidget)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font1)
        self.label_23.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_23, 6, 0, 1, 1)

        self.label_19 = QLabel(self.gridLayoutWidget)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font1)
        self.label_19.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_19, 8, 0, 1, 1)

        self.label_17 = QLabel(self.gridLayoutWidget)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font1)
        self.label_17.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_17, 3, 0, 1, 1)

        self.label_24 = QLabel(self.gridLayoutWidget)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font1)
        self.label_24.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_24, 13, 0, 1, 1)

        self.lineEditNumRest = QLineEdit(self.gridLayoutWidget)
        self.lineEditNumRest.setObjectName(u"lineEditNumRest")
        self.lineEditNumRest.setStyleSheet(u"QLineEdit\n"
"{\n"
"	background-color: #f6f6f6;\n"
"	color : #000;\n"
"	border: 1px solid #343434;\n"
"	padding: 3px;\n"
"	padding-left: 5px;\n"
"\n"
"}")

        self.gridLayout.addWidget(self.lineEditNumRest, 2, 1, 1, 1)

        self.lineEditNumPeding = QLineEdit(self.gridLayoutWidget)
        self.lineEditNumPeding.setObjectName(u"lineEditNumPeding")
        self.lineEditNumPeding.setStyleSheet(u"QLineEdit\n"
"{\n"
"	background-color: #f6f6f6;\n"
"	color : #000;\n"
"	border: 1px solid #343434;\n"
"	padding: 3px;\n"
"	padding-left: 5px;\n"
"\n"
"}")

        self.gridLayout.addWidget(self.lineEditNumPeding, 3, 1, 1, 1)

        self.lineEditNumCanceld = QLineEdit(self.gridLayoutWidget)
        self.lineEditNumCanceld.setObjectName(u"lineEditNumCanceld")
        self.lineEditNumCanceld.setStyleSheet(u"QLineEdit\n"
"{\n"
"	background-color: #f6f6f6;\n"
"	color : #000;\n"
"	border: 1px solid #343434;\n"
"	padding: 3px;\n"
"	padding-left: 5px;\n"
"\n"
"}")

        self.gridLayout.addWidget(self.lineEditNumCanceld, 4, 1, 1, 1)

        self.lineEditNumShipped = QLineEdit(self.gridLayoutWidget)
        self.lineEditNumShipped.setObjectName(u"lineEditNumShipped")
        self.lineEditNumShipped.setStyleSheet(u"QLineEdit\n"
"{\n"
"	background-color: #f6f6f6;\n"
"	color : #000;\n"
"	border: 1px solid #343434;\n"
"	padding: 3px;\n"
"	padding-left: 5px;\n"
"\n"
"}")

        self.gridLayout.addWidget(self.lineEditNumShipped, 5, 1, 1, 1)

        self.lineEditNumInDelivery = QLineEdit(self.gridLayoutWidget)
        self.lineEditNumInDelivery.setObjectName(u"lineEditNumInDelivery")
        self.lineEditNumInDelivery.setStyleSheet(u"QLineEdit\n"
"{\n"
"	background-color: #f6f6f6;\n"
"	color : #000;\n"
"	border: 1px solid #343434;\n"
"	padding: 3px;\n"
"	padding-left: 5px;\n"
"\n"
"}")

        self.gridLayout.addWidget(self.lineEditNumInDelivery, 6, 1, 1, 1)

        self.lineEditNumReturned = QLineEdit(self.gridLayoutWidget)
        self.lineEditNumReturned.setObjectName(u"lineEditNumReturned")
        self.lineEditNumReturned.setStyleSheet(u"QLineEdit\n"
"{\n"
"	background-color: #f6f6f6;\n"
"	color : #000;\n"
"	border: 1px solid #343434;\n"
"	padding: 3px;\n"
"	padding-left: 5px;\n"
"\n"
"}")

        self.gridLayout.addWidget(self.lineEditNumReturned, 7, 1, 1, 1)

        self.lineEditNumPostponed = QLineEdit(self.gridLayoutWidget)
        self.lineEditNumPostponed.setObjectName(u"lineEditNumPostponed")
        self.lineEditNumPostponed.setStyleSheet(u"QLineEdit\n"
"{\n"
"	background-color: #f6f6f6;\n"
"	color : #000;\n"
"	border: 1px solid #343434;\n"
"	padding: 3px;\n"
"	padding-left: 5px;\n"
"\n"
"}")

        self.gridLayout.addWidget(self.lineEditNumPostponed, 8, 1, 1, 1)

        self.lineEditNumNotAvailble = QLineEdit(self.gridLayoutWidget)
        self.lineEditNumNotAvailble.setObjectName(u"lineEditNumNotAvailble")
        self.lineEditNumNotAvailble.setStyleSheet(u"QLineEdit\n"
"{\n"
"	background-color: #f6f6f6;\n"
"	color : #000;\n"
"	border: 1px solid #343434;\n"
"	padding: 3px;\n"
"	padding-left: 5px;\n"
"\n"
"}")

        self.gridLayout.addWidget(self.lineEditNumNotAvailble, 9, 1, 1, 1)

        self.lineEditNumNoLine = QLineEdit(self.gridLayoutWidget)
        self.lineEditNumNoLine.setObjectName(u"lineEditNumNoLine")
        self.lineEditNumNoLine.setStyleSheet(u"QLineEdit\n"
"{\n"
"	background-color: #f6f6f6;\n"
"	color : #000;\n"
"	border: 1px solid #343434;\n"
"	padding: 3px;\n"
"	padding-left: 5px;\n"
"\n"
"}")

        self.gridLayout.addWidget(self.lineEditNumNoLine, 10, 1, 1, 1)

        self.lineEditNumNoAnswer = QLineEdit(self.gridLayoutWidget)
        self.lineEditNumNoAnswer.setObjectName(u"lineEditNumNoAnswer")
        self.lineEditNumNoAnswer.setStyleSheet(u"QLineEdit\n"
"{\n"
"	background-color: #f6f6f6;\n"
"	color : #000;\n"
"	border: 1px solid #343434;\n"
"	padding: 3px;\n"
"	padding-left: 5px;\n"
"\n"
"}")

        self.gridLayout.addWidget(self.lineEditNumNoAnswer, 11, 1, 1, 1)

        self.lineEditNumSpecial = QLineEdit(self.gridLayoutWidget)
        self.lineEditNumSpecial.setObjectName(u"lineEditNumSpecial")
        self.lineEditNumSpecial.setStyleSheet(u"QLineEdit\n"
"{\n"
"	background-color: #f6f6f6;\n"
"	color : #000;\n"
"	border: 1px solid #343434;\n"
"	padding: 3px;\n"
"	padding-left: 5px;\n"
"\n"
"}")

        self.gridLayout.addWidget(self.lineEditNumSpecial, 12, 1, 1, 1)

        self.lineEditNumSum = QLineEdit(self.gridLayoutWidget)
        self.lineEditNumSum.setObjectName(u"lineEditNumSum")
        self.lineEditNumSum.setStyleSheet(u"QLineEdit\n"
"{\n"
"	background-color: #f6f6f6;\n"
"	color : #000;\n"
"	border: 1px solid #343434;\n"
"	padding: 3px;\n"
"	padding-left: 5px;\n"
"\n"
"}")

        self.gridLayout.addWidget(self.lineEditNumSum, 13, 1, 1, 1)

        self.lineEditRateRest = QLineEdit(self.gridLayoutWidget)
        self.lineEditRateRest.setObjectName(u"lineEditRateRest")
        self.lineEditRateRest.setStyleSheet(u"QLineEdit\n"
"{\n"
"	background-color: #f6f6f6;\n"
"	color : #000;\n"
"	border: 1px solid #343434;\n"
"	padding: 3px;\n"
"	padding-left: 5px;\n"
"\n"
"}")

        self.gridLayout.addWidget(self.lineEditRateRest, 2, 2, 1, 1)

        self.lineEditRatePedning = QLineEdit(self.gridLayoutWidget)
        self.lineEditRatePedning.setObjectName(u"lineEditRatePedning")
        self.lineEditRatePedning.setStyleSheet(u"QLineEdit\n"
"{\n"
"	background-color: #f6f6f6;\n"
"	color : #000;\n"
"	border: 1px solid #343434;\n"
"	padding: 3px;\n"
"	padding-left: 5px;\n"
"\n"
"}")

        self.gridLayout.addWidget(self.lineEditRatePedning, 3, 2, 1, 1)

        self.lineEditRateCanceld = QLineEdit(self.gridLayoutWidget)
        self.lineEditRateCanceld.setObjectName(u"lineEditRateCanceld")
        self.lineEditRateCanceld.setStyleSheet(u"QLineEdit\n"
"{\n"
"	background-color: #f6f6f6;\n"
"	color : #000;\n"
"	border: 1px solid #343434;\n"
"	padding: 3px;\n"
"	padding-left: 5px;\n"
"\n"
"}")

        self.gridLayout.addWidget(self.lineEditRateCanceld, 4, 2, 1, 1)

        self.lineEditRateShipped = QLineEdit(self.gridLayoutWidget)
        self.lineEditRateShipped.setObjectName(u"lineEditRateShipped")
        self.lineEditRateShipped.setStyleSheet(u"QLineEdit\n"
"{\n"
"	background-color: #f6f6f6;\n"
"	color : #000;\n"
"	border: 1px solid #343434;\n"
"	padding: 3px;\n"
"	padding-left: 5px;\n"
"\n"
"}")

        self.gridLayout.addWidget(self.lineEditRateShipped, 5, 2, 1, 1)

        self.lineEditRateInDelivery = QLineEdit(self.gridLayoutWidget)
        self.lineEditRateInDelivery.setObjectName(u"lineEditRateInDelivery")
        self.lineEditRateInDelivery.setStyleSheet(u"QLineEdit\n"
"{\n"
"	background-color: #f6f6f6;\n"
"	color : #000;\n"
"	border: 1px solid #343434;\n"
"	padding: 3px;\n"
"	padding-left: 5px;\n"
"\n"
"}")

        self.gridLayout.addWidget(self.lineEditRateInDelivery, 6, 2, 1, 1)

        self.lineEditRateReturned = QLineEdit(self.gridLayoutWidget)
        self.lineEditRateReturned.setObjectName(u"lineEditRateReturned")
        self.lineEditRateReturned.setStyleSheet(u"QLineEdit\n"
"{\n"
"	background-color: #f6f6f6;\n"
"	color : #000;\n"
"	border: 1px solid #343434;\n"
"	padding: 3px;\n"
"	padding-left: 5px;\n"
"\n"
"}")

        self.gridLayout.addWidget(self.lineEditRateReturned, 7, 2, 1, 1)

        self.lineEditRatePostPoned = QLineEdit(self.gridLayoutWidget)
        self.lineEditRatePostPoned.setObjectName(u"lineEditRatePostPoned")
        self.lineEditRatePostPoned.setStyleSheet(u"QLineEdit\n"
"{\n"
"	background-color: #f6f6f6;\n"
"	color : #000;\n"
"	border: 1px solid #343434;\n"
"	padding: 3px;\n"
"	padding-left: 5px;\n"
"\n"
"}")

        self.gridLayout.addWidget(self.lineEditRatePostPoned, 8, 2, 1, 1)

        self.lineEditRateNotAvailble = QLineEdit(self.gridLayoutWidget)
        self.lineEditRateNotAvailble.setObjectName(u"lineEditRateNotAvailble")
        self.lineEditRateNotAvailble.setStyleSheet(u"QLineEdit\n"
"{\n"
"	background-color: #f6f6f6;\n"
"	color : #000;\n"
"	border: 1px solid #343434;\n"
"	padding: 3px;\n"
"	padding-left: 5px;\n"
"\n"
"}")

        self.gridLayout.addWidget(self.lineEditRateNotAvailble, 9, 2, 1, 1)

        self.lineEditRateNoLine = QLineEdit(self.gridLayoutWidget)
        self.lineEditRateNoLine.setObjectName(u"lineEditRateNoLine")
        self.lineEditRateNoLine.setStyleSheet(u"QLineEdit\n"
"{\n"
"	background-color: #f6f6f6;\n"
"	color : #000;\n"
"	border: 1px solid #343434;\n"
"	padding: 3px;\n"
"	padding-left: 5px;\n"
"\n"
"}")

        self.gridLayout.addWidget(self.lineEditRateNoLine, 10, 2, 1, 1)

        self.lineEditRateNoAnswer = QLineEdit(self.gridLayoutWidget)
        self.lineEditRateNoAnswer.setObjectName(u"lineEditRateNoAnswer")
        self.lineEditRateNoAnswer.setStyleSheet(u"QLineEdit\n"
"{\n"
"	background-color: #f6f6f6;\n"
"	color : #000;\n"
"	border: 1px solid #343434;\n"
"	padding: 3px;\n"
"	padding-left: 5px;\n"
"\n"
"}")

        self.gridLayout.addWidget(self.lineEditRateNoAnswer, 11, 2, 1, 1)

        self.lineEditRateSpecial = QLineEdit(self.gridLayoutWidget)
        self.lineEditRateSpecial.setObjectName(u"lineEditRateSpecial")
        self.lineEditRateSpecial.setStyleSheet(u"QLineEdit\n"
"{\n"
"	background-color: #f6f6f6;\n"
"	color : #000;\n"
"	border: 1px solid #343434;\n"
"	padding: 3px;\n"
"	padding-left: 5px;\n"
"\n"
"}")

        self.gridLayout.addWidget(self.lineEditRateSpecial, 12, 2, 1, 1)

        self.lineEditRateSum = QLineEdit(self.gridLayoutWidget)
        self.lineEditRateSum.setObjectName(u"lineEditRateSum")
        self.lineEditRateSum.setStyleSheet(u"QLineEdit\n"
"{\n"
"	background-color: #f6f6f6;\n"
"	color : #000;\n"
"	border: 1px solid #343434;\n"
"	padding: 3px;\n"
"	padding-left: 5px;\n"
"\n"
"}")

        self.gridLayout.addWidget(self.lineEditRateSum, 13, 2, 1, 1)

        self.gridLayout.setColumnStretch(0, 2)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnStretch(2, 2)
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(340, 110, 341, 381))
        self.frame_3.setFrameShape(QFrame.Box)
        self.frame_3.setFrameShadow(QFrame.Sunken)
        self.gridLayoutWidget_2 = QWidget(self.frame_3)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(10, 10, 321, 121))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_39 = QLabel(self.gridLayoutWidget_2)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setFont(font1)
        self.label_39.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_39, 1, 0, 1, 1)

        self.lineEditNumShippingDisc = QLineEdit(self.gridLayoutWidget_2)
        self.lineEditNumShippingDisc.setObjectName(u"lineEditNumShippingDisc")
        self.lineEditNumShippingDisc.setStyleSheet(u"QLineEdit\n"
"{\n"
"	background-color: #f6f6f6;\n"
"	color : #000;\n"
"	border: 1px solid #343434;\n"
"	padding: 3px;\n"
"	padding-left: 5px;\n"
"\n"
"}")

        self.gridLayout_2.addWidget(self.lineEditNumShippingDisc, 2, 1, 1, 1)

        self.label_32 = QLabel(self.gridLayoutWidget_2)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setFont(font1)
        self.label_32.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_32, 2, 0, 1, 1)

        self.lineEditRateDiliveryDisc = QLineEdit(self.gridLayoutWidget_2)
        self.lineEditRateDiliveryDisc.setObjectName(u"lineEditRateDiliveryDisc")
        self.lineEditRateDiliveryDisc.setStyleSheet(u"QLineEdit\n"
"{\n"
"	background-color: #f6f6f6;\n"
"	color : #000;\n"
"	border: 1px solid #343434;\n"
"	padding: 3px;\n"
"	padding-left: 5px;\n"
"\n"
"}")

        self.gridLayout_2.addWidget(self.lineEditRateDiliveryDisc, 1, 2, 1, 1)

        self.lineEditNumDileveryDisc = QLineEdit(self.gridLayoutWidget_2)
        self.lineEditNumDileveryDisc.setObjectName(u"lineEditNumDileveryDisc")
        self.lineEditNumDileveryDisc.setStyleSheet(u"QLineEdit\n"
"{\n"
"	background-color: #f6f6f6;\n"
"	color : #000;\n"
"	border: 1px solid #343434;\n"
"	padding: 3px;\n"
"	padding-left: 5px;\n"
"\n"
"}")

        self.gridLayout_2.addWidget(self.lineEditNumDileveryDisc, 1, 1, 1, 1)

        self.lineEditNumSumDisc = QLineEdit(self.gridLayoutWidget_2)
        self.lineEditNumSumDisc.setObjectName(u"lineEditNumSumDisc")
        self.lineEditNumSumDisc.setStyleSheet(u"QLineEdit\n"
"{\n"
"	background-color: #f6f6f6;\n"
"	color : #000;\n"
"	border: 1px solid #343434;\n"
"	padding: 3px;\n"
"	padding-left: 5px;\n"
"\n"
"}")

        self.gridLayout_2.addWidget(self.lineEditNumSumDisc, 3, 1, 1, 1)

        self.lineEditRateSumDisc = QLineEdit(self.gridLayoutWidget_2)
        self.lineEditRateSumDisc.setObjectName(u"lineEditRateSumDisc")
        self.lineEditRateSumDisc.setStyleSheet(u"QLineEdit\n"
"{\n"
"	background-color: #f6f6f6;\n"
"	color : #000;\n"
"	border: 1px solid #343434;\n"
"	padding: 3px;\n"
"	padding-left: 5px;\n"
"\n"
"}")

        self.gridLayout_2.addWidget(self.lineEditRateSumDisc, 3, 2, 1, 1)

        self.lineEditRateShippingDisc_2 = QLineEdit(self.gridLayoutWidget_2)
        self.lineEditRateShippingDisc_2.setObjectName(u"lineEditRateShippingDisc_2")
        self.lineEditRateShippingDisc_2.setStyleSheet(u"QLineEdit\n"
"{\n"
"	background-color: #f6f6f6;\n"
"	color : #000;\n"
"	border: 1px solid #343434;\n"
"	padding: 3px;\n"
"	padding-left: 5px;\n"
"\n"
"}")

        self.gridLayout_2.addWidget(self.lineEditRateShippingDisc_2, 2, 2, 1, 1)

        self.label_42 = QLabel(self.gridLayoutWidget_2)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setFont(font1)
        self.label_42.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_42, 3, 0, 1, 1)

        self.label_31 = QLabel(self.gridLayoutWidget_2)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font2)
        self.label_31.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_31, 0, 0, 1, 1)

        self.label_38 = QLabel(self.gridLayoutWidget_2)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setFont(font)
        self.label_38.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_38, 0, 1, 1, 1)

        self.label_29 = QLabel(self.gridLayoutWidget_2)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font)
        self.label_29.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_29, 0, 2, 1, 1)

        self.gridLayout_2.setColumnStretch(0, 2)
        self.gridLayout_2.setColumnStretch(1, 1)
        self.gridLayout_2.setColumnStretch(2, 2)
        self.formLayoutWidget = QWidget(self.frame_3)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(30, 170, 281, 72))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_3)

        self.inpuAchivment = QLineEdit(self.formLayoutWidget)
        self.inpuAchivment.setObjectName(u"inpuAchivment")
        font3 = QFont()
        font3.setPointSize(14)
        self.inpuAchivment.setFont(font3)
        self.inpuAchivment.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.inpuAchivment)

        self.label_4 = QLabel(self.formLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_4)

        self.inputNetto = QLineEdit(self.formLayoutWidget)
        self.inputNetto.setObjectName(u"inputNetto")
        self.inputNetto.setFont(font3)
        self.inputNetto.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.inputNetto)

        self.horizontalLayoutWidget = QWidget(self.frame_3)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 300, 321, 61))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_28 = QLabel(self.horizontalLayoutWidget)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font1)
        self.label_28.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_28)

        self.cbStatus = QComboBox(self.horizontalLayoutWidget)
        self.cbStatus.setObjectName(u"cbStatus")
        self.cbStatus.setLayoutDirection(Qt.LeftToRight)
        self.cbStatus.setStyleSheet(u"QComboBox::drop-down\n"
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

        self.verticalLayout.addWidget(self.cbStatus)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_40 = QLabel(self.horizontalLayoutWidget)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setFont(font1)
        self.label_40.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_40)

        self.lineEditNumStatus = QLineEdit(self.horizontalLayoutWidget)
        self.lineEditNumStatus.setObjectName(u"lineEditNumStatus")
        self.lineEditNumStatus.setStyleSheet(u"QLineEdit\n"
"{\n"
"	background-color: #f6f6f6;\n"
"	color : #000;\n"
"	border: 1px solid #343434;\n"
"	padding: 3px;\n"
"	padding-left: 5px;\n"
"\n"
"}")

        self.verticalLayout_2.addWidget(self.lineEditNumStatus)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_30 = QLabel(self.horizontalLayoutWidget)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font1)
        self.label_30.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_30)

        self.lineEditRate = QLineEdit(self.horizontalLayoutWidget)
        self.lineEditRate.setObjectName(u"lineEditRate")
        self.lineEditRate.setStyleSheet(u"QLineEdit\n"
"{\n"
"	background-color: #f6f6f6;\n"
"	color : #000;\n"
"	border: 1px solid #343434;\n"
"	padding: 3px;\n"
"	padding-left: 5px;\n"
"\n"
"}")

        self.verticalLayout_3.addWidget(self.lineEditRate)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 2)
        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(20, 110, 311, 211))
        self.frame_4.setFrameShape(QFrame.Box)
        self.frame_4.setFrameShadow(QFrame.Sunken)
        self.formLayoutWidget_3 = QWidget(self.frame_4)
        self.formLayoutWidget_3.setObjectName(u"formLayoutWidget_3")
        self.formLayoutWidget_3.setGeometry(QRect(10, 10, 291, 186))
        self.formLayout_3 = QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.formLayoutWidget_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_5)

        self.inputSumMarketing = QLineEdit(self.formLayoutWidget_3)
        self.inputSumMarketing.setObjectName(u"inputSumMarketing")
        self.inputSumMarketing.setFont(font3)
        self.inputSumMarketing.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.inputSumMarketing)

        self.label_6 = QLabel(self.formLayoutWidget_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_6)

        self.inputSumMarketingDisc = QLineEdit(self.formLayoutWidget_3)
        self.inputSumMarketingDisc.setObjectName(u"inputSumMarketingDisc")
        self.inputSumMarketingDisc.setFont(font3)
        self.inputSumMarketingDisc.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.inputSumMarketingDisc)

        self.label_9 = QLabel(self.formLayoutWidget_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label_9)

        self.label_8 = QLabel(self.formLayoutWidget_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.label_8)

        self.label_7 = QLabel(self.formLayoutWidget_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.formLayout_3.setWidget(4, QFormLayout.LabelRole, self.label_7)

        self.inputSumMarketingPayed = QLineEdit(self.formLayoutWidget_3)
        self.inputSumMarketingPayed.setObjectName(u"inputSumMarketingPayed")
        self.inputSumMarketingPayed.setFont(font3)
        self.inputSumMarketingPayed.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.inputSumMarketingPayed)

        self.inputSumMarketingRest = QLineEdit(self.formLayoutWidget_3)
        self.inputSumMarketingRest.setObjectName(u"inputSumMarketingRest")
        self.inputSumMarketingRest.setFont(font3)
        self.inputSumMarketingRest.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.inputSumMarketingRest)

        self.inputSumMarketingNetto = QLineEdit(self.formLayoutWidget_3)
        self.inputSumMarketingNetto.setObjectName(u"inputSumMarketingNetto")
        self.inputSumMarketingNetto.setFont(font3)
        self.inputSumMarketingNetto.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout_3.setWidget(4, QFormLayout.FieldRole, self.inputSumMarketingNetto)

        self.frame_5 = QFrame(self.centralwidget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(20, 369, 311, 91))
        self.frame_5.setFrameShape(QFrame.Box)
        self.frame_5.setFrameShadow(QFrame.Sunken)
        self.horizontalLayoutWidget_2 = QWidget(self.frame_5)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(30, 30, 251, 31))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btnPay = QPushButton(self.horizontalLayoutWidget_2)
        self.btnPay.setObjectName(u"btnPay")
        self.btnPay.setStyleSheet(u"QPushButton\n"
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
"QPushButton#btnPay::flat\n"
"{\n"
"	background-color: transparent;\n"
"	border: none;\n"
"	color: #000;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton#btnPay::disabled\n"
"{\n"
"	background-color: #606060;\n"
"	color: #959595;\n"
"	border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton#btnPay::hover\n"
"{\n"
"	background-color: rgba(70,162,218,50%);\n"
"	border: 1px solid #46a2da;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton#btnPay::pressed\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(174, 174, 174, 255),stop:1 rgba(149, 149, 149, 255));\n"
"	border: 1px solid #46a2da;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton#btnPay::checked\n"
"{\n"
"	background-color: qline"
                        "argradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(174, 174, 174, 255),stop:1 rgba(149, 149, 149, 255));\n"
"	border: 1px solid #222;\n"
"\n"
"}")

        self.horizontalLayout_2.addWidget(self.btnPay)

        self.btnClose = QPushButton(self.horizontalLayoutWidget_2)
        self.btnClose.setObjectName(u"btnClose")
        self.btnClose.setStyleSheet(u"QPushButton\n"
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
"QPushButton#btnClose::flat\n"
"{\n"
"	background-color: transparent;\n"
"	border: none;\n"
"	color: #000;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton#btnClose::disabled\n"
"{\n"
"	background-color: #606060;\n"
"	color: #959595;\n"
"	border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton#btnClose::hover\n"
"{\n"
"	background-color: rgba(70,162,218,50%);\n"
"	border: 1px solid #46a2da;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton#btnClose::pressed\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(174, 174, 174, 255),stop:1 rgba(149, 149, 149, 255));\n"
"	border: 1px solid #46a2da;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton#btnClose::checked\n"
"{\n"
"	background-co"
                        "lor: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(174, 174, 174, 255),stop:1 rgba(149, 149, 149, 255));\n"
"	border: 1px solid #222;\n"
"\n"
"}")

        self.horizontalLayout_2.addWidget(self.btnClose)

        self.btnBack = QPushButton(self.centralwidget)
        self.btnBack.setObjectName(u"btnBack")
        self.btnBack.setGeometry(QRect(20, 530, 153, 28))
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
        self.lblDate.setGeometry(QRect(20, 45, 241, 31))
        self.lblDate.setFrameShape(QFrame.Panel)
        self.lblDate.setFrameShadow(QFrame.Raised)
        self.lblDate.setAlignment(Qt.AlignCenter)
        Marketing.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Marketing)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1058, 22))
        Marketing.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Marketing)
        self.statusbar.setObjectName(u"statusbar")
        Marketing.setStatusBar(self.statusbar)

        self.retranslateUi(Marketing)

        QMetaObject.connectSlotsByName(Marketing)
    # setupUi

    def retranslateUi(self, Marketing):
        Marketing.setWindowTitle(QCoreApplication.translate("Marketing", u"Marketing", None))
        self.label.setText(QCoreApplication.translate("Marketing", u"\u062d\u0633\u0627\u0628 \u0627\u0644\u0645\u0633\u0648\u0642\u0627\u062a", None))
        self.label_2.setText(QCoreApplication.translate("Marketing", u"\u0627\u0644\u0645\u0646\u062f\u0648\u0628\u0629/\u0627\u0644\u0645\u0633\u0648\u0642\u0629", None))
        self.label_18.setText(QCoreApplication.translate("Marketing", u"\u063a\u064a\u0631 \u0645\u062a\u0648\u0641\u0631", None))
        self.label_14.setText(QCoreApplication.translate("Marketing", u"\u0627\u0644\u0642\u064a\u0645\u0629(\u0627\u0644\u0646\u0633\u0628\u0629)", None))
        self.label_25.setText(QCoreApplication.translate("Marketing", u"\u062e\u0637 \u0645\u063a\u0644\u0642", None))
        self.label_12.setText(QCoreApplication.translate("Marketing", u"\u0627\u0633\u0645 \u0627\u0644\u0632\u0628\u0648\u0646", None))
        self.label_16.setText(QCoreApplication.translate("Marketing", u"\u0627\u0644\u0637\u0644\u0628\u0627\u062a \u0627\u0644\u0645\u062a\u0628\u0642\u064a\u0629", None))
        self.label_20.setText(QCoreApplication.translate("Marketing", u"\u0637\u0644\u0628 \u062e\u0627\u0635", None))
        self.label_22.setText(QCoreApplication.translate("Marketing", u"\u0627\u0644\u0637\u0644\u0628\u0627\u062a \u0627\u0644\u0645\u0634\u062d\u0648\u0646\u0629", None))
        self.label_21.setText(QCoreApplication.translate("Marketing", u"\u0627\u0644\u0637\u0644\u0628\u0627\u062a \u0627\u0644\u0645\u0631\u062a\u062c\u0639\u0629", None))
        self.label_27.setText(QCoreApplication.translate("Marketing", u"\u0644\u0645 \u064a\u062c\u064a\u0628", None))
        self.label_26.setText(QCoreApplication.translate("Marketing", u"\u0627\u0644\u0637\u0644\u0628\u0627\u062a \u0627\u0644\u0645\u0644\u063a\u0627\u062a", None))
        self.label_13.setText(QCoreApplication.translate("Marketing", u"\u0627\u0644\u0639\u062f\u062f", None))
        self.label_15.setText(QCoreApplication.translate("Marketing", u"\u0627\u0644\u0637\u0644\u0628\u0627\u062a \u0627\u0644\u0645\u0633\u062f\u062f\u0629", None))
        self.label_23.setText(QCoreApplication.translate("Marketing", u"\u0627\u0644\u0637\u0644\u0628\u0627\u062a \u0641\u064a \u0627\u0644\u062a\u0648\u0635\u064a\u0644", None))
        self.label_19.setText(QCoreApplication.translate("Marketing", u"\u0627\u0644\u0637\u0644\u0628\u0627\u062a \u0627\u0644\u0645\u0624\u062c\u0644\u0629", None))
        self.label_17.setText(QCoreApplication.translate("Marketing", u"\u0627\u0644\u0637\u0644\u0628\u0627\u062a \u0627\u0644\u0645\u0639\u0644\u0642\u0629", None))
        self.label_24.setText(QCoreApplication.translate("Marketing", u"\u0639\u062f\u062f \u0627\u0644\u0637\u0644\u0628\u0627\u062a \u0627\u0644\u0643\u0644\u064a", None))
        self.label_39.setText(QCoreApplication.translate("Marketing", u"\u062e\u0635\u0648\u0645\u0627\u062a \u0627\u0644\u062a\u0648\u0635\u064a\u0644", None))
        self.label_32.setText(QCoreApplication.translate("Marketing", u"\u062e\u0635\u0648\u0645\u0627\u062a \u0627\u0644\u0634\u062d\u0646", None))
        self.label_42.setText(QCoreApplication.translate("Marketing", u"\u0645\u062c\u0645\u0648\u0639 \u0627\u0644\u062e\u0635\u0648\u0645\u0627\u062a", None))
        self.label_31.setText(QCoreApplication.translate("Marketing", u"\u0627\u0644\u062e\u0635\u0648\u0645\u0627\u062a", None))
        self.label_38.setText(QCoreApplication.translate("Marketing", u"\u0627\u0644\u0639\u062f\u062f", None))
        self.label_29.setText(QCoreApplication.translate("Marketing", u"\u0627\u0644\u0642\u064a\u0645\u0629(\u0627\u0644\u0646\u0633\u0628\u0629)", None))
        self.label_3.setText(QCoreApplication.translate("Marketing", u"\u0627\u0644\u0637\u0644\u0628\u0627\u062a \u0627\u0644\u0645\u062d\u0642\u0642\u0629", None))
        self.label_4.setText(QCoreApplication.translate("Marketing", u"\u0635\u0627\u0641\u064a \u0627\u0644\u062d\u0633\u0627\u0628", None))
        self.label_28.setText(QCoreApplication.translate("Marketing", u"\u0627\u062e\u062a\u0631 \u0627\u0644\u062d\u0627\u0644\u0629", None))
        self.label_40.setText(QCoreApplication.translate("Marketing", u"\u0627\u0644\u0639\u062f\u062f", None))
        self.label_30.setText(QCoreApplication.translate("Marketing", u"\u0627\u0644\u0642\u064a\u0645\u0629(\u0627\u0644\u0646\u0633\u0628\u0629)", None))
        self.label_5.setText(QCoreApplication.translate("Marketing", u"\u0645\u062c\u0645\u0648\u0639 \u062d\u0633\u0627\u0628 \u0627\u0644\u0645\u0633\u0648\u0642\u0627\u062a", None))
        self.label_6.setText(QCoreApplication.translate("Marketing", u"\u0645\u062c\u0645\u0648\u0639 \u062e\u0635\u0648\u0645\u0627\u062a \u0627\u0644\u0645\u0633\u0648\u0642\u0627\u062a", None))
        self.label_9.setText(QCoreApplication.translate("Marketing", u"\u0645\u062c\u0645\u0648\u0639 \u0627\u0644\u0645\u0633\u062f\u062f \u0644\u0644\u0645\u0633\u0648\u0642\u0627\u062a", None))
        self.label_8.setText(QCoreApplication.translate("Marketing", u"\u0645\u062c\u0645\u0648\u0639 \u0627\u0644\u0645\u062a\u0628\u0642\u064a \u0644\u0644\u0645\u0633\u0648\u0642\u0627\u062a", None))
        self.label_7.setText(QCoreApplication.translate("Marketing", u"\u0645\u062c\u0645\u0648\u0639 \u0635\u0627\u0641\u064a \u0627\u0644\u0645\u0633\u0648\u0642\u0627\u062a", None))
        self.btnPay.setText(QCoreApplication.translate("Marketing", u"\u062a\u0633\u062f\u064a\u062f \u0627\u0644\u062d\u0633\u0627\u0628", None))
        self.btnClose.setText(QCoreApplication.translate("Marketing", u"\u0627\u063a\u0644\u0627\u0642 \u0627\u0644\u062d\u0633\u0627\u0628", None))
        self.btnBack.setText(QCoreApplication.translate("Marketing", u"\u0631\u062c\u0648\u0639", None))
        self.lblDate.setText("")
    # retranslateUi

